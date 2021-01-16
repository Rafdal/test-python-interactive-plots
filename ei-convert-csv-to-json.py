import csv, json, math, hmac, hashlib
from pathlib import Path


movdir = Path('mov')
flojdir = Path('floj')
pesodir = Path('peso')

pre = Path('PRE')
post = Path('JSON')

def dumpToJson(filename, subfolder):
    header = None
    # keep track of the first row to know the beginning timestamp
    first_row = True
    begin_ts = 0
    next_ts = 0
    values = []

    HMAC_KEY = "fed53116f20684c067774ebf9e7bcbdc"
    # Parse the CSV file
    name = filename + '.CSV'
    with open(pre / subfolder / name, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            if (not header):
                header = row
                continue

            if not begin_ts:
                begin_ts = int(row[0])
            elif not next_ts:
                next_ts = int(row[0])

            # skip over timestamp column, and add the rest
            values.append([ float(x) for x in row[1:] ])

    # empty signature (all zeros). HS256 gives 32 byte signature, and we encode in hex, so we need 64 characters here
    emptySignature = ''.join(['0'] * 64)

    # This is the Edge Impulse Data Acquisition Format, it has the protected header
    data = {
        "protected": {
            "ver": "v1",
            "alg": "HS256",
            "iat": math.floor(begin_ts / 1000) # epoch time, seconds since 1970 (the timestamp earlier was in ms.)
        },
        "signature": emptySignature,
        "payload": {
            "device_type": "CSV_IMPORTER",
            "interval_ms": next_ts - begin_ts,
            "sensors": [ { "name": x, "units": "m/s2" } for x in header[1:] ],
            "values": values
        }
    }

    # encode in JSON
    encoded = json.dumps(data)

    # sign message
    signature = hmac.new(bytes(HMAC_KEY, 'utf-8'), msg = encoded.encode('utf-8'), digestmod = hashlib.sha256).hexdigest()

    # set the signature again in the message, and encode again
    data['signature'] = signature
    encoded = json.dumps(data)

    outname = filename + '.json'
    with open(post / subfolder / outname, "w") as text_file:
        print(encoded, file=text_file)
    pass

#a


for i in range(0,256):
    name = 'PESO' + str(i)
    dumpToJson(name, pesodir)
    