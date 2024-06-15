# Fork, by Memoize Labs (V0.0.1)

**_Report bugs and get support at contact@memoizelabs.com_**

## Installation
For first-time users, begin by running:
```console 
foo@user:~$ pip install memoizelabs
``` 
For upgrading to the latest version, upgrade to the latest version by running:
```console 
foo@user:~$ pip install --upgrade memoizelabs
```

## Usage

### Methods

```fork(id, file_paths, isolated_voice_path, description='')```
* **Parameters:**
  * **id** _(str)_: the user-specified ID of the model. 
  * **file_paths** _(str array)_: a string of file paths containing objects to fine tune on. These can be .txt, .mp3, or .mp4 files. 
  * **isolated_voice_path** _(str)_: a path to a .mp3 file containing a clean recording of the target at least 30 seconds in length, used to pre-process submitted files and identify the target's voice within them before finetuning for better results. 
  * **description** _(str, optional)_: a description of the target (ex: An elderly woman with a deep, soothing voice, a British accent, and a witty sense of humor). 


### Classes

```Fork(api_key)```
* **Parameters:**
  * **api_key** _(str)_:

```StateMachine() ```
