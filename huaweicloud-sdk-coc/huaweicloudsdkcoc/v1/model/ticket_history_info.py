# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicketHistoryInfo:

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
        'comment': 'str',
        'id': 'str',
        'ticket_id': 'str',
        'start_time': 'int',
        'stop_time': 'int',
        'target_type': 'str',
        'target_value': 'str',
        'is_deteted': 'bool',
        'update_time': 'int',
        'action_name_zh': 'str',
        'action_name_en': 'str',
        'action_template_zh': 'str',
        'action_template_en': 'str',
        'status': 'str',
        'final_sub_action': 'str',
        'enum_data_list': 'list[EnumDataInfo]'
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
        'comment': 'comment',
        'id': 'id',
        'ticket_id': 'ticket_id',
        'start_time': 'start_time',
        'stop_time': 'stop_time',
        'target_type': 'target_type',
        'target_value': 'target_value',
        'is_deteted': 'is_deteted',
        'update_time': 'update_time',
        'action_name_zh': 'action_name_zh',
        'action_name_en': 'action_name_en',
        'action_template_zh': 'action_template_zh',
        'action_template_en': 'action_template_en',
        'status': 'status',
        'final_sub_action': 'final_sub_action',
        'enum_data_list': 'enum_data_list'
    }

    def __init__(self, current_cloud_service_id=None, description=None, level_id=None, mtm_region=None, mtm_type=None, source_id=None, title=None, is_change_event=None, is_service_interrupt=None, action_id=None, action=None, sub_action=None, operator=None, comment=None, id=None, ticket_id=None, start_time=None, stop_time=None, target_type=None, target_value=None, is_deteted=None, update_time=None, action_name_zh=None, action_name_en=None, action_template_zh=None, action_template_en=None, status=None, final_sub_action=None, enum_data_list=None):
        r"""TicketHistoryInfo

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
        :param id: 主键
        :type id: str
        :param ticket_id: 单号
        :type ticket_id: str
        :param start_time: 起始时间
        :type start_time: int
        :param stop_time: 结束时间
        :type stop_time: int
        :param target_type: 对象类型
        :type target_type: str
        :param target_value: 对象值
        :type target_value: str
        :param is_deteted: 待修改
        :type is_deteted: bool
        :param update_time: 更新时间
        :type update_time: int
        :param action_name_zh: action中文名
        :type action_name_zh: str
        :param action_name_en: action英文名
        :type action_name_en: str
        :param action_template_zh: action中文模板
        :type action_template_zh: str
        :param action_template_en: action中文模板
        :type action_template_en: str
        :param status: 工单状态
        :type status: str
        :param final_sub_action: 最终子动作
        :type final_sub_action: str
        :param enum_data_list: 枚举数据
        :type enum_data_list: list[:class:`huaweicloudsdkcoc.v1.EnumDataInfo`]
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
        self._id = None
        self._ticket_id = None
        self._start_time = None
        self._stop_time = None
        self._target_type = None
        self._target_value = None
        self._is_deteted = None
        self._update_time = None
        self._action_name_zh = None
        self._action_name_en = None
        self._action_template_zh = None
        self._action_template_en = None
        self._status = None
        self._final_sub_action = None
        self._enum_data_list = None
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
        if id is not None:
            self.id = id
        if ticket_id is not None:
            self.ticket_id = ticket_id
        if start_time is not None:
            self.start_time = start_time
        if stop_time is not None:
            self.stop_time = stop_time
        if target_type is not None:
            self.target_type = target_type
        if target_value is not None:
            self.target_value = target_value
        if is_deteted is not None:
            self.is_deteted = is_deteted
        if update_time is not None:
            self.update_time = update_time
        if action_name_zh is not None:
            self.action_name_zh = action_name_zh
        if action_name_en is not None:
            self.action_name_en = action_name_en
        if action_template_zh is not None:
            self.action_template_zh = action_template_zh
        if action_template_en is not None:
            self.action_template_en = action_template_en
        if status is not None:
            self.status = status
        if final_sub_action is not None:
            self.final_sub_action = final_sub_action
        if enum_data_list is not None:
            self.enum_data_list = enum_data_list

    @property
    def current_cloud_service_id(self):
        r"""Gets the current_cloud_service_id of this TicketHistoryInfo.

        扩展字段

        :return: The current_cloud_service_id of this TicketHistoryInfo.
        :rtype: str
        """
        return self._current_cloud_service_id

    @current_cloud_service_id.setter
    def current_cloud_service_id(self, current_cloud_service_id):
        r"""Sets the current_cloud_service_id of this TicketHistoryInfo.

        扩展字段

        :param current_cloud_service_id: The current_cloud_service_id of this TicketHistoryInfo.
        :type current_cloud_service_id: str
        """
        self._current_cloud_service_id = current_cloud_service_id

    @property
    def description(self):
        r"""Gets the description of this TicketHistoryInfo.

        扩展字段

        :return: The description of this TicketHistoryInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TicketHistoryInfo.

        扩展字段

        :param description: The description of this TicketHistoryInfo.
        :type description: str
        """
        self._description = description

    @property
    def level_id(self):
        r"""Gets the level_id of this TicketHistoryInfo.

        扩展字段

        :return: The level_id of this TicketHistoryInfo.
        :rtype: str
        """
        return self._level_id

    @level_id.setter
    def level_id(self, level_id):
        r"""Sets the level_id of this TicketHistoryInfo.

        扩展字段

        :param level_id: The level_id of this TicketHistoryInfo.
        :type level_id: str
        """
        self._level_id = level_id

    @property
    def mtm_region(self):
        r"""Gets the mtm_region of this TicketHistoryInfo.

        扩展字段

        :return: The mtm_region of this TicketHistoryInfo.
        :rtype: str
        """
        return self._mtm_region

    @mtm_region.setter
    def mtm_region(self, mtm_region):
        r"""Sets the mtm_region of this TicketHistoryInfo.

        扩展字段

        :param mtm_region: The mtm_region of this TicketHistoryInfo.
        :type mtm_region: str
        """
        self._mtm_region = mtm_region

    @property
    def mtm_type(self):
        r"""Gets the mtm_type of this TicketHistoryInfo.

        扩展字段

        :return: The mtm_type of this TicketHistoryInfo.
        :rtype: str
        """
        return self._mtm_type

    @mtm_type.setter
    def mtm_type(self, mtm_type):
        r"""Sets the mtm_type of this TicketHistoryInfo.

        扩展字段

        :param mtm_type: The mtm_type of this TicketHistoryInfo.
        :type mtm_type: str
        """
        self._mtm_type = mtm_type

    @property
    def source_id(self):
        r"""Gets the source_id of this TicketHistoryInfo.

        扩展字段

        :return: The source_id of this TicketHistoryInfo.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this TicketHistoryInfo.

        扩展字段

        :param source_id: The source_id of this TicketHistoryInfo.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def title(self):
        r"""Gets the title of this TicketHistoryInfo.

        扩展字段

        :return: The title of this TicketHistoryInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this TicketHistoryInfo.

        扩展字段

        :param title: The title of this TicketHistoryInfo.
        :type title: str
        """
        self._title = title

    @property
    def is_change_event(self):
        r"""Gets the is_change_event of this TicketHistoryInfo.

        是否变更事件

        :return: The is_change_event of this TicketHistoryInfo.
        :rtype: bool
        """
        return self._is_change_event

    @is_change_event.setter
    def is_change_event(self, is_change_event):
        r"""Sets the is_change_event of this TicketHistoryInfo.

        是否变更事件

        :param is_change_event: The is_change_event of this TicketHistoryInfo.
        :type is_change_event: bool
        """
        self._is_change_event = is_change_event

    @property
    def is_service_interrupt(self):
        r"""Gets the is_service_interrupt of this TicketHistoryInfo.

        是否变更事件

        :return: The is_service_interrupt of this TicketHistoryInfo.
        :rtype: bool
        """
        return self._is_service_interrupt

    @is_service_interrupt.setter
    def is_service_interrupt(self, is_service_interrupt):
        r"""Sets the is_service_interrupt of this TicketHistoryInfo.

        是否变更事件

        :param is_service_interrupt: The is_service_interrupt of this TicketHistoryInfo.
        :type is_service_interrupt: bool
        """
        self._is_service_interrupt = is_service_interrupt

    @property
    def action_id(self):
        r"""Gets the action_id of this TicketHistoryInfo.

        操作标识

        :return: The action_id of this TicketHistoryInfo.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this TicketHistoryInfo.

        操作标识

        :param action_id: The action_id of this TicketHistoryInfo.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def action(self):
        r"""Gets the action of this TicketHistoryInfo.

        动作

        :return: The action of this TicketHistoryInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this TicketHistoryInfo.

        动作

        :param action: The action of this TicketHistoryInfo.
        :type action: str
        """
        self._action = action

    @property
    def sub_action(self):
        r"""Gets the sub_action of this TicketHistoryInfo.

        子动作

        :return: The sub_action of this TicketHistoryInfo.
        :rtype: str
        """
        return self._sub_action

    @sub_action.setter
    def sub_action(self, sub_action):
        r"""Sets the sub_action of this TicketHistoryInfo.

        子动作

        :param sub_action: The sub_action of this TicketHistoryInfo.
        :type sub_action: str
        """
        self._sub_action = sub_action

    @property
    def operator(self):
        r"""Gets the operator of this TicketHistoryInfo.

        操作人

        :return: The operator of this TicketHistoryInfo.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this TicketHistoryInfo.

        操作人

        :param operator: The operator of this TicketHistoryInfo.
        :type operator: str
        """
        self._operator = operator

    @property
    def comment(self):
        r"""Gets the comment of this TicketHistoryInfo.

        评论

        :return: The comment of this TicketHistoryInfo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this TicketHistoryInfo.

        评论

        :param comment: The comment of this TicketHistoryInfo.
        :type comment: str
        """
        self._comment = comment

    @property
    def id(self):
        r"""Gets the id of this TicketHistoryInfo.

        主键

        :return: The id of this TicketHistoryInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TicketHistoryInfo.

        主键

        :param id: The id of this TicketHistoryInfo.
        :type id: str
        """
        self._id = id

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this TicketHistoryInfo.

        单号

        :return: The ticket_id of this TicketHistoryInfo.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this TicketHistoryInfo.

        单号

        :param ticket_id: The ticket_id of this TicketHistoryInfo.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def start_time(self):
        r"""Gets the start_time of this TicketHistoryInfo.

        起始时间

        :return: The start_time of this TicketHistoryInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TicketHistoryInfo.

        起始时间

        :param start_time: The start_time of this TicketHistoryInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def stop_time(self):
        r"""Gets the stop_time of this TicketHistoryInfo.

        结束时间

        :return: The stop_time of this TicketHistoryInfo.
        :rtype: int
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        r"""Sets the stop_time of this TicketHistoryInfo.

        结束时间

        :param stop_time: The stop_time of this TicketHistoryInfo.
        :type stop_time: int
        """
        self._stop_time = stop_time

    @property
    def target_type(self):
        r"""Gets the target_type of this TicketHistoryInfo.

        对象类型

        :return: The target_type of this TicketHistoryInfo.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this TicketHistoryInfo.

        对象类型

        :param target_type: The target_type of this TicketHistoryInfo.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def target_value(self):
        r"""Gets the target_value of this TicketHistoryInfo.

        对象值

        :return: The target_value of this TicketHistoryInfo.
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        r"""Sets the target_value of this TicketHistoryInfo.

        对象值

        :param target_value: The target_value of this TicketHistoryInfo.
        :type target_value: str
        """
        self._target_value = target_value

    @property
    def is_deteted(self):
        r"""Gets the is_deteted of this TicketHistoryInfo.

        待修改

        :return: The is_deteted of this TicketHistoryInfo.
        :rtype: bool
        """
        return self._is_deteted

    @is_deteted.setter
    def is_deteted(self, is_deteted):
        r"""Sets the is_deteted of this TicketHistoryInfo.

        待修改

        :param is_deteted: The is_deteted of this TicketHistoryInfo.
        :type is_deteted: bool
        """
        self._is_deteted = is_deteted

    @property
    def update_time(self):
        r"""Gets the update_time of this TicketHistoryInfo.

        更新时间

        :return: The update_time of this TicketHistoryInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TicketHistoryInfo.

        更新时间

        :param update_time: The update_time of this TicketHistoryInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def action_name_zh(self):
        r"""Gets the action_name_zh of this TicketHistoryInfo.

        action中文名

        :return: The action_name_zh of this TicketHistoryInfo.
        :rtype: str
        """
        return self._action_name_zh

    @action_name_zh.setter
    def action_name_zh(self, action_name_zh):
        r"""Sets the action_name_zh of this TicketHistoryInfo.

        action中文名

        :param action_name_zh: The action_name_zh of this TicketHistoryInfo.
        :type action_name_zh: str
        """
        self._action_name_zh = action_name_zh

    @property
    def action_name_en(self):
        r"""Gets the action_name_en of this TicketHistoryInfo.

        action英文名

        :return: The action_name_en of this TicketHistoryInfo.
        :rtype: str
        """
        return self._action_name_en

    @action_name_en.setter
    def action_name_en(self, action_name_en):
        r"""Sets the action_name_en of this TicketHistoryInfo.

        action英文名

        :param action_name_en: The action_name_en of this TicketHistoryInfo.
        :type action_name_en: str
        """
        self._action_name_en = action_name_en

    @property
    def action_template_zh(self):
        r"""Gets the action_template_zh of this TicketHistoryInfo.

        action中文模板

        :return: The action_template_zh of this TicketHistoryInfo.
        :rtype: str
        """
        return self._action_template_zh

    @action_template_zh.setter
    def action_template_zh(self, action_template_zh):
        r"""Sets the action_template_zh of this TicketHistoryInfo.

        action中文模板

        :param action_template_zh: The action_template_zh of this TicketHistoryInfo.
        :type action_template_zh: str
        """
        self._action_template_zh = action_template_zh

    @property
    def action_template_en(self):
        r"""Gets the action_template_en of this TicketHistoryInfo.

        action中文模板

        :return: The action_template_en of this TicketHistoryInfo.
        :rtype: str
        """
        return self._action_template_en

    @action_template_en.setter
    def action_template_en(self, action_template_en):
        r"""Sets the action_template_en of this TicketHistoryInfo.

        action中文模板

        :param action_template_en: The action_template_en of this TicketHistoryInfo.
        :type action_template_en: str
        """
        self._action_template_en = action_template_en

    @property
    def status(self):
        r"""Gets the status of this TicketHistoryInfo.

        工单状态

        :return: The status of this TicketHistoryInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TicketHistoryInfo.

        工单状态

        :param status: The status of this TicketHistoryInfo.
        :type status: str
        """
        self._status = status

    @property
    def final_sub_action(self):
        r"""Gets the final_sub_action of this TicketHistoryInfo.

        最终子动作

        :return: The final_sub_action of this TicketHistoryInfo.
        :rtype: str
        """
        return self._final_sub_action

    @final_sub_action.setter
    def final_sub_action(self, final_sub_action):
        r"""Sets the final_sub_action of this TicketHistoryInfo.

        最终子动作

        :param final_sub_action: The final_sub_action of this TicketHistoryInfo.
        :type final_sub_action: str
        """
        self._final_sub_action = final_sub_action

    @property
    def enum_data_list(self):
        r"""Gets the enum_data_list of this TicketHistoryInfo.

        枚举数据

        :return: The enum_data_list of this TicketHistoryInfo.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.EnumDataInfo`]
        """
        return self._enum_data_list

    @enum_data_list.setter
    def enum_data_list(self, enum_data_list):
        r"""Sets the enum_data_list of this TicketHistoryInfo.

        枚举数据

        :param enum_data_list: The enum_data_list of this TicketHistoryInfo.
        :type enum_data_list: list[:class:`huaweicloudsdkcoc.v1.EnumDataInfo`]
        """
        self._enum_data_list = enum_data_list

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
        if not isinstance(other, TicketHistoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
