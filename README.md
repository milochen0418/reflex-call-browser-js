# reflex-call-browser-js
Make sure to install `reflex==0.2.0`
```bash
pip install -r requirements.txt
```

## Explain
We rewrite window.alert in the frontend.  
So that we have a easy way to verify our frontend code have the ability to call browser-side js.   
Then we can start to make a new special event in the reflex framework to support something like
`call_browser_js`

This small project make for solve the the step 2 for this issue 

- https://github.com/reflex-dev/reflex/issues/1346

