from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.html import format_html
from django.views.generic import FormView
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.utils import json

from allauth.account import app_settings
from allauth.account.forms import LoginForm
from allauth.account.utils import passthrough_next_redirect_url, get_next_redirect_url
from allauth.account.views import sensitive_post_parameters_m, AjaxCapableProcessFormViewMixin, \
    RedirectAuthenticatedUserMixin
from allauth.exceptions import ImmediateHttpResponse
from allauth.utils import get_request_param, get_form_class
from cms.models import Page, reverse
from djangocms_blog.models import Post
from invoicing.models import Invoice
from tracker.models import Story, Developer, Task
from .forms import QueryForm
from .models import Post as ApiPost, Donation, Volunteer, BeautifulGumtreeQuery, GumtreeLocation, GumtreeProvince, \
    GumtreeCategory, GumtreeCategoryLabel
from .serializer import UserSerializer, PageSerializer, PostSerializer
from django.template.loader import get_template
from django.template import Context


# views.py
from django.views import generic


class QueryResultView(generic.View):

    def get(self, request, *args, **kwargs):
        query_result = get_object_or_404(BeautifulGumtreeQuery, pk=kwargs['pk'])
        context = {'query_result': query_result}
        return render(request, 'api/results.html', context)


class QueryCreateView(generic.View):

    def get(self, request, *args, **kwargs):
        form = QueryForm()
        context = {'form': form}
        return render(request, 'api/beautifulgumtreequery_form.html', context)

    def post(self, request, *args, **kwargs):
        form = QueryForm(data=request.POST)
        if form.is_valid():
            form.save()

            return render(
                request,
                'api/beautifulgumtreequery_form.html',
                {
                    'form': form,
                    'query': BeautifulGumtreeQuery.objects.all().order_by("-id")[0]
                }
            )
        return render(request, 'api/beautifulgumtreequery_form.html', {'form': form})



def add_gumtree_query(request):

   template = get_template("dashboard/add_gumtree_query.html")
   html = template.render({
       'request': request
   })
   return HttpResponse(html)

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSets define the view behavior.
class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = ApiPost.objects.all()
    serializer_class = PostSerializer


# ViewSets define the view behavior.
class SearchViewSet(viewsets.ModelViewSet):
    queryset = ApiPost.objects.all()
    serializer_class = PostSerializer


class DonateView(View):
    def get(self, *args, **kwargs):
        user = self.request.user
        response = "No entry"

        if user.is_authenticated:
            try:
                response = user.get_full_name()
            except:
                response = ''

            if self.request.GET.get('fundraiser'):
                fundraiser = Post.objects.get(id=str(self.request.GET['fundraiser']))
                try:
                    donation_check = Donation.objects.get(author=user, charity=fundraiser)
                except:
                    Donation.objects.filter(author=user, charity=fundraiser).delete()
                    donation_check = False
                if not donation_check:
                    donation = Donation(
                        author=user,
                        charity=fundraiser,
                        amount=fundraiser.amount.replace("R", ""),
                    ).save()
                response = 'Thank you ' + response + ' success'

        return HttpResponse(format_html(response), content_type='text/html', status=200)


class AddGumtreeQuery(View):
    def get(self, *args, **kwargs):
        user = self.request.user
        response = "No entry"

        return HttpResponse(format_html(response), content_type='text/html', status=200)

    def post(self, *args, **kwargs):
        user = self.request.user
        response = "No entry"

        if not user.is_authenticated:
            return HttpResponse(format_html(response), content_type='text/html', status=400)

        label = self.request.POST.get('label')
        province = self.request.POST.get('province')
        terms = self.request.POST.get('term')
        location = [loc for loc in self.request.POST.getlist('location[]') if loc]
        category = [cat for cat in self.request.POST.getlist('category[]') if cat]

        query = BeautifulGumtreeQuery()
        query.term = terms
        query.label_id = GumtreeCategoryLabel.objects.get(link=label).id
        query.province_id = GumtreeProvince.objects.get(link=province).id
        query.save()
        query.label = GumtreeCategoryLabel.objects.get(link=label)
        locations = GumtreeLocation.objects.filter(id__in=location)
        category = GumtreeCategory.objects.filter(id__in=category)
        query.location.set(locations)
        query.category.set(category)


        return HttpResponse(format_html(str(response)), content_type='text/html', status=200)


class VolunteerAjax(View):
    def get(self, *args, **kwargs):
        user = self.request.user
        response = "No entry"

        if user.is_authenticated:
            try:
                response = user.get_full_name()
            except:
                response = ''

            if self.request.GET.get('volunteer'):
                volunteer = self.request.GET.get('volunteer')
                try:
                    volunteer_check = Volunteer.objects.filter(author=user)
                except:
                    volunteer_check = False
                if not volunteer_check:
                    testimonial = Volunteer(
                        author=user,
                    ).save()
                response = 'Thank you ' + response + ' success'

        return HttpResponse(format_html(response), content_type='text/html', status=200)


