import vcr
from functools import wraps

my_vcr = vcr.VCR(
    serializer='yaml',
    cassette_library_dir='tests/cassettes',
    record_mode='once',
    match_on=['uri', 'method'],
    path_transformer=vcr.VCR.ensure_suffix('.yaml'),
    decode_compressed_response=True,
    filter_headers=['authorization'],
)


def vcr_test(func):
    """Decorator to use VCR with dynamically generated cassette names based on the test function."""
    cassette_name = f"tests/cassettes/{func.__name__}.yaml"

    @my_vcr.use_cassette(cassette_name)
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
