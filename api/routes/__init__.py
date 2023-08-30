from .history import router as history_router
from .recommendation import router as recommendation_router
from .cashback import router as cashback_router

# Route for terminal
from .terminal import router as terminal_router

# Route that imitates MIR microservice
from .mir import router as mir_router