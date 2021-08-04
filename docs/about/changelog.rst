*********
Changelog
*********

This changelog is used to track all major changes to **nlpsandboxclient**.

For older releases, visit the `GitHub releases`_.

.. _Github releases: https://github.com/nlpsandbox/nlpsandbox-client/releases

4.2.0
-----
- Update synapse login utility
- Add in retry logic for all services (exponential backoff)

4.1.1
-----
- Patch small cli bug: change physical address to location.

4.1.0
-----
- Scoring code should use `location` instead of `address`

4.0.0
-----
- Update to support schemas 1.2.0

3.1.0
-----
- Implement scoring for `Id` and `Contact` annotators

3.0.0
-----
- Change `nlpsandboxsdk` to `nlpsandbox`

2.1.0
-----
- Fixed bug - tool names in `annotate_note` were incorrect caused by an aggressive search and find.

2.0.0
-----
- Update to support schemas 1.1.2
- Remove `datanode` and `annotator` package by merging into one `nlpsandboxsdk`

1.1.0
-----
- Update to support schemas 1.1.1

1.0.1
-----
- Fix version in `__init__.py`
- Change `note_type` to `type`

1.0.0
-----
- Client uses NLP sandbox API version 1.0.2
- Update annotate note to accept `Note` instead of `TextAnnotatorRequest` object
- Update client to support v1.0.2 schemas
- Change `date`, `person`, `address` to `nlpsandbox:date-annotator`, `nlpsandbox:person-name-annotator` and `nlpsandbox:physical-address-annotator`
- Add support for `Python` 3.9
- Add initial unit tests
- Create `tool` and `datanode` cli modules

0.4.1
-----
- Client uses NLP sandbox API version 1.0.1

0.3.1
-----
- Client uses NLP sandbox API version 1.0.0
