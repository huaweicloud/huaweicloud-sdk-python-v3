# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowStepExecutionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'count': 'int',
        'items': 'list[StepExecutionResp]',
        'default_order': 'str',
        'compare_columns': 'CompareColumns'
    }

    attribute_map = {
        'total': 'total',
        'count': 'count',
        'items': 'items',
        'default_order': 'default_order',
        'compare_columns': 'compare_columns'
    }

    def __init__(self, total=None, count=None, items=None, default_order=None, compare_columns=None):
        r"""ListWorkflowStepExecutionResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**：总数。 **取值范围**：不涉及。
        :type total: int
        :param count: **参数解释**：返回个数。 **取值范围**：不涉及。
        :type count: int
        :param items: **参数解释**：StepExecution数组。
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.StepExecutionResp`]
        :param default_order: **参数解释**：默认排序。 **取值范围**：不涉及。
        :type default_order: str
        :param compare_columns: 
        :type compare_columns: :class:`huaweicloudsdkmodelarts.v1.CompareColumns`
        """
        
        super().__init__()

        self._total = None
        self._count = None
        self._items = None
        self._default_order = None
        self._compare_columns = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if count is not None:
            self.count = count
        if items is not None:
            self.items = items
        if default_order is not None:
            self.default_order = default_order
        if compare_columns is not None:
            self.compare_columns = compare_columns

    @property
    def total(self):
        r"""Gets the total of this ListWorkflowStepExecutionResponse.

        **参数解释**：总数。 **取值范围**：不涉及。

        :return: The total of this ListWorkflowStepExecutionResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListWorkflowStepExecutionResponse.

        **参数解释**：总数。 **取值范围**：不涉及。

        :param total: The total of this ListWorkflowStepExecutionResponse.
        :type total: int
        """
        self._total = total

    @property
    def count(self):
        r"""Gets the count of this ListWorkflowStepExecutionResponse.

        **参数解释**：返回个数。 **取值范围**：不涉及。

        :return: The count of this ListWorkflowStepExecutionResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListWorkflowStepExecutionResponse.

        **参数解释**：返回个数。 **取值范围**：不涉及。

        :param count: The count of this ListWorkflowStepExecutionResponse.
        :type count: int
        """
        self._count = count

    @property
    def items(self):
        r"""Gets the items of this ListWorkflowStepExecutionResponse.

        **参数解释**：StepExecution数组。

        :return: The items of this ListWorkflowStepExecutionResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.StepExecutionResp`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListWorkflowStepExecutionResponse.

        **参数解释**：StepExecution数组。

        :param items: The items of this ListWorkflowStepExecutionResponse.
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.StepExecutionResp`]
        """
        self._items = items

    @property
    def default_order(self):
        r"""Gets the default_order of this ListWorkflowStepExecutionResponse.

        **参数解释**：默认排序。 **取值范围**：不涉及。

        :return: The default_order of this ListWorkflowStepExecutionResponse.
        :rtype: str
        """
        return self._default_order

    @default_order.setter
    def default_order(self, default_order):
        r"""Sets the default_order of this ListWorkflowStepExecutionResponse.

        **参数解释**：默认排序。 **取值范围**：不涉及。

        :param default_order: The default_order of this ListWorkflowStepExecutionResponse.
        :type default_order: str
        """
        self._default_order = default_order

    @property
    def compare_columns(self):
        r"""Gets the compare_columns of this ListWorkflowStepExecutionResponse.

        :return: The compare_columns of this ListWorkflowStepExecutionResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CompareColumns`
        """
        return self._compare_columns

    @compare_columns.setter
    def compare_columns(self, compare_columns):
        r"""Sets the compare_columns of this ListWorkflowStepExecutionResponse.

        :param compare_columns: The compare_columns of this ListWorkflowStepExecutionResponse.
        :type compare_columns: :class:`huaweicloudsdkmodelarts.v1.CompareColumns`
        """
        self._compare_columns = compare_columns

    def to_dict(self):
        import warnings
        warnings.warn("ListWorkflowStepExecutionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListWorkflowStepExecutionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
