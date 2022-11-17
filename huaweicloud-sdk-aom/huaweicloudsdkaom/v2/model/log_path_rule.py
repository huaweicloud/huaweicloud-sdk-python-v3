# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogPathRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'args': 'list[str]',
        'name_type': 'str',
        'value': 'list[str]'
    }

    attribute_map = {
        'args': 'args',
        'name_type': 'nameType',
        'value': 'value'
    }

    def __init__(self, args=None, name_type=None, value=None):
        """LogPathRule

        The model defined in huaweicloud sdk

        :param args: 命令行。
        :type args: list[str]
        :param name_type: 取值类型。 cmdLineHash
        :type name_type: str
        :param value: 日志路径。
        :type value: list[str]
        """
        
        

        self._args = None
        self._name_type = None
        self._value = None
        self.discriminator = None

        self.args = args
        self.name_type = name_type
        self.value = value

    @property
    def args(self):
        """Gets the args of this LogPathRule.

        命令行。

        :return: The args of this LogPathRule.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this LogPathRule.

        命令行。

        :param args: The args of this LogPathRule.
        :type args: list[str]
        """
        self._args = args

    @property
    def name_type(self):
        """Gets the name_type of this LogPathRule.

        取值类型。 cmdLineHash

        :return: The name_type of this LogPathRule.
        :rtype: str
        """
        return self._name_type

    @name_type.setter
    def name_type(self, name_type):
        """Sets the name_type of this LogPathRule.

        取值类型。 cmdLineHash

        :param name_type: The name_type of this LogPathRule.
        :type name_type: str
        """
        self._name_type = name_type

    @property
    def value(self):
        """Gets the value of this LogPathRule.

        日志路径。

        :return: The value of this LogPathRule.
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this LogPathRule.

        日志路径。

        :param value: The value of this LogPathRule.
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
        if not isinstance(other, LogPathRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
