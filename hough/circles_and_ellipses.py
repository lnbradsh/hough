def generate_circles_and_ellipses(res,imax,jmax,con=True)
    """

    """
    fig = plt.figure()
    ax = fig.add_subplot(111,aspect='equal')
    theta_vals = np.arange(0,2*np.pi+res,res)
    xvals = np.cos(theta_vals)
    yvals = np.sin(theta_vals)
    i = np.arange(1,imax+1)
    j = np.arange(1,jmax+1)
    for a in i:
        for b in j:
            if con:
                plt.plot(a*xvals,b*yvals,'-o')
            else:
                plt.plot(a*xvals,b*yvals,'o')
    ax.set_xlim(-imax,imax)
    ax.set_ylim(-jmax,jmax)
