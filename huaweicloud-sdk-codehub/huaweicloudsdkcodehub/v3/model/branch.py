# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Branch:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_protected': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'is_protected': 'is_protected',
        'name': 'name'
    }

    def __init__(self, is_protected=None, name=None):
        """Branch

        The model defined in huaweicloud sdk

        :param is_protected: 是否开启保护分支功能
        :type is_protected: bool
        :param name: 分支名
        :type name: str
        """
        
        

        self._is_protected = None
        self._name = None
        self.discriminator = None

        if is_protected is not None:
            self.is_protected = is_protected
        if name is not None:
            self.name = name

    @property
    def is_protected(self):
        """Gets the is_protected of this Branch.

        是否开启保护分支功能

        :return: The is_protected of this Branch.
        :rtype: bool
        """
        return self._is_protected

    @is_protected.setter
    def is_protected(self, is_protected):
        """Sets the is_protected of this Branch.

        是否开启保护分支功能

        :param is_protected: The is_protected of this Branch.
        :type is_protected: bool
        """
        self._is_protected = is_protected

    @property
    def name(self):
        """Gets the name of this Branch.

        分支名

        :return: The name of this Branch.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Branch.

        分支名

        :param name: The name of this Branch.
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
        if not isinstance(other, Branch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
