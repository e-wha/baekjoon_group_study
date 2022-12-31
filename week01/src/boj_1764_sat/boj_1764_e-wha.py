class not_heard_not_seen:
    def __init__(self, N, M, not_heard_people, not_seen_people):
        self.N = N
        self.M = M
        self.not_heard_people = not_heard_people
        self.not_seen_people = not_seen_people

    def print_people(self):
        people_1 , people_2 = set(self.not_heard_people), set(self.not_seen_people)
        nhns_people = list(people_1 & people_2)
        nhns_people.sort()
        print(len(nhns_people))
        for i in range(len(nhns_people)):
            print(nhns_people[i])
'''     people_count, nhns_people = 0, []
        for i in range(self.N):
            for j in range(self.M):
                if self.not_heard_people[i] == self.not_seen_people[j]:
                    people_count += 1
                    nhns_people.append(self.not_heard_people[i])
        print(people_count)
        nhns_people.sort()
        for k in range(len(nhns_people)):
            print(nhns_people[k])
'''
                
            

def main():
    N, M = map(int, input().split())
    not_heard_people, not_seen_people = [], []
    for i in range(N):
        people = input()
        not_heard_people.append(people)
    for j in range(M):
        people = input()
        not_seen_people.append(people)
    nhns = not_heard_not_seen(N, M, not_heard_people, not_seen_people)
    nhns.print_people()
    
if __name__ == "__main__":
    main()
    


