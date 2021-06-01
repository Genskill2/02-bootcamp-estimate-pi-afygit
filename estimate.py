import math
import unittest

def monte_carlo(n):
    poi_in_cir=0
    poi_in_sqr=0
    for i in range(n**2):  #since we need both x and y coordinates
        x_rand=random.uniform(-1,1)
        y_rand=random.uniform(-1,1)
        in_circ=((x_rand)**2+(y_rand)**2)**0.5
        if in_circ<=1:
            poi_in_cir+=1
        else:
            poi_in_sqr+=1
            
    pi_mon=(poi_in_cir/poi_in_sqr)*4
    return pi_mon

def wallis(n):
    pi_wal_half=1
    for i in range(1,n):
        pi_wal_half*=((2*n)**2)/(((2*n)-1)*((2*n)+1))
        
    p_wal =(pi_wal_half*2)
    return p_wal

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
