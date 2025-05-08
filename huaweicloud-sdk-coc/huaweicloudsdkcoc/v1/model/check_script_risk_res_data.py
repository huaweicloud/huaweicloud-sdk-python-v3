# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckScriptRiskResData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_level': 'str',
        'blacklist_commands': 'list[CheckScriptRiskResDataBlacklistCommands]'
    }

    attribute_map = {
        'risk_level': 'risk_level',
        'blacklist_commands': 'blacklist_commands'
    }

    def __init__(self, risk_level=None, blacklist_commands=None):
        r"""CheckScriptRiskResData

        The model defined in huaweicloud sdk

        :param risk_level: 风险等级。
        :type risk_level: str
        :param blacklist_commands: 黑名单列表。
        :type blacklist_commands: list[:class:`huaweicloudsdkcoc.v1.CheckScriptRiskResDataBlacklistCommands`]
        """
        
        

        self._risk_level = None
        self._blacklist_commands = None
        self.discriminator = None

        self.risk_level = risk_level
        if blacklist_commands is not None:
            self.blacklist_commands = blacklist_commands

    @property
    def risk_level(self):
        r"""Gets the risk_level of this CheckScriptRiskResData.

        风险等级。

        :return: The risk_level of this CheckScriptRiskResData.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this CheckScriptRiskResData.

        风险等级。

        :param risk_level: The risk_level of this CheckScriptRiskResData.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def blacklist_commands(self):
        r"""Gets the blacklist_commands of this CheckScriptRiskResData.

        黑名单列表。

        :return: The blacklist_commands of this CheckScriptRiskResData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CheckScriptRiskResDataBlacklistCommands`]
        """
        return self._blacklist_commands

    @blacklist_commands.setter
    def blacklist_commands(self, blacklist_commands):
        r"""Sets the blacklist_commands of this CheckScriptRiskResData.

        黑名单列表。

        :param blacklist_commands: The blacklist_commands of this CheckScriptRiskResData.
        :type blacklist_commands: list[:class:`huaweicloudsdkcoc.v1.CheckScriptRiskResDataBlacklistCommands`]
        """
        self._blacklist_commands = blacklist_commands

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
        if not isinstance(other, CheckScriptRiskResData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
