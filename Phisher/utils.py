def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def increment_hit_count(hits:dict, uri:str):
    try:
        hits[uri] += 1
        return True
    except Exception as e:
        print(e)
        return False