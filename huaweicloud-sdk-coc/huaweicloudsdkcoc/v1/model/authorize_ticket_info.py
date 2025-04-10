# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizeTicketInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_id': 'str',
        'target_id': 'str',
        'scope_id': 'str',
        'title': 'str',
        'ticket_type': 'str',
        'owner': 'list[str]',
        'level': 'str',
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'ticket_id': 'ticket_id',
        'target_id': 'target_id',
        'scope_id': 'scope_id',
        'title': 'title',
        'ticket_type': 'ticket_type',
        'owner': 'owner',
        'level': 'level',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, ticket_id=None, target_id=None, scope_id=None, title=None, ticket_type=None, owner=None, level=None, status=None, begin_time=None, end_time=None):
        r"""AuthorizeTicketInfo

        The model defined in huaweicloud sdk

        :param ticket_id: 关联单号
        :type ticket_id: str
        :param target_id: 目标 ID，一般为应用id
        :type target_id: str
        :param scope_id: scope ID，一般为region id
        :type scope_id: str
        :param title: 工单名称
        :type title: str
        :param ticket_type: 授权单类型，取值：CHANGE/INCIDENT/WAR_ROOM/ALARM
        :type ticket_type: str
        :param owner: 当前责任人
        :type owner: list[str]
        :param level: 级别
        :type level: str
        :param status: 状态，取值：open/close
        :type status: str
        :param begin_time: 起始时间
        :type begin_time: str
        :param end_time: 结束时间
        :type end_time: str
        """
        
        

        self._ticket_id = None
        self._target_id = None
        self._scope_id = None
        self._title = None
        self._ticket_type = None
        self._owner = None
        self._level = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if ticket_id is not None:
            self.ticket_id = ticket_id
        if target_id is not None:
            self.target_id = target_id
        if scope_id is not None:
            self.scope_id = scope_id
        if title is not None:
            self.title = title
        if ticket_type is not None:
            self.ticket_type = ticket_type
        if owner is not None:
            self.owner = owner
        if level is not None:
            self.level = level
        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this AuthorizeTicketInfo.

        关联单号

        :return: The ticket_id of this AuthorizeTicketInfo.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this AuthorizeTicketInfo.

        关联单号

        :param ticket_id: The ticket_id of this AuthorizeTicketInfo.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def target_id(self):
        r"""Gets the target_id of this AuthorizeTicketInfo.

        目标 ID，一般为应用id

        :return: The target_id of this AuthorizeTicketInfo.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this AuthorizeTicketInfo.

        目标 ID，一般为应用id

        :param target_id: The target_id of this AuthorizeTicketInfo.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def scope_id(self):
        r"""Gets the scope_id of this AuthorizeTicketInfo.

        scope ID，一般为region id

        :return: The scope_id of this AuthorizeTicketInfo.
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        r"""Sets the scope_id of this AuthorizeTicketInfo.

        scope ID，一般为region id

        :param scope_id: The scope_id of this AuthorizeTicketInfo.
        :type scope_id: str
        """
        self._scope_id = scope_id

    @property
    def title(self):
        r"""Gets the title of this AuthorizeTicketInfo.

        工单名称

        :return: The title of this AuthorizeTicketInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this AuthorizeTicketInfo.

        工单名称

        :param title: The title of this AuthorizeTicketInfo.
        :type title: str
        """
        self._title = title

    @property
    def ticket_type(self):
        r"""Gets the ticket_type of this AuthorizeTicketInfo.

        授权单类型，取值：CHANGE/INCIDENT/WAR_ROOM/ALARM

        :return: The ticket_type of this AuthorizeTicketInfo.
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        r"""Sets the ticket_type of this AuthorizeTicketInfo.

        授权单类型，取值：CHANGE/INCIDENT/WAR_ROOM/ALARM

        :param ticket_type: The ticket_type of this AuthorizeTicketInfo.
        :type ticket_type: str
        """
        self._ticket_type = ticket_type

    @property
    def owner(self):
        r"""Gets the owner of this AuthorizeTicketInfo.

        当前责任人

        :return: The owner of this AuthorizeTicketInfo.
        :rtype: list[str]
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this AuthorizeTicketInfo.

        当前责任人

        :param owner: The owner of this AuthorizeTicketInfo.
        :type owner: list[str]
        """
        self._owner = owner

    @property
    def level(self):
        r"""Gets the level of this AuthorizeTicketInfo.

        级别

        :return: The level of this AuthorizeTicketInfo.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this AuthorizeTicketInfo.

        级别

        :param level: The level of this AuthorizeTicketInfo.
        :type level: str
        """
        self._level = level

    @property
    def status(self):
        r"""Gets the status of this AuthorizeTicketInfo.

        状态，取值：open/close

        :return: The status of this AuthorizeTicketInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AuthorizeTicketInfo.

        状态，取值：open/close

        :param status: The status of this AuthorizeTicketInfo.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this AuthorizeTicketInfo.

        起始时间

        :return: The begin_time of this AuthorizeTicketInfo.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this AuthorizeTicketInfo.

        起始时间

        :param begin_time: The begin_time of this AuthorizeTicketInfo.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this AuthorizeTicketInfo.

        结束时间

        :return: The end_time of this AuthorizeTicketInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this AuthorizeTicketInfo.

        结束时间

        :param end_time: The end_time of this AuthorizeTicketInfo.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, AuthorizeTicketInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
