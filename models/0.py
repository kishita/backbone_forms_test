if request.is_local:
	from gluon.custom_import import track_changes
	track_changes(True)