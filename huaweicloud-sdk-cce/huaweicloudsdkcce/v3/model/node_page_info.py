# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_count': 'int',
        'next_marker': 'str'
    }

    attribute_map = {
        'current_count': 'currentCount',
        'next_marker': 'nextMarker'
    }

    def __init__(self, current_count=None, next_marker=None):
        r"""NodePageInfo

        The model defined in huaweicloud sdk

        :param current_count: **参数解释**： 当前页返回的所有节点数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type current_count: int
        :param next_marker: **参数解释**： 当前页最后一条记录，为查询下一页的marker取值，最后一页时无nextMarker字段。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type next_marker: str
        """
        
        

        self._current_count = None
        self._next_marker = None
        self.discriminator = None

        self.current_count = current_count
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def current_count(self):
        r"""Gets the current_count of this NodePageInfo.

        **参数解释**： 当前页返回的所有节点数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The current_count of this NodePageInfo.
        :rtype: int
        """
        return self._current_count

    @current_count.setter
    def current_count(self, current_count):
        r"""Sets the current_count of this NodePageInfo.

        **参数解释**： 当前页返回的所有节点数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param current_count: The current_count of this NodePageInfo.
        :type current_count: int
        """
        self._current_count = current_count

    @property
    def next_marker(self):
        r"""Gets the next_marker of this NodePageInfo.

        **参数解释**： 当前页最后一条记录，为查询下一页的marker取值，最后一页时无nextMarker字段。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The next_marker of this NodePageInfo.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this NodePageInfo.

        **参数解释**： 当前页最后一条记录，为查询下一页的marker取值，最后一页时无nextMarker字段。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param next_marker: The next_marker of this NodePageInfo.
        :type next_marker: str
        """
        self._next_marker = next_marker

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
        if not isinstance(other, NodePageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
