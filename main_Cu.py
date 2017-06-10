from tracing import *

from tools_setup import SetupTools as st
from tools import Tools as tl
import numpy as np
import math as m

import time

t = time.time()

c = Crystal(d=1.5414, D=2.4, r=38, loc=[5.619336625089284, 0, 29.469018577040025], rc=1)
s = Source(loc=[0, 0, 0], wavelength=tl.ang_from_kev(8.0478), intensity=1000, number=1000000)
d = Detector(dim=[1, 1], loc=[15.344294488940394, 0.0, -21.53076717546531], res=50)
dm = Detector(dim=[1, 1], loc=[14.870837373296506, 0.0, -19.04785549616726], res=50)
ds = Detector(dim=[1, 1], loc=[15.81775160458428, 0.0, -24.013678854763363], res=50)

print('Bragg: {}'.format(tl.deg_from_rad(c.bragg_angle(s.wl, 2))))

print(s.wl)

# st.display_source(s)

# SETUPS
# setup = SetUp(source=[s], crystal=c, detector=d)
# setup.work()
# setup = SetUp(source=[s], crystal=c, detector=dm)
# setup.work()
# setup = SetUp(source=[s], crystal=c, detector=ds)
# setup.work()

st.display_crystal(c)
st.adjustment(c, z_dist=30, oq=51.92)
print('Final elapsed time: {}s'.format(int(time.time() - t)))
