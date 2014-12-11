from numpy import *
import matplotlib.pyplot as plt

# Compare basic facts in the Pleiades set that isn't working, and the Pleiades set that *is* working

broken = set(['./4259_Pleaides/aspcapStar-v304-2m03415868+2342263.fits',
 './4259_Pleaides/aspcapStar-v304-2m03422154+2439527.fits',
 './4259_Pleaides/aspcapStar-v304-2m03453903+2513279.fits',
 './4259_Pleaides/aspcapStar-v304-2m03463533+2324422.fits',
 './4259_Pleaides/aspcapStar-v304-2m03472083+2505124.fits',
 './4259_Pleaides/aspcapStar-v304-2m03473521+2532383.fits',
 './4259_Pleaides/aspcapStar-v304-2m03475973+2443528.fits',
 './4259_Pleaides/aspcapStar-v304-2m03482277+2358212.fits'])

allPleiades = set(['./4259_Pleaides/aspcapStar-v304-2m03403073+2429143.fits', './4259_Pleaides/aspcapStar-v304-2m03405126+2335544.fits', './4259_Pleaides/aspcapStar-v304-2m03415366+2327287.fits', './4259_Pleaides/aspcapStar-v304-2m03415868+2342263.fits', './4259_Pleaides/aspcapStar-v304-2m03420383+2442454.fits', './4259_Pleaides/aspcapStar-v304-2m03422154+2439527.fits', './4259_Pleaides/aspcapStar-v304-2m03422760+2502492.fits', './4259_Pleaides/aspcapStar-v304-2m03432662+2459395.fits', './4259_Pleaides/aspcapStar-v304-2m03433660+2327141.fits', './4259_Pleaides/aspcapStar-v304-2m03433692+2423382.fits', './4259_Pleaides/aspcapStar-v304-2m03434860+2332218.fits', './4259_Pleaides/aspcapStar-v304-2m03435214+2450297.fits', './4259_Pleaides/aspcapStar-v304-2m03440509+2529017.fits', './4259_Pleaides/aspcapStar-v304-2m03443742+2508161.fits', './4259_Pleaides/aspcapStar-v304-2m03445017+2454401.fits', './4259_Pleaides/aspcapStar-v304-2m03445896+2323202.fits', './4259_Pleaides/aspcapStar-v304-2m03451199+2435102.fits', './4259_Pleaides/aspcapStar-v304-2m03452219+2328182.fits', './4259_Pleaides/aspcapStar-v304-2m03453903+2513279.fits', './4259_Pleaides/aspcapStar-v304-2m03454245+2503255.fits', './4259_Pleaides/aspcapStar-v304-2m03460381+2527108.fits', './4259_Pleaides/aspcapStar-v304-2m03460525+2258540.fits', './4259_Pleaides/aspcapStar-v304-2m03460649+2434027.fits', './4259_Pleaides/aspcapStar-v304-2m03460777+2452005.fits', './4259_Pleaides/aspcapStar-v304-2m03461175+2437203.fits', './4259_Pleaides/aspcapStar-v304-2m03462047+2447077.fits', './4259_Pleaides/aspcapStar-v304-2m03462863+2445324.fits', './4259_Pleaides/aspcapStar-v304-2m03463533+2324422.fits', './4259_Pleaides/aspcapStar-v304-2m03463727+2420367.fits', './4259_Pleaides/aspcapStar-v304-2m03463777+2444517.fits', './4259_Pleaides/aspcapStar-v304-2m03463888+2431132.fits', './4259_Pleaides/aspcapStar-v304-2m03464027+2455517.fits', './4259_Pleaides/aspcapStar-v304-2m03464831+2418060.fits', './4259_Pleaides/aspcapStar-v304-2m03471481+2522186.fits', './4259_Pleaides/aspcapStar-v304-2m03471806+2423268.fits', './4259_Pleaides/aspcapStar-v304-2m03472083+2505124.fits', './4259_Pleaides/aspcapStar-v304-2m03473368+2441032.fits', './4259_Pleaides/aspcapStar-v304-2m03473521+2532383.fits', './4259_Pleaides/aspcapStar-v304-2m03473801+2328050.fits', './4259_Pleaides/aspcapStar-v304-2m03475973+2443528.fits', './4259_Pleaides/aspcapStar-v304-2m03481018+2300041.fits', './4259_Pleaides/aspcapStar-v304-2m03481099+2330253.fits','./4259_Pleaides/aspcapStar-v304-2m03481729+2430159.fits', './4259_Pleaides/aspcapStar-v304-2m03482277+2358212.fits'])

working = allPleiades-broken

linAges = [0.9395086, -0.03496745, 0.17592847, 0.03340704,-0.249263, -0.07592404, 0.00795182, 0.41577723, -0.01287296, -0.27449848, 0.11714356, -0.09121608, 0.46303688, -0.01371456, 0.01447818, -0.03052806, 0.03608639, 0.42034812, 0.17061592, 0.20533904, 0.05538382, 0.17288485, 0.04453659, 1.03850584, 1.07263929, 0.03092605, 0.01257345, -0.14581354, 0.0517022, 0.59801695, -0.08681423, 0.33839347, -0.28472519, 0.84659455, 0.41893599, 0.41788005, 0.01303621, 0.81614632, 0.04816583, 0.42475709, -0.04324743, -0.0281678, 0.07737133, 0.76944678]

logAges = [8.11894956, 8.11207383, 8.13607165, 9.95616439, 8.09061697, 9.9765686, 8.1227628, 8.18651006, 8.11408725, 8.05059853, 8.15764743, 8.1059421, 8.10766008, 8.13074422, 8.12143394, 8.11297022, 8.12831998, 8.1340771, 10.14725175, 8.11899054, 8.12952193, 8.15221549, 8.1356128, 8.23349497, 8.12809746, 8.13079917, 8.138712, 9.99598242, 8.14077088, 8.20355362, 8.12313408, 8.16263621, 8.07449536, 8.07038524, 8.15365346, 10.23576383, 8.13941618, 9.91912385, 8.13421706, 9.81563788,  8.12090039, 8.12390428, 8.13512813, 10.21895611]


filein2 = 'data_Pleiades.txt'
filenames = loadtxt(filein2, dtype='str', usecols=(0,), unpack=1)
t,g,feh,t_err,feh_err = loadtxt(filein2, usecols = (4,6,8,16,17), unpack =1)
tA,gA,fehA = loadtxt(filein2, usecols = (3,5,7), unpack =1)
g_err = [0]*len(g)
g_err = array(g_err)
diffT = abs(array(t) - array(tA) )
pick = diffT < 600.
t,g,feh,t_err,g_err,feh_err = t[pick], g[pick], feh[pick], t_err[pick], g_err[pick], feh_err[pick]
filenames = filenames[pick]

fig, ax = plt.subplots()
ax.scatter(t, g, c=logAges)
ax.set_xlabel('temperature')
ax.set_ylabel('log g')
fig.savefig('tg.png')
