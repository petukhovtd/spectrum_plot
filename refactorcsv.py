def re_factory_csv(file_name):
    out_file_name = file_name[0:-4] + "_r.csv"
    with open(file_name, 'r') as in_file:
        with open(out_file_name, 'w') as out_file:
            count = 0
            for line in in_file:
                if count == 0:
                    new_line = line.replace(';', ',')
                else:
                    new_line_temp = line.replace(',', '.')
                    new_line = new_line_temp.replace(';', ',')
                count = count + 1
                out_file.write(new_line)
    return out_file_name


if __name__ == "__main__":
    file_name = input("Input csv file name: ")
    new_file_name = re_factory_csv(file_name)
    print("Refactory to: ", new_file_name)
