with open(r"E:\Programming\Python\python-practice\MergeEmail\Input\Names\invited_names.txt") as name :
    names = name.readlines()
    names = [line.strip() for line in names]
with open(r"E:\Programming\Python\python-practice\MergeEmail\Input\Letters\starting_letter.txt") as data :
    lines = data.readlines()
for name in names:    
    with open(rf"E:\Programming\Python\python-practice\MergeEmail\Output\ReadyToSend\{name}.txt",mode='w') as write:
        write.write(lines[0].replace("[name]", name))
        for line in lines[1:] :
            write.write(line) 

