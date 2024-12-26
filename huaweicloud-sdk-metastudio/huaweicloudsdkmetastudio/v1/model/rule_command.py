# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleCommand:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'room_id': 'str',
        'job_id': 'str',
        'command_id': 'str',
        'interaction_rules': 'list[LiveRoomInteractionRuleInfo]'
    }

    attribute_map = {
        'room_id': 'room_id',
        'job_id': 'job_id',
        'command_id': 'command_id',
        'interaction_rules': 'interaction_rules'
    }

    def __init__(self, room_id=None, job_id=None, command_id=None, interaction_rules=None):
        """RuleCommand

        The model defined in huaweicloud sdk

        :param room_id: 直播间ID
        :type room_id: str
        :param job_id: 直播任务ID。
        :type job_id: str
        :param command_id: 命令ID。
        :type command_id: str
        :param interaction_rules: 互动规则列表
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionRuleInfo`]
        """
        
        

        self._room_id = None
        self._job_id = None
        self._command_id = None
        self._interaction_rules = None
        self.discriminator = None

        if room_id is not None:
            self.room_id = room_id
        if job_id is not None:
            self.job_id = job_id
        if command_id is not None:
            self.command_id = command_id
        if interaction_rules is not None:
            self.interaction_rules = interaction_rules

    @property
    def room_id(self):
        """Gets the room_id of this RuleCommand.

        直播间ID

        :return: The room_id of this RuleCommand.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this RuleCommand.

        直播间ID

        :param room_id: The room_id of this RuleCommand.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def job_id(self):
        """Gets the job_id of this RuleCommand.

        直播任务ID。

        :return: The job_id of this RuleCommand.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RuleCommand.

        直播任务ID。

        :param job_id: The job_id of this RuleCommand.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def command_id(self):
        """Gets the command_id of this RuleCommand.

        命令ID。

        :return: The command_id of this RuleCommand.
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this RuleCommand.

        命令ID。

        :param command_id: The command_id of this RuleCommand.
        :type command_id: str
        """
        self._command_id = command_id

    @property
    def interaction_rules(self):
        """Gets the interaction_rules of this RuleCommand.

        互动规则列表

        :return: The interaction_rules of this RuleCommand.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionRuleInfo`]
        """
        return self._interaction_rules

    @interaction_rules.setter
    def interaction_rules(self, interaction_rules):
        """Sets the interaction_rules of this RuleCommand.

        互动规则列表

        :param interaction_rules: The interaction_rules of this RuleCommand.
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionRuleInfo`]
        """
        self._interaction_rules = interaction_rules

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
        if not isinstance(other, RuleCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
