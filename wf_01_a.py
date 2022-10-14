import sys
import os
import mupif
import mupif as mp
import numpy as np
import Pyro5.api
import time
import logging
log=logging.getLogger()

@Pyro5.api.expose
class Eudoxos_WF_01_a(mp.Model):
    def __init__(self,metadata=None):
        MD = {
            "Name": "UNIX timestamp",
            "ID": "Eudoxos_WF_01_a",
            "Description": "Return current UNIX timestamp",
            "Version_date": "1.0.0, August 2022",
            'Physics': {'Type':'Other','Entity':'Other'},
            "Outputs": [
                {
                    "Name": "timestamp",
                    "Type_ID": 'mupif.DataID.PID_Time',
                    "Type": "mupif.Property",
                    "Required": False,
                    "Units": "s",
                    "ValueType": "Scalar",
                }
            ],
            "Inputs":[],
            "Solver":{
                'Software': 'Python script',
                'Language': 'Python3',
                'License': 'LGPL',
                'Creator': 'Eudoxos',
                'Version_date': '08/2022',
                'Type': 'Summator',
                'Documentation': 'Nowhere',
                'Estim_time_step_s': 1,
                'Estim_comp_time_s': 0.01,
                'Estim_execution_cost_EUR': 0.01,
                'Estim_personnel_cost_EUR': 0.01,
                'Required_expertise': 'None',
                'Accuracy': 'High',
                'Sensitivity': 'High',
                'Complexity': 'Low',
                'Robustness': 'High'
            },
            'Execution':{ 'ID': '123' }
        }
        super().__init__(metadata=MD)
        self.updateMetadata(metadata)
        self.timestamp=np.nan*mp.U.s
    def get(self,objectTypeID,time=None,objectID=''):
        if objectTypeID==mp.DataID.PID_Time:
            return mp.ConstantProperty(quantity=self.timestamp,propID=objectTypeID,time=time)
    def solveStep(self, tstep,stageID=0,runInBackground=False):
        import socket
        log.error(f'+ This is solveStep in the wf_01_a model running on {socket.getfqdn()=}')
        log.error(f'+ {os.environ["MUPIF_LOG_PYRO"]=}')
        self.timestamp=time.time()*mp.U.s
        for i in range(180):
            log.error(f'Tick is {i}/180')
            time.sleep(1)

# Eudoxos_WF_01_a.__module__='wf_01_a'

# locate nameserver
