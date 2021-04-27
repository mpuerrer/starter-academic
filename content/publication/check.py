import glob



files = glob.glob('*/index.md')
for f in files:
    print('*'*80)
    print(f)
    print('*'*80)
    in_authors = False
    with open(f, 'r') as fp:
        for line in fp:
            if 'authors:' in line:
                in_authors = True
                continue
            if in_authors and line[0] != '-':
                in_authors = False
            if in_authors:
                print(line.strip())
    print()

