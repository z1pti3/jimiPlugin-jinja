from core import plugin, model

class _jinja(plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        model.registerModel("jinjaFormat","_jinjaFormat","_action","plugins.jinja.models.action")
        return True

    def uninstall(self):
        # deregister models
        model.deregisterModel("jinjaFormat","_jinjaFormat","_action","plugins.jinja.models.action")
        return True
    
    def upgrade(self,LatestPluginVersion):
        # if self.version < 1.2:
        #     model.registerModel("scriptBlock","_scriptBlock","_action","plugins.script.models.action")
        return True
