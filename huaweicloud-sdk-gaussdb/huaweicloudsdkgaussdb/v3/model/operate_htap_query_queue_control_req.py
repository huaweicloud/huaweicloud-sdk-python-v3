# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateHtapQueryQueueControlReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_query_queue_select': 'str'
    }

    attribute_map = {
        'enable_query_queue_select': 'enable_query_queue_select'
    }

    def __init__(self, enable_query_queue_select=None):
        r"""OperateHtapQueryQueueControlReq

        The model defined in huaweicloud sdk

        :param enable_query_queue_select: **参数解释**：  查询队列的开关状态。  **约束限制**：  不涉及。  **取值范围**：  - true：表示开启。 - false：表示关闭。  **默认值**：  false。
        :type enable_query_queue_select: str
        """
        
        

        self._enable_query_queue_select = None
        self.discriminator = None

        self.enable_query_queue_select = enable_query_queue_select

    @property
    def enable_query_queue_select(self):
        r"""Gets the enable_query_queue_select of this OperateHtapQueryQueueControlReq.

        **参数解释**：  查询队列的开关状态。  **约束限制**：  不涉及。  **取值范围**：  - true：表示开启。 - false：表示关闭。  **默认值**：  false。

        :return: The enable_query_queue_select of this OperateHtapQueryQueueControlReq.
        :rtype: str
        """
        return self._enable_query_queue_select

    @enable_query_queue_select.setter
    def enable_query_queue_select(self, enable_query_queue_select):
        r"""Sets the enable_query_queue_select of this OperateHtapQueryQueueControlReq.

        **参数解释**：  查询队列的开关状态。  **约束限制**：  不涉及。  **取值范围**：  - true：表示开启。 - false：表示关闭。  **默认值**：  false。

        :param enable_query_queue_select: The enable_query_queue_select of this OperateHtapQueryQueueControlReq.
        :type enable_query_queue_select: str
        """
        self._enable_query_queue_select = enable_query_queue_select

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
        if not isinstance(other, OperateHtapQueryQueueControlReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
