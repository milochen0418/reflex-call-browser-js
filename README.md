# reflex-call-browser-js

### Run the early version 
The early version could use the following way to setup.  
Make sure to install `reflex==0.2.0`
```bash
pip install -r requirements.txt
```

### Run the latest version 
Or you can use the following `codna` way to run your code in  
the latest source code of reflex.  
(The terminal in the VSCode sometimes is unstable, so please use the pure Terminal app)

```
git clone https://github.com/reflex-dev/reflex
cd reflex
conda create -n reflex-core python=3.11
conda activate reflex-core
pip install poetry
poetry install
mkdir examples
cd examples
git clone https://github.com/milochen0418/reflex-call-browser-js
cd reflex-call-browser-js
reflex init
reflex run
```

## Explain
We rewrite window.alert in the frontend.  
So that we have a easy way to verify our frontend code has the ability to call browser-side js.   
Then we can start to make a new special event in the reflex framework to support something like
`call_browser_js`

This small project makes for solving step 2 for this issue. 

- https://github.com/reflex-dev/reflex/issues/1346

YouTube Demo is here https://www.youtube.com/watch?v=_gfbeOXPD6g
