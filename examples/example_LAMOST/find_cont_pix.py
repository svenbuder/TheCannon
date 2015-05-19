start = 300
end = 400
contmask = np.ma.array(contmask, mask=bad)
# make sure dataset here is pseudo_cont_norm dataset
f_bar = np.zeros(len(dataset.wl))
sigma_f = np.zeros(len(dataset.wl))
nbad = np.zeros(len(dataset.wl))
for wl in range(0,len(dataset.wl)):
    array = dataset.tr_fluxes[:,wl]
    f_bar[wl] = np.median(array[array>0])
    nbad[wl] = sum(array==0)
    ngood = len(array==0)-sum(array==0)
    sigma_f[wl] = np.sqrt(np.var(array[array>0]))
    nbad[wl] = sum(array==0)

bad = np.var(dataset.tr_ivars, axis=0) == 0
f_bar = np.ma.array(f_bar, mask=bad)
sigma_f = np.ma.array(sigma_f, mask=bad)

start = 1900
end = 2000 

f,axarr = plt.subplots(2,sharex=True)
axarr[0].plot(dataset.wl[start:end], f_bar[start:end], alpha=0.5)
axarr[0].fill_between(dataset.wl[start:end], (f_bar+sigma_f)[start:end], (f_bar-sigma_f)[start:end], alpha=0.2)
axarr[0].set_ylabel("Med & Var Flux Across Stars")
axarr[1].plot(dataset.wl[start:end], nbad[start:end], alpha=0.7)
axarr[1].set_ylabel("# Bad Stars")
axarr[1].set_xlabel("Wavelength (A)")
axarr[0].set_title("Pixel Consistency Across Stars")

# the number of bad pixels in each star
ax.imshow(dataset.tr_fluxes)

f_bar_x = np.median(dataset.tr_fluxes[:,start:end], axis=0)
sigma_f_x = np.var(dataset.tr_fluxes[:,start:end], axis=0)
plot(sigma_f)
plot(f_bar)
bad = f_bar == 0
f_bar = np.ma.array(f_bar, mask=bad)
sigma_f = np.ma.array(sigma_f, mask=bad)
npix = len(bad)-sum(bad)
np.ma.mean(sigma_f)
0.15
np.ma.mean(f_bar)
0.87
scatter(sigma_f, np.abs(f_bar-1))

f_cut = 0.006
sig_cut = 0.003

contmask = np.zeros(end-start, dtype=bool)
#contmask = sigma_f[start:end] <= sig_cut
contmask[np.logical_and(np.abs(f_bar[start:end]-1) <= f_cut, sigma_f[start:end] <= sig_cut)] = True
contmask = np.ma.array(contmask, mask=bad[start:end])
contmask = np.ma.filled(contmask, fill_value=False)
sum(contmask) # looking for ~60-100...
err = np.sqrt(sigma_f)

plot(dataset.wl[start:end], f_bar[start:end], alpha=0.7)
fill_between(dataset.wl[start:end], (f_bar+sigma_f)[start:end], (f_bar-sigma_f)[start:end], alpha=0.2)
scatter(dataset.wl[start:end][contmask], f_bar[start:end][contmask], c='r')
#errorbar(dataset.wl[start:end][contmask], f_bar[start:end][contmask], yerr=err[start:end][contmask], c='r', fmt=None)
scatter(sigma_f[start:end][contmask], np.abs(1-f_bar[start:end][contmask]))
scatter(sigma_f[start:end], np.abs(1-f_bar[start:end]))
np.where(contmask==True)

filein = "pixlist_lamost.txt"
contpix = np.loadtxt(filein)
contpix = [int(item) for item in contpix]
npix = len(dataset.wl)
contmask = np.zeros(npix, dtype=bool)
contmask[contpix] = True
dataset.set_continuum(contmask)

pseudo_cont_dataset.find_continuum(f_cut=0.003, sig_cut=0.09)
dataset.set_continuum(pseudo_cont_dataset.contmask)

dataset.ranges = [[0,1883],[2094,3899]]

tr_cont, test_cont = dataset.fit_continuum(deg=3)
