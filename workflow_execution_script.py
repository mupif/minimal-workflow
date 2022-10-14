import importlib
import sys
import os

# os.environ["MUPIF_LOG_LEVEL"] = "INFO"
# os.environ["MUPIF_LOG_FILE"] = "mupif.log"

import logging
import argparse
# import mupifDB
import mupif as mp



log = logging.getLogger()
log.setLevel(logging.DEBUG)
tailHandler=mp.pyrolog.TailLogHandler(capacity=10000)
log.addHandler(tailHandler)
log.info('Execution script started with args: {sys.argv}')

daemon=mp.pyroutil.getDaemon()
logUri=str(daemon.register(mp.pyrolog.PyroLogReceiver(tailHandler=tailHandler)))

if __name__ == "__main__":
    workflow = None

    try:
        import sys
        sys.path.append('.')
        import wf_01

        workflow_class = wf_01.Eudoxos_WF_01
        #
        workflow = workflow_class()
        workflow.initialize(metadata={'Execution': {'ID': '<TEST>', 'Use_case_ID': '<TEST>', 'Task_ID': '<TEST>', 'Log_URI': logUri}})
        import rich.pretty
        rich.pretty.pprint(workflow.getAllMetadata())
        workflow.solve()
        workflow.terminate()
    except Exception as err:
        log.exception(err)
        try:
            workflow.terminate()
        except:
            pass
        if type(err) == mp.JobManNoResourcesException:
            print("Not enough resources")
            log.error('Not enough resources')
            sys.exit(2)
        sys.exit(1)

    except:
        print("Unknown error")
        log.info("Unknown error")
        if workflow is not None:
            workflow.terminate()
        sys.exit(1)

    sys.exit(0)
