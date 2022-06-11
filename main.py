import ssl
ssl._create_default_https_context = ssl._create_unverified_context
try:
    from googlesearch import *
except ImportError:
    print("No module named 'google' found")

tender_results = []

#to search
def main(tender_results):
    prefix = "filetype:pdf https://www.emservices.com.sg/wp-content/uploads/"
    year = int(input("Enter year: "))
    query = prefix + str(year) + '/'
    count = 0
    find_links(query, tender_results, count)
    add(tender_results)

def add(tender_results):
    with open('Tender Results.txt', 'a+') as f:
        #keeping track of duplicates
        check = []
        f.seek(0)
        contents = f.readlines()
        for content in contents:
            line = content[content.index('k') + 3:len(content)].strip()
            check.append(line)

        print("Tenders scraped: ")
        for tender in tender_results:
            print(tender)
        print()

        new = 0
        num = len(check)
        output = []
        for tender in tender_results:
            if tender not in check:
                #adding
                f.write(f"ID: {num + 1}, Link: {tender}")
                f.write('\n')
                num += 1
                new += 1
                output.append(tender)

        print(f"Number of new tenders added: {new}")
        print("New tenders added: ")
        for new_tender in output:
            print(new_tender)
        print()
        print(f"Number of tenders in database: {num}")
        print("Displaying tenders in database:")
        print()

        f.seek(0)
        display = f.readlines()
        for info in display:
            print(info)

def find_links(query, tender_results, count):
    for j in search(query, tld="co.in", num=11, stop=11, pause=2):
        tender = j[49:-4]
        if '.' not in tender and '_' not in tender:
            tender_results.append(j)
            count += 1
    print(f"Number of tenders scraped: {count}")

main(tender_results)