class ContactAjax(View):
    def get(self, *args, **kwargs):

        response = "No entry"
        name = self.request.GET.get('name')
        subject = self.request.GET.get('subject')
        email = self.request.GET.get('email')
        phone = self.request.GET.get('phone')
        message = self.request.GET.get('message')
        new_story = Story()

        if phone == "Task":

            task = Task()
            task.name = name
            task.description = message.split("=id")[1]
            task.estimate = 1
            task.iteration = 1
            task.completed = False

            task.developer = Developer.objects.get(id=1)
            try:
                task.parent_story = Story.objects.get(id=message.split("=id")[0])
                task.save()
                response = 'Updated ' + name + ' to tasks!'
            except:
                response = 'error...{}'.format(task)

        elif name and email and message:

            new_story.name = "{}".format(name)
            new_story.description = "{}\n".format(subject)
            new_story.description += "Contact {} on {} or by email {}\n".format(name, phone, email)
            new_story.description += "{}\n".format(message)
            new_story.estimate = 1
            new_story.save()
            response = 'Thank you ' + name + ' We will contact you shortly'

        return HttpResponse(format_html(response), content_type='text/html', status=200)

# Under development
def create_invoice():
    from datetime import date
    today = date.today().isoformat()

    customer = {
        "invoice":
            {
                'type': 'Invoice',
                # INVOICE/Invoice ADVANCE/Advance invoice PROFORMA/Proforma invoice CREDIT_NOTE/Credit note
                'sequence': 1,
                'number': 1,  # invoice number
                'status': 'NEW',
                'subtitle': 'Invoice for name',
                'note': 'Thank you',
                'date_issue': today,
                'date_tax_point': today,  # time of supply
                'date_due': today,
                'currency': 'R',
                'credit': '0.00',
                'payment_method': 'CASH',
                'constant_symbol': '0008',
                'reference': 'referenceno',
                'issuer_name': 'issuer_name',
                'issuer_email': '',
                'issuer_phone': '',
                'customer_name': '',
                'customer_street': '',
                'customer_zip': '',
                'customer_city': '',
                'customer_country': '',
                'customer_additional_info': '',
                'customer_email': '',
                'customer_phone': '',
                'customer_registration_id': 1,
                'customer_tax_id': 1,
                'customer_vat_id': 1
            }
    }

    bank = {
        'bank_name': 'Example bank',
        'bank_street': 'Example street',
        'bank_zip': 'Example ZIP code',
        'bank_city': 'Example city',
        'bank_country': 'SK',
        'bank_iban': 'SK0000000000000000000028',
        'bank_swift_bic': 'EXAMPLEBANK'
    }

    supplier = {
        'supplier_name': 'Jody Beggs',
        'supplier_street': 'Internet',
        'supplier_city': 'Johannesburg',
        'supplier_zip': '3214',
        'supplier_country': 'ZA',
        'supplier_registration_id': '?',
        'supplier_tax_id': 'None',
        'supplier_vat_id': 'None',
        'supplier_additional_info': json.dumps({
            "www": "www.example.com"
            # ... legal matters
        }),
    }
    customer['invoice'].update(bank)
    customer['invoice'].update(supplier)
    invoice = Invoice(**customer['invoice'])

    invoice.save()
    return True


class SocialLoginView(RedirectAuthenticatedUserMixin,
                      AjaxCapableProcessFormViewMixin,
                      FormView):
    form_class = LoginForm
    template_name = "account/social_login." + app_settings.TEMPLATE_EXTENSION
    success_url = None
    redirect_field_name = "next"

    @sensitive_post_parameters_m
    def dispatch(self, request, *args, **kwargs):
        return super(SocialLoginView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(SocialLoginView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_form_class(self):
        return get_form_class(app_settings.FORMS, 'login', self.form_class)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            return form.login(self.request, redirect_url=success_url)
        except ImmediateHttpResponse as e:
            return e.response

    def get_success_url(self):
        # Explicitly passed ?next= URL takes precedence
        ret = (get_next_redirect_url(
            self.request,
            self.redirect_field_name) or self.success_url)
        return ret

    def get_context_data(self, **kwargs):
        ret = super(SocialLoginView, self).get_context_data(**kwargs)
        signup_url = passthrough_next_redirect_url(self.request,
                                                   reverse("account_signup"),
                                                   self.redirect_field_name)
        redirect_field_value = get_request_param(self.request,
                                                 self.redirect_field_name)
        site = get_current_site(self.request)

        ret.update({"signup_url": signup_url,
                    "site": site,
                    "redirect_field_name": self.redirect_field_name,
                    "redirect_field_value": redirect_field_value})
        return ret


class RecordAudioAjax(View):
    def get(self, *args, **kwargs):
        response = "No entry"
        return HttpResponse(format_html(response), content_type='text/html', status=200)

    def post(self, *args, **kwargs):
        response = "No entry"

        audio_file = self.request.FILES['audio_data']
        reason = self.request.POST.get('reason')
        try:
            reason = int(reason)
        except:
            reason = 1
        task = Task()
        task.name = "Voice message"
        task.description = 'Voice message'
        task.estimate = 1
        task.iteration = 1
        task.completed = False
        task.audio_file = audio_file
        task.developer = Developer.objects.get(id=1)

        task.parent_story = Story.objects.get(id=reason)
        task.save()
        return HttpResponse(format_html(response), content_type='text/html', status=200)


social_login = SocialLoginView.as_view()
