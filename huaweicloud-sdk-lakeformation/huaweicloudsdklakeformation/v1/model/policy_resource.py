# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_excludes': 'bool',
        'is_recursive': 'bool',
        'values': 'list[str]'
    }

    attribute_map = {
        'is_excludes': 'is_excludes',
        'is_recursive': 'is_recursive',
        'values': 'values'
    }

    def __init__(self, is_excludes=None, is_recursive=None, values=None):
        r"""PolicyResource

        The model defined in huaweicloud sdk

        :param is_excludes: 是否排除
        :type is_excludes: bool
        :param is_recursive: 是否递归
        :type is_recursive: bool
        :param values: 值
        :type values: list[str]
        """
        
        

        self._is_excludes = None
        self._is_recursive = None
        self._values = None
        self.discriminator = None

        if is_excludes is not None:
            self.is_excludes = is_excludes
        if is_recursive is not None:
            self.is_recursive = is_recursive
        if values is not None:
            self.values = values

    @property
    def is_excludes(self):
        r"""Gets the is_excludes of this PolicyResource.

        是否排除

        :return: The is_excludes of this PolicyResource.
        :rtype: bool
        """
        return self._is_excludes

    @is_excludes.setter
    def is_excludes(self, is_excludes):
        r"""Sets the is_excludes of this PolicyResource.

        是否排除

        :param is_excludes: The is_excludes of this PolicyResource.
        :type is_excludes: bool
        """
        self._is_excludes = is_excludes

    @property
    def is_recursive(self):
        r"""Gets the is_recursive of this PolicyResource.

        是否递归

        :return: The is_recursive of this PolicyResource.
        :rtype: bool
        """
        return self._is_recursive

    @is_recursive.setter
    def is_recursive(self, is_recursive):
        r"""Sets the is_recursive of this PolicyResource.

        是否递归

        :param is_recursive: The is_recursive of this PolicyResource.
        :type is_recursive: bool
        """
        self._is_recursive = is_recursive

    @property
    def values(self):
        r"""Gets the values of this PolicyResource.

        值

        :return: The values of this PolicyResource.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this PolicyResource.

        值

        :param values: The values of this PolicyResource.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, PolicyResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
