# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_number': 'int',
        'page_size': 'int',
        'evaluators': 'list[OpsListEvaluatorsInfo]',
        'total': 'int',
        'total_pages': 'int'
    }

    attribute_map = {
        'page_number': 'page_number',
        'page_size': 'page_size',
        'evaluators': 'evaluators',
        'total': 'total',
        'total_pages': 'total_pages'
    }

    def __init__(self, page_number=None, page_size=None, evaluators=None, total=None, total_pages=None):
        r"""ListOpsEvaluatorsResponse

        The model defined in huaweicloud sdk

        :param page_number: **参数解释：** 当前页码。 **约束限制：** 不涉及。 **取值范围：** 正整数。
        :type page_number: int
        :param page_size: **参数解释：** 每页返回的记录条数。 **约束限制：** 不涉及。 **取值范围：** 1~100。
        :type page_size: int
        :param evaluators: **参数解释** 包含评估器元数据、配置信息及状态的详细信息列表。 **取值范围** 元素参考内部定义。 
        :type evaluators: list[:class:`huaweicloudsdkagentarts.v1.OpsListEvaluatorsInfo`]
        :param total: **参数解释** 符合当前过滤条件的评估器总记录数，常用于分页。 **取值范围** 非负整数。 
        :type total: int
        :param total_pages: **参数解释：** 总页数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。
        :type total_pages: int
        """
        
        super().__init__()

        self._page_number = None
        self._page_size = None
        self._evaluators = None
        self._total = None
        self._total_pages = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if evaluators is not None:
            self.evaluators = evaluators
        if total is not None:
            self.total = total
        if total_pages is not None:
            self.total_pages = total_pages

    @property
    def page_number(self):
        r"""Gets the page_number of this ListOpsEvaluatorsResponse.

        **参数解释：** 当前页码。 **约束限制：** 不涉及。 **取值范围：** 正整数。

        :return: The page_number of this ListOpsEvaluatorsResponse.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this ListOpsEvaluatorsResponse.

        **参数解释：** 当前页码。 **约束限制：** 不涉及。 **取值范围：** 正整数。

        :param page_number: The page_number of this ListOpsEvaluatorsResponse.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def page_size(self):
        r"""Gets the page_size of this ListOpsEvaluatorsResponse.

        **参数解释：** 每页返回的记录条数。 **约束限制：** 不涉及。 **取值范围：** 1~100。

        :return: The page_size of this ListOpsEvaluatorsResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListOpsEvaluatorsResponse.

        **参数解释：** 每页返回的记录条数。 **约束限制：** 不涉及。 **取值范围：** 1~100。

        :param page_size: The page_size of this ListOpsEvaluatorsResponse.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def evaluators(self):
        r"""Gets the evaluators of this ListOpsEvaluatorsResponse.

        **参数解释** 包含评估器元数据、配置信息及状态的详细信息列表。 **取值范围** 元素参考内部定义。 

        :return: The evaluators of this ListOpsEvaluatorsResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsListEvaluatorsInfo`]
        """
        return self._evaluators

    @evaluators.setter
    def evaluators(self, evaluators):
        r"""Sets the evaluators of this ListOpsEvaluatorsResponse.

        **参数解释** 包含评估器元数据、配置信息及状态的详细信息列表。 **取值范围** 元素参考内部定义。 

        :param evaluators: The evaluators of this ListOpsEvaluatorsResponse.
        :type evaluators: list[:class:`huaweicloudsdkagentarts.v1.OpsListEvaluatorsInfo`]
        """
        self._evaluators = evaluators

    @property
    def total(self):
        r"""Gets the total of this ListOpsEvaluatorsResponse.

        **参数解释** 符合当前过滤条件的评估器总记录数，常用于分页。 **取值范围** 非负整数。 

        :return: The total of this ListOpsEvaluatorsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOpsEvaluatorsResponse.

        **参数解释** 符合当前过滤条件的评估器总记录数，常用于分页。 **取值范围** 非负整数。 

        :param total: The total of this ListOpsEvaluatorsResponse.
        :type total: int
        """
        self._total = total

    @property
    def total_pages(self):
        r"""Gets the total_pages of this ListOpsEvaluatorsResponse.

        **参数解释：** 总页数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。

        :return: The total_pages of this ListOpsEvaluatorsResponse.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        r"""Sets the total_pages of this ListOpsEvaluatorsResponse.

        **参数解释：** 总页数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。

        :param total_pages: The total_pages of this ListOpsEvaluatorsResponse.
        :type total_pages: int
        """
        self._total_pages = total_pages

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsEvaluatorsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOpsEvaluatorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
