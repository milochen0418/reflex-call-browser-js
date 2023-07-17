import reflex as rx

class ReflexcallbrowserjsConfig(rx.Config):
    pass

config = ReflexcallbrowserjsConfig(
    app_name="reflex_call_browser_js",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)