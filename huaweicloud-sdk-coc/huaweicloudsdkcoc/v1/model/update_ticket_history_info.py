# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTicketHistoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_id': 'str',
        'action': 'str',
        'sub_action': 'str',
        'operator': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'action_id': 'action_id',
        'action': 'action',
        'sub_action': 'sub_action',
        'operator': 'operator',
        'comment': 'comment'
    }

    def __init__(self, action_id=None, action=None, sub_action=None, operator=None, comment=None):
        r"""UpdateTicketHistoryInfo

        The model defined in huaweicloud sdk

        :param action_id: 操作标识
        :type action_id: str
        :param action: 动作
        :type action: str
        :param sub_action: 子动作
        :type sub_action: str
        :param operator: 操作人
        :type operator: str
        :param comment: 评论
        :type comment: str
        """
        
        

        self._action_id = None
        self._action = None
        self._sub_action = None
        self._operator = None
        self._comment = None
        self.discriminator = None

        if action_id is not None:
            self.action_id = action_id
        if action is not None:
            self.action = action
        if sub_action is not None:
            self.sub_action = sub_action
        if operator is not None:
            self.operator = operator
        if comment is not None:
            self.comment = comment

    @property
    def action_id(self):
        r"""Gets the action_id of this UpdateTicketHistoryInfo.

        操作标识

        :return: The action_id of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this UpdateTicketHistoryInfo.

        操作标识

        :param action_id: The action_id of this UpdateTicketHistoryInfo.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def action(self):
        r"""Gets the action of this UpdateTicketHistoryInfo.

        动作

        :return: The action of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateTicketHistoryInfo.

        动作

        :param action: The action of this UpdateTicketHistoryInfo.
        :type action: str
        """
        self._action = action

    @property
    def sub_action(self):
        r"""Gets the sub_action of this UpdateTicketHistoryInfo.

        子动作

        :return: The sub_action of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._sub_action

    @sub_action.setter
    def sub_action(self, sub_action):
        r"""Sets the sub_action of this UpdateTicketHistoryInfo.

        子动作

        :param sub_action: The sub_action of this UpdateTicketHistoryInfo.
        :type sub_action: str
        """
        self._sub_action = sub_action

    @property
    def operator(self):
        r"""Gets the operator of this UpdateTicketHistoryInfo.

        操作人

        :return: The operator of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this UpdateTicketHistoryInfo.

        操作人

        :param operator: The operator of this UpdateTicketHistoryInfo.
        :type operator: str
        """
        self._operator = operator

    @property
    def comment(self):
        r"""Gets the comment of this UpdateTicketHistoryInfo.

        评论

        :return: The comment of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this UpdateTicketHistoryInfo.

        评论

        :param comment: The comment of this UpdateTicketHistoryInfo.
        :type comment: str
        """
        self._comment = comment

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateTicketHistoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
