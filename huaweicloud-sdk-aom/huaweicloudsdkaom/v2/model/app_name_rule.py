# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppNameRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name_type': 'str',
        'args': 'list[str]',
        'value': 'list[str]'
    }

    attribute_map = {
        'name_type': 'nameType',
        'args': 'args',
        'value': 'value'
    }

    def __init__(self, name_type=None, args=None, value=None):
        r"""AppNameRule

        The model defined in huaweicloud sdk

        :param name_type: 取值类型。从cmdLineHash、cmdLine、env、str里面选取。
        :type name_type: str
        :param args: 输入值。
        :type args: list[str]
        :param value: 服务名(仅nameType为cmdLineHash时填写)。
        :type value: list[str]
        """
        
        

        self._name_type = None
        self._args = None
        self._value = None
        self.discriminator = None

        self.name_type = name_type
        self.args = args
        if value is not None:
            self.value = value

    @property
    def name_type(self):
        r"""Gets the name_type of this AppNameRule.

        取值类型。从cmdLineHash、cmdLine、env、str里面选取。

        :return: The name_type of this AppNameRule.
        :rtype: str
        """
        return self._name_type

    @name_type.setter
    def name_type(self, name_type):
        r"""Sets the name_type of this AppNameRule.

        取值类型。从cmdLineHash、cmdLine、env、str里面选取。

        :param name_type: The name_type of this AppNameRule.
        :type name_type: str
        """
        self._name_type = name_type

    @property
    def args(self):
        r"""Gets the args of this AppNameRule.

        输入值。

        :return: The args of this AppNameRule.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        r"""Sets the args of this AppNameRule.

        输入值。

        :param args: The args of this AppNameRule.
        :type args: list[str]
        """
        self._args = args

    @property
    def value(self):
        r"""Gets the value of this AppNameRule.

        服务名(仅nameType为cmdLineHash时填写)。

        :return: The value of this AppNameRule.
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this AppNameRule.

        服务名(仅nameType为cmdLineHash时填写)。

        :param value: The value of this AppNameRule.
        :type value: list[str]
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
        if not isinstance(other, AppNameRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
