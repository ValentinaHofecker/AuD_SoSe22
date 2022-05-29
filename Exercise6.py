# Exercise 1
def transform_to_row(infile, outfile):
    with open(infile, 'r') as reader:
        content = reader.readlines()
        for line in content:
            content = line.rsplit(',')
    with open(outfile, 'w') as writer:
        for line in content:
            writer.write(line + '\n')


#transform_to_row("test.txt", "output.txt")


# Exercise 2
def add_greeting(infile, outfile):
    with open(infile, 'r') as reader:
        content = reader.readlines()
    with open(outfile, 'w') as writer:
        for line in content:
            writer.write('Hello ' + line)


#add_greeting("output.txt", "greetings.txt")


# Exercise 3
def strip_greeting(infile, outfile):
    with open(infile, 'r') as reader:
        content = reader.readlines()
        stripped_content = []
        for line in content:
            stripped_content.append(line.strip('Hello '))
    with open(outfile, 'w') as writer:
        for line in stripped_content:
            writer.write(line)


#strip_greeting("greetings.txt", "stripped.txt")


# Exercise 4
def combine_files(file1, file2, outfile):
    with open(file1, 'r') as reader:
        content1 = reader.readlines()
    with open(file2, 'r') as reader:
        content2 = reader.readlines()
    if (len(content1) is not len(content2)):
        print("Only files with the same amount of lines are accepted!")
        return
    with open(outfile, 'w') as writer:
        for line_num, line in enumerate(content1, 0):
            line = line.strip('\n')
            writer.write(line + ' ' + content2[line_num])


#combine_files("greetings.txt", "stripped2.txt", "combined.txt")
#combine_files("greetings.txt", "surnames.txt", "combined.txt")
