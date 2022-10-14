import sys
import mupif as mp
import numpy as np
import logging
log=logging.getLogger()

import time as timeT
start = timeT.time()

#log.info('Timer started')


class Eudoxos_WF_01(mp.Workflow):
    def __init__(self, metadata=None):
        MD = {
            'Name': 'Test workflow #01',
            'ID': 'Eudoxos_WF_01-ver1.0.0',
            'Description': 'Testing only',
            'Version_date': '1.0.0, August 2022',
            'Inputs': [
            ],
            'Outputs': [
                {'Type': 'mupif.Property', 'Type_ID': 'mupif.DataID.PID_Time', 'Name': 'UNIX time since epoch',
                 'Description': 'UNIX time since epoch', 'Units': 's', 'Origin': 'Simulated', "ValueType": "Scalar"}
            ],
            'Models': [
                {
                    'Name': 'm1',
                    'Jobmanager': 'eudoxos/wf-01-a'
                }
            ]
        }

        super().__init__(metadata=MD)
        self.updateMetadata(metadata)
        self.timestamp = mp.ConstantProperty(value=np.nan, propID=mp.DataID.PID_Time, valueType=mp.ValueType.Scalar, unit=mp.U.s, time=0*mp.U.s)
    def solveStep(self, istep, stageID=0, runInBackground=False):
        self.getModel('m1').solveStep(istep)
        self.timestamp = self.getModel('m1').get(mp.DataID.PID_Time,istep.getTime())
        log.info(f'Timestamp from model: {self.timestamp}')
    def get(self, objectTypeID, time=None, objectID=""):
        if objectTypeID == mp.DataID.PID_Time:
            return mp.ConstantProperty(value=self.timestamp.getValue(time), propID=mp.DataID.PID_Time, valueType=mp.ValueType.Scalar, unit=mp.U.s, time=time)
        else:
            raise mp.APIError('Unknown property ID')
    def set(self, obj, objectID=""):
        if obj.isInstance(mp.Property):
            super().set(obj=obj, objectID=objectID)
    def getCriticalTimeStep(self): return 1*mp.U.s

if __name__ == '__main__':
    targetTime = 1.*mp.U.s
    demo = Eudoxos_WF_01()
    executionMetadata = {'Execution':{'ID': '1','Use_case_ID': '1_1','Task_ID': '1'}}
    demo.initialize(metadata=executionMetadata,validateMetaData=False)
    demo.validateMetadata(mp.workflow.WorkflowSchema)
    demo.set(mp.ConstantProperty(value=targetTime, propID=mp.DataID.PID_Time, valueType=mp.ValueType.Scalar, unit=mp.U.s), objectID='targetTime')
    demo.solve()
    timestamp = demo.get(mp.DataID.PID_Time, targetTime)
    demo.terminate()
    log.info(f'{timestamp=}')
