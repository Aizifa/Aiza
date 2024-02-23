import datetime
orig = datetime.datetime.now()
print(f'original datetime: {orig}')
without_microsec = orig.replace(microsecond=0)
print(f'without_microsecond: {without_microsec}')
