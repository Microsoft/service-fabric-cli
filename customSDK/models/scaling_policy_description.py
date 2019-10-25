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

from msrest.serialization import Model


class ScalingPolicyDescription(Model):
    """Describes how the scaling should be performed.

    All required parameters must be populated in order to send to Azure.

    :param scaling_trigger: Required. Specifies the trigger associated with
     this scaling policy
    :type scaling_trigger:
     ~azure.servicefabric.models.ScalingTriggerDescription
    :param scaling_mechanism: Required. Specifies the mechanism associated
     with this scaling policy
    :type scaling_mechanism:
     ~azure.servicefabric.models.ScalingMechanismDescription
    """

    _validation = {
        'scaling_trigger': {'required': True},
        'scaling_mechanism': {'required': True},
    }

    _attribute_map = {
        'scaling_trigger': {'key': 'ScalingTrigger', 'type': 'ScalingTriggerDescription'},
        'scaling_mechanism': {'key': 'ScalingMechanism', 'type': 'ScalingMechanismDescription'},
    }

    def __init__(self, **kwargs):
        super(ScalingPolicyDescription, self).__init__(**kwargs)
        self.scaling_trigger = kwargs.get('scaling_trigger', None)
        self.scaling_mechanism = kwargs.get('scaling_mechanism', None)
