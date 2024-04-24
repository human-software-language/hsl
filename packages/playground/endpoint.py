from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

import solara.server.starlette
import solara.server.kernel_context
from app import VsCodeState


async def update_state(request: Request):
    # we import this late, otherwise we get circular imports
    import packages.playground.app as app

    state_data = await request.json()  # Parse JSON payload from the request
    vscode_state = VsCodeState(
        **state_data
    )  # Validate and create a VsCodeState instance

    # undocumented, *might* break in the future, but we do our best to keep it working
    # Reset the clicks for all kernels
    for kernel_id, context in solara.server.kernel_context.contexts.items():
        with context:
            app.vscode_state = vscode_state
            print(
                f"Updated VSCode state with file path: {vscode_state.file_path}, cursor location: {vscode_state.cursor_location}"
            )
    return JSONResponse({"status": "State updated"})


routes = [
    Route("/update_state", endpoint=update_state, methods=["POST"]),
    *solara.server.starlette.routes,
]
app = Starlette(routes=routes)
