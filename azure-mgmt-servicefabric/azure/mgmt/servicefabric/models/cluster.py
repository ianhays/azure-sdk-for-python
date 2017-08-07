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


class Cluster(Resource):
    """The cluster resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict
    :ivar available_cluster_versions: The available cluster code version which
     the cluster can upgrade to, note that you must choose upgradeMode to
     manual to upgrade to
    :vartype available_cluster_versions: list of :class:`ClusterVersionDetails
     <azure.mgmt.servicefabric.models.ClusterVersionDetails>`
    :ivar cluster_id: The unique identifier for the cluster resource
    :vartype cluster_id: str
    :ivar cluster_state: The state for the cluster. Possible values include:
     'WaitingForNodes', 'Deploying', 'BaselineUpgrade',
     'UpdatingUserConfiguration', 'UpdatingUserCertificate',
     'UpdatingInfrastructure', 'EnforcingClusterVersion',
     'UpgradeServiceUnreachable', 'AutoScale', 'Ready'
    :vartype cluster_state: str or :class:`enum
     <azure.mgmt.servicefabric.models.enum>`
    :ivar cluster_endpoint: The endpoint for the cluster connecting to
     servicefabric resource provider
    :vartype cluster_endpoint: str
    :param cluster_code_version: The ServiceFabric code version running in
     your cluster
    :type cluster_code_version: str
    :param certificate: This primay certificate will be used as cluster node
     to node security, SSL certificate for cluster management endpoint and
     default admin client
    :type certificate: :class:`CertificateDescription
     <azure.mgmt.servicefabric.models.CertificateDescription>`
    :param reliability_level: Cluster reliability level indicates replica set
     size of system service. Possible values include: 'Bronze', 'Silver',
     'Gold', 'Platinum'
    :type reliability_level: str or :class:`enum
     <azure.mgmt.servicefabric.models.enum>`
    :param upgrade_mode: Cluster upgrade mode indicates if fabric upgrade is
     initiated automatically by the system or not. Possible values include:
     'Automatic', 'Manual'
    :type upgrade_mode: str or :class:`enum
     <azure.mgmt.servicefabric.models.enum>`
    :param client_certificate_thumbprints: The client thumbprint details ,it
     is used for client access for cluster operation
    :type client_certificate_thumbprints: list of
     :class:`ClientCertificateThumbprint
     <azure.mgmt.servicefabric.models.ClientCertificateThumbprint>`
    :param client_certificate_common_names:  List of client certificates to
     whitelist based on common names
    :type client_certificate_common_names: list of
     :class:`ClientCertificateCommonName
     <azure.mgmt.servicefabric.models.ClientCertificateCommonName>`
    :param fabric_settings: List of custom fabric settings to configure the
     cluster.
    :type fabric_settings: list of :class:`SettingsSectionDescription
     <azure.mgmt.servicefabric.models.SettingsSectionDescription>`
    :param reverse_proxy_certificate: The server certificate used by reverse
     proxy
    :type reverse_proxy_certificate: :class:`CertificateDescription
     <azure.mgmt.servicefabric.models.CertificateDescription>`
    :param management_endpoint: The http management endpoint of the cluster
    :type management_endpoint: str
    :param node_types: The list of nodetypes that make up the cluster
    :type node_types: list of :class:`NodeTypeDescription
     <azure.mgmt.servicefabric.models.NodeTypeDescription>`
    :param azure_active_directory: The settings to enable AAD authentication
     on the cluster
    :type azure_active_directory: :class:`AzureActiveDirectory
     <azure.mgmt.servicefabric.models.AzureActiveDirectory>`
    :ivar provisioning_state: The provisioning state of the cluster resource.
     Possible values include: 'Updating', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or :class:`ProvisioningState
     <azure.mgmt.servicefabric.models.ProvisioningState>`
    :param vm_image: The name of VM image VMSS has been configured with.
     Generic names such as Windows or Linux can be used.
    :type vm_image: str
    :param diagnostics_storage_account_config: The storage diagnostics account
     configuration details
    :type diagnostics_storage_account_config:
     :class:`DiagnosticsStorageAccountConfig
     <azure.mgmt.servicefabric.models.DiagnosticsStorageAccountConfig>`
    :param upgrade_description: The policy to use when upgrading the cluster.
    :type upgrade_description: :class:`ClusterUpgradePolicy
     <azure.mgmt.servicefabric.models.ClusterUpgradePolicy>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'available_cluster_versions': {'readonly': True},
        'cluster_id': {'readonly': True},
        'cluster_state': {'readonly': True},
        'cluster_endpoint': {'readonly': True},
        'management_endpoint': {'required': True},
        'node_types': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'available_cluster_versions': {'key': 'properties.availableClusterVersions', 'type': '[ClusterVersionDetails]'},
        'cluster_id': {'key': 'properties.clusterId', 'type': 'str'},
        'cluster_state': {'key': 'properties.clusterState', 'type': 'str'},
        'cluster_endpoint': {'key': 'properties.clusterEndpoint', 'type': 'str'},
        'cluster_code_version': {'key': 'properties.clusterCodeVersion', 'type': 'str'},
        'certificate': {'key': 'properties.certificate', 'type': 'CertificateDescription'},
        'reliability_level': {'key': 'properties.reliabilityLevel', 'type': 'str'},
        'upgrade_mode': {'key': 'properties.upgradeMode', 'type': 'str'},
        'client_certificate_thumbprints': {'key': 'properties.clientCertificateThumbprints', 'type': '[ClientCertificateThumbprint]'},
        'client_certificate_common_names': {'key': 'properties.clientCertificateCommonNames', 'type': '[ClientCertificateCommonName]'},
        'fabric_settings': {'key': 'properties.fabricSettings', 'type': '[SettingsSectionDescription]'},
        'reverse_proxy_certificate': {'key': 'properties.reverseProxyCertificate', 'type': 'CertificateDescription'},
        'management_endpoint': {'key': 'properties.managementEndpoint', 'type': 'str'},
        'node_types': {'key': 'properties.nodeTypes', 'type': '[NodeTypeDescription]'},
        'azure_active_directory': {'key': 'properties.azureActiveDirectory', 'type': 'AzureActiveDirectory'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'vm_image': {'key': 'properties.vmImage', 'type': 'str'},
        'diagnostics_storage_account_config': {'key': 'properties.diagnosticsStorageAccountConfig', 'type': 'DiagnosticsStorageAccountConfig'},
        'upgrade_description': {'key': 'properties.upgradeDescription', 'type': 'ClusterUpgradePolicy'},
    }

    def __init__(self, location, management_endpoint, node_types, tags=None, cluster_code_version=None, certificate=None, reliability_level=None, upgrade_mode=None, client_certificate_thumbprints=None, client_certificate_common_names=None, fabric_settings=None, reverse_proxy_certificate=None, azure_active_directory=None, vm_image=None, diagnostics_storage_account_config=None, upgrade_description=None):
        super(Cluster, self).__init__(location=location, tags=tags)
        self.available_cluster_versions = None
        self.cluster_id = None
        self.cluster_state = None
        self.cluster_endpoint = None
        self.cluster_code_version = cluster_code_version
        self.certificate = certificate
        self.reliability_level = reliability_level
        self.upgrade_mode = upgrade_mode
        self.client_certificate_thumbprints = client_certificate_thumbprints
        self.client_certificate_common_names = client_certificate_common_names
        self.fabric_settings = fabric_settings
        self.reverse_proxy_certificate = reverse_proxy_certificate
        self.management_endpoint = management_endpoint
        self.node_types = node_types
        self.azure_active_directory = azure_active_directory
        self.provisioning_state = None
        self.vm_image = vm_image
        self.diagnostics_storage_account_config = diagnostics_storage_account_config
        self.upgrade_description = upgrade_description
