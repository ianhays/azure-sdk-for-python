# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class OfficeConsent(Resource):
    """Consent for Office365 tenant that already made.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param tenant_id: The tenantId of the Office365 with the concesnt.
    :type tenant_id: str
    :ivar tenant_name: The tenant name of the Office365 with the concesnt.
    :vartype tenant_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'tenant_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
        'tenant_name': {'key': 'properties.tenantName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OfficeConsent, self).__init__(**kwargs)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.tenant_name = None
