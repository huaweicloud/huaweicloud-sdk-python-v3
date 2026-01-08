# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteListenersRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'listener_ids': 'list[str]'
    }

    attribute_map = {
        'listener_ids': 'listener_ids'
    }

    def __init__(self, listener_ids=None):
        r"""BatchDeleteListenersRequestBody

        The model defined in huaweicloud sdk

        :param listener_ids: **参数解释**：待删除的监听器id列表。 **约束限制**：一次最多删除10个监听器。 **取值范围**：不涉及 **默认取值**：不涉及
        :type listener_ids: list[str]
        """
        
        

        self._listener_ids = None
        self.discriminator = None

        self.listener_ids = listener_ids

    @property
    def listener_ids(self):
        r"""Gets the listener_ids of this BatchDeleteListenersRequestBody.

        **参数解释**：待删除的监听器id列表。 **约束限制**：一次最多删除10个监听器。 **取值范围**：不涉及 **默认取值**：不涉及

        :return: The listener_ids of this BatchDeleteListenersRequestBody.
        :rtype: list[str]
        """
        return self._listener_ids

    @listener_ids.setter
    def listener_ids(self, listener_ids):
        r"""Sets the listener_ids of this BatchDeleteListenersRequestBody.

        **参数解释**：待删除的监听器id列表。 **约束限制**：一次最多删除10个监听器。 **取值范围**：不涉及 **默认取值**：不涉及

        :param listener_ids: The listener_ids of this BatchDeleteListenersRequestBody.
        :type listener_ids: list[str]
        """
        self._listener_ids = listener_ids

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
        if not isinstance(other, BatchDeleteListenersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
