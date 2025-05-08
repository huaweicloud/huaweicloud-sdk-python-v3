# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Brokers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'broker_name': 'str',
        'queues': 'list[Queue]'
    }

    attribute_map = {
        'broker_name': 'broker_name',
        'queues': 'queues'
    }

    def __init__(self, broker_name=None, queues=None):
        r"""Brokers

        The model defined in huaweicloud sdk

        :param broker_name: **参数解释**： Topic关联代理名称。 **取值范围**： 不涉及。
        :type broker_name: str
        :param queues: **参数解释**： 关联代理的队列详情。
        :type queues: list[:class:`huaweicloudsdkrocketmq.v2.Queue`]
        """
        
        

        self._broker_name = None
        self._queues = None
        self.discriminator = None

        if broker_name is not None:
            self.broker_name = broker_name
        if queues is not None:
            self.queues = queues

    @property
    def broker_name(self):
        r"""Gets the broker_name of this Brokers.

        **参数解释**： Topic关联代理名称。 **取值范围**： 不涉及。

        :return: The broker_name of this Brokers.
        :rtype: str
        """
        return self._broker_name

    @broker_name.setter
    def broker_name(self, broker_name):
        r"""Sets the broker_name of this Brokers.

        **参数解释**： Topic关联代理名称。 **取值范围**： 不涉及。

        :param broker_name: The broker_name of this Brokers.
        :type broker_name: str
        """
        self._broker_name = broker_name

    @property
    def queues(self):
        r"""Gets the queues of this Brokers.

        **参数解释**： 关联代理的队列详情。

        :return: The queues of this Brokers.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.Queue`]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        r"""Sets the queues of this Brokers.

        **参数解释**： 关联代理的队列详情。

        :param queues: The queues of this Brokers.
        :type queues: list[:class:`huaweicloudsdkrocketmq.v2.Queue`]
        """
        self._queues = queues

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
        if not isinstance(other, Brokers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
