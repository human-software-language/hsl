import dspy
from dspy import Module, OpenAI
from pydantic import BaseModel, Field
from pathlib import Path
from typing import List, Dict
import json


def load_json_file(json_file_path: str) -> dict:
    """Load a JSON file from the specified path."""

    with open(json_file_path, "r") as file:
        data = json.load(file)
    return data


def convert_reasoning_modules_json_to_text(reasoning_modules_json: str) -> str:
    """Convert reasoning modules JSON object to a simplified text representation of tuples."""

    reasoning_modules = reasoning_modules_json.get("reasoning_modules", [])
    # Convert each module to a tuple (module_type, description) and join into a long text text
    reasoning_modules_text = ", ".join(
        [f'({module["type"]}: {module["description"]})' for module in reasoning_modules]
    )
    return reasoning_modules_text


# STAGE 1: SELECT
class SelectReasoningModules(dspy.Signature):
    task_description: str = dspy.InputField(desc="The task(s) to solve.")
    reasoning_modules: str = dspy.InputField(
        desc="List of relevant reasoning modules to solve task(s) with."
    )
    selected_reasoning_modules = dspy.OutputField(
        desc="Select few reasoning modules that are the most appropriate for solving the given task(s). Do NOT elaborate on why, just provide a list of `{module type}: {description}`.",
    )


class SelectReasoningModule(dspy.Module):
    def __init__(self, reasoning_modules):
        super().__init__()

        self.reasoning_modules = reasoning_modules
        self.generate = dspy.ChainOfThought(SelectReasoningModules)

    def forward(self, task_description: str) -> dspy.Prediction:
        prediction = self.generate(
            task_description=task_description, reasoning_modules=self.reasoning_modules
        )

        return prediction


# STAGE 1: ADAPT


class AdaptReasoningModules(dspy.Signature):
    """Rephrase and specify each selected reasoning module so that it better helps solving the given task(s)."""

    task_description = dspy.InputField(
        prefix="Task(s) Description:", desc="The task(s) to solve."
    )
    selected_reasoning_modules = dspy.InputField(
        prefix="Selected Reasoning Modules:",
        desc="The selected reasoning modules that will be adapted to solve the task(s).",
    )
    adapted_reasoning_modules = dspy.OutputField(
        prefix="Adapted Reasoning Modules:",
        desc="Adapt and tailor each selected reasoning module's description to better solve the task(s). Do NOT work out the full solution.",
    )


class AdaptReasoningModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(AdaptReasoningModules)

    def forward(
        self, task_description: str, selected_reasoning_modules: str
    ) -> dspy.Prediction:
        prediction = self.generate(
            task_description=task_description,
            selected_reasoning_modules=selected_reasoning_modules,
        )
        return prediction


# STAGE 1: IMPLEMENT


class ImplementReasoningStructures(dspy.Signature):
    """Combine all adapted reasoning modules into one step-by-step structured reasoning plan template to solve the task(s)."""

    task_description = dspy.InputField(
        prefix="Task(s) Description:", desc="The task(s) to solve."
    )
    adapted_reasoning_modules = dspy.InputField(
        prefix="Task Adapted Reasoning Modules:",
        desc="The adapted reasoning modules that will be combined into one plan to better solve the task(s).",
    )
    implemented_reasoning_structures = dspy.OutputField(
        prefix="Implemented Reasoning Structures:",
        desc="Implement a markdown-formmated reasoning structure template for solvers to follow step-by-step and arrive at correct answers. You should use knowledge from adapted reasoning modules and combine that knowledge to one step-by-step plan. Do NOT work out the full solution.",
    )


