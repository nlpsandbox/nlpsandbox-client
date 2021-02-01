
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.service_api import ServiceApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from annotator.api.service_api import ServiceApi
from annotator.api.text_date_annotation_api import TextDateAnnotationApi
from annotator.api.text_person_name_annotation_api import TextPersonNameAnnotationApi
from annotator.api.text_physical_address_annotation_api import TextPhysicalAddressAnnotationApi
