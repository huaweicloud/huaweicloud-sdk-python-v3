# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PhoneProperty:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone_id': 'str',
        '_property': 'str'
    }

    attribute_map = {
        'phone_id': 'phone_id',
        '_property': 'property'
    }

    def __init__(self, phone_id=None, _property=None):
        """PhoneProperty

        The model defined in huaweicloud sdk

        :param phone_id: 云手机id
        :type phone_id: str
        :param _property: 云手机属性列表
        :type _property: str
        """
        
        

        self._phone_id = None
        self.__property = None
        self.discriminator = None

        self.phone_id = phone_id
        if _property is not None:
            self._property = _property

    @property
    def phone_id(self):
        """Gets the phone_id of this PhoneProperty.

        云手机id

        :return: The phone_id of this PhoneProperty.
        :rtype: str
        """
        return self._phone_id

    @phone_id.setter
    def phone_id(self, phone_id):
        """Sets the phone_id of this PhoneProperty.

        云手机id

        :param phone_id: The phone_id of this PhoneProperty.
        :type phone_id: str
        """
        self._phone_id = phone_id

    @property
    def _property(self):
        """Gets the _property of this PhoneProperty.

        云手机属性列表

        :return: The _property of this PhoneProperty.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this PhoneProperty.

        云手机属性列表

        :param _property: The _property of this PhoneProperty.
        :type _property: str
        """
        self.__property = _property

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
        if not isinstance(other, PhoneProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
