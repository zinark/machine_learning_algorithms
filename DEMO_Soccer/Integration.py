import pandas as pd
import urllib, json, urllib2, zipfile, io

from datetime import datetime, date, timedelta


class Integration(object):
    url = "http://www.borsaistanbul.com/data/thb/{0}/{1}/thb{0}{1}{2}{3}.zip"

    def __init__(self, file):
        df = pd.read_csv(file, sep="\t")
        df = df[["TARIH", "ISLEM  KODU", "DEGISIM (%)"]]
        no = [x for x in range(len(df))]
        df["no"] = no
        df.columns = ["date", "code", "diff", "no"]
        self.df = df

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
    def dump(filename="output.csv", years=[2017]):
        list = []
        for year in years:
            for m in range(1, 12):
                for d in range(1, 31):
                    try:
                        df = Integration.get(year, m, d).iloc[1:]
                        list.append(df)
                    except:
                        pass

        df = pd.concat(list)
        df.to_csv(filename, sep='\t', encoding='utf-8', index=False)

    @staticmethod
    def dump_range(filename="output.csv", d1=datetime.today(), d2=datetime.today()):
        delta = d2 - d1
        dates = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]
        list = []

        for dt in dates:
            m = dt.month
            d = dt.day
            y = dt.year
            try:
                df = Integration.get(y, m, d).iloc[1:]
                list.append(df)
            except:
                pass

        df = pd.concat(list)
        df.to_csv(filename, sep='\t', encoding='utf-8', index=False)

    def get_stock(self, code="ADEL.E"):
        df = self.df
        result = df[df["code"] == code]
        return result
