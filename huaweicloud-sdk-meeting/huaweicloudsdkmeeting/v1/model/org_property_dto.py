# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrgPropertyDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'property_key': 'str',
        'property_value': 'str'
    }

    attribute_map = {
        'property_key': 'propertyKey',
        'property_value': 'propertyValue'
    }

    def __init__(self, property_key=None, property_value=None):
        """OrgPropertyDTO

        The model defined in huaweicloud sdk

        :param property_key: 配置项key。 开通本地录制功能，参数填写：enableClientRecord。 
        :type property_key: str
        :param property_value: 配置项值。 开通本地录制功能，参数填写：true。 
        :type property_value: str
        """
        
        

        self._property_key = None
        self._property_value = None
        self.discriminator = None

        if property_key is not None:
            self.property_key = property_key
        if property_value is not None:
            self.property_value = property_value

    @property
    def property_key(self):
        """Gets the property_key of this OrgPropertyDTO.

        配置项key。 开通本地录制功能，参数填写：enableClientRecord。 

        :return: The property_key of this OrgPropertyDTO.
        :rtype: str
        """
        return self._property_key

    @property_key.setter
    def property_key(self, property_key):
        """Sets the property_key of this OrgPropertyDTO.

        配置项key。 开通本地录制功能，参数填写：enableClientRecord。 

        :param property_key: The property_key of this OrgPropertyDTO.
        :type property_key: str
        """
        self._property_key = property_key

    @property
    def property_value(self):
        """Gets the property_value of this OrgPropertyDTO.

        配置项值。 开通本地录制功能，参数填写：true。 

        :return: The property_value of this OrgPropertyDTO.
        :rtype: str
        """
        return self._property_value

    @property_value.setter
    def property_value(self, property_value):
        """Sets the property_value of this OrgPropertyDTO.

        配置项值。 开通本地录制功能，参数填写：true。 

        :param property_value: The property_value of this OrgPropertyDTO.
        :type property_value: str
        """
        self._property_value = property_value

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
        if not isinstance(other, OrgPropertyDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
