# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PropertyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'object',
        'device_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'device_id': 'device_id'
    }

    def __init__(self, name=None, value=None, device_id=None):
        """PropertyRequest

        The model defined in huaweicloud sdk

        :param name: 属性名称，必须是模型中已存在的
        :type name: str
        :param value: 值，只有static型属性可以填写
        :type value: object
        :param device_id: 设备ID，只有measurement型属性可以填写
        :type device_id: str
        """
        
        

        self._name = None
        self._value = None
        self._device_id = None
        self.discriminator = None

        self.name = name
        if value is not None:
            self.value = value
        if device_id is not None:
            self.device_id = device_id

    @property
    def name(self):
        """Gets the name of this PropertyRequest.

        属性名称，必须是模型中已存在的

        :return: The name of this PropertyRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PropertyRequest.

        属性名称，必须是模型中已存在的

        :param name: The name of this PropertyRequest.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this PropertyRequest.

        值，只有static型属性可以填写

        :return: The value of this PropertyRequest.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PropertyRequest.

        值，只有static型属性可以填写

        :param value: The value of this PropertyRequest.
        :type value: object
        """
        self._value = value

    @property
    def device_id(self):
        """Gets the device_id of this PropertyRequest.

        设备ID，只有measurement型属性可以填写

        :return: The device_id of this PropertyRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this PropertyRequest.

        设备ID，只有measurement型属性可以填写

        :param device_id: The device_id of this PropertyRequest.
        :type device_id: str
        """
        self._device_id = device_id

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
        if not isinstance(other, PropertyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
