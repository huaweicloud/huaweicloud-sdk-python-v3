# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'description': 'str',
        'event_id': 'str',
        'name': 'str',
        'display_name': 'str',
        'name_space': 'str',
        'severity': 'str',
        'source_type': 'str',
        'occur_time': 'int',
        'project_id': 'str',
        'source_id': 'str',
        'source_name': 'str',
        'status': 'int',
        'subject': 'str',
        'context': 'str'
    }

    attribute_map = {
        'category': 'category',
        'description': 'description',
        'event_id': 'event_id',
        'name': 'name',
        'display_name': 'display_name',
        'name_space': 'name_space',
        'severity': 'severity',
        'source_type': 'source_type',
        'occur_time': 'occur_time',
        'project_id': 'project_id',
        'source_id': 'source_id',
        'source_name': 'source_name',
        'status': 'status',
        'subject': 'subject',
        'context': 'context'
    }

    def __init__(self, category=None, description=None, event_id=None, name=None, display_name=None, name_space=None, severity=None, source_type=None, occur_time=None, project_id=None, source_id=None, source_name=None, status=None, subject=None, context=None):
        """EventResponse

        The model defined in huaweicloud sdk

        :param category: 事件类别
        :type category: str
        :param description: 事件描述
        :type description: str
        :param event_id: 事件ID
        :type event_id: str
        :param name: 事件定义名称
        :type name: str
        :param display_name: 事件显示名称
        :type display_name: str
        :param name_space: 所属服务
        :type name_space: str
        :param severity: 事件级别
        :type severity: str
        :param source_type: 事件源类别
        :type source_type: str
        :param occur_time: 时间
        :type occur_time: int
        :param project_id: 租户凭证ID
        :type project_id: str
        :param source_id: 事件源ID
        :type source_id: str
        :param source_name: 事件源名称
        :type source_name: str
        :param status: 状态
        :type status: int
        :param subject: 事件主题
        :type subject: str
        :param context: 事件信息
        :type context: str
        """
        
        

        self._category = None
        self._description = None
        self._event_id = None
        self._name = None
        self._display_name = None
        self._name_space = None
        self._severity = None
        self._source_type = None
        self._occur_time = None
        self._project_id = None
        self._source_id = None
        self._source_name = None
        self._status = None
        self._subject = None
        self._context = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if event_id is not None:
            self.event_id = event_id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if name_space is not None:
            self.name_space = name_space
        if severity is not None:
            self.severity = severity
        if source_type is not None:
            self.source_type = source_type
        if occur_time is not None:
            self.occur_time = occur_time
        if project_id is not None:
            self.project_id = project_id
        if source_id is not None:
            self.source_id = source_id
        if source_name is not None:
            self.source_name = source_name
        if status is not None:
            self.status = status
        if subject is not None:
            self.subject = subject
        if context is not None:
            self.context = context

    @property
    def category(self):
        """Gets the category of this EventResponse.

        事件类别

        :return: The category of this EventResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this EventResponse.

        事件类别

        :param category: The category of this EventResponse.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        """Gets the description of this EventResponse.

        事件描述

        :return: The description of this EventResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventResponse.

        事件描述

        :param description: The description of this EventResponse.
        :type description: str
        """
        self._description = description

    @property
    def event_id(self):
        """Gets the event_id of this EventResponse.

        事件ID

        :return: The event_id of this EventResponse.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this EventResponse.

        事件ID

        :param event_id: The event_id of this EventResponse.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def name(self):
        """Gets the name of this EventResponse.

        事件定义名称

        :return: The name of this EventResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventResponse.

        事件定义名称

        :param name: The name of this EventResponse.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this EventResponse.

        事件显示名称

        :return: The display_name of this EventResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this EventResponse.

        事件显示名称

        :param display_name: The display_name of this EventResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def name_space(self):
        """Gets the name_space of this EventResponse.

        所属服务

        :return: The name_space of this EventResponse.
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        """Sets the name_space of this EventResponse.

        所属服务

        :param name_space: The name_space of this EventResponse.
        :type name_space: str
        """
        self._name_space = name_space

    @property
    def severity(self):
        """Gets the severity of this EventResponse.

        事件级别

        :return: The severity of this EventResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this EventResponse.

        事件级别

        :param severity: The severity of this EventResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def source_type(self):
        """Gets the source_type of this EventResponse.

        事件源类别

        :return: The source_type of this EventResponse.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this EventResponse.

        事件源类别

        :param source_type: The source_type of this EventResponse.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def occur_time(self):
        """Gets the occur_time of this EventResponse.

        时间

        :return: The occur_time of this EventResponse.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        """Sets the occur_time of this EventResponse.

        时间

        :param occur_time: The occur_time of this EventResponse.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def project_id(self):
        """Gets the project_id of this EventResponse.

        租户凭证ID

        :return: The project_id of this EventResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this EventResponse.

        租户凭证ID

        :param project_id: The project_id of this EventResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def source_id(self):
        """Gets the source_id of this EventResponse.

        事件源ID

        :return: The source_id of this EventResponse.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this EventResponse.

        事件源ID

        :param source_id: The source_id of this EventResponse.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def source_name(self):
        """Gets the source_name of this EventResponse.

        事件源名称

        :return: The source_name of this EventResponse.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this EventResponse.

        事件源名称

        :param source_name: The source_name of this EventResponse.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def status(self):
        """Gets the status of this EventResponse.

        状态

        :return: The status of this EventResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EventResponse.

        状态

        :param status: The status of this EventResponse.
        :type status: int
        """
        self._status = status

    @property
    def subject(self):
        """Gets the subject of this EventResponse.

        事件主题

        :return: The subject of this EventResponse.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EventResponse.

        事件主题

        :param subject: The subject of this EventResponse.
        :type subject: str
        """
        self._subject = subject

    @property
    def context(self):
        """Gets the context of this EventResponse.

        事件信息

        :return: The context of this EventResponse.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this EventResponse.

        事件信息

        :param context: The context of this EventResponse.
        :type context: str
        """
        self._context = context

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
        if not isinstance(other, EventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
