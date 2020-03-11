#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Charging graph
import numpy as np
import matplotlib.pyplot as plt
plt.plot([3.7,6.07,8.02,9.03,9.72,10,10.14,10.26,10.31,10.32,10.38,10.48],[10,20,30,40,50,60,70,80,90,100,110,120])
plt.xlabel('Voltage(V)')
plt.ylabel('Time(sec)')
plt.title('Voltage vs. Time(Charging)')
plt.show()


# In[9]:


#Discharging graph
import numpy as np
import matplotlib.pyplot as plt
plt.plot([8.61,5.86,4.08,2.84,1.92,1.34,.92,.66,.45,.32,.23,.17],[10,20,30,40,50,60,70,80,90,100,110,120])
plt.xlabel('Voltage(V)')
plt.ylabel('Time(sec)')
plt.title('Voltage vs. Time(Discharging)')

plt.show()


# In[ ]:




