# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentConfigCompare:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_version': 'str',
        'compare_version': 'str'
    }

    attribute_map = {
        'base_version': 'base_version',
        'compare_version': 'compare_version'
    }

    def __init__(self, base_version=None, compare_version=None):
        """ComponentConfigCompare

        The model defined in huaweicloud sdk

        :param base_version: 
        :type base_version: str
        :param compare_version: 
        :type compare_version: str
        """
        
        

        self._base_version = None
        self._compare_version = None
        self.discriminator = None

        if base_version is not None:
            self.base_version = base_version
        if compare_version is not None:
            self.compare_version = compare_version

    @property
    def base_version(self):
        """Gets the base_version of this ComponentConfigCompare.

        :return: The base_version of this ComponentConfigCompare.
        :rtype: str
        """
        return self._base_version

    @base_version.setter
    def base_version(self, base_version):
        """Sets the base_version of this ComponentConfigCompare.

        :param base_version: The base_version of this ComponentConfigCompare.
        :type base_version: str
        """
        self._base_version = base_version

    @property
    def compare_version(self):
        """Gets the compare_version of this ComponentConfigCompare.

        :return: The compare_version of this ComponentConfigCompare.
        :rtype: str
        """
        return self._compare_version

    @compare_version.setter
    def compare_version(self, compare_version):
        """Sets the compare_version of this ComponentConfigCompare.

        :param compare_version: The compare_version of this ComponentConfigCompare.
        :type compare_version: str
        """
        self._compare_version = compare_version

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
        if not isinstance(other, ComponentConfigCompare):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
