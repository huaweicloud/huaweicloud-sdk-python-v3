# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchConfirmLiveCommandsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command': 'str',
        'action': 'str',
        'command_ids': 'list[str]'
    }

    attribute_map = {
        'command': 'command',
        'action': 'action',
        'command_ids': 'command_ids'
    }

    def __init__(self, command=None, action=None, command_ids=None):
        r"""BatchConfirmLiveCommandsReq

        The model defined in huaweicloud sdk

        :param command: 命令名称。 - REWRITE_PLAY_SCRIPT: 动态编辑未播放剧本。 - REWRITE_INTERACTION_RULES: 动态修改互动规则。
        :type command: str
        :param action: 确认操作。 * confirm: 确认。 * reject: 拒绝。
        :type action: str
        :param command_ids: 命令ID列表。不填则为全部未播放的插入命令均清理。
        :type command_ids: list[str]
        """
        
        

        self._command = None
        self._action = None
        self._command_ids = None
        self.discriminator = None

        if command is not None:
            self.command = command
        if action is not None:
            self.action = action
        if command_ids is not None:
            self.command_ids = command_ids

    @property
    def command(self):
        r"""Gets the command of this BatchConfirmLiveCommandsReq.

        命令名称。 - REWRITE_PLAY_SCRIPT: 动态编辑未播放剧本。 - REWRITE_INTERACTION_RULES: 动态修改互动规则。

        :return: The command of this BatchConfirmLiveCommandsReq.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this BatchConfirmLiveCommandsReq.

        命令名称。 - REWRITE_PLAY_SCRIPT: 动态编辑未播放剧本。 - REWRITE_INTERACTION_RULES: 动态修改互动规则。

        :param command: The command of this BatchConfirmLiveCommandsReq.
        :type command: str
        """
        self._command = command

    @property
    def action(self):
        r"""Gets the action of this BatchConfirmLiveCommandsReq.

        确认操作。 * confirm: 确认。 * reject: 拒绝。

        :return: The action of this BatchConfirmLiveCommandsReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchConfirmLiveCommandsReq.

        确认操作。 * confirm: 确认。 * reject: 拒绝。

        :param action: The action of this BatchConfirmLiveCommandsReq.
        :type action: str
        """
        self._action = action

    @property
    def command_ids(self):
        r"""Gets the command_ids of this BatchConfirmLiveCommandsReq.

        命令ID列表。不填则为全部未播放的插入命令均清理。

        :return: The command_ids of this BatchConfirmLiveCommandsReq.
        :rtype: list[str]
        """
        return self._command_ids

    @command_ids.setter
    def command_ids(self, command_ids):
        r"""Sets the command_ids of this BatchConfirmLiveCommandsReq.

        命令ID列表。不填则为全部未播放的插入命令均清理。

        :param command_ids: The command_ids of this BatchConfirmLiveCommandsReq.
        :type command_ids: list[str]
        """
        self._command_ids = command_ids

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
        if not isinstance(other, BatchConfirmLiveCommandsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
