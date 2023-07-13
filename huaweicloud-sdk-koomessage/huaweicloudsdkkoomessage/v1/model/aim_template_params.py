# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIMTemplateParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'name': 'str',
        'has_length': 'bool',
        'fix_length': 'int',
        'length_restrict': 'bool',
        'min_length': 'int',
        'max_length': 'int'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'has_length': 'has_length',
        'fix_length': 'fix_length',
        'length_restrict': 'length_restrict',
        'min_length': 'min_length',
        'max_length': 'max_length'
    }

    def __init__(self, type=None, name=None, has_length=None, fix_length=None, length_restrict=None, min_length=None, max_length=None):
        """AIMTemplateParams

        The model defined in huaweicloud sdk

        :param type: 参数类型。 - string：文本 - integer：数字 
        :type type: str
        :param name: 参数名称。
        :type name: str
        :param has_length: 动态参数是否长度限制。 - false：不可设置  - true：可设置 
        :type has_length: bool
        :param fix_length: 固定长度。
        :type fix_length: int
        :param length_restrict: 长度限制。
        :type length_restrict: bool
        :param min_length: 最小长度。
        :type min_length: int
        :param max_length: 最大长度。
        :type max_length: int
        """
        
        

        self._type = None
        self._name = None
        self._has_length = None
        self._fix_length = None
        self._length_restrict = None
        self._min_length = None
        self._max_length = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if has_length is not None:
            self.has_length = has_length
        if fix_length is not None:
            self.fix_length = fix_length
        if length_restrict is not None:
            self.length_restrict = length_restrict
        if min_length is not None:
            self.min_length = min_length
        if max_length is not None:
            self.max_length = max_length

    @property
    def type(self):
        """Gets the type of this AIMTemplateParams.

        参数类型。 - string：文本 - integer：数字 

        :return: The type of this AIMTemplateParams.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AIMTemplateParams.

        参数类型。 - string：文本 - integer：数字 

        :param type: The type of this AIMTemplateParams.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this AIMTemplateParams.

        参数名称。

        :return: The name of this AIMTemplateParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AIMTemplateParams.

        参数名称。

        :param name: The name of this AIMTemplateParams.
        :type name: str
        """
        self._name = name

    @property
    def has_length(self):
        """Gets the has_length of this AIMTemplateParams.

        动态参数是否长度限制。 - false：不可设置  - true：可设置 

        :return: The has_length of this AIMTemplateParams.
        :rtype: bool
        """
        return self._has_length

    @has_length.setter
    def has_length(self, has_length):
        """Sets the has_length of this AIMTemplateParams.

        动态参数是否长度限制。 - false：不可设置  - true：可设置 

        :param has_length: The has_length of this AIMTemplateParams.
        :type has_length: bool
        """
        self._has_length = has_length

    @property
    def fix_length(self):
        """Gets the fix_length of this AIMTemplateParams.

        固定长度。

        :return: The fix_length of this AIMTemplateParams.
        :rtype: int
        """
        return self._fix_length

    @fix_length.setter
    def fix_length(self, fix_length):
        """Sets the fix_length of this AIMTemplateParams.

        固定长度。

        :param fix_length: The fix_length of this AIMTemplateParams.
        :type fix_length: int
        """
        self._fix_length = fix_length

    @property
    def length_restrict(self):
        """Gets the length_restrict of this AIMTemplateParams.

        长度限制。

        :return: The length_restrict of this AIMTemplateParams.
        :rtype: bool
        """
        return self._length_restrict

    @length_restrict.setter
    def length_restrict(self, length_restrict):
        """Sets the length_restrict of this AIMTemplateParams.

        长度限制。

        :param length_restrict: The length_restrict of this AIMTemplateParams.
        :type length_restrict: bool
        """
        self._length_restrict = length_restrict

    @property
    def min_length(self):
        """Gets the min_length of this AIMTemplateParams.

        最小长度。

        :return: The min_length of this AIMTemplateParams.
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this AIMTemplateParams.

        最小长度。

        :param min_length: The min_length of this AIMTemplateParams.
        :type min_length: int
        """
        self._min_length = min_length

    @property
    def max_length(self):
        """Gets the max_length of this AIMTemplateParams.

        最大长度。

        :return: The max_length of this AIMTemplateParams.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this AIMTemplateParams.

        最大长度。

        :param max_length: The max_length of this AIMTemplateParams.
        :type max_length: int
        """
        self._max_length = max_length

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
        if not isinstance(other, AIMTemplateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
