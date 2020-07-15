# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowPolicyAndInstanceQuotaResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'all_quotas': 'PolicyInstanceQuotas'
    }

    attribute_map = {
        'all_quotas': 'AllQuotas'
    }

    def __init__(self, all_quotas=None):
        """ShowPolicyAndInstanceQuotaResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._all_quotas = None
        self.discriminator = None

        if all_quotas is not None:
            self.all_quotas = all_quotas

    @property
    def all_quotas(self):
        """Gets the all_quotas of this ShowPolicyAndInstanceQuotaResponse.


        :return: The all_quotas of this ShowPolicyAndInstanceQuotaResponse.
        :rtype: PolicyInstanceQuotas
        """
        return self._all_quotas

    @all_quotas.setter
    def all_quotas(self, all_quotas):
        """Sets the all_quotas of this ShowPolicyAndInstanceQuotaResponse.


        :param all_quotas: The all_quotas of this ShowPolicyAndInstanceQuotaResponse.
        :type: PolicyInstanceQuotas
        """
        self._all_quotas = all_quotas

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
        if not isinstance(other, ShowPolicyAndInstanceQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
