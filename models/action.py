from jinja2 import Template

import jimi

class _jinjaFormat(jimi.action._action):
    customData = dict()
    template = str()

    def doAction(self,data):
        customData = jimi.helpers.evalDict(self.customData, {"data" : data["flowData"]})
        template = jimi.helpers.evalString(self.template, {"data" : data["flowData"]})

        template = Template(template)
        renderedTemplate = template.render(data=data,customData=customData)

        return {"result" : True, "rc" : 0, "renderedTemplate" : renderedTemplate}
