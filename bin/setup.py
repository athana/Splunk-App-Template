import splunk.admin as admin
import splunk.entity as en

class ConfigApp(admin.MConfigHandler):
	'''
	Setup supported arguments
	'''
	def setup(self):
		if self.requestedAction == admin.ACTION_EDIT:
			for arg in ['server', 'port', 'lookup_input_field', 'lookup_output_fields']:
				self.supportedArgs.addOptArg(arg)

	'''
	Read initial values
	'''
	def handleList(self, confInfo):
		confDict = self.readConf("setup")
		if None != confDict:
			for stanza, settings in confDict.items():
				for key, val in settings.items():
					if key in ['server', 'port', 'lookup_input_field', 'lookup_output_fields'] and val in [None, '']:
						val = ''
					confInfo[stanza].append(key, val)

	def handleEdit(self, confInfo):
		name = self.callerArgs.id
		args = self.callerArgs

		if self.callerArgs.data['server'][0] in [None, '']:
			self.callerArgs.data['server'][0] = ''

		if self.callerArgs.data['port'][0] in [None, '']:
			self.callerArgs.data['port'][0] = ''

		if self.callerArgs.data['lookup_input_field'][0] in [None, '']:
			self.callerArgs.data['lookup_input_field'][0] = ''

		if self.callerArgs.data['lookup_output_fields'][0] in [None, '']:
			self.callerArgs.data['lookup_output_fields'][0] = ''

		self.writeConf('setup', 'mystanza', self.callerArgs.data)

admin.init(ConfigApp, admin.CONTEXT_NONE)