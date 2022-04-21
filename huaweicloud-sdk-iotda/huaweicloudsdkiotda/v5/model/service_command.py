# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceCommand:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'command_name': 'str',
        'paras': 'list[ServiceCommandPara]',
        'responses': 'list[ServiceCommandResponse]'
    }

    attribute_map = {
        'command_name': 'command_name',
        'paras': 'paras',
        'responses': 'responses'
    }

    def __init__(self, command_name=None, paras=None, responses=None):
        """ServiceCommand

        The model defined in huaweicloud sdk

        :param command_name: **参数说明**：设备命令名称。注：设备服务内不允许重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type command_name: str
        :param paras: **参数说明**：设备命令的参数列表。
        :type paras: list[:class:`huaweicloudsdkiotda.v5.ServiceCommandPara`]
        :param responses: **参数说明**：设备命令的响应列表。
        :type responses: list[:class:`huaweicloudsdkiotda.v5.ServiceCommandResponse`]
        """
        
        

        self._command_name = None
        self._paras = None
        self._responses = None
        self.discriminator = None

        self.command_name = command_name
        if paras is not None:
            self.paras = paras
        if responses is not None:
            self.responses = responses

    @property
    def command_name(self):
        """Gets the command_name of this ServiceCommand.

        **参数说明**：设备命令名称。注：设备服务内不允许重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The command_name of this ServiceCommand.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """Sets the command_name of this ServiceCommand.

        **参数说明**：设备命令名称。注：设备服务内不允许重复。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param command_name: The command_name of this ServiceCommand.
        :type command_name: str
        """
        self._command_name = command_name

    @property
    def paras(self):
        """Gets the paras of this ServiceCommand.

        **参数说明**：设备命令的参数列表。

        :return: The paras of this ServiceCommand.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ServiceCommandPara`]
        """
        return self._paras

    @paras.setter
    def paras(self, paras):
        """Sets the paras of this ServiceCommand.

        **参数说明**：设备命令的参数列表。

        :param paras: The paras of this ServiceCommand.
        :type paras: list[:class:`huaweicloudsdkiotda.v5.ServiceCommandPara`]
        """
        self._paras = paras

    @property
    def responses(self):
        """Gets the responses of this ServiceCommand.

        **参数说明**：设备命令的响应列表。

        :return: The responses of this ServiceCommand.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.ServiceCommandResponse`]
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """Sets the responses of this ServiceCommand.

        **参数说明**：设备命令的响应列表。

        :param responses: The responses of this ServiceCommand.
        :type responses: list[:class:`huaweicloudsdkiotda.v5.ServiceCommandResponse`]
        """
        self._responses = responses

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
        if not isinstance(other, ServiceCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
