from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import PsychologicalTestResult
from .serializers import PsychologicalTestResultSerializer
from .utils import send_sms
from Accounts.models import UserTrustedContact
from Accounts.models import UserProfile


class SubmitTestResultView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PsychologicalTestResultSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save(user=request.user)
            risk = result.risk_level

            if risk == 'high':
                try:
                    trusted_link = UserTrustedContact.objects.get(user=request.user)

                    message = (
                        f"هشدار: {request.user.name} {request.user.last_name} در وضعیت پرخطر روانی قرار دارد. "
                        f"این پیام برای فرد معتمد {trusted_link.trusted_name} {trusted_link.trusted_lastname} ارسال شده است. "
                        f"لطفاً با شماره {trusted_link.trusted_phone_number} تماس بگیرید."
                    )
                    send_sms(trusted_link.trusted_phone_number, message)
                except UserTrustedContact.DoesNotExist:
                    print("فرد معتمد برای این کاربر ثبت نشده.")

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
