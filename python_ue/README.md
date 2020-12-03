Notes and Python Scripts for Unreal Engine Editor

## Overview of Python in UE

### Links

UE Notes on Python = https://docs.unrealengine.com/en-US/Engine/Editor/ScriptingAndAutomation/Python/index.html 
UE Python API Docs = https://docs.unrealengine.com/en-US/PythonAPI/index.html
Python script examples = https://github.com/mamoniem/UnrealEditorPythonScripts


### Setup 

1. Install Python 3.x
2. Install your python editor (currently VS Code)
3. Unreal Engine > Settings > Plugins > Scripting and enable Python
4. restart UE and go to Project Settings > Python (in plugins section at end) > Enable Developer Mode
5. In the above settings section, set your paths for scripts then restart editor

### Quick Sample script

example script (TODO)

### Issues

UE only uses python 2 but it appears 3.x will be coming soon

Epic has substantially increased the amount of API's for python in the last few releases, so they are taking it seriously.


## Running Python in blueprints

create a custom event
the event calls a blueprint "Execute Console Command"

Also, you can call the python script from event begin play to log events. It WORKS in runtime (only from the editor or Dev builds which will be great for automated testing AND level generation)
