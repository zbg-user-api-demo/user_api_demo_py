import hashlib
import json
import time
import requests
import config_params


def public_request_get(api_url, **payload):
    return public_request('GET',api_url,**payload)


def public_request_post(api_url, **payload):
    return public_request('POST',api_url,**payload)


# 不需要签名的接口
def public_request(method, api_url, **payload):
    """request public url"""
    r_url = api_url
    try:
        r = requests.request(method, r_url, params=payload)
        r.raise_for_status()
        if r.status_code == 200:
            return True, r.json()
        else:
            return False, {'error': 'E10000', 'data': r.status_code}
    except requests.exceptions.HTTPError as err:
        return False, {'error': 'E10001', 'data': r.text}
    except Exception as err:
        return False, {'error': 'E10002', 'data': err}


def signed_request_get(api_url, **payload):
    return signed_request('GET',api_url,**payload)


def signed_request_post(api_url, **payload):
    return signed_request('POST',api_url,**payload)


def signed_request(method, api_url, **payload):
    """request a signed url"""
    timestamp = str(int(time.time() * 1000))
    full_url = api_url

    param = ''
    if method == 'GET' and payload:
        for k in sorted(payload):
            param += k + payload[k].__str__()
    elif method == 'POST' and payload:
        param = json.dumps(payload)
    elif not payload:
        payload = ''

    sig_str = config_params.API_ID + timestamp + param + config_params.API_SECRET
    signature = hashlib.md5(sig_str.encode('utf-8')).hexdigest()

    headers = {
        'Apiid': config_params.API_ID,
        'Timestamp': timestamp,
        'Sign': signature
    }

    try:
        r = requests.request(method, full_url, headers=headers, json=payload) if method == 'POST' else requests.request(
            method, full_url, headers=headers, data=payload)
        r.raise_for_status()
        if r.status_code == 200:
            return True, r.json()
        else:
            return False, {'error': 'E10000', 'data': r.status_code}
    except requests.exceptions.HTTPError as err:
        return False, {'error': 'E10001', 'data': r.text}
    except Exception as err:
        return False, {'error': 'E10002', 'data': err}
