# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LifecycleEntrypoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command': 'list[str]',
        'args': 'list[str]'
    }

    attribute_map = {
        'command': 'command',
        'args': 'args'
    }

    def __init__(self, command=None, args=None):
        r"""LifecycleEntrypoint

        The model defined in huaweicloud sdk

        :param command: 执行命令行
        :type command: list[str]
        :param args: 运行参数
        :type args: list[str]
        """
        
        

        self._command = None
        self._args = None
        self.discriminator = None

        if command is not None:
            self.command = command
        if args is not None:
            self.args = args

    @property
    def command(self):
        r"""Gets the command of this LifecycleEntrypoint.

        执行命令行

        :return: The command of this LifecycleEntrypoint.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this LifecycleEntrypoint.

        执行命令行

        :param command: The command of this LifecycleEntrypoint.
        :type command: list[str]
        """
        self._command = command

    @property
    def args(self):
        r"""Gets the args of this LifecycleEntrypoint.

        运行参数

        :return: The args of this LifecycleEntrypoint.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        r"""Sets the args of this LifecycleEntrypoint.

        运行参数

        :param args: The args of this LifecycleEntrypoint.
        :type args: list[str]
        """
        self._args = args

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
        if not isinstance(other, LifecycleEntrypoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
