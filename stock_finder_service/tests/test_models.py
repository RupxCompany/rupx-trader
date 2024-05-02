from django.test import TestCase
from ..models import HistoricalCandleData
from django.utils import timezone
from datetime import datetime


class HistoricalCandleDataModelTestCase(TestCase):
    def setUp(self):
        # Set up test data
        HistoricalCandleData.objects.create(
            instrument_key='AAPL',
            interval='day',
            timestamp=timezone.make_aware(datetime(2022, 1, 1)),
            open_price=100.0,
            high_price=105.0,
            low_price=95.0,
            close_price=102.0,
            volume=100000,
            open_interest=5000
        )

    def test_historical_candle_data_creation(self):
        """Test that HistoricalCandleData model can create entries."""
        candle_data = HistoricalCandleData.objects.get(instrument_key='AAPL')
        self.assertEqual(candle_data.instrument_key, 'AAPL')
        self.assertEqual(candle_data.interval, 'day')
        self.assertEqual(candle_data.timestamp, timezone.make_aware(datetime(2022, 1, 1)))
        self.assertEqual(candle_data.open_price, 100.0)
        self.assertEqual(candle_data.high_price, 105.0)
        self.assertEqual(candle_data.low_price, 95.0)
        self.assertEqual(candle_data.close_price, 102.0)
        self.assertEqual(candle_data.volume, 100000)
        self.assertEqual(candle_data.open_interest, 5000)

    def test_historical_candle_data_str_representation(self):
        """Test that HistoricalCandleData model's __str__ method returns the expected string."""
        candle_data = HistoricalCandleData.objects.get(instrument_key='AAPL')
        expected_string = f'AAPL day {timezone.make_aware(datetime(2022, 1, 1))}'
        self.assertEqual(str(candle_data), expected_string)
