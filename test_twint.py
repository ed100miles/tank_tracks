import twint
import csv
import requests
import os
import tqdm

locations = {
    "donetsk": ('Donetsk', "48.0149464,37.897126"),
    "kharkiv": ("Kharkiv","50.069101,36.2497915")
    }

radius = "50km"

for location in locations:
    location_name = locations[location][0]
    location_long_lats = locations[location][1]

    print(f"Scraping {location_name}")

    datapath = f'{os.getcwd()}/Data'
    location_path = f'{os.getcwd()}/Data/{location_name}'
    imgs_path = f'{os.getcwd()}/Data/{location_name}/imgs/'
    csvs_path = f'{os.getcwd()}/Data/{location_name}/csvs/'

    dirs = [datapath, location_path, imgs_path, csvs_path]

    for dir in dirs:
        if not os.path.isdir(dir):
            os.mkdir(dir)

    c = twint.Config()
    c.Images = True
    c.Geo = f"{location_long_lats},{radius}"
    c.Filter_retweets = True
    c.Store_csv = True
    c.Output = f"{csvs_path}/raw_tweets.csv"
    c.Since = "2022-02-24"
    c.Until = "2022-02-25"
    c.Hide_output = True
    twint.run.Search(c)

    with open(f"{csvs_path}/raw_tweets.csv", "r") as file:
        reader = csv.reader(file)
        with open(f"{csvs_path}/processed_tweets.csv", "w") as out_file:
            writer = csv.writer(out_file)
            for row in tqdm(reader, desc=f"{location_name}: "):
                writer.writerow(
                    (row[0], row[14][1:-1], {row[3], row[4], row[9], row[11], row[26]})
                )
                try:
                    img_data = requests.get(row[14][2:-2]).content
                    with open(f"{imgs_path}/{row[2]}_{row[3]}_{row[0]}.jpg", "wb") as handler:
                        handler.write(img_data)
                except requests.exceptions.MissingSchema as e:
                    print(f"couldnt fetch image url: {row[14][1:-1]}\n{e}")
