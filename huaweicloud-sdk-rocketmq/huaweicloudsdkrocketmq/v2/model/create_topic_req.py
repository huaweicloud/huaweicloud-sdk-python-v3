# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTopicReq:

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
        'brokers': 'list[str]',
        'queue_num': 'float',
        'permission': 'str',
        'message_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'brokers': 'brokers',
        'queue_num': 'queue_num',
        'permission': 'permission',
        'message_type': 'message_type'
    }

    def __init__(self, name=None, brokers=None, queue_num=None, permission=None, message_type=None):
        """CreateTopicReq

        The model defined in huaweicloud sdk

        :param name: 主题名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。
        :type name: str
        :param brokers: 关联的代理。
        :type brokers: list[str]
        :param queue_num: 队列数，范围1~50。
        :type queue_num: float
        :param permission: 权限。
        :type permission: str
        :param message_type: 消息类型。
        :type message_type: str
        """
        
        

        self._name = None
        self._brokers = None
        self._queue_num = None
        self._permission = None
        self._message_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if brokers is not None:
            self.brokers = brokers
        if queue_num is not None:
            self.queue_num = queue_num
        if permission is not None:
            self.permission = permission
        if message_type is not None:
            self.message_type = message_type

    @property
    def name(self):
        """Gets the name of this CreateTopicReq.

        主题名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。

        :return: The name of this CreateTopicReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTopicReq.

        主题名称，只能由英文字母、数字、百分号、竖线、中划线、下划线组成，长度3~64个字符。

        :param name: The name of this CreateTopicReq.
        :type name: str
        """
        self._name = name

    @property
    def brokers(self):
        """Gets the brokers of this CreateTopicReq.

        关联的代理。

        :return: The brokers of this CreateTopicReq.
        :rtype: list[str]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this CreateTopicReq.

        关联的代理。

        :param brokers: The brokers of this CreateTopicReq.
        :type brokers: list[str]
        """
        self._brokers = brokers

    @property
    def queue_num(self):
        """Gets the queue_num of this CreateTopicReq.

        队列数，范围1~50。

        :return: The queue_num of this CreateTopicReq.
        :rtype: float
        """
        return self._queue_num

    @queue_num.setter
    def queue_num(self, queue_num):
        """Sets the queue_num of this CreateTopicReq.

        队列数，范围1~50。

        :param queue_num: The queue_num of this CreateTopicReq.
        :type queue_num: float
        """
        self._queue_num = queue_num

    @property
    def permission(self):
        """Gets the permission of this CreateTopicReq.

        权限。

        :return: The permission of this CreateTopicReq.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this CreateTopicReq.

        权限。

        :param permission: The permission of this CreateTopicReq.
        :type permission: str
        """
        self._permission = permission

    @property
    def message_type(self):
        """Gets the message_type of this CreateTopicReq.

        消息类型。

        :return: The message_type of this CreateTopicReq.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this CreateTopicReq.

        消息类型。

        :param message_type: The message_type of this CreateTopicReq.
        :type message_type: str
        """
        self._message_type = message_type

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
        if not isinstance(other, CreateTopicReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
