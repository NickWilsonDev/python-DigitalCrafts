# Person.py

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.greeting_list = set()

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1
        self.greeting_list.add(other_person)
            

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" %(self.name, self.email, self.name, self.phone)

    def add_friend(self, person):
        self.friends.append(person)

    def num_friends(self):
        return len(self.friends)

    def num_unique_people_greeted(self):
        return len(self.greeting_list)


sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)

print sonny.email + ' ' + sonny.phone
print jordan.email + ' ' +jordan.phone

jordan.friends.append(sonny)
sonny.friends.append(jordan)

sonny.greet(jordan)
print sonny.num_unique_people_greeted()

nick = Person('nick', 'asdf@a.com', '123-456-7890')
sonny.greet(nick)

print sonny.friends
print sonny.num_unique_people_greeted()
