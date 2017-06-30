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

from enum import Enum


class SkuName(Enum):

    basic = "Basic"
    managed_basic = "Managed_Basic"
    managed_standard = "Managed_Standard"
    managed_premium = "Managed_Premium"


class SkuTier(Enum):

    basic = "Basic"
    managed = "Managed"


class ProvisioningState(Enum):

    creating = "Creating"
    updating = "Updating"
    deleting = "Deleting"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"


class PasswordName(Enum):

    password = "password"
    password2 = "password2"


class RegistryUsageUnit(Enum):

    count = "Count"
    bytes = "Bytes"


class WebhookStatus(Enum):

    enabled = "enabled"
    disabled = "disabled"


class WebhookAction(Enum):

    push = "push"
    delete = "delete"
