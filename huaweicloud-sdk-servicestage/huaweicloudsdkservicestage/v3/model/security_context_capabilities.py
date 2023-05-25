# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityContextCapabilities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add': 'list[str]',
        'drop': 'list[str]'
    }

    attribute_map = {
        'add': 'add',
        'drop': 'drop'
    }

    def __init__(self, add=None, drop=None):
        """SecurityContextCapabilities

        The model defined in huaweicloud sdk

        :param add: 
        :type add: list[str]
        :param drop: 
        :type drop: list[str]
        """
        
        

        self._add = None
        self._drop = None
        self.discriminator = None

        if add is not None:
            self.add = add
        if drop is not None:
            self.drop = drop

    @property
    def add(self):
        """Gets the add of this SecurityContextCapabilities.

        :return: The add of this SecurityContextCapabilities.
        :rtype: list[str]
        """
        return self._add

    @add.setter
    def add(self, add):
        """Sets the add of this SecurityContextCapabilities.

        :param add: The add of this SecurityContextCapabilities.
        :type add: list[str]
        """
        self._add = add

    @property
    def drop(self):
        """Gets the drop of this SecurityContextCapabilities.

        :return: The drop of this SecurityContextCapabilities.
        :rtype: list[str]
        """
        return self._drop

    @drop.setter
    def drop(self, drop):
        """Sets the drop of this SecurityContextCapabilities.

        :param drop: The drop of this SecurityContextCapabilities.
        :type drop: list[str]
        """
        self._drop = drop

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
        if not isinstance(other, SecurityContextCapabilities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
