from rest_framework.views import APIView
from rest_framework.response import Response
from sales.models import Sales

class SummaryReportView(APIView):
    def get(self, request):
        # Generate a summary report here
        sales = Sales.objects.all()
        total_sales = sum(sale.total_sales for sale in sales)
        return Response({'total_sales': total_sales})
