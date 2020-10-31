import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_func(self) : 
       for mu in [-1,0,1,2,3,4] : 
           for sig2 in [1,2,3,4] :
              mean=0
              for i in range(100) : mean = mean + normal(mu,sig2)
              mean = mean / 100

              bar = np.sqrt(sig2/100)*st.norm.ppf( (0.99 + 1) / 2 )
              self.assertTrue( np.fabs( mean - mu )<bar, "your function appears to be sampling from the wrong distribution" )
