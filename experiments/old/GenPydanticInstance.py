import ast
import logging
import inspect

from typing import Type, TypeVar, Optional, List
from dspy import Assert, Module, ChainOfThought, Signature, InputField, OutputField
from pydantic import BaseModel, ValidationError, Field


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


def eval_dict_str(dict_str: str) -> dict:
    """Safely convert str to dict"""
    return ast.literal_eval(dict_str)


class PromptToPydanticInstanceSignature(Signature):
    """
    Synthesize the prompt into the kwargs fit the model.
    Do not duplicate the field descriptions
    """

    root_pydantic_model_class_name = InputField(
        desc="The class name of the pydantic model to receive the kwargs"
    )
    pydantic_model_definitions = InputField(
        desc="Pydantic model class definitions as a string"
    )
    prompt = InputField(
        desc="The prompt to be synthesized into data. Do not duplicate descriptions"
    )
    root_model_kwargs_dict = OutputField(
        prefix="kwargs_dict: dict = ",
        desc="Generate a Python dictionary as a string with minimized whitespace that only contains json valid values.",
    )


class PromptToPydanticInstanceErrorSignature(Signature):
    """Synthesize the prompt into the kwargs fit the model"""

    error = InputField(desc="Error message to fix the kwargs")

    root_pydantic_model_class_name = InputField(
        desc="The class name of the pydantic model to receive the kwargs"
    )
    pydantic_model_definitions = InputField(
        desc="Pydantic model class definitions as a string"
    )
    prompt = InputField(desc="The prompt to be synthesized into data")
    root_model_kwargs_dict = OutputField(
        prefix="kwargs_dict = ",
        desc="Generate a Python dictionary as a string with minimized whitespace that only contains json valid values.",
    )


T = TypeVar("T", bound=BaseModel)


class GenPydanticInstance(Module):
    """
    A module for generating and validating Pydantic model instances based on prompts.

    Usage:
        To use this module, instantiate the GenPydanticInstance class with the desired
        root Pydantic model and optional child models. Then, call the `forward` method
        with a prompt to generate Pydantic model instances based on the provided prompt.
    """

    def __init__(
        self,
        root_model: Type[T],
        child_models: list[Type[BaseModel]] = None,
        generate_sig=PromptToPydanticInstanceSignature,
        correct_generate_sig=PromptToPydanticInstanceErrorSignature,
    ):
        super().__init__()

        self.models = [root_model]  # Always include root_model in models list

        self.models.extend(child_models)

        self.output_key = "root_model_kwargs_dict"
        self.root_model = root_model

        # Concatenate source code of models for use in generation/correction logic
        self.model_sources = "\n".join(
            [inspect.getsource(model) for model in self.models]
        )

        # Initialize DSPy ChainOfThought modules for generation and correction
        self.generate = ChainOfThought(generate_sig)
        self.correct_generate = ChainOfThought(correct_generate_sig)
        self.validation_error = None

    def validate_root_model(self, output: str) -> bool:
        """Validates whether the generated output conforms to the root Pydantic model."""
        try:
            model_inst = self.root_model.model_validate(eval_dict_str(output))
            return isinstance(model_inst, self.root_model)
        except (ValidationError, ValueError, TypeError, SyntaxError) as error:
            self.validation_error = error
            logger.debug(f"Validation error: {error}")
            return False

    def validate_output(self, output) -> T:
        """Validates the generated output and returns an instance of the root Pydantic model if successful."""
        Assert(
            self.validate_root_model(output),
            f"""You need to create a kwargs dict for {self.root_model.__name__}\n
            Validation error:\n{self.validation_error}""",
        )

        return self.root_model.model_validate(eval_dict_str(output))

    def forward(self, prompt) -> T:
        """
        Takes a prompt as input and generates a Python dictionary that represents an instance of the
        root Pydantic model. It also handles error correction and validation.
        """
        output = self.generate(
            prompt=prompt,
            root_pydantic_model_class_name=self.root_model.__name__,
            pydantic_model_definitions=self.model_sources,
        )

        output = output[self.output_key]

        try:
            return self.validate_output(output)
        except (AssertionError, ValueError, TypeError) as error:
            logger.error(f"Error {str(error)}\nOutput:\n{output}")

            # Correction attempt
            corrected_output = self.correct_generate(
                prompt=prompt,
                root_pydantic_model_class_name=self.root_model.__name__,
                pydantic_model_definitions=self.model_sources,
                error=f"str(error){self.validation_error}",
            )[self.output_key]

            return self.validate_output(corrected_output)

    def __call__(self, *args, **kwargs):
        return self.forward(kwargs.get("prompt"))


class Event(BaseModel):
    name: str
    description: str
    timestamp: Optional[str] = Field(
        None, description="The timestamp when the event occurs"
    )


class Command(BaseModel):
    name: str
    description: str
    target_aggregate: str
    required_data: Optional[List[str]] = Field(
        default_factory=list,
        description="List of data fields required to execute the command",
    )


class Query(BaseModel):
    name: str
    description: str
    return_type: str
    parameters: Optional[List[str]] = Field(
        default_factory=list,
        description="List of parameters required to perform the query",
    )


class EventStormModel(BaseModel):
    events: List[Event] = Field(
        default_factory=list, description="List of events in the system"
    )
    commands: List[Command] = Field(
        default_factory=list, description="List of commands in the system"
    )
    queries: List[Query] = Field(
        default_factory=list, description="List of queries in the system"
    )


def main():
    import dspy

    lm = dspy.OpenAI(max_tokens=3000, model="gpt-4")
    dspy.settings.configure(lm=lm)
    prompt = """
    ```prompt
    Automated Hygen template full stack system for NextJS.
    Express
Express.js is arguably the most popular web framework for Node.js

A typical app structure for express celebrates the notion of routes and handlers, while views and data are left for interpretation (probably because the rise of microservices and client-side apps).

So an app structure may look like this:

app/
  routes.js
  handlers/
    health.js
    shazam.js
While routes.js glues everything together:

// ... some code ...
const health = require('./handlers/health')
const shazam = require('./handlers/shazam')
app.get('/health', health)
app.post('/shazam', shazam)

module.exports = app
Unlike React Native, you could dynamically load modules here. However, there's still a need for judgement when constructing the routes (app.get/post part).

Using hygen let's see how we could build something like this:

$ hygen route new --method post --name auth
Since we've been through a few templates as with previous use cases, let's jump straight to the interesting part, the inject part.

So let's say our generator is structured like this:

_templates/
  route/
    new/
      handler.ejs.t
      inject_handler.ejs.t
Then inject_handler looks like this:

---
inject: true
to: app/routes.js
skip_if: <%= name %>
before: "module.exports = app"
---
app.<%= method %>('/<%= name %>', <%= name %>)
Note how we're anchoring this inject to before: "module.exports = app". If in previous occasions we appended content to a given line, we're now prepending it.
```    
    
You are a Event Storm assistant that comes up with Events, Commands, and Queries for Reactive Domain Driven Design based on the ```prompt```
    """

    model_module = GenPydanticInstance(
        root_model=EventStormModel, child_models=[Event, Command, Query]
    )
    model_inst = model_module(prompt=prompt)
    print(model_inst)


value = """"""

if __name__ == "__main__":
    main()
