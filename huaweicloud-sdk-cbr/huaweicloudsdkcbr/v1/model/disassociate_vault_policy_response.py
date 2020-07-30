# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class DisassociateVaultPolicyResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dissociate_policy': 'VaultPolicyResp'
    }

    attribute_map = {
        'dissociate_policy': 'dissociate_policy'
    }

    def __init__(self, dissociate_policy=None):
        """DisassociateVaultPolicyResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._dissociate_policy = None
        self.discriminator = None

        if dissociate_policy is not None:
            self.dissociate_policy = dissociate_policy

    @property
    def dissociate_policy(self):
        """Gets the dissociate_policy of this DisassociateVaultPolicyResponse.


        :return: The dissociate_policy of this DisassociateVaultPolicyResponse.
        :rtype: VaultPolicyResp
        """
        return self._dissociate_policy

    @dissociate_policy.setter
    def dissociate_policy(self, dissociate_policy):
        """Sets the dissociate_policy of this DisassociateVaultPolicyResponse.


        :param dissociate_policy: The dissociate_policy of this DisassociateVaultPolicyResponse.
        :type: VaultPolicyResp
        """
        self._dissociate_policy = dissociate_policy

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DisassociateVaultPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
