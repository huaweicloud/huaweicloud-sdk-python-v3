# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOneTopicResponse(SdkResponse):

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
        'total_read_queue_num': 'float',
        'total_write_queue_num': 'float',
        'permission': 'str',
        'brokers': 'list[TopicBrokers]',
        'message_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'total_read_queue_num': 'total_read_queue_num',
        'total_write_queue_num': 'total_write_queue_num',
        'permission': 'permission',
        'brokers': 'brokers',
        'message_type': 'message_type'
    }

    def __init__(self, name=None, total_read_queue_num=None, total_write_queue_num=None, permission=None, brokers=None, message_type=None):
        r"""ShowOneTopicResponse

        The model defined in huaweicloud sdk

        :param name: **参数解释**： Topic名称。 **取值范围**： 不涉及。
        :type name: str
        :param total_read_queue_num: **参数解释**： 总读队列个数。 **取值范围**： 不涉及。
        :type total_read_queue_num: float
        :param total_write_queue_num: **参数解释**： 总写队列个数。 **取值范围**： 不涉及。
        :type total_write_queue_num: float
        :param permission: **参数解释**： 权限。 **取值范围**： - sub：拥有订阅权限。 - pub：拥有发布权限。 - all：拥有发布、订阅权限。
        :type permission: str
        :param brokers: 关联的代理。
        :type brokers: list[:class:`huaweicloudsdkrocketmq.v2.TopicBrokers`]
        :param message_type: **参数解释**： 消息类型（RocketMQ实例5.x版本才包含此参数）。 **取值范围**： - NORMAL：普通消息。 - FIFO：顺序消息。 - DELAY：定时消息。 - TRANSACTION：事务消息。
        :type message_type: str
        """
        
        super(ShowOneTopicResponse, self).__init__()

        self._name = None
        self._total_read_queue_num = None
        self._total_write_queue_num = None
        self._permission = None
        self._brokers = None
        self._message_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if total_read_queue_num is not None:
            self.total_read_queue_num = total_read_queue_num
        if total_write_queue_num is not None:
            self.total_write_queue_num = total_write_queue_num
        if permission is not None:
            self.permission = permission
        if brokers is not None:
            self.brokers = brokers
        if message_type is not None:
            self.message_type = message_type

    @property
    def name(self):
        r"""Gets the name of this ShowOneTopicResponse.

        **参数解释**： Topic名称。 **取值范围**： 不涉及。

        :return: The name of this ShowOneTopicResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowOneTopicResponse.

        **参数解释**： Topic名称。 **取值范围**： 不涉及。

        :param name: The name of this ShowOneTopicResponse.
        :type name: str
        """
        self._name = name

    @property
    def total_read_queue_num(self):
        r"""Gets the total_read_queue_num of this ShowOneTopicResponse.

        **参数解释**： 总读队列个数。 **取值范围**： 不涉及。

        :return: The total_read_queue_num of this ShowOneTopicResponse.
        :rtype: float
        """
        return self._total_read_queue_num

    @total_read_queue_num.setter
    def total_read_queue_num(self, total_read_queue_num):
        r"""Sets the total_read_queue_num of this ShowOneTopicResponse.

        **参数解释**： 总读队列个数。 **取值范围**： 不涉及。

        :param total_read_queue_num: The total_read_queue_num of this ShowOneTopicResponse.
        :type total_read_queue_num: float
        """
        self._total_read_queue_num = total_read_queue_num

    @property
    def total_write_queue_num(self):
        r"""Gets the total_write_queue_num of this ShowOneTopicResponse.

        **参数解释**： 总写队列个数。 **取值范围**： 不涉及。

        :return: The total_write_queue_num of this ShowOneTopicResponse.
        :rtype: float
        """
        return self._total_write_queue_num

    @total_write_queue_num.setter
    def total_write_queue_num(self, total_write_queue_num):
        r"""Sets the total_write_queue_num of this ShowOneTopicResponse.

        **参数解释**： 总写队列个数。 **取值范围**： 不涉及。

        :param total_write_queue_num: The total_write_queue_num of this ShowOneTopicResponse.
        :type total_write_queue_num: float
        """
        self._total_write_queue_num = total_write_queue_num

    @property
    def permission(self):
        r"""Gets the permission of this ShowOneTopicResponse.

        **参数解释**： 权限。 **取值范围**： - sub：拥有订阅权限。 - pub：拥有发布权限。 - all：拥有发布、订阅权限。

        :return: The permission of this ShowOneTopicResponse.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this ShowOneTopicResponse.

        **参数解释**： 权限。 **取值范围**： - sub：拥有订阅权限。 - pub：拥有发布权限。 - all：拥有发布、订阅权限。

        :param permission: The permission of this ShowOneTopicResponse.
        :type permission: str
        """
        self._permission = permission

    @property
    def brokers(self):
        r"""Gets the brokers of this ShowOneTopicResponse.

        关联的代理。

        :return: The brokers of this ShowOneTopicResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.TopicBrokers`]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        r"""Sets the brokers of this ShowOneTopicResponse.

        关联的代理。

        :param brokers: The brokers of this ShowOneTopicResponse.
        :type brokers: list[:class:`huaweicloudsdkrocketmq.v2.TopicBrokers`]
        """
        self._brokers = brokers

    @property
    def message_type(self):
        r"""Gets the message_type of this ShowOneTopicResponse.

        **参数解释**： 消息类型（RocketMQ实例5.x版本才包含此参数）。 **取值范围**： - NORMAL：普通消息。 - FIFO：顺序消息。 - DELAY：定时消息。 - TRANSACTION：事务消息。

        :return: The message_type of this ShowOneTopicResponse.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        r"""Sets the message_type of this ShowOneTopicResponse.

        **参数解释**： 消息类型（RocketMQ实例5.x版本才包含此参数）。 **取值范围**： - NORMAL：普通消息。 - FIFO：顺序消息。 - DELAY：定时消息。 - TRANSACTION：事务消息。

        :param message_type: The message_type of this ShowOneTopicResponse.
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
        if not isinstance(other, ShowOneTopicResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
