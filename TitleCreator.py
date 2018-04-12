# We're now approaching enterprise grade.
from random import seed, choice

seed()

def ofprefix():
    l = ['Viceroy', 'Commandant', 'Grand Poo-Bah', 'Archon', 'Duke', 'Chancellor', 'President', 'Marquis',
            'Earl', 'Director', 'Chair', 'Head', 'Senior Director', 'Vice President', 'Dark Lord',
            'Dread Lord', 'Czar', 'Emperor', 'Baron', 'Guru', 'Administrator']
    return choice(l)

def prefix():
    l = ['Principal', 'Chief', 'Head', 'Lead', 'Senior', 'Master', 'Arch', 'Grand', 'Premier']
    return choice(l)

def job():
    l = ['Solutions', 'Systems', 'Network', 'Security', 'Compliance', 'Information', 'Scalability',
            'Database', 'Platform', 'Storage', 'Cloud', 'DevOps', 'Blockchain', 'Serverless']
    return choice(l)

def ofpostfix():
    l = ['Engineering',
            'Management', 'Development', 'Deployment', 'Technical Training', 'Operations', 'Architecture',
            'Infrastructure', 'Technology', 'Administration', 'Thought Leadership', 'Shiny Things']
    return choice(l)

def postfix():
    l = ['Engineer', 'Architect', 'Designer', 'Consultant', 'Manager', 'Officer', 'Leader', 'Janitor', 'Plumber']
    return choice(l)

def ofornot():
    l = ['1', '0']
    return choice(l)

print("Congratulations! Your new title is:")
if ofornot() == '1':
    print(ofprefix() + ' of ' + job() + ' ' + ofpostfix())
else:
    print(prefix() + ' ' + job() + ' ' + postfix())
