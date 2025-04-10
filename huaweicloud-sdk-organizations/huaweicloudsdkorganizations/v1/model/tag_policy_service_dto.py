# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagPolicyServiceDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'resource_types': 'list[str]',
        'support_all': 'bool'
    }

    attribute_map = {
        'service_name': 'service_name',
        'resource_types': 'resource_types',
        'support_all': 'support_all'
    }

    def __init__(self, service_name=None, resource_types=None, support_all=None):
        r"""TagPolicyServiceDto

        The model defined in huaweicloud sdk

        :param service_name: 服务名称。
        :type service_name: str
        :param resource_types: 资源类型。
        :type resource_types: list[str]
        :param support_all: resource_type是否支持全量选择，即*
        :type support_all: bool
        """
        
        

        self._service_name = None
        self._resource_types = None
        self._support_all = None
        self.discriminator = None

        self.service_name = service_name
        self.resource_types = resource_types
        self.support_all = support_all

    @property
    def service_name(self):
        r"""Gets the service_name of this TagPolicyServiceDto.

        服务名称。

        :return: The service_name of this TagPolicyServiceDto.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this TagPolicyServiceDto.

        服务名称。

        :param service_name: The service_name of this TagPolicyServiceDto.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def resource_types(self):
        r"""Gets the resource_types of this TagPolicyServiceDto.

        资源类型。

        :return: The resource_types of this TagPolicyServiceDto.
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        r"""Sets the resource_types of this TagPolicyServiceDto.

        资源类型。

        :param resource_types: The resource_types of this TagPolicyServiceDto.
        :type resource_types: list[str]
        """
        self._resource_types = resource_types

    @property
    def support_all(self):
        r"""Gets the support_all of this TagPolicyServiceDto.

        resource_type是否支持全量选择，即*

        :return: The support_all of this TagPolicyServiceDto.
        :rtype: bool
        """
        return self._support_all

    @support_all.setter
    def support_all(self, support_all):
        r"""Sets the support_all of this TagPolicyServiceDto.

        resource_type是否支持全量选择，即*

        :param support_all: The support_all of this TagPolicyServiceDto.
        :type support_all: bool
        """
        self._support_all = support_all

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
        if not isinstance(other, TagPolicyServiceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
