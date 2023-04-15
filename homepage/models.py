from django.db import models
from django.utils.translation import gettext_lazy as _


class Member(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Имя"))
    phone_number = models.CharField(max_length=255, verbose_name=_("Телефон"))
    email = models.CharField(max_length=255, verbose_name=_("Эл. почта"))
    created_at = models.DateTimeField(
        verbose_name=_("Дата и время отправки заявки"),
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Клиент")
        verbose_name_plural = _("Клиенты")


class Job(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    wage = models.CharField(max_length=255)
    photo = models.ImageField(
        verbose_name="Фото",
        upload_to="photos",
        null=True,
        blank=True,
    )
    details = models.TextField()
    created_at = models.DateTimeField(
        verbose_name="Дата и время создания вакансии",
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"