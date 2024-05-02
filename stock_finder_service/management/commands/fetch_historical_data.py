from django.core.management.base import BaseCommand
from stock_finder_service.models import HistoricalCandleData
from upstox_service.utils import fetch_historic_data


class Command(BaseCommand):
    help = 'Fetch and store historical stock data'

    def handle(self, *args, **options):
        data = fetch_historic_data('api_key', 'access_token', 'instrument_key', 'start_date', 'end_date')

        for entry in data:
            HistoricalCandleData.objects.create(
                instrument_key='instrument_key',
                interval='day',
                timestamp=entry[0],
                open_price=entry[1],
                high_price=entry[2],
                low_price=entry[3],
                close_price=entry[4],
                volume=entry[5],
                open_interest=entry[6]
            )
        self.stdout.write(self.style.SUCCESS('Successfully stored historical data'))
