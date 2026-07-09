# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlavorByTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'cluster_id': 'str',
        'change_mode': 'int'
    }

    attribute_map = {
        'order_id': 'orderId',
        'cluster_id': 'clusterId',
        'change_mode': 'changeMode'
    }

    def __init__(self, order_id=None, cluster_id=None, change_mode=None):
        r"""UpdateFlavorByTypeResponse

        The model defined in huaweicloud sdk

        :param order_id: **参数解释**： 变更订单ID，仅包周期集群返回。 **取值范围**： 不涉及
        :type order_id: str
        :param cluster_id: **参数解释**： 集群ID，仅包周期集群返回。 **取值范围**： 不涉及
        :type cluster_id: str
        :param change_mode: **参数解释**： 变更模式，仅包周期集群返回。 **取值范围**： - 10：升配。 - 30：降配。
        :type change_mode: int
        """
        
        super().__init__()

        self._order_id = None
        self._cluster_id = None
        self._change_mode = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if change_mode is not None:
            self.change_mode = change_mode

    @property
    def order_id(self):
        r"""Gets the order_id of this UpdateFlavorByTypeResponse.

        **参数解释**： 变更订单ID，仅包周期集群返回。 **取值范围**： 不涉及

        :return: The order_id of this UpdateFlavorByTypeResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this UpdateFlavorByTypeResponse.

        **参数解释**： 变更订单ID，仅包周期集群返回。 **取值范围**： 不涉及

        :param order_id: The order_id of this UpdateFlavorByTypeResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdateFlavorByTypeResponse.

        **参数解释**： 集群ID，仅包周期集群返回。 **取值范围**： 不涉及

        :return: The cluster_id of this UpdateFlavorByTypeResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdateFlavorByTypeResponse.

        **参数解释**： 集群ID，仅包周期集群返回。 **取值范围**： 不涉及

        :param cluster_id: The cluster_id of this UpdateFlavorByTypeResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def change_mode(self):
        r"""Gets the change_mode of this UpdateFlavorByTypeResponse.

        **参数解释**： 变更模式，仅包周期集群返回。 **取值范围**： - 10：升配。 - 30：降配。

        :return: The change_mode of this UpdateFlavorByTypeResponse.
        :rtype: int
        """
        return self._change_mode

    @change_mode.setter
    def change_mode(self, change_mode):
        r"""Sets the change_mode of this UpdateFlavorByTypeResponse.

        **参数解释**： 变更模式，仅包周期集群返回。 **取值范围**： - 10：升配。 - 30：降配。

        :param change_mode: The change_mode of this UpdateFlavorByTypeResponse.
        :type change_mode: int
        """
        self._change_mode = change_mode

    def to_dict(self):
        import warnings
        warnings.warn("UpdateFlavorByTypeResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdateFlavorByTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
