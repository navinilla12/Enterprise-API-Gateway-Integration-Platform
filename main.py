
from fastapi import FastAPI

from routers.users import router as users_router
from routers.integrations import router as integrations_router
from routers.analytics import router as analytics_router


app = FastAPI(

    title="Enterprise API Gateway Platform",

    description="""
    Enterprise SaaS Integration Platform
    with JWT, OAuth2, API Keys,
    RBAC and API Monitoring
    """,

    version="1.0"

)


app.include_router(users_router)

app.include_router(integrations_router)

app.include_router(analytics_router)



@app.get("/")
def home():

    return {

        "platform":
        "Enterprise API Gateway",

        "status":
        "Running"

    }
