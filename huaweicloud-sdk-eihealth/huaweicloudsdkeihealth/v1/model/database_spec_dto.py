# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseSpecDto:

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
        'name': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name'
    }

    def __init__(self, code=None, name=None):
        """DatabaseSpecDto

        The model defined in huaweicloud sdk

        :param code: 规格编号
        :type code: str
        :param name: 规格名称
        :type name: str
        """
        
        

        self._code = None
        self._name = None
        self.discriminator = None

        self.code = code
        self.name = name

    @property
    def code(self):
        """Gets the code of this DatabaseSpecDto.

        规格编号

        :return: The code of this DatabaseSpecDto.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DatabaseSpecDto.

        规格编号

        :param code: The code of this DatabaseSpecDto.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this DatabaseSpecDto.

        规格名称

        :return: The name of this DatabaseSpecDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatabaseSpecDto.

        规格名称

        :param name: The name of this DatabaseSpecDto.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, DatabaseSpecDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
