# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizeSourceCreateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'channel_id': 'str',
        'type': 'str',
        'detail': 'object'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'channel_id': 'channel_id',
        'type': 'type',
        'detail': 'detail'
    }

    def __init__(self, name=None, description=None, channel_id=None, type=None, detail=None):
        """CustomizeSourceCreateReq

        The model defined in huaweicloud sdk

        :param name: 自定义事件源名称，租户下唯一，由小写字母、数字、点、下划线和中划线组成，必须以字母或数字开头，且不能以hc.开头
        :type name: str
        :param description: 事件源描述
        :type description: str
        :param channel_id: 指导事件源归属的事件通道ID
        :type channel_id: str
        :param type: 事件源类型
        :type type: str
        :param detail: json格式封装消息实例链接信息：如RabbitMQ实例的instance_id字段、虚拟主机vhost字段、队列queue字段、用户名、密码等
        :type detail: object
        """
        
        

        self._name = None
        self._description = None
        self._channel_id = None
        self._type = None
        self._detail = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if channel_id is not None:
            self.channel_id = channel_id
        if type is not None:
            self.type = type
        if detail is not None:
            self.detail = detail

    @property
    def name(self):
        """Gets the name of this CustomizeSourceCreateReq.

        自定义事件源名称，租户下唯一，由小写字母、数字、点、下划线和中划线组成，必须以字母或数字开头，且不能以hc.开头

        :return: The name of this CustomizeSourceCreateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomizeSourceCreateReq.

        自定义事件源名称，租户下唯一，由小写字母、数字、点、下划线和中划线组成，必须以字母或数字开头，且不能以hc.开头

        :param name: The name of this CustomizeSourceCreateReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CustomizeSourceCreateReq.

        事件源描述

        :return: The description of this CustomizeSourceCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomizeSourceCreateReq.

        事件源描述

        :param description: The description of this CustomizeSourceCreateReq.
        :type description: str
        """
        self._description = description

    @property
    def channel_id(self):
        """Gets the channel_id of this CustomizeSourceCreateReq.

        指导事件源归属的事件通道ID

        :return: The channel_id of this CustomizeSourceCreateReq.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this CustomizeSourceCreateReq.

        指导事件源归属的事件通道ID

        :param channel_id: The channel_id of this CustomizeSourceCreateReq.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def type(self):
        """Gets the type of this CustomizeSourceCreateReq.

        事件源类型

        :return: The type of this CustomizeSourceCreateReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomizeSourceCreateReq.

        事件源类型

        :param type: The type of this CustomizeSourceCreateReq.
        :type type: str
        """
        self._type = type

    @property
    def detail(self):
        """Gets the detail of this CustomizeSourceCreateReq.

        json格式封装消息实例链接信息：如RabbitMQ实例的instance_id字段、虚拟主机vhost字段、队列queue字段、用户名、密码等

        :return: The detail of this CustomizeSourceCreateReq.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this CustomizeSourceCreateReq.

        json格式封装消息实例链接信息：如RabbitMQ实例的instance_id字段、虚拟主机vhost字段、队列queue字段、用户名、密码等

        :param detail: The detail of this CustomizeSourceCreateReq.
        :type detail: object
        """
        self._detail = detail

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
        if not isinstance(other, CustomizeSourceCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
