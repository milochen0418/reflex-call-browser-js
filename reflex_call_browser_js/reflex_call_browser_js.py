import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.fragment(
        rx.center(
            rx.vstack(
                rx.heading("Hello"),
            ),        
        ),
    )

# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.compile()
