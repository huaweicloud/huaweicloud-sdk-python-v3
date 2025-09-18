# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudConnectionEnterpriseSupportSitesCapabilityValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'support_sites': 'list[str]'
    }

    attribute_map = {
        'support_sites': 'support_sites'
    }

    def __init__(self, support_sites=None):
        r"""CloudConnectionEnterpriseSupportSitesCapabilityValue

        The model defined in huaweicloud sdk

        :param support_sites: 租户支持的Site列表。
        :type support_sites: list[str]
        """
        
        

        self._support_sites = None
        self.discriminator = None

        self.support_sites = support_sites

    @property
    def support_sites(self):
        r"""Gets the support_sites of this CloudConnectionEnterpriseSupportSitesCapabilityValue.

        租户支持的Site列表。

        :return: The support_sites of this CloudConnectionEnterpriseSupportSitesCapabilityValue.
        :rtype: list[str]
        """
        return self._support_sites

    @support_sites.setter
    def support_sites(self, support_sites):
        r"""Sets the support_sites of this CloudConnectionEnterpriseSupportSitesCapabilityValue.

        租户支持的Site列表。

        :param support_sites: The support_sites of this CloudConnectionEnterpriseSupportSitesCapabilityValue.
        :type support_sites: list[str]
        """
        self._support_sites = support_sites

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudConnectionEnterpriseSupportSitesCapabilityValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
