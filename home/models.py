from django.db import models

from wagtail.models import Page


class HomePage(Page):
    subpage_types = [
        #(アプリ名).(モデル名)
        "mentor.MentorIntroductionPage",
        "form.FormPage",
        "contents.ContentsSelectingPage",
        "introduction.QuestionListingPage",
    ]

    def get_admin_display_title(self):
        return "CraftGuild"
