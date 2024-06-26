from django.urls import path

from .views import (
    MailingCreateView,
    MailingListView,
    MailingRetrieveView,
)

urlpatterns = [
    path("mailings/send/", MailingCreateView.as_view(), name="send-mailing"),
    path("mailings/", MailingListView.as_view(), name="get-mailings"),
    path("mailings/<int:pk>/", MailingRetrieveView.as_view(), name="get-mailing-by-id"),
]
