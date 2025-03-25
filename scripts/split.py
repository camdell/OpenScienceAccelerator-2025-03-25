from pathlib import Path
from csv import reader as csv_reader, writer as csv_writer
from json import dump

data_dir_orig  = Path('data', 'original')
data_dir_deriv = Path('data', 'derived')
data_dir_deriv.mkdir(exist_ok=True)

with open(data_dir_orig / 'open-meteo-38.56N121.55W22m.original.csv', mode='r') as f:
    reader = csv_reader(f)
    meta_header = next(reader)
    meta_body = next(reader)

    metadata = dict(zip(meta_header, meta_body))
    with open(data_dir_deriv / 'metadata.json', 'w') as metadata_f:
        dump(metadata, metadata_f, indent=2)

    with open(data_dir_deriv / 'weather.csv', 'w') as data_f:
        writer_f = csv_writer(data_f)

        for row in reader:
            if not row: continue
            writer_f.writerow(row)





