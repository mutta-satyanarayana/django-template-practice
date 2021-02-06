from django.shortcuts import render
from datetime import datetime

# Create your views here.
def display(request):
	name = 'Narayana'
	doing = 'Django Practice'
	num = 10
	desc = "django is a python-based free and open-source web framework that follows the model-template-views architectural pattern. It is maintained by the Django Software Foundation, an American independent organization established as a 501 non-profit."
	status = "Narayana"
	status1 = ""
	list1= ['1',"2",3,(1,2,3)]
	list2 = []
	date = datetime.now()
	float_value = 15.56102
	float_value1 = 21.3333333
	test = [{"foo":[1,2,3],'bar':[4,5,6]},{"baz":[7,8,9]}]
	data1 = {
		'one' :{"one1": "ramu", "one2":'ram_value'},
		'two' :{"two1": "sitha", "two2":'sitha_value'},
		'three' :{"three1": "kiran", "three2":'kiran_value'},
	}
	return render(request, 'app/display.html', {'name': name, 'doing' : doing, 'num': num,
	 'desc': desc, 'status':status,"status1":status1, 'list1': list1, 'date':date,
	 'float_value':float_value, "float_value1":float_value1, "test":test, 'list2':list2, 'data1':data1})