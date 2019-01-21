import tempfile
import subprocess

import condep.prolog.converter as prolog_converter
from ..cd_event import CDEvent


def run_prolog_enivornment(cd_event:CDEvent):
    tempFileWrapepr = _setup_prolog(cd_event)
    
    subprocess.run(["swilgt","-s", "prolog/condep.lgt", "-s", tempFileWrapepr.name])#-s prolog/condep.lgt


def query_prolog(cd_event:CDEvent):
    tempFileWrapper = _setup_prolog(cd_event)

    eventName = 'eve' + str(id(cd_event))

    goal = f'state::actorOfEvent(A,{eventName}), nonvar(A), write(A)'
    try:
        proc = subprocess.Popen(
            ["swilgt",'-q',"-s", "prolog/condep.lgt", "-s", tempFileWrapper.name, '-g', f'{goal}.', '-t', 'halt'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )#-s prolog/condep.lgt
        
        return_code = proc.wait()

        if return_code == 0:
            answer = proc.communicate(timeout=15)[0].decode()
        else:
            out, errs = proc.communicate(timeout=15)
            raise ChildProcessError(errs.decode())

        return answer
    finally:
        proc.wait()


## PRIVATE

def _setup_prolog(cd_event):
    tempFileWrapepr = tempfile.NamedTemporaryFile(suffix='.lgt')

    predicates = prolog_converter.convert_to_prolog(cd_event)
    fileContents = prolog_converter.output_logtalk_file(predicates)

    with open(tempFileWrapepr.name, "w") as tempFile:
        tempFile.write(fileContents)
    return tempFileWrapepr
