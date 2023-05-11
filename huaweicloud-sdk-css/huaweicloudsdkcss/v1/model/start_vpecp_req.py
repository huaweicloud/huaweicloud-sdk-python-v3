# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartVpecpReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_with_dns_name': 'bool'
    }

    attribute_map = {
        'endpoint_with_dns_name': 'endpointWithDnsName'
    }

    def __init__(self, endpoint_with_dns_name=None):
        """StartVpecpReq

        The model defined in huaweicloud sdk

        :param endpoint_with_dns_name: 是否开启内网域名。 - true：开启。 - false：不开启。
        :type endpoint_with_dns_name: bool
        """
        
        

        self._endpoint_with_dns_name = None
        self.discriminator = None

        if endpoint_with_dns_name is not None:
            self.endpoint_with_dns_name = endpoint_with_dns_name

    @property
    def endpoint_with_dns_name(self):
        """Gets the endpoint_with_dns_name of this StartVpecpReq.

        是否开启内网域名。 - true：开启。 - false：不开启。

        :return: The endpoint_with_dns_name of this StartVpecpReq.
        :rtype: bool
        """
        return self._endpoint_with_dns_name

    @endpoint_with_dns_name.setter
    def endpoint_with_dns_name(self, endpoint_with_dns_name):
        """Sets the endpoint_with_dns_name of this StartVpecpReq.

        是否开启内网域名。 - true：开启。 - false：不开启。

        :param endpoint_with_dns_name: The endpoint_with_dns_name of this StartVpecpReq.
        :type endpoint_with_dns_name: bool
        """
        self._endpoint_with_dns_name = endpoint_with_dns_name

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
        if not isinstance(other, StartVpecpReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
