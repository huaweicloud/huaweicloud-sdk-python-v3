# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsLabelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'labels': 'list[OpsLabelItem]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'labels': 'labels'
    }

    def __init__(self, total_count=None, labels=None):
        r"""ShowOpsLabelResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释：** 满足查询条件的标签总数量。 **取值范围：** 0到1000000。 
        :type total_count: int
        :param labels: **参数解释：** 当前页展示的标签详细信息列表。 **取值范围：** 不涉及。 
        :type labels: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelItem`]
        """
        
        super().__init__()

        self._total_count = None
        self._labels = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if labels is not None:
            self.labels = labels

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowOpsLabelResponse.

        **参数解释：** 满足查询条件的标签总数量。 **取值范围：** 0到1000000。 

        :return: The total_count of this ShowOpsLabelResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowOpsLabelResponse.

        **参数解释：** 满足查询条件的标签总数量。 **取值范围：** 0到1000000。 

        :param total_count: The total_count of this ShowOpsLabelResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def labels(self):
        r"""Gets the labels of this ShowOpsLabelResponse.

        **参数解释：** 当前页展示的标签详细信息列表。 **取值范围：** 不涉及。 

        :return: The labels of this ShowOpsLabelResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelItem`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ShowOpsLabelResponse.

        **参数解释：** 当前页展示的标签详细信息列表。 **取值范围：** 不涉及。 

        :param labels: The labels of this ShowOpsLabelResponse.
        :type labels: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelItem`]
        """
        self._labels = labels

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsLabelResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsLabelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
