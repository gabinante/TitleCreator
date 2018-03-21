import random

Prefixlist = ['Viceroy','Commandant', 'Grand Poo-Bah', 'Archon', 'Duke', 'Chancellor', 'President', 'Marquis', 'Earl', 'Director', 'Chair', 'Head', 'Senior Director']

Prefixlist2 = ['Principal','Chief','Head','Lead', 'Senior', 'Master']

Joblist = ['Solutions', 'Systems', 'Network', 'Security', 'Compliance', 'Information', 'Scalability', 'Thought']

Postfixlist = ['Engineer', 'Architect', 'Designer', 'Consultant', 'Manager', 'Officer', 'Leader', 'Janitor']

Postfixlist2 = ['Engineering', 'Management', 'Development', 'Deployment', 'Technical Training', 'Operations', 'Architecture', 'Infrastructure', 'Technology', 'Administration', 'Management', 'Computational Analytics', 'Database Administration']

RandomDecider = random.randint(0, 1)
RandomPre = random.choice(Prefixlist)
RandomPre2 = random.choice(Prefixlist2)
RandomJob = random.choice(Joblist)
RandomPost = random.choice(Postfixlist)
RandomPost2 = random.choice(Postfixlist2)

print("Congratulations! Your new title is:")

if RandomDecider == 1:
  print(RandomPre + ' of ' + RandomJob + ' ' + RandomPost2)

else:
  print(RandomPre2 + ' ' + RandomJob + ' ' + RandomPost)
