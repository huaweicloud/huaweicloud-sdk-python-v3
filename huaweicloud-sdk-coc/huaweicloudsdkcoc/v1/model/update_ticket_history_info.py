# coding: utf-8

import six

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
        'current_cloud_service_id': 'str',
        'description': 'str',
        'level_id': 'str',
        'mtm_region': 'str',
        'mtm_type': 'str',
        'source_id': 'str',
        'title': 'str',
        'is_change_event': 'bool',
        'is_service_interrupt': 'bool',
        'action_id': 'str',
        'action': 'str',
        'sub_action': 'str',
        'operator': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'current_cloud_service_id': 'current_cloud_service_id',
        'description': 'description',
        'level_id': 'level_id',
        'mtm_region': 'mtm_region',
        'mtm_type': 'mtm_type',
        'source_id': 'source_id',
        'title': 'title',
        'is_change_event': 'is_change_event',
        'is_service_interrupt': 'is_service_interrupt',
        'action_id': 'action_id',
        'action': 'action',
        'sub_action': 'sub_action',
        'operator': 'operator',
        'comment': 'comment'
    }

    def __init__(self, current_cloud_service_id=None, description=None, level_id=None, mtm_region=None, mtm_type=None, source_id=None, title=None, is_change_event=None, is_service_interrupt=None, action_id=None, action=None, sub_action=None, operator=None, comment=None):
        r"""UpdateTicketHistoryInfo

        The model defined in huaweicloud sdk

        :param current_cloud_service_id: 扩展字段
        :type current_cloud_service_id: str
        :param description: 扩展字段
        :type description: str
        :param level_id: 扩展字段
        :type level_id: str
        :param mtm_region: 扩展字段
        :type mtm_region: str
        :param mtm_type: 扩展字段
        :type mtm_type: str
        :param source_id: 扩展字段
        :type source_id: str
        :param title: 扩展字段
        :type title: str
        :param is_change_event: 是否变更事件
        :type is_change_event: bool
        :param is_service_interrupt: 是否变更事件
        :type is_service_interrupt: bool
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
        
        

        self._current_cloud_service_id = None
        self._description = None
        self._level_id = None
        self._mtm_region = None
        self._mtm_type = None
        self._source_id = None
        self._title = None
        self._is_change_event = None
        self._is_service_interrupt = None
        self._action_id = None
        self._action = None
        self._sub_action = None
        self._operator = None
        self._comment = None
        self.discriminator = None

        if current_cloud_service_id is not None:
            self.current_cloud_service_id = current_cloud_service_id
        if description is not None:
            self.description = description
        if level_id is not None:
            self.level_id = level_id
        if mtm_region is not None:
            self.mtm_region = mtm_region
        if mtm_type is not None:
            self.mtm_type = mtm_type
        if source_id is not None:
            self.source_id = source_id
        if title is not None:
            self.title = title
        if is_change_event is not None:
            self.is_change_event = is_change_event
        if is_service_interrupt is not None:
            self.is_service_interrupt = is_service_interrupt
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
    def current_cloud_service_id(self):
        r"""Gets the current_cloud_service_id of this UpdateTicketHistoryInfo.

        扩展字段

        :return: The current_cloud_service_id of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._current_cloud_service_id

    @current_cloud_service_id.setter
    def current_cloud_service_id(self, current_cloud_service_id):
        r"""Sets the current_cloud_service_id of this UpdateTicketHistoryInfo.

        扩展字段

        :param current_cloud_service_id: The current_cloud_service_id of this UpdateTicketHistoryInfo.
        :type current_cloud_service_id: str
        """
        self._current_cloud_service_id = current_cloud_service_id

    @property
    def description(self):
        r"""Gets the description of this UpdateTicketHistoryInfo.

        扩展字段

        :return: The description of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateTicketHistoryInfo.

        扩展字段

        :param description: The description of this UpdateTicketHistoryInfo.
        :type description: str
        """
        self._description = description

    @property
    def level_id(self):
        r"""Gets the level_id of this UpdateTicketHistoryInfo.

        扩展字段

        :return: The level_id of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._level_id

    @level_id.setter
    def level_id(self, level_id):
        r"""Sets the level_id of this UpdateTicketHistoryInfo.

        扩展字段

        :param level_id: The level_id of this UpdateTicketHistoryInfo.
        :type level_id: str
        """
        self._level_id = level_id

    @property
    def mtm_region(self):
        r"""Gets the mtm_region of this UpdateTicketHistoryInfo.

        扩展字段

        :return: The mtm_region of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._mtm_region

    @mtm_region.setter
    def mtm_region(self, mtm_region):
        r"""Sets the mtm_region of this UpdateTicketHistoryInfo.

        扩展字段

        :param mtm_region: The mtm_region of this UpdateTicketHistoryInfo.
        :type mtm_region: str
        """
        self._mtm_region = mtm_region

    @property
    def mtm_type(self):
        r"""Gets the mtm_type of this UpdateTicketHistoryInfo.

        扩展字段

        :return: The mtm_type of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._mtm_type

    @mtm_type.setter
    def mtm_type(self, mtm_type):
        r"""Sets the mtm_type of this UpdateTicketHistoryInfo.

        扩展字段

        :param mtm_type: The mtm_type of this UpdateTicketHistoryInfo.
        :type mtm_type: str
        """
        self._mtm_type = mtm_type

    @property
    def source_id(self):
        r"""Gets the source_id of this UpdateTicketHistoryInfo.

        扩展字段

        :return: The source_id of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this UpdateTicketHistoryInfo.

        扩展字段

        :param source_id: The source_id of this UpdateTicketHistoryInfo.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def title(self):
        r"""Gets the title of this UpdateTicketHistoryInfo.

        扩展字段

        :return: The title of this UpdateTicketHistoryInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this UpdateTicketHistoryInfo.

        扩展字段

        :param title: The title of this UpdateTicketHistoryInfo.
        :type title: str
        """
        self._title = title

    @property
    def is_change_event(self):
        r"""Gets the is_change_event of this UpdateTicketHistoryInfo.

        是否变更事件

        :return: The is_change_event of this UpdateTicketHistoryInfo.
        :rtype: bool
        """
        return self._is_change_event

    @is_change_event.setter
    def is_change_event(self, is_change_event):
        r"""Sets the is_change_event of this UpdateTicketHistoryInfo.

        是否变更事件

        :param is_change_event: The is_change_event of this UpdateTicketHistoryInfo.
        :type is_change_event: bool
        """
        self._is_change_event = is_change_event

    @property
    def is_service_interrupt(self):
        r"""Gets the is_service_interrupt of this UpdateTicketHistoryInfo.

        是否变更事件

        :return: The is_service_interrupt of this UpdateTicketHistoryInfo.
        :rtype: bool
        """
        return self._is_service_interrupt

    @is_service_interrupt.setter
    def is_service_interrupt(self, is_service_interrupt):
        r"""Sets the is_service_interrupt of this UpdateTicketHistoryInfo.

        是否变更事件

        :param is_service_interrupt: The is_service_interrupt of this UpdateTicketHistoryInfo.
        :type is_service_interrupt: bool
        """
        self._is_service_interrupt = is_service_interrupt

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
        if not isinstance(other, UpdateTicketHistoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
