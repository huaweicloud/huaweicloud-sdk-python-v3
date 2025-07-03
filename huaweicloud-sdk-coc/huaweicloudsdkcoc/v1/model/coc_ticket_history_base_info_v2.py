# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocTicketHistoryBaseInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'action_name_zh': 'str',
        'action_name_en': 'str',
        'operator': 'str',
        'status': 'str',
        'start_time': 'str',
        'stop_time': 'str',
        'comment': 'str',
        'enum_data_list': 'list[CocTicketEnumDataV2]'
    }

    attribute_map = {
        'action': 'action',
        'action_name_zh': 'action_name_zh',
        'action_name_en': 'action_name_en',
        'operator': 'operator',
        'status': 'status',
        'start_time': 'start_time',
        'stop_time': 'stop_time',
        'comment': 'comment',
        'enum_data_list': 'enum_data_list'
    }

    def __init__(self, action=None, action_name_zh=None, action_name_en=None, operator=None, status=None, start_time=None, stop_time=None, comment=None, enum_data_list=None):
        r"""CocTicketHistoryBaseInfoV2

        The model defined in huaweicloud sdk

        :param action: action
        :type action: str
        :param action_name_zh: action中文名称
        :type action_name_zh: str
        :param action_name_en: action英文名称
        :type action_name_en: str
        :param operator: 操作人ID
        :type operator: str
        :param status: 当前状态
        :type status: str
        :param start_time: 操作开始时间
        :type start_time: str
        :param stop_time: 操作结束时间
        :type stop_time: str
        :param comment: 备注信息
        :type comment: str
        :param enum_data_list: 枚举数据列表
        :type enum_data_list: list[:class:`huaweicloudsdkcoc.v1.CocTicketEnumDataV2`]
        """
        
        

        self._action = None
        self._action_name_zh = None
        self._action_name_en = None
        self._operator = None
        self._status = None
        self._start_time = None
        self._stop_time = None
        self._comment = None
        self._enum_data_list = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if action_name_zh is not None:
            self.action_name_zh = action_name_zh
        if action_name_en is not None:
            self.action_name_en = action_name_en
        if operator is not None:
            self.operator = operator
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if stop_time is not None:
            self.stop_time = stop_time
        if comment is not None:
            self.comment = comment
        if enum_data_list is not None:
            self.enum_data_list = enum_data_list

    @property
    def action(self):
        r"""Gets the action of this CocTicketHistoryBaseInfoV2.

        action

        :return: The action of this CocTicketHistoryBaseInfoV2.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CocTicketHistoryBaseInfoV2.

        action

        :param action: The action of this CocTicketHistoryBaseInfoV2.
        :type action: str
        """
        self._action = action

    @property
    def action_name_zh(self):
        r"""Gets the action_name_zh of this CocTicketHistoryBaseInfoV2.

        action中文名称

        :return: The action_name_zh of this CocTicketHistoryBaseInfoV2.
        :rtype: str
        """
        return self._action_name_zh

    @action_name_zh.setter
    def action_name_zh(self, action_name_zh):
        r"""Sets the action_name_zh of this CocTicketHistoryBaseInfoV2.

        action中文名称

        :param action_name_zh: The action_name_zh of this CocTicketHistoryBaseInfoV2.
        :type action_name_zh: str
        """
        self._action_name_zh = action_name_zh

    @property
    def action_name_en(self):
        r"""Gets the action_name_en of this CocTicketHistoryBaseInfoV2.

        action英文名称

        :return: The action_name_en of this CocTicketHistoryBaseInfoV2.
        :rtype: str
        """
        return self._action_name_en

    @action_name_en.setter
    def action_name_en(self, action_name_en):
        r"""Sets the action_name_en of this CocTicketHistoryBaseInfoV2.

        action英文名称

        :param action_name_en: The action_name_en of this CocTicketHistoryBaseInfoV2.
        :type action_name_en: str
        """
        self._action_name_en = action_name_en

    @property
    def operator(self):
        r"""Gets the operator of this CocTicketHistoryBaseInfoV2.

        操作人ID

        :return: The operator of this CocTicketHistoryBaseInfoV2.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this CocTicketHistoryBaseInfoV2.

        操作人ID

        :param operator: The operator of this CocTicketHistoryBaseInfoV2.
        :type operator: str
        """
        self._operator = operator

    @property
    def status(self):
        r"""Gets the status of this CocTicketHistoryBaseInfoV2.

        当前状态

        :return: The status of this CocTicketHistoryBaseInfoV2.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CocTicketHistoryBaseInfoV2.

        当前状态

        :param status: The status of this CocTicketHistoryBaseInfoV2.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this CocTicketHistoryBaseInfoV2.

        操作开始时间

        :return: The start_time of this CocTicketHistoryBaseInfoV2.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CocTicketHistoryBaseInfoV2.

        操作开始时间

        :param start_time: The start_time of this CocTicketHistoryBaseInfoV2.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def stop_time(self):
        r"""Gets the stop_time of this CocTicketHistoryBaseInfoV2.

        操作结束时间

        :return: The stop_time of this CocTicketHistoryBaseInfoV2.
        :rtype: str
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        r"""Sets the stop_time of this CocTicketHistoryBaseInfoV2.

        操作结束时间

        :param stop_time: The stop_time of this CocTicketHistoryBaseInfoV2.
        :type stop_time: str
        """
        self._stop_time = stop_time

    @property
    def comment(self):
        r"""Gets the comment of this CocTicketHistoryBaseInfoV2.

        备注信息

        :return: The comment of this CocTicketHistoryBaseInfoV2.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this CocTicketHistoryBaseInfoV2.

        备注信息

        :param comment: The comment of this CocTicketHistoryBaseInfoV2.
        :type comment: str
        """
        self._comment = comment

    @property
    def enum_data_list(self):
        r"""Gets the enum_data_list of this CocTicketHistoryBaseInfoV2.

        枚举数据列表

        :return: The enum_data_list of this CocTicketHistoryBaseInfoV2.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CocTicketEnumDataV2`]
        """
        return self._enum_data_list

    @enum_data_list.setter
    def enum_data_list(self, enum_data_list):
        r"""Sets the enum_data_list of this CocTicketHistoryBaseInfoV2.

        枚举数据列表

        :param enum_data_list: The enum_data_list of this CocTicketHistoryBaseInfoV2.
        :type enum_data_list: list[:class:`huaweicloudsdkcoc.v1.CocTicketEnumDataV2`]
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
        if not isinstance(other, CocTicketHistoryBaseInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
