
# Sample minimal workflow for MuPIF

This is a minimal workflow consisting of the workflow ifself in [wf_01.py](wf_01.py), the mode in [wf_01_a.py](wf_01_a.py) and the job manager [wf_01_a-jobman.py](wf_01_a-jobman.py).

The workflow itself must be uploaded to the MuPIF database, and then whenever a new execution is scheduled, the scheduler will automatically contact the jobmanager (provided it is running on your machine), which will in turn run the model as defined in [wf_01_a.py](wf_01_a.py).

## Remote logging

The model does runs for 3 minutes and outputs tick counter every second into the log. To do this in your own model, do:

1. `import mupif` (this has to be done first, as it sets up the logging system, including remote logger — this is prepared by the job manager)
  
   Technically speaking, mupif adds remote logger to the root handler, so it will be used automatically by normal loggers.

2. `import logging` and `log=logging.getLogger()`, use the logger normally

3. Messages going to plain output (`print` or subprocesses just outputting to STDOUT) do *not* do to the remote logger. For subprocesses, this must be worked around (work-in-progress on our side)

This can be later (work in progress) seen in the monitor; there are two executions of the workflow running simultaneously.

https://user-images.githubusercontent.com/1029876/195792405-f0de0ba7-da06-4a4e-8f88-5c2055fcaf41.mp4

