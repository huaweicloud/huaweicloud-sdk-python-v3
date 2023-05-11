# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_name': 'str',
        'resource_value': 'int'
    }

    attribute_map = {
        'resource_name': 'resource_name',
        'resource_value': 'resource_value'
    }

    def __init__(self, resource_name=None, resource_value=None):
        """WorkloadResource

        The model defined in huaweicloud sdk

        :param resource_name: 资源名称。
        :type resource_name: str
        :param resource_value: 资源属性值。
        :type resource_value: int
        """
        
        

        self._resource_name = None
        self._resource_value = None
        self.discriminator = None

        self.resource_name = resource_name
        self.resource_value = resource_value

    @property
    def resource_name(self):
        """Gets the resource_name of this WorkloadResource.

        资源名称。

        :return: The resource_name of this WorkloadResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this WorkloadResource.

        资源名称。

        :param resource_name: The resource_name of this WorkloadResource.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_value(self):
        """Gets the resource_value of this WorkloadResource.

        资源属性值。

        :return: The resource_value of this WorkloadResource.
        :rtype: int
        """
        return self._resource_value

    @resource_value.setter
    def resource_value(self, resource_value):
        """Sets the resource_value of this WorkloadResource.

        资源属性值。

        :param resource_value: The resource_value of this WorkloadResource.
        :type resource_value: int
        """
        self._resource_value = resource_value

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
        if not isinstance(other, WorkloadResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
