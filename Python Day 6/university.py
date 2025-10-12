university = "Bahria University karachi campus"
words = university.split()
uniName = words[0] + " " + words[1]
campus = words[2].title() + " " + words[3].title()

""" here in above the title is used because we
 didn't capitalize the campus name in the original
string so for the capitalization we use title method """

sentence = (" come to university daily")


print(f'''University Name: {uniName}
Campus: {campus.title()}
rule: {sentence.upper()}
''')