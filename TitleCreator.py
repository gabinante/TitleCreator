from random import seed, randchoice

# make enterprise level
seed()

def prefix():
    l = ['Viceroy', 'Commandant', 'Grand Poo-Bah', 'Archon', 'Duke', 'Chancellor', 'President', 'Marquis', 
            'Earl', 'Director', 'Chair', 'Head', 'Senior Director', 'Vice President', 'Principal', 'Chief', 
            'Head', 'Lead', 'Senior', 'Master', 'Dark Lord',]
    return randchoice(l)

def job():
    l = ['Solutions', 'Systems', 'Network', 'Security', 'Compliance', 'Information', 'Scalability', 
            'Thought', 'Database', 'Platform', 'Storage', 'Cloud']
    return randchoice(l)

def postfix():
    l = ['Engineer', 'Architect', 'Designer', 'Consultant', 'Manager', 'Officer', 'Leader', 'Janitor', 'Engineering',
            'Management', 'Development', 'Deployment', 'Technical Training', 'Operations', 'Architecture', 
            'Infrastructure', 'Technology', 'Administration', 'Leadership']
    return randchoice(l)

print("Congratulations! Your new title is:")

print(prefix() + ' of ' + job() + ' ' + postfix())
