#coding: utf8

def user_active(request):
	data = {}
	if request.user.is_authenticated():
		data['uanombrecompleto'] = request.user.get_full_name()
		data['uanombre'] = request.user.get_short_name()
		data['uausuario'] = request.user.get_username()

	
	else:
		data['uanombre'] = 'Usuario anónimo'

	return data
