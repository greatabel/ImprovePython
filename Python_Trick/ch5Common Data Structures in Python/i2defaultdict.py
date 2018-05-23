from collections import defaultdict

dd = defaultdict(list)

dd['dogs'].append('Rufus0')
dd['dogs'].append('Rufus1')
dd['dogs'].append('Rufus2')

dd['cats'].append('cat0')
dd['cats'].append('cat1')
dd['cats'].append('cat2')
print(dd['dogs'], dd['cats'])