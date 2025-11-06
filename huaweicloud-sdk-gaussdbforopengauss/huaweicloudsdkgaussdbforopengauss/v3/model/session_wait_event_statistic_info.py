# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionWaitEventStatisticInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_name': 'str',
        'event_name': 'str',
        'count': 'str'
    }

    attribute_map = {
        'node_name': 'node_name',
        'event_name': 'event_name',
        'count': 'count'
    }

    def __init__(self, node_name=None, event_name=None, count=None):
        r"""SessionWaitEventStatisticInfo

        The model defined in huaweicloud sdk

        :param node_name: **参数解释**: 组件名称。 **取值范围**: 不涉及。 
        :type node_name: str
        :param event_name: **参数解释**: 等待事件名称。 **取值范围**: 不涉及。 
        :type event_name: str
        :param count: **参数解释**: 等待事件数量。 **取值范围**: 不涉及。 
        :type count: str
        """
        
        

        self._node_name = None
        self._event_name = None
        self._count = None
        self.discriminator = None

        if node_name is not None:
            self.node_name = node_name
        if event_name is not None:
            self.event_name = event_name
        if count is not None:
            self.count = count

    @property
    def node_name(self):
        r"""Gets the node_name of this SessionWaitEventStatisticInfo.

        **参数解释**: 组件名称。 **取值范围**: 不涉及。 

        :return: The node_name of this SessionWaitEventStatisticInfo.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this SessionWaitEventStatisticInfo.

        **参数解释**: 组件名称。 **取值范围**: 不涉及。 

        :param node_name: The node_name of this SessionWaitEventStatisticInfo.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def event_name(self):
        r"""Gets the event_name of this SessionWaitEventStatisticInfo.

        **参数解释**: 等待事件名称。 **取值范围**: 不涉及。 

        :return: The event_name of this SessionWaitEventStatisticInfo.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this SessionWaitEventStatisticInfo.

        **参数解释**: 等待事件名称。 **取值范围**: 不涉及。 

        :param event_name: The event_name of this SessionWaitEventStatisticInfo.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def count(self):
        r"""Gets the count of this SessionWaitEventStatisticInfo.

        **参数解释**: 等待事件数量。 **取值范围**: 不涉及。 

        :return: The count of this SessionWaitEventStatisticInfo.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this SessionWaitEventStatisticInfo.

        **参数解释**: 等待事件数量。 **取值范围**: 不涉及。 

        :param count: The count of this SessionWaitEventStatisticInfo.
        :type count: str
        """
        self._count = count

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SessionWaitEventStatisticInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
