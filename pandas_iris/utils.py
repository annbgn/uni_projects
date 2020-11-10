def grouper(x, lower, higher):
    if x <= lower:
        return 'Small'
    elif lower < x <= higher:
        return 'Medium'
    else:
        return 'Large'