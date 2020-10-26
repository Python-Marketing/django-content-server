# Python Django Test

### Please note this is a simplified version

Code [Source](python_test.py)

The link above to to the working code


#### Question 1
You are given an integer followed by n email addresses in a text file. Your task is to print a list containing only valid email addresses in lexicographical order.


Email list [Source](emails.csv)
```
Answer
def valid_emails(email_list=[]):
    for email in email_list:
        try:
            validate_email(email)
        except:
            emails.remove(email)
    return sorted(email_list, key=str.lower)

lexicographical_order = valid_emails(emails)
```


#### Question 2
You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as 0. Output a single line, the integer value of the maximum level of nesting in the XML document.

XML [Source](test.xml)
```
def maximum_depth(self, xml=False, level=-1, max_depth=0):
    if xml:
        xml_root = xml.getroot()
    else:
        xml_root = {}

    """function to get the maxdepth"""
    if level == max_depth:
        max_depth += 1
        '''
        Being recursive it was hard to get at the variable value

        So I used self to pass the anser back
        '''
        self.max_depth = max_depth

    # recursive call to function to get the depth
    for child in xml_root:
        maximum_depth(self, child, level + 1, max_depth)

maximum_depth(xml)
print(str(self.max_depth))
```

#### Question 3
Given a n space-separated integers as input, create a tuple t, of those n integers. Then compute and print the result of hash(t).

```

input_string = '1 2'

def computed_hash(input_string):
    t = tuple(input_string.split(' '))
    return hash(t)

hashed_integer = computed_hash(input_string)
print(str(hashed_integer))

```


#### Question 4
You are given some information about N people in a text file. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person&#39;s name should be printed first. For two people of the same age, print them in the order of their input.

Person [Source](persons.csv)

```
def people(persons):
    """Simple sort by the age"""
    sorted_list = sorted(persons, key=lambda k: k['age'])
    return sorted_list

sorted_people = people(people_list)
print(str(sorted_people))

```
#### Question 5
You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer, i.e. the integer if reversed does not change its value, e.g. 121 is a palindrom integer.

```

def palindrome_integer(string):
    """Split string and loop"""
    integers = string.split(" ")
    for integer in integers:
        reverse = str(int)[::-1]
        '''Check if not palindrome then return False'''
        if integer != reverse:
            return False
    return True

input_string = '121 12'
palindrome = palindrome_integer(input_string)
print(str(palindrome))

```

#### Question 6
In Django backend, how can you limit admin access so that the objects can only be edited by those users who have created them?


```
1.
We could use auth directly

from django.contrib.auth.models import User
user = User.objects.get(id=1)
perm = user.has_perm('auth.edit_object')

2.
Or a function on the request

from django.core.exceptions import PermissionDenied

def user_edit_object(request):
    if not request.user.has_perm('auth.edit_object'):
        raise PermissionDenied()

3.
Or use the decorator

from django.contrib.auth.decorators import permission_required
@permission_required('auth.view_user')
def user_edit_object(request):
    pass

```


#### Question 7
How do you set/unset a session in django views?
```
# Setting the session variable
request.session['key'] = 'value'

# unsetting the session variable
del request.session['key']

```
#### Question 8
In less than 5 sentences, explain the Architectural pattern of Django?

```
Django MVC.

Django model view controller layout makes it simple to setup the layout of the application.

Firstly the model is used as a mediator of sorts between the web interface and the database.

Then the view contains the components needed. I.E. html, css and javascript

The controller manages the whole process by selecting the view component requested by the user.
```

#### Question 9
What is the difference between a Project and an App?

```

A project is the the whole application, the sum of its parts.

The app is a component of the projects. And must be in the settings file in INSTALLED_APPS

```

#### Question 10
What is a Meta Class in Django? Give three situations where you would use it.

```
 1. The internal class is a namespace used to share data amongst all the instances
 
 2. The model meta options can be used to change the database table name or the related name.
 Used for sorting

 3. Class Meta is code logic where the model.fields meet the form.widgets.
 So under Class Meta() a link is create between your model fields and the widgets wanted in the form.

```

## Completed by Jody Beggs
