import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

start = "http://www.admin.ch"
df = pd.DataFrame(columns=["source", "URL", "nr_referenced"])  # create empty dataframe
# links = list()
# links.append(["http://www.admin.ch"])

lnks = ["http://www.admin.ch"]


sources = ["http://www.admin.ch"]
levels = 1


def extract_links_for_levels(sources, levels):
    for run in range(levels):
        print(f"level {run} with {len(lnks)} links")

        if len(lnks) > 10000:
            # print(lnks)
            print(f"stop due to len(lnks) > 100000.  len(links) is {len(lnks)}")
            return

        for link in lnks:
            # print(link)
            source_url = requests.get(link)
            soup = BeautifulSoup(source_url.content, "html.parser")

            try:
                deps = ["edi", "eda", "wbf", "vbs", "bk", "efd", "ejpd", "uvek", "gov"]
                weiterleitung = []

                for l in soup.find_all("a", href=True):
                    for dep in deps:
                        if (
                            (
                                l.get("href").startswith(f"https://www.{dep}.admin.ch/")
                                or l.get("href").startswith(
                                    f"http://www.{dep}.admin.ch/"
                                )
                            )
                        ) and l.get("href") not in lnks:
                            sources.append(link)
                            bla = l.get("href")
                            # print(f"append link {bla}")
                        lnks.append(l.get("href"))
                        # extract_links(link.get("href"))
                        # print(f"length of links is now {len(links)}")
                        # print(f"length of lnks is now {len(lnks)}")
                        # lnks.append(weiterleitung)
                    print(f"length of lnks is now {len(lnks)}")

            except Exception as e:
                print("Unhandled exception", e)

            # print("done running all deps for link")
            sleep(0.4)
            # links.extend(weiterleitung)
        # print("done running all links for start")
        # links.extend(weiterleitung)
    return lnks, sources, weiterleitung


# extract_links(start, links, sources)
lnks, sources, weiterleitung = extract_links_for_levels(sources, levels)
# links, sources = run_levels(sources, levels)

# df["URL"] = lnks
# df["source"] = sources

print(df.shape)
print(df.head(100))

# print(links)
print(f"number lnks is {len(lnks)}")
print(f"number sources is {len(sources)}")
print(f"number weiterleitung is {len(weiterleitung)}")
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

# from time import sleep

start = "http://www.admin.ch/gov/de/start"
df = pd.DataFrame(columns=["source", "URL"])  # create empty dataframe


def extract_links():
    links = ["http://www.admin.ch/gov/de/start"]
    sources = ["http://www.admin.ch/gov/de/start"]
    levels = 3
    for level in range(levels):
        for l in links:
            source_url = requests.get(l)
            soup = BeautifulSoup(source_url.content, "html.parser")
            deps = ["edi", "eda", "wbf", "vbs", "bk", "efd", "ejpd", "uvek", "gov"]

            for dep in deps:
                for link in soup.find_all("a", href=True):
                    try:
                        if len(links) > 100:
                            print("stop")
                            return
                        if (
                            link.get("href").startswith(f"https://www.{dep}")
                            or link.get("href").startswith(f"/de/{dep}/")
                            and link.get("href") not in links
                        ):
                            sources = sources.append(l)
                            links = links.append(link.get("href"))

                            # sleep(0.3)
                    except Exception as e:
                        print("Unhandled exception", e)
                        continue
    return links, sources


def main():
    links, sources = extract_links()
    df["URL"] = links
    df["source"] = sources
    print(df.shape)
    print(df.head())
    print(df.tail())

    # print(links)
    print(len(links))
    print(len(sources))


if __name__ == "__main__":
    main()
    
"""

"""
def extract_links(start, lnks, sources):
    # print("source url", start)

    source_url = requests.get(start)
    soup = BeautifulSoup(source_url.content, "html.parser")
    deps = ["edi", "eda", "wbf", "vbs", "bk", "efd", "ejpd", "uvek", "gov"]

    for dep in deps:
        for link in soup.find_all("a", href=True):
            try:
                if len(lnks) > 1000:
                    return
                if (
                    link.get("href").startswith(f"https://www.{dep}.admin.ch/")
                    and link.get("href") not in lnks
                ):
                    sources.append(start)
                    lnks.append(link.get("href"))
                    # extract_links(link.get("href"))
                    # sleep(0.3)
            except Exception as e:
                print("Unhandled exception", e)
"""
"""
def run_levels(sources, levels):
    # print("source url", start)

    for run in range(levels):
        print(len(lnks))
        print(f"level {run}")
        extract_links_for_levels(sources, levels)
        print(len(lnks))

    return lnks, sources
"""
