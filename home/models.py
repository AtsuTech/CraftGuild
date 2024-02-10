from django.db import models

from wagtail.models import Page


class HomePage(Page):
    subpage_types = [
        #(アプリ名).(モデル名)
        "mentor.MentorIntroductionPage",
        "form.FormPage",
        "contents.ContentsSelectingPage",
        "creation_flow.CreationFlow",
        "learn.LearnItemList",
        "particular.Particular",
        "price_plan.PricePlan",
        "price_plan.PriceDescription",
        "trial_flow.TrialFlow",
        "question.Question",
    ]

    def get_admin_display_title(self):
        return "CraftGuild"
