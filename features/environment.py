from app import app


def before_scenario(context, scenario):
    # Use Flask's test client so behave scenarios can interact with the app without a live server.
    context.client = app.test_client()
    context.response = None
    context.a = None
    context.b = None
