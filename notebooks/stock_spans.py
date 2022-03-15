import time

def simple_stock_span(quotes: list[float]) -> list[int]:
    spans = []
    for i in range(len(quotes)):
        k = 1
        span_end = False
        while i - k >= 0 and not span_end:
            if quotes[i - k] <= quotes[i]:
                k += 1
            else:
                span_end = True
        spans.append(k)
    return spans

def stack_stock_span(quotes: list[float]) -> list[int]:
    spans = [1]
    s = []
    s.append(0)
    for i in range(1, len(quotes)):
        while len(s) != 0 and quotes[s[-1]] <= quotes[i]:
            s.pop()
        if len(s) == 0:
            spans.append(i+1)
        else:
            spans.append(i - s[-1])
        s.append(i)
    return spans

def read_quotes(filename: str) -> tuple[list[str], list[float]]:
    dates = []
    quotes = []
    with open(filename) as quotes_file:
        for line in quotes_file:
            if line.startswith('#'):
                continue
            parts = line.split(',')
            if len(parts) != 2:
                continue
            month, day, year = parts[0].split('/')
            date = '/'.join((year, month, day))
            dates.append(date)
            quotes.append(float(parts[-1]))
    return dates, quotes

_, quotes = read_quotes("djia.csv")  # we use _ for a variable that we
# don't care to use


spans_simple = simple_stock_span(quotes)

spans_stack = stack_stock_span(quotes)

print('spans_simple == spans_stack:', spans_simple == spans_stack)