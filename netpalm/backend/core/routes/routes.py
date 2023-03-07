# load plugins
from netpalm.backend.core.calls.dryrun.dryrun import dryrun
from netpalm.backend.core.calls.getconfig.exec_command import exec_command
from netpalm.backend.core.calls.getconfig.ncclient_get import ncclient_get
from netpalm.backend.core.calls.scriptrunner.script import script_kiddy
from netpalm.backend.core.calls.service.procedures import (
    create,
    update,
    delete,
    re_deploy,
    validate,
    health_check,
)
from netpalm.backend.core.calls.setconfig.exec_config import exec_config
from netpalm.backend.core.utilities.jinja2.j2 import j2gettemplate
from netpalm.backend.core.utilities.jinja2.j2 import render_j2template
from netpalm.backend.core.utilities.ls.ls import list_files
from netpalm.backend.core.utilities.textfsm.template import (
    listtemplates,
    pushtemplate,
    addtemplate,
    removetemplate,
    gettemplate,
)

routes = {
    "getconfig": exec_command,
    "setconfig": exec_config,
    "listtemplates": listtemplates,
    "gettemplate": gettemplate,  # replace with universal template mgr get_template in future
    "addtemplate": addtemplate,
    "pushtemplate": pushtemplate,
    "removetemplate": removetemplate,
    "ls": list_files,
    "script": script_kiddy,
    "j2gettemplate": j2gettemplate,
    "render_j2template": render_j2template,
    "dryrun": dryrun,
    "ncclient_get": ncclient_get,
    "service_create": create,
    "service_update": update,
    "service_delete": delete,
    "service_re_deploy": re_deploy,
    "service_validate": validate,
    "service_health_check": health_check,
}
