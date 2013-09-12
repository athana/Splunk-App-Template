from splunk.clilib import cli_common as cli

cfg = cli.getConfStanza('setup', 'mystanza')

MY_SERVER_URL = 'http://' + cfg.get('server') + ':' + cfg.get('port')

LOOKUP_INPUT_FIELD = cfg.get('lookup_input_field')
LOOKUP_OUTPUT_FIELDS = cfg.get('lookup_output_fields')