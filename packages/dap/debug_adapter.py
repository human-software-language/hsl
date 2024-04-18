import os
from typing import Dict, List, Optional
from debugpy.common import messaging
from packages.logger import logger
from packages.runtime import HSLRuntime


class HSLDebugAdapter:
    def __init__(self):
        self._runtime = None
        self._breakpoints: Dict[str, List[int]] = {}
        self._launch_config: Optional[Dict] = None

    def handle_event(self, event: messaging.Event):
        if event.event == "output":
            self._handle_output_event(event)
        # Handle other events if needed

    def _handle_output_event(self, event: messaging.Event):
        category = event("category", str)
        output = event("output", str)
        logger.debug(f"Received output event - category: {category}, output: {output}")
        # Handle output event based on category and output

    def handle_request(self, request: messaging.Request) -> messaging.Response:
        command = request.command

        if command == "initialize":
            return self._handle_initialize_request(request)
        elif command == "launch":
            return self._handle_launch_request(request)
        elif command == "setBreakpoints":
            return self._handle_set_breakpoints_request(request)
        elif command == "configurationDone":
            return self._handle_configuration_done_request(request)
        elif command == "disconnect":
            return self._handle_disconnect_request(request)
        else:
            raise request.isnt_valid(f"Unsupported request: {command}")

    def _handle_initialize_request(
        self, request: messaging.Request
    ) -> messaging.Response:
        self._runtime.initialize(request.arguments)
        capabilities = {
            "supportsConfigurationDoneRequest": True,
            "supportsSetVariable": True,
            "supportsConditionalBreakpoints": True,
            "supportsHitConditionalBreakpoints": True,
            "supportsFunctionBreakpoints": True,
            "supportsLogPoints": True,
            "supportsSetExpression": True,
            "supportsTerminateRequest": True,
            "supportsExceptionOptions": True,
            "supportsValueFormattingOptions": True,
            "supportsExceptionInfoRequest": True,
            "supportsDelayedStackTraceLoading": True,
            "supportsLoadedSourcesRequest": True,
            "supportsModulesRequest": True,
            "supportsTerminateThreadsRequest": True,
            "supportsCompletionsRequest": True,
            "supportsRestartFrame": True,
            "supportsStepInTargetsRequest": True,
            "supportsGotoTargetsRequest": True,
            "supportsStepBack": True,
            "supportsEvaluateForHovers": True,
            "exceptionBreakpointFilters": [
                {"filter": "raised", "label": "Raised Exceptions", "default": False},
                {"filter": "uncaught", "label": "Uncaught Exceptions", "default": True},
            ],
        }
        return messaging.Response(request, success=True, body=capabilities)

    def _handle_launch_request(self, request: messaging.Request) -> messaging.Response:
        self._launch_config = request.arguments
        program = self._launch_config.get("program")
        if not program:
            return messaging.Response(
                request,
                success=False,
                message="Missing 'program' in launch configuration",
            )

        if not os.path.exists(program):
            return messaging.Response(
                request,
                success=False,
                message=f"Program '{program}' does not exist",
            )

        self._runtime = HSLRuntime(debug_adapter=self, file_path=program)
        self._runtime.launch()

        return messaging.Response(request, success=True)

    def _handle_set_breakpoints_request(
        self, request: messaging.Request
    ) -> messaging.Response:
        source = request.arguments.get("source")
        breakpoints = request.arguments.get("breakpoints", [])

        if not source or "path" not in source:
            return messaging.Response(
                request,
                success=False,
                message="Missing or invalid 'source' in setBreakpoints request",
            )

        path = source["path"]
        self._breakpoints[path] = [bp["line"] for bp in breakpoints]
        self._runtime.set_breakpoints(path, self._breakpoints[path])

        return messaging.Response(
            request,
            success=True,
            body={
                "breakpoints": [
                    {"verified": True, "line": line} for line in self._breakpoints[path]
                ]
            },
        )

    def _handle_configuration_done_request(
        self, request: messaging.Request
    ) -> messaging.Response:
        if self._launch_config is None:
            return messaging.Response(
                request,
                success=False,
                message="No launch configuration available",
            )

        self._runtime.configuration_done()
        return messaging.Response(request, success=True)

    def _handle_disconnect_request(
        self, request: messaging.Request
    ) -> messaging.Response:
        terminate_debuggee = request.arguments.get("terminateDebuggee", False)
        self._runtime.disconnect(terminate_debuggee)
        return messaging.Response(request, success=True)
