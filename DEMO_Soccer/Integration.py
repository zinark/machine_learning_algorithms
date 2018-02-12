import pandas as pd
import urllib, json, urllib2, zipfile, io

from datetime import datetime


class Integration(object):
    url = "http://www.borsaistanbul.com/data/thb/{0}/{1}/thb{0}{1}{2}{3}.zip"

    @staticmethod
    def get(year, month, day):
        url = Integration.url.format(
            "{0:04d}".format(year),
            "{0:02d}".format(month),
            "{0:02d}".format(day),
            "1",  # S
        )
        print "getting", url
        response = urllib2.urlopen(url)
        content = response.read()
        zip = zipfile.ZipFile(io.BytesIO(content))
        csv = zip.read(zip.infolist()[0])
        csv = unicode(csv, "utf-8")
        df = pd.read_csv(io.StringIO(csv), sep=";")

        return df

    @staticmethod
    def download_today():
        url = "https://www.doviz.com/api/v1/stocks/all/latest"
        response = urllib.urlopen(url)
        r = response.readlines()[0]
        print r
        today = datetime.date.today()
        fname = "{0}-{1}-{2}.json".format(today.year, today.month, today.day)
        with open(fname, "w") as f:
            f.write(r)
            f.write("\n")
            f.flush()

    @staticmethod
    def dump(year):
        list = []
        for m in range(1, 12):
            for d in range(1, 31):
                try:
                    df = Integration.get(year, m, d).iloc[1:]
                    list.append(df)
                except:
                    pass

        df = pd.concat(list)
        df.to_csv(str(year) + ".csv", sep='\t', encoding='utf-8', index=False)

    @staticmethod
    def get_stock(file, code="ADEL.E"):
        df = pd.read_csv(file, sep="\t")
        df = df[["TARIH", "ISLEM  KODU", "DEGISIM (%)"]]
        df = df[df["ISLEM  KODU"] == code]
        no = [x for x in range(len(df))]
        df["no"] = no

        df.columns = ["date", "code", "diff", "no"]

        return df
