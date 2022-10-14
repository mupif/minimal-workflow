import sys
import mupif as mp
sys.path.append('.')
import wf_01_a
import json
md=wf_01_a.Eudoxos_WF_01_a().getAllMetadata()
mp.SimpleJobManager(
    ns=mp.pyroutil.connectNameserver(),
    appClass=wf_01_a.Eudoxos_WF_01_a,
    appName='eudoxos/wf-01-a',
    maxJobs=1000,
).runServer()

