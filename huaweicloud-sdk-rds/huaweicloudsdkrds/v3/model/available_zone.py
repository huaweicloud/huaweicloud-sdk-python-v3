# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableZone:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'description': 'str'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description'
    }

    def __init__(self, code=None, description=None):
        """AvailableZone

        The model defined in huaweicloud sdk

        :param code: 可用区编码。
        :type code: str
        :param description: 可用区描述。
        :type description: str
        """
        
        

        self._code = None
        self._description = None
        self.discriminator = None

        self.code = code
        self.description = description

    @property
    def code(self):
        """Gets the code of this AvailableZone.

        可用区编码。

        :return: The code of this AvailableZone.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AvailableZone.

        可用区编码。

        :param code: The code of this AvailableZone.
        :type code: str
        """
        self._code = code

    @property
    def description(self):
        """Gets the description of this AvailableZone.

        可用区描述。

        :return: The description of this AvailableZone.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AvailableZone.

        可用区描述。

        :param description: The description of this AvailableZone.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, AvailableZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
