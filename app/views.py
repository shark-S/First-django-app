from django.shortcuts import render, HttpResponse	
import requests
import json
# Create your views here.

def index(request):
	return HttpResponse('hello World!')
def test(request):
	return HttpResponse('second view')

def profile(request):
	parseData = []
	if request.method == 'POST':
		username = request.POST.get('user')
		jsonlist = []
		req = requests.get('http://api.github.com/users/'+username)
		jsonlist.append(json.loads(req.content))
		
		userData ={}
		for data in jsonlist:
			userData['name']=data['name']
			userData['blog']=data['blog']
			userData['email']=data['email']
			userData['public_gists'] = data['public_gists']
			userData['public_repos'] = data['public_repos']
			userData['avatar_url'] = data['avatar_url']
			userData['followers'] = data['followers']
			userData['following'] = data['following']
		parseData.append(userData)
		#template_name = 'app/profile.html'
	return render(request, 'app/profile.html',{'data':parseData})
