# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlDomainAccessSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sl_domain_access_enabled': 'bool'
    }

    attribute_map = {
        'sl_domain_access_enabled': 'sl_domain_access_enabled'
    }

    def __init__(self, sl_domain_access_enabled=None):
        """SlDomainAccessSetting

        The model defined in huaweicloud sdk

        :param sl_domain_access_enabled: 设置调试域名是否可以访问，true为可以访问，false为禁止访问
        :type sl_domain_access_enabled: bool
        """
        
        

        self._sl_domain_access_enabled = None
        self.discriminator = None

        self.sl_domain_access_enabled = sl_domain_access_enabled

    @property
    def sl_domain_access_enabled(self):
        """Gets the sl_domain_access_enabled of this SlDomainAccessSetting.

        设置调试域名是否可以访问，true为可以访问，false为禁止访问

        :return: The sl_domain_access_enabled of this SlDomainAccessSetting.
        :rtype: bool
        """
        return self._sl_domain_access_enabled

    @sl_domain_access_enabled.setter
    def sl_domain_access_enabled(self, sl_domain_access_enabled):
        """Sets the sl_domain_access_enabled of this SlDomainAccessSetting.

        设置调试域名是否可以访问，true为可以访问，false为禁止访问

        :param sl_domain_access_enabled: The sl_domain_access_enabled of this SlDomainAccessSetting.
        :type sl_domain_access_enabled: bool
        """
        self._sl_domain_access_enabled = sl_domain_access_enabled

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
        if not isinstance(other, SlDomainAccessSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
