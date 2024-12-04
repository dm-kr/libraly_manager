from datetime import datetime, timedelta

a = ["asasdadasdsad" for _ in range(100_000_000)]

start = datetime.now()

for item in a:
    str(item)

end = datetime.now() - start

print(end)

a = [x for x in range(100_000_000)]

start = datetime.now()

for item in a:
    str(item)

end = datetime.now() - start

print(end)
