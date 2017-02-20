def generate_circles(res,rmax,con=True):
    """
    res: Defines the step size used for theta_vals

    rmax: Defines the maximum radius for the constructed circles

    con: Used to decide whether or not to connect the points on the output graph. Default     value is True.

    """
    fig = plt.figure()
    ax = fig.add_subplot(111,aspect='equal')
    theta_vals = np.arange(0,2*np.pi+res,res)
    xvals = np.cos(theta_vals)
    yvals = np.sin(theta_vals)
    r = np.arange(1,rmax+1)
    for i in r:
        if con:
            plt.plot(i*xvals,i*yvals,'-o')
        else:
            plt.plot(i*xvals,i*yvals,'o')
    ax.set_xlim(-rmax,rmax)
    ax.set_ylim(-rmax,rmax)
