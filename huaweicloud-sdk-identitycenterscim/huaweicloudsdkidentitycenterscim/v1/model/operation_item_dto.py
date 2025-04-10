# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationItemDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'op': 'str',
        'path': 'str',
        'value': 'object'
    }

    attribute_map = {
        'op': 'op',
        'path': 'path',
        'value': 'value'
    }

    def __init__(self, op=None, path=None, value=None):
        r"""OperationItemDto

        The model defined in huaweicloud sdk

        :param op: 要执行的修改操作类型。 add：添加属性，replace：替换属性，remove：删除属性
        :type op: str
        :param path: 要修改的属性路径
        :type path: str
        :param value: 要修改的属性值。执行删除操作时不填写
        :type value: object
        """
        
        

        self._op = None
        self._path = None
        self._value = None
        self.discriminator = None

        self.op = op
        if path is not None:
            self.path = path
        if value is not None:
            self.value = value

    @property
    def op(self):
        r"""Gets the op of this OperationItemDto.

        要执行的修改操作类型。 add：添加属性，replace：替换属性，remove：删除属性

        :return: The op of this OperationItemDto.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        r"""Sets the op of this OperationItemDto.

        要执行的修改操作类型。 add：添加属性，replace：替换属性，remove：删除属性

        :param op: The op of this OperationItemDto.
        :type op: str
        """
        self._op = op

    @property
    def path(self):
        r"""Gets the path of this OperationItemDto.

        要修改的属性路径

        :return: The path of this OperationItemDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this OperationItemDto.

        要修改的属性路径

        :param path: The path of this OperationItemDto.
        :type path: str
        """
        self._path = path

    @property
    def value(self):
        r"""Gets the value of this OperationItemDto.

        要修改的属性值。执行删除操作时不填写

        :return: The value of this OperationItemDto.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OperationItemDto.

        要修改的属性值。执行删除操作时不填写

        :param value: The value of this OperationItemDto.
        :type value: object
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
        if not isinstance(other, OperationItemDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
