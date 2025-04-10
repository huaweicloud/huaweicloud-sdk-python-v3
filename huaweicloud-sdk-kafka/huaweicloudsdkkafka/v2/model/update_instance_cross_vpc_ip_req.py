# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceCrossVpcIpReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'advertised_ip_contents': 'dict(str, str)'
    }

    attribute_map = {
        'advertised_ip_contents': 'advertised_ip_contents'
    }

    def __init__(self, advertised_ip_contents=None):
        r"""UpdateInstanceCrossVpcIpReq

        The model defined in huaweicloud sdk

        :param advertised_ip_contents: 用户自定义的advertised_ip_contents键值对。  键是listeners IP。  值是advertised.listeners IP，或者域名。  &gt; IP修改未修改项也需填上。
        :type advertised_ip_contents: dict(str, str)
        """
        
        

        self._advertised_ip_contents = None
        self.discriminator = None

        self.advertised_ip_contents = advertised_ip_contents

    @property
    def advertised_ip_contents(self):
        r"""Gets the advertised_ip_contents of this UpdateInstanceCrossVpcIpReq.

        用户自定义的advertised_ip_contents键值对。  键是listeners IP。  值是advertised.listeners IP，或者域名。  > IP修改未修改项也需填上。

        :return: The advertised_ip_contents of this UpdateInstanceCrossVpcIpReq.
        :rtype: dict(str, str)
        """
        return self._advertised_ip_contents

    @advertised_ip_contents.setter
    def advertised_ip_contents(self, advertised_ip_contents):
        r"""Sets the advertised_ip_contents of this UpdateInstanceCrossVpcIpReq.

        用户自定义的advertised_ip_contents键值对。  键是listeners IP。  值是advertised.listeners IP，或者域名。  > IP修改未修改项也需填上。

        :param advertised_ip_contents: The advertised_ip_contents of this UpdateInstanceCrossVpcIpReq.
        :type advertised_ip_contents: dict(str, str)
        """
        self._advertised_ip_contents = advertised_ip_contents

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
        if not isinstance(other, UpdateInstanceCrossVpcIpReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
