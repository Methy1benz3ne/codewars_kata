def format_duration(seconds):
    if seconds == 0 :
        return 'now'
    res = []
    yy = seconds // (60*60*24*365)
    seconds = seconds % (60*60*24*365)
    dd = seconds // (60*60*24)
    seconds = seconds % (60*60*24)
    hh = seconds // (60*60)
    seconds = seconds %(60*60)
    mm = seconds // 60
    ss = seconds % 60

    if yy == 1 :
        res.append('1 year')
    if yy > 1 :
        res.append('%d years' % (yy))

    if dd == 1:
        res.append('1 day')
    if dd>1 :
        res.append('%d days' % (dd) )
    if hh == 1:
        res.append('1 hour')
    if hh > 1:
        res.append('%d hours' % (hh))
    if mm == 1:
        res.append('1 minute')
    if mm> 1 :
        res.append('%d minutes' % (mm))
    if ss == 1 :
        res.append('1 second')
    if ss > 1:
        res.append('%d seconds' % (ss))
    # if seconds == 0 :
    #     return 'now'
    if len(res) == 1 :
        return res[0]
    ans = [', '.join(res[:-1])] + [res[-1]]
    ans = ' and '.join(ans)

    # res = 'and '.join(res)

    return ans

print(format_duration(1
                      ))