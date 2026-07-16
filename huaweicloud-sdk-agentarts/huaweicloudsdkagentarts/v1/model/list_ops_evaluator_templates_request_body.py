# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorTemplatesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter_option': 'object',
        'page_size': 'int',
        'page_number': 'int'
    }

    attribute_map = {
        'filter_option': 'filter_option',
        'page_size': 'page_size',
        'page_number': 'page_number'
    }

    def __init__(self, filter_option=None, page_size=None, page_number=None):
        r"""ListOpsEvaluatorTemplatesRequestBody

        The model defined in huaweicloud sdk

        :param filter_option: **参数解释：** 用于设置获取评估器模板时的过滤条件，可以基于多个条件进行筛选。 **约束限制：** 过滤条件对象内包含逻辑操作和具体的条件列表。 **取值范围：** - 过滤条件数量不涉及最小数量限制，最大为10000。 - 逻辑操作（logic_op）长度不涉及最小值，最大长度为100。示例值为And。 - tag_key长度不涉及最小值，最大长度为100。示例值为Category。 - 操作（operator）长度不涉及最小值，最大长度为100。示例值为In。 - 值（value）长度不涉及最小值，最大长度为100。示例值为LLM。 **默认取值：** 不涉及。
        :type filter_option: object
        :param page_size: **参数解释：** 指定每次请求返回的评估器模板数量，用于控制每次分页返回的数据量。 **约束限制：** 必须为0到10,000 之间的整数。 **取值范围：** 类型为整数，取值范围为0-10000的整数。 **默认取值：** 不涉及。
        :type page_size: int
        :param page_number: **参数解释：** 指定获取的页码，用于控制数据分页的页数定位。 **约束限制：** 必须为0到10,000之间的整数。 **取值范围：** 类型为整数，取值范围为0-10000的整数。 **默认取值：** 不涉及。
        :type page_number: int
        """
        
        

        self._filter_option = None
        self._page_size = None
        self._page_number = None
        self.discriminator = None

        if filter_option is not None:
            self.filter_option = filter_option
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number

    @property
    def filter_option(self):
        r"""Gets the filter_option of this ListOpsEvaluatorTemplatesRequestBody.

        **参数解释：** 用于设置获取评估器模板时的过滤条件，可以基于多个条件进行筛选。 **约束限制：** 过滤条件对象内包含逻辑操作和具体的条件列表。 **取值范围：** - 过滤条件数量不涉及最小数量限制，最大为10000。 - 逻辑操作（logic_op）长度不涉及最小值，最大长度为100。示例值为And。 - tag_key长度不涉及最小值，最大长度为100。示例值为Category。 - 操作（operator）长度不涉及最小值，最大长度为100。示例值为In。 - 值（value）长度不涉及最小值，最大长度为100。示例值为LLM。 **默认取值：** 不涉及。

        :return: The filter_option of this ListOpsEvaluatorTemplatesRequestBody.
        :rtype: object
        """
        return self._filter_option

    @filter_option.setter
    def filter_option(self, filter_option):
        r"""Sets the filter_option of this ListOpsEvaluatorTemplatesRequestBody.

        **参数解释：** 用于设置获取评估器模板时的过滤条件，可以基于多个条件进行筛选。 **约束限制：** 过滤条件对象内包含逻辑操作和具体的条件列表。 **取值范围：** - 过滤条件数量不涉及最小数量限制，最大为10000。 - 逻辑操作（logic_op）长度不涉及最小值，最大长度为100。示例值为And。 - tag_key长度不涉及最小值，最大长度为100。示例值为Category。 - 操作（operator）长度不涉及最小值，最大长度为100。示例值为In。 - 值（value）长度不涉及最小值，最大长度为100。示例值为LLM。 **默认取值：** 不涉及。

        :param filter_option: The filter_option of this ListOpsEvaluatorTemplatesRequestBody.
        :type filter_option: object
        """
        self._filter_option = filter_option

    @property
    def page_size(self):
        r"""Gets the page_size of this ListOpsEvaluatorTemplatesRequestBody.

        **参数解释：** 指定每次请求返回的评估器模板数量，用于控制每次分页返回的数据量。 **约束限制：** 必须为0到10,000 之间的整数。 **取值范围：** 类型为整数，取值范围为0-10000的整数。 **默认取值：** 不涉及。

        :return: The page_size of this ListOpsEvaluatorTemplatesRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListOpsEvaluatorTemplatesRequestBody.

        **参数解释：** 指定每次请求返回的评估器模板数量，用于控制每次分页返回的数据量。 **约束限制：** 必须为0到10,000 之间的整数。 **取值范围：** 类型为整数，取值范围为0-10000的整数。 **默认取值：** 不涉及。

        :param page_size: The page_size of this ListOpsEvaluatorTemplatesRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        r"""Gets the page_number of this ListOpsEvaluatorTemplatesRequestBody.

        **参数解释：** 指定获取的页码，用于控制数据分页的页数定位。 **约束限制：** 必须为0到10,000之间的整数。 **取值范围：** 类型为整数，取值范围为0-10000的整数。 **默认取值：** 不涉及。

        :return: The page_number of this ListOpsEvaluatorTemplatesRequestBody.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this ListOpsEvaluatorTemplatesRequestBody.

        **参数解释：** 指定获取的页码，用于控制数据分页的页数定位。 **约束限制：** 必须为0到10,000之间的整数。 **取值范围：** 类型为整数，取值范围为0-10000的整数。 **默认取值：** 不涉及。

        :param page_number: The page_number of this ListOpsEvaluatorTemplatesRequestBody.
        :type page_number: int
        """
        self._page_number = page_number

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
        if not isinstance(other, ListOpsEvaluatorTemplatesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
