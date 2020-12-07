from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on the Messages created against this Course'),
		'fieldname': 'course',
		'transactions': [
			{
				'label': _('Messages'),
				'items': ['pibiMessage']
			},
		]
	}
