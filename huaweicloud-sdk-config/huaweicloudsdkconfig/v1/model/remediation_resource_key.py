# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemediationResourceKey:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_provider': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_provider': 'resource_provider',
        'resource_type': 'resource_type'
    }

    def __init__(self, resource_id=None, resource_provider=None, resource_type=None):
        r"""RemediationResourceKey

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_provider: 云服务名称，为兼容部分合规结果中云服务名称为空的场景，可为空字符串。
        :type resource_provider: str
        :param resource_type: 资源类型，为兼容部分合规结果中资源类型为空的场景，可为空字符串。
        :type resource_type: str
        """
        
        

        self._resource_id = None
        self._resource_provider = None
        self._resource_type = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_provider = resource_provider
        self.resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this RemediationResourceKey.

        资源ID。

        :return: The resource_id of this RemediationResourceKey.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this RemediationResourceKey.

        资源ID。

        :param resource_id: The resource_id of this RemediationResourceKey.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_provider(self):
        r"""Gets the resource_provider of this RemediationResourceKey.

        云服务名称，为兼容部分合规结果中云服务名称为空的场景，可为空字符串。

        :return: The resource_provider of this RemediationResourceKey.
        :rtype: str
        """
        return self._resource_provider

    @resource_provider.setter
    def resource_provider(self, resource_provider):
        r"""Sets the resource_provider of this RemediationResourceKey.

        云服务名称，为兼容部分合规结果中云服务名称为空的场景，可为空字符串。

        :param resource_provider: The resource_provider of this RemediationResourceKey.
        :type resource_provider: str
        """
        self._resource_provider = resource_provider

    @property
    def resource_type(self):
        r"""Gets the resource_type of this RemediationResourceKey.

        资源类型，为兼容部分合规结果中资源类型为空的场景，可为空字符串。

        :return: The resource_type of this RemediationResourceKey.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this RemediationResourceKey.

        资源类型，为兼容部分合规结果中资源类型为空的场景，可为空字符串。

        :param resource_type: The resource_type of this RemediationResourceKey.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, RemediationResourceKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
