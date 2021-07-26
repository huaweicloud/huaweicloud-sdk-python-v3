# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Validity:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'start_from': 'str',
        'type': 'str',
        'value': 'int'
    }

    attribute_map = {
        'start_from': 'start_from',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, start_from=None, type=None, value=None):
        """Validity - a model defined in huaweicloud sdk"""
        
        

        self._start_from = None
        self._type = None
        self._value = None
        self.discriminator = None

        if start_from is not None:
            self.start_from = start_from
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def start_from(self):
        """Gets the start_from of this Validity.

        起始时间

        :return: The start_from of this Validity.
        :rtype: str
        """
        return self._start_from

    @start_from.setter
    def start_from(self, start_from):
        """Sets the start_from of this Validity.

        起始时间

        :param start_from: The start_from of this Validity.
        :type: str
        """
        self._start_from = start_from

    @property
    def type(self):
        """Gets the type of this Validity.

        有效期类型

        :return: The type of this Validity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Validity.

        有效期类型

        :param type: The type of this Validity.
        :type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this Validity.

        路径长度

        :return: The value of this Validity.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Validity.

        路径长度

        :param value: The value of this Validity.
        :type: int
        """
        self._value = value

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Validity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
