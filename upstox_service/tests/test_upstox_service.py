import pytest
from ..upstox_service import UpstoxService
from utils.vcr_utils import vcr_test


@pytest.fixture(scope="module")
def upstox_service():
    api_key = "your_test_api_key"
    return UpstoxService(api_key=api_key)


@vcr_test
def test_fetch_historic_candle_data_success(upstox_service):
    instrument_key = "NSE_EQ|INE669E01016"
    interval = "day"
    from_date = "2021-01-01"
    to_date = "2021-01-10"
    result = upstox_service.fetch_historic_candle_data(instrument_key, interval, from_date, to_date)
    print(result)
    assert result is not None
    assert 'data' in result


@vcr_test
def test_fetch_historic_candle_data_failure(upstox_service):
    instrument_key = "invalid_instrument"
    interval = "1d"
    from_date = "2021-01-01"
    to_date = "2021-01-10"
    result = upstox_service.fetch_historic_candle_data(instrument_key, interval, from_date, to_date)
    assert result is None


@vcr_test
def test_fetch_intraday_candle_data(upstox_service):
    instrument_key = "NSE_EQ|INE669E01016"
    result = upstox_service.fetch_intraday_candle_data(instrument_key, '1minute')
    assert result is not None
    print(result)
    assert 'data' in result


@vcr_test
def test_fetch_full_market_quote(upstox_service):
    print(upstox_service.access_token)
    instrument_keys = "NSE_EQ|INE669E01016,NSE_EQ|IN2920210241"
    result = upstox_service.fetch_full_market_quote(instrument_keys)
    assert result is not None
    print(result)
    assert 'data' in result
