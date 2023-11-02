# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadResourceItem:

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
        'resource_value': 'int',
        'value_unit': 'str',
        'resource_description': 'str'
    }

    attribute_map = {
        'resource_name': 'resource_name',
        'resource_value': 'resource_value',
        'value_unit': 'value_unit',
        'resource_description': 'resource_description'
    }

    def __init__(self, resource_name=None, resource_value=None, value_unit=None, resource_description=None):
        """WorkloadResourceItem

        The model defined in huaweicloud sdk

        :param resource_name: 资源名称。
        :type resource_name: str
        :param resource_value: 资源属性值。
        :type resource_value: int
        :param value_unit: 资源属性单位。
        :type value_unit: str
        :param resource_description: 资源附加描述
        :type resource_description: str
        """
        
        

        self._resource_name = None
        self._resource_value = None
        self._value_unit = None
        self._resource_description = None
        self.discriminator = None

        self.resource_name = resource_name
        self.resource_value = resource_value
        if value_unit is not None:
            self.value_unit = value_unit
        if resource_description is not None:
            self.resource_description = resource_description

    @property
    def resource_name(self):
        """Gets the resource_name of this WorkloadResourceItem.

        资源名称。

        :return: The resource_name of this WorkloadResourceItem.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this WorkloadResourceItem.

        资源名称。

        :param resource_name: The resource_name of this WorkloadResourceItem.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_value(self):
        """Gets the resource_value of this WorkloadResourceItem.

        资源属性值。

        :return: The resource_value of this WorkloadResourceItem.
        :rtype: int
        """
        return self._resource_value

    @resource_value.setter
    def resource_value(self, resource_value):
        """Sets the resource_value of this WorkloadResourceItem.

        资源属性值。

        :param resource_value: The resource_value of this WorkloadResourceItem.
        :type resource_value: int
        """
        self._resource_value = resource_value

    @property
    def value_unit(self):
        """Gets the value_unit of this WorkloadResourceItem.

        资源属性单位。

        :return: The value_unit of this WorkloadResourceItem.
        :rtype: str
        """
        return self._value_unit

    @value_unit.setter
    def value_unit(self, value_unit):
        """Sets the value_unit of this WorkloadResourceItem.

        资源属性单位。

        :param value_unit: The value_unit of this WorkloadResourceItem.
        :type value_unit: str
        """
        self._value_unit = value_unit

    @property
    def resource_description(self):
        """Gets the resource_description of this WorkloadResourceItem.

        资源附加描述

        :return: The resource_description of this WorkloadResourceItem.
        :rtype: str
        """
        return self._resource_description

    @resource_description.setter
    def resource_description(self, resource_description):
        """Sets the resource_description of this WorkloadResourceItem.

        资源附加描述

        :param resource_description: The resource_description of this WorkloadResourceItem.
        :type resource_description: str
        """
        self._resource_description = resource_description

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
        if not isinstance(other, WorkloadResourceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
