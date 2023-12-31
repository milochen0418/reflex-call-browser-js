import reflex as rx

javascript_functions = """<script>
function test_func_1(jobj) {
  console.log('My name is ' + jobj.myname + ' and my action is ' + jobj.myaction);
}
function test_func_2(jobj) {
  console.log('My course is ' + jobj.mycourse + ' and my score is ' + jobj.myscore);
}
</script>"""

def scripts(js=javascript_functions):
    return rx.box(rx.html(js))

class State(rx.State):
    def btn_test_func_1(self):
        dobj = {"__func__":"test_func_1", "myname":"Milo", "myaction":"Jump"}
        yield rx.browsercall(dobj)
    def btn_test_func_2(self):
        dobj = {"__func__":"test_func_2", "mycourse":"Math", "myscore":99}
        yield rx.browsercall(dobj)
    def btn_test_func_3(self):
        dobj = {"__func__":"test_func_3", "mycourse":"Math", "myscore":"99"}
        yield rx.browsercall(dobj)

def index() -> rx.Component:
    return rx.fragment(
        rx.center(
            rx.vstack(
                rx.heading("Call Browser-Side JavaScript"),
                rx.button("browser call test_func_1", on_click=State.btn_test_func_1),
                rx.button("browser call test_func_2", on_click=State.btn_test_func_2),
                rx.button("browser call test_func_3", on_click=State.btn_test_func_3),
            ),
        ),
    )

app = rx.App(state=State)
app.add_page(index, script_tags = [scripts()] )
app.compile()
