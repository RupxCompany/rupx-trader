from django.db import models


class HistoricalCandleData(models.Model):
    instrument_key = models.CharField(
        max_length=20, help_text="The unique identifier for the financial instrument.")
    interval = models.CharField(
        max_length=10, help_text="The time frame of the candles (1minute, 30minute, day, week, month).")
    timestamp = models.DateTimeField(
        help_text="The start time of the candle's timeframe.")
    open_price = models.DecimalField(
        max_digits=15, decimal_places=5, help_text="The opening price of the asset for the given timeframe.")
    high_price = models.DecimalField(
        max_digits=15, decimal_places=5, help_text="The highest price at which the asset traded during the timeframe.")
    low_price = models.DecimalField(max_digits=15, decimal_places=5,
                                    help_text="The lowest price at which the asset traded during the timeframe.")
    close_price = models.DecimalField(
        max_digits=15, decimal_places=5, help_text="The closing price of the asset for the given timeframe.")
    volume = models.BigIntegerField(
        help_text="The total amount of the asset that was traded during the timeframe.")
    open_interest = models.BigIntegerField(
        help_text="The total number of outstanding derivative contracts, such as options or futures.")

    class Meta:
        unique_together = ('instrument_key', 'interval', 'timestamp')

    def __str__(self):
        return f"{self.instrument_key} {self.interval} {self.timestamp}"