class ImplementReasoningStructure(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(ImplementReasoningStructures)

    def forward(
        self, task_description: str, adapted_reasoning_modules: str
    ) -> dspy.Prediction:
        prediction = self.generate(
            task_description=task_description,
            adapted_reasoning_modules=adapted_reasoning_modules,
        )
        return prediction


# STAGE 2: EXECUTE


class ExecuteReasoningStructures(dspy.Signature):
    """Execute the given reasoning structure to solve a specific task(s)."""

    task_description = dspy.InputField(
        prefix="Task(s) Description:", desc="The task(s) to solve."
    )
    implemented_reasoning_structures = dspy.InputField(
        desc="The markdown-formatted reasoning structure template that will be used to solve the task(s).",
    )
    executed_reasoning_structures = dspy.OutputField(
        desc="Using the reasoning structure as a guide, solve the task(s) and provide the final answer(s).",
    )


class ExecuteReasoningStructure(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate = dspy.Predict(ExecuteReasoningStructures)

    def forward(
        self, task_description: str, implemented_reasoning_structures: str
    ) -> dspy.Prediction:
        prediction = self.generate(
            task_description=task_description,
            implemented_reasoning_structures=implemented_reasoning_structures,
        )
        return prediction


# DSPy Self-Discover Module


class SelfDiscover(dspy.Module):
    """A comprehensive DSPy module encapsulating the Self-Discover approach.

    This module integrates the processes of:
    - STAGE 1: selecting, adapting, and implementing reasoning module structures
    - STAGE 2: executing reasoning module structures to solve a given task(s)

    It represents a full cycle of the Self-Discover reasoning process, from initial selection to final execution.
    """

    def __init__(self, model="gpt-3.5-turbo-0125"):
        super().__init__()

        # Configure dspy
        # lm = dspy.OpenAI(model="gpt-3.5-turbo-0125", max_tokens=4096)
        # lm = dspy.OpenAI(model="gpt-4-turbo-preview", max_tokens=4096)
        self.lm = dspy.OpenAI(model=model, max_tokens=4096)
        dspy.settings.configure(lm=self.lm)

        # Load json
        cwd = Path.cwd()
        fp_reasoning_modules_json = cwd / "./src/reasoning_general.json"
        reasoning_modules_json = load_json_file(fp_reasoning_modules_json)
        # Convert the reasoning modules JSON to a simplified text representation for LLM
        self.reasoning_modules = convert_reasoning_modules_json_to_text(
            reasoning_modules_json
        )
        print(self.reasoning_modules[0:500])

        self.select_reasoning_module = SelectReasoningModule(
            reasoning_modules=self.reasoning_modules
        )
        self.adapt_reasoning_module = AdaptReasoningModule()
        self.implement_reasoning_module = ImplementReasoningStructure()
        self.execute_reasoning_structure = ExecuteReasoningStructure()

    def forward(self, task_description: str) -> dspy.Prediction:
        # STAGE 1: SELECT, ADAPT, IMPLEMENT
        selected_reasoning_modules = self.select_reasoning_module.forward(
            task_description
        ).selected_reasoning_modules
        adapted_reasoning_modules = self.adapt_reasoning_module.forward(
            task_description, selected_reasoning_modules
        ).adapted_reasoning_modules
        implemented_reasoning_structures = self.implement_reasoning_module.forward(
            task_description, adapted_reasoning_modules
        ).implemented_reasoning_structures

        # STAGE 2: EXECUTE
        executed_reasoning_structures = self.execute_reasoning_structure.forward(
            task_description, implemented_reasoning_structures
        ).executed_reasoning_structures

        # SOLUTION
        prediction = dspy.Prediction(solution=executed_reasoning_structures)

        self.lm.inspect_history(n=10)
        return prediction


def main():

    # Discover
    self_discover = SelfDiscover(model="gpt-4-turbo-preview")
    # self_discover = SelfDiscover(model="gpt-3.5-turbo-0125")

    # task = "Parse all ai projects managers in London at linkedin"
    # - Later, we should execute js code created from result of that plan in background.js using exec() method inside our chrome extension.
    # - Each step should have what we should do: Inputs, outputs, sub steps related to that action and validation strategy for each sub step.
    #     - Each input and output should be always data structure: detailed typescript interfaces with all arguments, they can be nested
    task = """
    Write Expected output and Plan for Example 2
    
    ## Example 1
    Task: Search in google wakeboarding spots near Fortaleza, Brazil.
    Expected output: table with results
    Plan:
    1. Go to https://google.com
    2. Find search bar and type "Parque de wakeboard Fortaleza Brasil"
    3. Click search button
    4. Parse all results on first page into table
    
    ## Example 2
    Task: Find project managers at linkedin in London.
    Expected output:
    """
    self_discover.forward(task)


if __name__ == "__main__":
    main()
