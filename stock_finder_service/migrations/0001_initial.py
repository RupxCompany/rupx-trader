# Generated by Django 5.0.4 on 2024-05-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalCandleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument_key', models.CharField(help_text='The unique identifier for the financial instrument.', max_length=20)),
                ('interval', models.CharField(help_text='The time frame of the candles (1minute, 30minute, day, week, month).', max_length=10)),
                ('timestamp', models.DateTimeField(help_text="The start time of the candle's timeframe.")),
                ('open_price', models.DecimalField(decimal_places=5, help_text='The opening price of the asset for the given timeframe.', max_digits=15)),
                ('high_price', models.DecimalField(decimal_places=5, help_text='The highest price at which the asset traded during the timeframe.', max_digits=15)),
                ('low_price', models.DecimalField(decimal_places=5, help_text='The lowest price at which the asset traded during the timeframe.', max_digits=15)),
                ('close_price', models.DecimalField(decimal_places=5, help_text='The closing price of the asset for the given timeframe.', max_digits=15)),
                ('volume', models.BigIntegerField(help_text='The total amount of the asset that was traded during the timeframe.')),
                ('open_interest', models.BigIntegerField(help_text='The total number of outstanding derivative contracts, such as options or futures.')),
            ],
            options={
                'unique_together': {('instrument_key', 'interval', 'timestamp')},
            },
        ),
    ]
