# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEventSourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'label': 'str',
        'description': 'str',
        'provider_type': 'str',
        'event_types': 'list[CustomizeSourceInfoEventTypes]',
        'created_time': 'str',
        'updated_time': 'str',
        'channel_id': 'str',
        'channel_name': 'str',
        'type': 'str',
        'detail': 'object',
        'status': 'str',
        'error_info': 'ErrorInfo',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'label': 'label',
        'description': 'description',
        'provider_type': 'provider_type',
        'event_types': 'event_types',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'channel_id': 'channel_id',
        'channel_name': 'channel_name',
        'type': 'type',
        'detail': 'detail',
        'status': 'status',
        'error_info': 'error_info',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, id=None, name=None, label=None, description=None, provider_type=None, event_types=None, created_time=None, updated_time=None, channel_id=None, channel_name=None, type=None, detail=None, status=None, error_info=None, x_request_id=None):
        r"""UpdateEventSourceResponse

        The model defined in huaweicloud sdk

        :param id: 事件源ID
        :type id: str
        :param name: 事件源名称
        :type name: str
        :param label: 事件源名称展示
        :type label: str
        :param description: 事件源描述
        :type description: str
        :param provider_type: 事件源提供方类型，OFFICIAL：官方云服务事件源；CUSTOM：用户创建的自定义事件源；PARTNER：伙伴事件源
        :type provider_type: str
        :param event_types: 事件源提供的事件类型列表，只有官方云服务事件源提供事件类型
        :type event_types: list[:class:`huaweicloudsdkeg.v1.CustomizeSourceInfoEventTypes`]
        :param created_time: 创建UTC时间
        :type created_time: str
        :param updated_time: 更新UTC时间
        :type updated_time: str
        :param channel_id: 事件源归属的事件通道ID
        :type channel_id: str
        :param channel_name: 事件源归属的事件通道名称
        :type channel_name: str
        :param type: 事件源类型
        :type type: str
        :param detail: json格式封装消息实例链接信息：如RabbitMQ实例的instance_id字段、虚拟主机vhost字段、队列queue字段、用户名、密码等
        :type detail: object
        :param status: 自定义事件源状态
        :type status: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkeg.v1.ErrorInfo`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateEventSourceResponse, self).__init__()

        self._id = None
        self._name = None
        self._label = None
        self._description = None
        self._provider_type = None
        self._event_types = None
        self._created_time = None
        self._updated_time = None
        self._channel_id = None
        self._channel_name = None
        self._type = None
        self._detail = None
        self._status = None
        self._error_info = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if description is not None:
            self.description = description
        if provider_type is not None:
            self.provider_type = provider_type
        if event_types is not None:
            self.event_types = event_types
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if channel_id is not None:
            self.channel_id = channel_id
        if channel_name is not None:
            self.channel_name = channel_name
        if type is not None:
            self.type = type
        if detail is not None:
            self.detail = detail
        if status is not None:
            self.status = status
        if error_info is not None:
            self.error_info = error_info
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this UpdateEventSourceResponse.

        事件源ID

        :return: The id of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateEventSourceResponse.

        事件源ID

        :param id: The id of this UpdateEventSourceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateEventSourceResponse.

        事件源名称

        :return: The name of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateEventSourceResponse.

        事件源名称

        :param name: The name of this UpdateEventSourceResponse.
        :type name: str
        """
        self._name = name

    @property
    def label(self):
        r"""Gets the label of this UpdateEventSourceResponse.

        事件源名称展示

        :return: The label of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this UpdateEventSourceResponse.

        事件源名称展示

        :param label: The label of this UpdateEventSourceResponse.
        :type label: str
        """
        self._label = label

    @property
    def description(self):
        r"""Gets the description of this UpdateEventSourceResponse.

        事件源描述

        :return: The description of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateEventSourceResponse.

        事件源描述

        :param description: The description of this UpdateEventSourceResponse.
        :type description: str
        """
        self._description = description

    @property
    def provider_type(self):
        r"""Gets the provider_type of this UpdateEventSourceResponse.

        事件源提供方类型，OFFICIAL：官方云服务事件源；CUSTOM：用户创建的自定义事件源；PARTNER：伙伴事件源

        :return: The provider_type of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this UpdateEventSourceResponse.

        事件源提供方类型，OFFICIAL：官方云服务事件源；CUSTOM：用户创建的自定义事件源；PARTNER：伙伴事件源

        :param provider_type: The provider_type of this UpdateEventSourceResponse.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def event_types(self):
        r"""Gets the event_types of this UpdateEventSourceResponse.

        事件源提供的事件类型列表，只有官方云服务事件源提供事件类型

        :return: The event_types of this UpdateEventSourceResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.CustomizeSourceInfoEventTypes`]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        r"""Sets the event_types of this UpdateEventSourceResponse.

        事件源提供的事件类型列表，只有官方云服务事件源提供事件类型

        :param event_types: The event_types of this UpdateEventSourceResponse.
        :type event_types: list[:class:`huaweicloudsdkeg.v1.CustomizeSourceInfoEventTypes`]
        """
        self._event_types = event_types

    @property
    def created_time(self):
        r"""Gets the created_time of this UpdateEventSourceResponse.

        创建UTC时间

        :return: The created_time of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this UpdateEventSourceResponse.

        创建UTC时间

        :param created_time: The created_time of this UpdateEventSourceResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this UpdateEventSourceResponse.

        更新UTC时间

        :return: The updated_time of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this UpdateEventSourceResponse.

        更新UTC时间

        :param updated_time: The updated_time of this UpdateEventSourceResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def channel_id(self):
        r"""Gets the channel_id of this UpdateEventSourceResponse.

        事件源归属的事件通道ID

        :return: The channel_id of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this UpdateEventSourceResponse.

        事件源归属的事件通道ID

        :param channel_id: The channel_id of this UpdateEventSourceResponse.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def channel_name(self):
        r"""Gets the channel_name of this UpdateEventSourceResponse.

        事件源归属的事件通道名称

        :return: The channel_name of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        r"""Sets the channel_name of this UpdateEventSourceResponse.

        事件源归属的事件通道名称

        :param channel_name: The channel_name of this UpdateEventSourceResponse.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def type(self):
        r"""Gets the type of this UpdateEventSourceResponse.

        事件源类型

        :return: The type of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateEventSourceResponse.

        事件源类型

        :param type: The type of this UpdateEventSourceResponse.
        :type type: str
        """
        self._type = type

    @property
    def detail(self):
        r"""Gets the detail of this UpdateEventSourceResponse.

        json格式封装消息实例链接信息：如RabbitMQ实例的instance_id字段、虚拟主机vhost字段、队列queue字段、用户名、密码等

        :return: The detail of this UpdateEventSourceResponse.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this UpdateEventSourceResponse.

        json格式封装消息实例链接信息：如RabbitMQ实例的instance_id字段、虚拟主机vhost字段、队列queue字段、用户名、密码等

        :param detail: The detail of this UpdateEventSourceResponse.
        :type detail: object
        """
        self._detail = detail

    @property
    def status(self):
        r"""Gets the status of this UpdateEventSourceResponse.

        自定义事件源状态

        :return: The status of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateEventSourceResponse.

        自定义事件源状态

        :param status: The status of this UpdateEventSourceResponse.
        :type status: str
        """
        self._status = status

    @property
    def error_info(self):
        r"""Gets the error_info of this UpdateEventSourceResponse.

        :return: The error_info of this UpdateEventSourceResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.ErrorInfo`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this UpdateEventSourceResponse.

        :param error_info: The error_info of this UpdateEventSourceResponse.
        :type error_info: :class:`huaweicloudsdkeg.v1.ErrorInfo`
        """
        self._error_info = error_info

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateEventSourceResponse.

        :return: The x_request_id of this UpdateEventSourceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateEventSourceResponse.

        :param x_request_id: The x_request_id of this UpdateEventSourceResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, UpdateEventSourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
