# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailOfEventSourceResponse(SdkResponse):

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
        'status': 'str'
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
        'status': 'status'
    }

    def __init__(self, id=None, name=None, label=None, description=None, provider_type=None, event_types=None, created_time=None, updated_time=None, channel_id=None, channel_name=None, type=None, detail=None, status=None):
        """ShowDetailOfEventSourceResponse

        The model defined in huaweicloud sdk

        :param id: 事件源ID
        :type id: str
        :param name: 事件源名称
        :type name: str
        :param label: 事件源名称展示
        :type label: str
        :param description: 事件源描述
        :type description: str
        :param provider_type: 事件源提供方类型，OFFICIAL：官方云服务事件源；CUSTOM：用户创建的自定义事件源
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
        """
        
        super(ShowDetailOfEventSourceResponse, self).__init__()

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

    @property
    def id(self):
        """Gets the id of this ShowDetailOfEventSourceResponse.

        事件源ID

        :return: The id of this ShowDetailOfEventSourceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDetailOfEventSourceResponse.

        事件源ID

        :param id: The id of this ShowDetailOfEventSourceResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowDetailOfEventSourceResponse.

        事件源名称

        :return: The name of this ShowDetailOfEventSourceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDetailOfEventSourceResponse.

        事件源名称

        :param name: The name of this ShowDetailOfEventSourceResponse.
        :type name: str
        """
        self._name = name

    @property
    def label(self):
        """Gets the label of this ShowDetailOfEventSourceResponse.

        事件源名称展示

        :return: The label of this ShowDetailOfEventSourceResponse.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ShowDetailOfEventSourceResponse.

        事件源名称展示

        :param label: The label of this ShowDetailOfEventSourceResponse.
        :type label: str
        """
        self._label = label

    @property
    def description(self):
        """Gets the description of this ShowDetailOfEventSourceResponse.

        事件源描述

        :return: The description of this ShowDetailOfEventSourceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowDetailOfEventSourceResponse.

        事件源描述

        :param description: The description of this ShowDetailOfEventSourceResponse.
        :type description: str
        """
        self._description = description

    @property
    def provider_type(self):
        """Gets the provider_type of this ShowDetailOfEventSourceResponse.

        事件源提供方类型，OFFICIAL：官方云服务事件源；CUSTOM：用户创建的自定义事件源

        :return: The provider_type of this ShowDetailOfEventSourceResponse.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this ShowDetailOfEventSourceResponse.

        事件源提供方类型，OFFICIAL：官方云服务事件源；CUSTOM：用户创建的自定义事件源

        :param provider_type: The provider_type of this ShowDetailOfEventSourceResponse.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def event_types(self):
        """Gets the event_types of this ShowDetailOfEventSourceResponse.

        事件源提供的事件类型列表，只有官方云服务事件源提供事件类型

        :return: The event_types of this ShowDetailOfEventSourceResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.CustomizeSourceInfoEventTypes`]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this ShowDetailOfEventSourceResponse.

        事件源提供的事件类型列表，只有官方云服务事件源提供事件类型

        :param event_types: The event_types of this ShowDetailOfEventSourceResponse.
        :type event_types: list[:class:`huaweicloudsdkeg.v1.CustomizeSourceInfoEventTypes`]
        """
        self._event_types = event_types

    @property
    def created_time(self):
        """Gets the created_time of this ShowDetailOfEventSourceResponse.

        创建UTC时间

        :return: The created_time of this ShowDetailOfEventSourceResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowDetailOfEventSourceResponse.

        创建UTC时间

        :param created_time: The created_time of this ShowDetailOfEventSourceResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this ShowDetailOfEventSourceResponse.

        更新UTC时间

        :return: The updated_time of this ShowDetailOfEventSourceResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ShowDetailOfEventSourceResponse.

        更新UTC时间

        :param updated_time: The updated_time of this ShowDetailOfEventSourceResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def channel_id(self):
        """Gets the channel_id of this ShowDetailOfEventSourceResponse.

        事件源归属的事件通道ID

        :return: The channel_id of this ShowDetailOfEventSourceResponse.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ShowDetailOfEventSourceResponse.

        事件源归属的事件通道ID

        :param channel_id: The channel_id of this ShowDetailOfEventSourceResponse.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def channel_name(self):
        """Gets the channel_name of this ShowDetailOfEventSourceResponse.

        事件源归属的事件通道名称

        :return: The channel_name of this ShowDetailOfEventSourceResponse.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this ShowDetailOfEventSourceResponse.

        事件源归属的事件通道名称

        :param channel_name: The channel_name of this ShowDetailOfEventSourceResponse.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def type(self):
        """Gets the type of this ShowDetailOfEventSourceResponse.

        事件源类型

        :return: The type of this ShowDetailOfEventSourceResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowDetailOfEventSourceResponse.

        事件源类型

        :param type: The type of this ShowDetailOfEventSourceResponse.
        :type type: str
        """
        self._type = type

    @property
    def detail(self):
        """Gets the detail of this ShowDetailOfEventSourceResponse.

        json格式封装消息实例链接信息：如RabbitMQ实例的instance_id字段、虚拟主机vhost字段、队列queue字段、用户名、密码等

        :return: The detail of this ShowDetailOfEventSourceResponse.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ShowDetailOfEventSourceResponse.

        json格式封装消息实例链接信息：如RabbitMQ实例的instance_id字段、虚拟主机vhost字段、队列queue字段、用户名、密码等

        :param detail: The detail of this ShowDetailOfEventSourceResponse.
        :type detail: object
        """
        self._detail = detail

    @property
    def status(self):
        """Gets the status of this ShowDetailOfEventSourceResponse.

        自定义事件源状态

        :return: The status of this ShowDetailOfEventSourceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDetailOfEventSourceResponse.

        自定义事件源状态

        :param status: The status of this ShowDetailOfEventSourceResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ShowDetailOfEventSourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
