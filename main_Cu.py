from tracing import *

from tools_setup import SetupTools as st
from tools import Tools as tl
import numpy as np
import math as m

import time

t = time.time()

c = Crystal(d=1.5414, D=2.4, r=38, loc=[0.9468818588710745, 0, 29.98505318896968], rc=1)
s = Source(loc=[0, 0, 0], wavelength=tl.ang_from_kev(8.0478), photon_count=1000, number=500000)


d = Detector(dim=[1, 1], loc=[2.582407536995195, 0.0, -21.80738954401], res=50)
dm = Detector(dim=[1, 1], loc=[2.5801846299221762, 0.0, -21.73699640447085], res=5)
ds = Detector(dim=[1, 1], loc=[2.5846304440682135, 0.0, -21.87778268354915], res=5)

print('Bragg: {}'.format(tl.deg_from_rad(c.bragg_angle(s.wl, 2))))


# st.display_source(s)
s=st.generate_eliptical_source([0.005,0.005], 20)
# SETUPS
setup = SetUp(source=s, crystal=c, detector=d)
setup.work()
# setup = SetUp(source=[s], crystal=c, detector=dm)
# setup.work()
# setup = SetUp(source=[s], crystal=c, detector=ds)
# setup.work()

st.display_crystal(c)
# st.adjustment(c, z_dist=30, oq=51.92)
print('Final elapsed time: {}s'.format(int(time.time() - t)))
