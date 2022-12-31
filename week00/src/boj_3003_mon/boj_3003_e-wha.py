class old_chess:
    def __init__(self, K, Q, L, B, KN, P):
        self.mychess = [int(K), int(Q), int(L), int(B), int(KN), int(P)]
        self.chess = [1, 1, 2, 2, 2, 8]
        
    def compare(self):
        for i in range(len(self.mychess)):
            print(self.chess[i] - self.mychess[i])
    

def main():
    K, Q, L, B, KN, P = input().split()
    mychess = old_chess(K, Q, L, B, KN, P)
    mychess.compare()
    
if __name__ == "__main__":
    main()

