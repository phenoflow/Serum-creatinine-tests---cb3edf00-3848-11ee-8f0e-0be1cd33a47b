# Kethryn E Mansfield, Dorothea Nitsch, Liam Smeeth, Krishnan Bhaskaram, Laurie A Tomlinson, 2023.

import sys, csv, re

codes = [{"code":"4....11","system":"readv2"},{"code":"4....12","system":"readv2"},{"code":"413..00","system":"readv2"},{"code":"41B..00","system":"readv2"},{"code":"41BZ.00","system":"readv2"},{"code":"41G3.00","system":"readv2"},{"code":"41H..00","system":"readv2"},{"code":"8H7P.11","system":"readv2"},{"code":"8HP..00","system":"readv2"},{"code":"98F..00","system":"readv2"},{"code":"9b0P.00","system":"readv2"},{"code":"ZV72600","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('serum-creatinine-tests-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["serum-creatinine-tests-laboratory---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["serum-creatinine-tests-laboratory---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["serum-creatinine-tests-laboratory---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
