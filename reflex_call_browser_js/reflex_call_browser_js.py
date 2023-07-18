from typing import Any, Dict
import reflex as rx
import json

javascript_functions = """
<script>

function dispatch(jobj) {
  var func = jobj.__func__;
  eval(func + '(jobj)');
}

browsercall = function(msg) {
    console.log('browsercall is calling')
    try {
        var jobj = JSON.parse(msg);
        dispatch(jobj);
    } catch(e) {
        console.log(e.name);
        console.log(e.message);
    }
};


window.alert = function(msg) {
    try {
        var jobj = JSON.parse(msg);
        dispatch(jobj);
    } catch(e) {
        console.log(e.name);
        console.log(e.message);
    }
};


function test_func_1(jobj) {
  console.log('My name is ' + jobj.myname + ' and my action is ' + jobj.myaction);
}

function test_func_2(jobj) {
  console.log('My course is ' + jobj.mycourse + ' and my score is ' + jobj.myscore);
}

</script>
"""

def scripts(js=javascript_functions):
    return rx.box(rx.html(js))

class State(rx.State):
    def btn_test_func_1(self):
        dobj = {"__func__":"test_func_1", "myname":"Milo", "myaction":"Jump"}
        yield browser_js_call_1(dobj)
    def btn_test_func_2(self):
        dobj = {"__func__":"test_func_2", "mycourse":"Math", "myscore":99}
        yield browser_js_call_1(dobj)
    def btn_test_func_3(self):
        dobj = {"__func__":"test_func_3", "mycourse":"Math", "myscore":"99"}
        yield browser_js_call_1(dobj)
    def btn_test_func_4(self):
        dobj = {"__func__":"test_func_1", "myname":"Milo", "myaction":"Jump"}
        yield browser_js_call_2(dobj)
    def btn_test_func_5(self):
        dobj = {"__func__":"test_func_2", "mycourse":"Math", "myscore":99}
        yield browser_js_call_2(dobj)
    def btn_test_func_6(self):
        dobj = {"__func__":"test_func_3", "mycourse":"Math", "myscore":"99"}
        yield browser_js_call_2(dobj)


def browser_js_call_1(dobj:Dict[str,Any]):
    return rx.window_alert(str(json.dumps(dobj)))
    #return rx.browsercall(str(json.dumps(dobj)))

def browser_js_call_2(dobj:Dict[str,Any]):
    return rx.browsercall(str(json.dumps(dobj)))

def index() -> rx.Component:
    return rx.fragment(
        rx.center(
            rx.vstack(
                rx.heading("Call Browser-Side JavaScript"),
                rx.button("wa call test_func_1", on_click=State.btn_test_func_1),
                rx.button("wa call test_func_2", on_click=State.btn_test_func_2),
                rx.button("wa call test_func_3", on_click=State.btn_test_func_3),
                rx.button("bc call test_func_1", on_click=State.btn_test_func_4),
                rx.button("bc call test_func_2", on_click=State.btn_test_func_5),
                rx.button("bc call test_func_3", on_click=State.btn_test_func_6),

            ),
        ),
    )

# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index,
    script_tags = [
        scripts(),
    ],
)

app.compile()
