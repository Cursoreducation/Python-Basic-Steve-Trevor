
class HTTPError(Exception):
    pass

class Error404(HTTPError):
    pass

class Error403(HTTPError):
    pass

class Error500(HTTPError):
    pass


# try:
#     raise Error404()
# except Error500 as er:
#     print("except ", er.__class__)
#     print("ok")
# except Error404 as er:
#     print("except ", er.__class__)
#     print("not ok")


try:
    raise Error500()
except HTTPError as er:
    print("except ", er.__class__)
