# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from annotator.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from annotator.model.error import Error
from annotator.model.note import Note
from annotator.model.service import Service
from annotator.model.text_annotation import TextAnnotation
from annotator.model.text_date_annotation import TextDateAnnotation
from annotator.model.text_date_annotation_all_of import TextDateAnnotationAllOf
from annotator.model.text_date_annotation_request import TextDateAnnotationRequest
from annotator.model.text_date_annotations import TextDateAnnotations
from annotator.model.text_person_name_annotation import TextPersonNameAnnotation
from annotator.model.text_person_name_annotation_request import TextPersonNameAnnotationRequest
from annotator.model.text_person_name_annotations import TextPersonNameAnnotations
from annotator.model.text_physical_address_annotation import TextPhysicalAddressAnnotation
from annotator.model.text_physical_address_annotation_all_of import TextPhysicalAddressAnnotationAllOf
from annotator.model.text_physical_address_annotation_request import TextPhysicalAddressAnnotationRequest
from annotator.model.text_physical_address_annotations import TextPhysicalAddressAnnotations
