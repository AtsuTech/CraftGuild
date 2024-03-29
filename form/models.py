
# Create your models here.
from django.db import models

# import parentalKey:
from modelcluster.fields import ParentalKey

# import FieldRowPanel and InlinePanel:
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PublishingPanel,
)

from wagtail.fields import RichTextField
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)

# import AbstractEmailForm and AbstractFormField:
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

# import FormSubmissionsPanel:
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.snippets.models import register_snippet

#QuestionPageモデルをインポート
#from introduction.models import QuestionPage


# ... keep the definition of NavigationSettings and FooterText. Add FormField and FormPage:
class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    #intro = RichTextField(blank=True)
    intro = models.CharField(
        verbose_name="フォームのタイトル(例:お問合せ)",
        max_length=100,
        blank=True,
        null=True,
    )
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address'),
                FieldPanel('to_address'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        #Q&Aのデータを取得しpostsに格納
        # questions = QuestionPage.objects.live().public()
        
        # context["questions"] = questions

        return context