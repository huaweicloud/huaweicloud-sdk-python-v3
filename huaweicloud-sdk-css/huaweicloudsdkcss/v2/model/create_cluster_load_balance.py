# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterLoadBalance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint_with_dns_name': 'bool',
        'vpc_permissions': 'list[str]'
    }

    attribute_map = {
        'endpoint_with_dns_name': 'endpointWithDnsName',
        'vpc_permissions': 'vpcPermissions'
    }

    def __init__(self, endpoint_with_dns_name=None, vpc_permissions=None):
        """CreateClusterLoadBalance

        The model defined in huaweicloud sdk

        :param endpoint_with_dns_name: 是否开启内网域名。 - true： 开启内网域名。 - false： 关闭内网域名。
        :type endpoint_with_dns_name: bool
        :param vpc_permissions: 访问控制。
        :type vpc_permissions: list[str]
        """
        
        

        self._endpoint_with_dns_name = None
        self._vpc_permissions = None
        self.discriminator = None

        self.endpoint_with_dns_name = endpoint_with_dns_name
        if vpc_permissions is not None:
            self.vpc_permissions = vpc_permissions

    @property
    def endpoint_with_dns_name(self):
        """Gets the endpoint_with_dns_name of this CreateClusterLoadBalance.

        是否开启内网域名。 - true： 开启内网域名。 - false： 关闭内网域名。

        :return: The endpoint_with_dns_name of this CreateClusterLoadBalance.
        :rtype: bool
        """
        return self._endpoint_with_dns_name

    @endpoint_with_dns_name.setter
    def endpoint_with_dns_name(self, endpoint_with_dns_name):
        """Sets the endpoint_with_dns_name of this CreateClusterLoadBalance.

        是否开启内网域名。 - true： 开启内网域名。 - false： 关闭内网域名。

        :param endpoint_with_dns_name: The endpoint_with_dns_name of this CreateClusterLoadBalance.
        :type endpoint_with_dns_name: bool
        """
        self._endpoint_with_dns_name = endpoint_with_dns_name

    @property
    def vpc_permissions(self):
        """Gets the vpc_permissions of this CreateClusterLoadBalance.

        访问控制。

        :return: The vpc_permissions of this CreateClusterLoadBalance.
        :rtype: list[str]
        """
        return self._vpc_permissions

    @vpc_permissions.setter
    def vpc_permissions(self, vpc_permissions):
        """Sets the vpc_permissions of this CreateClusterLoadBalance.

        访问控制。

        :param vpc_permissions: The vpc_permissions of this CreateClusterLoadBalance.
        :type vpc_permissions: list[str]
        """
        self._vpc_permissions = vpc_permissions

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
        if not isinstance(other, CreateClusterLoadBalance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
