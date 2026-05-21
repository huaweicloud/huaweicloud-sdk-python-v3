# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRelatedDnsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'related_data_nodes': 'list[RelatedDnVO]',
        'latest_restorable_time': 'str',
        'offset': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'related_data_nodes': 'related_data_nodes',
        'latest_restorable_time': 'latest_restorable_time',
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, related_data_nodes=None, latest_restorable_time=None, offset=None, limit=None, total=None):
        r"""ShowRelatedDnsResponse

        The model defined in huaweicloud sdk

        :param related_data_nodes: 关联DN。
        :type related_data_nodes: list[:class:`huaweicloudsdkddm.v1.RelatedDnVO`]
        :param latest_restorable_time: 最近恢复时间点。
        :type latest_restorable_time: str
        :param offset: **参数解释**：  分页参数: 起始值。  **参数范围**：   大于等于0。
        :type offset: int
        :param limit: **参数解释**：  分页参数: 每页记录数。  **参数范围**：  大于0且小于等于128。
        :type limit: int
        :param total: **参数解释**：  总记录数。  **参数范围**：  不涉及。
        :type total: int
        """
        
        super().__init__()

        self._related_data_nodes = None
        self._latest_restorable_time = None
        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if related_data_nodes is not None:
            self.related_data_nodes = related_data_nodes
        if latest_restorable_time is not None:
            self.latest_restorable_time = latest_restorable_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def related_data_nodes(self):
        r"""Gets the related_data_nodes of this ShowRelatedDnsResponse.

        关联DN。

        :return: The related_data_nodes of this ShowRelatedDnsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.RelatedDnVO`]
        """
        return self._related_data_nodes

    @related_data_nodes.setter
    def related_data_nodes(self, related_data_nodes):
        r"""Sets the related_data_nodes of this ShowRelatedDnsResponse.

        关联DN。

        :param related_data_nodes: The related_data_nodes of this ShowRelatedDnsResponse.
        :type related_data_nodes: list[:class:`huaweicloudsdkddm.v1.RelatedDnVO`]
        """
        self._related_data_nodes = related_data_nodes

    @property
    def latest_restorable_time(self):
        r"""Gets the latest_restorable_time of this ShowRelatedDnsResponse.

        最近恢复时间点。

        :return: The latest_restorable_time of this ShowRelatedDnsResponse.
        :rtype: str
        """
        return self._latest_restorable_time

    @latest_restorable_time.setter
    def latest_restorable_time(self, latest_restorable_time):
        r"""Sets the latest_restorable_time of this ShowRelatedDnsResponse.

        最近恢复时间点。

        :param latest_restorable_time: The latest_restorable_time of this ShowRelatedDnsResponse.
        :type latest_restorable_time: str
        """
        self._latest_restorable_time = latest_restorable_time

    @property
    def offset(self):
        r"""Gets the offset of this ShowRelatedDnsResponse.

        **参数解释**：  分页参数: 起始值。  **参数范围**：   大于等于0。

        :return: The offset of this ShowRelatedDnsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowRelatedDnsResponse.

        **参数解释**：  分页参数: 起始值。  **参数范围**：   大于等于0。

        :param offset: The offset of this ShowRelatedDnsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowRelatedDnsResponse.

        **参数解释**：  分页参数: 每页记录数。  **参数范围**：  大于0且小于等于128。

        :return: The limit of this ShowRelatedDnsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowRelatedDnsResponse.

        **参数解释**：  分页参数: 每页记录数。  **参数范围**：  大于0且小于等于128。

        :param limit: The limit of this ShowRelatedDnsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this ShowRelatedDnsResponse.

        **参数解释**：  总记录数。  **参数范围**：  不涉及。

        :return: The total of this ShowRelatedDnsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowRelatedDnsResponse.

        **参数解释**：  总记录数。  **参数范围**：  不涉及。

        :param total: The total of this ShowRelatedDnsResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ShowRelatedDnsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRelatedDnsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
