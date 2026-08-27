# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cost_time': 'int',
        'current_time': 'int'
    }

    attribute_map = {
        'cost_time': 'cost_time',
        'current_time': 'current_time'
    }

    def __init__(self, cost_time=None, current_time=None):
        r"""MetaInfo

        The model defined in huaweicloud sdk

        :param cost_time: **参数解释**： 请求用时。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 
        :type cost_time: int
        :param current_time: **参数解释**： 请求结束时间。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 
        :type current_time: int
        """
        
        

        self._cost_time = None
        self._current_time = None
        self.discriminator = None

        if cost_time is not None:
            self.cost_time = cost_time
        if current_time is not None:
            self.current_time = current_time

    @property
    def cost_time(self):
        r"""Gets the cost_time of this MetaInfo.

        **参数解释**： 请求用时。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :return: The cost_time of this MetaInfo.
        :rtype: int
        """
        return self._cost_time

    @cost_time.setter
    def cost_time(self, cost_time):
        r"""Sets the cost_time of this MetaInfo.

        **参数解释**： 请求用时。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :param cost_time: The cost_time of this MetaInfo.
        :type cost_time: int
        """
        self._cost_time = cost_time

    @property
    def current_time(self):
        r"""Gets the current_time of this MetaInfo.

        **参数解释**： 请求结束时间。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :return: The current_time of this MetaInfo.
        :rtype: int
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        r"""Sets the current_time of this MetaInfo.

        **参数解释**： 请求结束时间。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,9999999999999]。 **默认取值**： 不涉及 

        :param current_time: The current_time of this MetaInfo.
        :type current_time: int
        """
        self._current_time = current_time

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
        if not isinstance(other, MetaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
