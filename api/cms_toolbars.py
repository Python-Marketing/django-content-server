from cms.extensions.toolbar import ExtensionToolbar
from cms.toolbar_pool import toolbar_pool
from django.utils.translation import ugettext_lazy as _
from cms.api import get_page_draft
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from cms.utils.page_permissions import user_can_change_page
from django.urls import reverse, NoReverseMatch
from django.utils.translation import ugettext_lazy as _
from .models import PageDetailExtension


@toolbar_pool.register
class PageDetailExtensionToolbar(CMSToolbar):
    # defines the model for the current toolbar
    model = PageDetailExtension

    def populate(self):
        # always use draft if we have a page
        self.page = get_page_draft(self.request.current_page)

        if not self.page:
            # Nothing to do
            return

        if user_can_change_page(user=self.request.user, page=self.page):
            try:
                page_extension = PageDetailExtension.objects.get(extended_object_id=self.page.id)
            except PageDetailExtension.DoesNotExist:
                page_extension = None
            try:
                if page_extension:
                    url = reverse('admin:api_pagedetailextension_change', args=(page_extension.pk,))
                else:
                    url = reverse('admin:api_pagedetailextension_add') + '?extended_object=%s' % self.page.pk

                test = url
            except NoReverseMatch:
                # not in urls
                pass
            else:
                not_edit_mode = not self.toolbar.edit_mode_active
                current_page_menu = self.toolbar.get_or_create_menu('page')
                current_page_menu.add_modal_item(_('Page Extention'), url=url, disabled=not_edit_mode)