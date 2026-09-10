# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsSampleStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sample_ratio': 'int',
        'max_sample_count': 'int',
        'filters': 'list[OpsSampleFilter]',
        'filter_sign': 'str'
    }

    attribute_map = {
        'sample_ratio': 'sample_ratio',
        'max_sample_count': 'max_sample_count',
        'filters': 'filters',
        'filter_sign': 'filter_sign'
    }

    def __init__(self, sample_ratio=None, max_sample_count=None, filters=None, filter_sign=None):
        r"""OpsSampleStrategy

        The model defined in huaweicloud sdk

        :param sample_ratio: **参数解释：** 数据采样率。  **约束限制：** 不涉及  **取值范围：** 数值在1到100之间。  **默认取值：** 100。
        :type sample_ratio: int
        :param max_sample_count: **参数解释：** 最大数据采样个数。  **约束限制：** 不涉及  **取值范围：** 数值在1到500之间。  **默认取值：** 100。
        :type max_sample_count: int
        :param filters: **参数解释：** 数据采样的筛选条件。  **约束限制：** 不涉及  **取值范围：** 数组长度0-5。  **默认取值：** 空数组。
        :type filters: list[:class:`huaweicloudsdkagentarts.v1.OpsSampleFilter`]
        :param filter_sign: **参数解释：** 连接标识，用于标明查询语句中条件之间且或者或的关系。 **约束限制：** 不涉及  **取值范围：** and，or **默认取值：** and
        :type filter_sign: str
        """
        
        

        self._sample_ratio = None
        self._max_sample_count = None
        self._filters = None
        self._filter_sign = None
        self.discriminator = None

        if sample_ratio is not None:
            self.sample_ratio = sample_ratio
        if max_sample_count is not None:
            self.max_sample_count = max_sample_count
        if filters is not None:
            self.filters = filters
        if filter_sign is not None:
            self.filter_sign = filter_sign

    @property
    def sample_ratio(self):
        r"""Gets the sample_ratio of this OpsSampleStrategy.

        **参数解释：** 数据采样率。  **约束限制：** 不涉及  **取值范围：** 数值在1到100之间。  **默认取值：** 100。

        :return: The sample_ratio of this OpsSampleStrategy.
        :rtype: int
        """
        return self._sample_ratio

    @sample_ratio.setter
    def sample_ratio(self, sample_ratio):
        r"""Sets the sample_ratio of this OpsSampleStrategy.

        **参数解释：** 数据采样率。  **约束限制：** 不涉及  **取值范围：** 数值在1到100之间。  **默认取值：** 100。

        :param sample_ratio: The sample_ratio of this OpsSampleStrategy.
        :type sample_ratio: int
        """
        self._sample_ratio = sample_ratio

    @property
    def max_sample_count(self):
        r"""Gets the max_sample_count of this OpsSampleStrategy.

        **参数解释：** 最大数据采样个数。  **约束限制：** 不涉及  **取值范围：** 数值在1到500之间。  **默认取值：** 100。

        :return: The max_sample_count of this OpsSampleStrategy.
        :rtype: int
        """
        return self._max_sample_count

    @max_sample_count.setter
    def max_sample_count(self, max_sample_count):
        r"""Sets the max_sample_count of this OpsSampleStrategy.

        **参数解释：** 最大数据采样个数。  **约束限制：** 不涉及  **取值范围：** 数值在1到500之间。  **默认取值：** 100。

        :param max_sample_count: The max_sample_count of this OpsSampleStrategy.
        :type max_sample_count: int
        """
        self._max_sample_count = max_sample_count

    @property
    def filters(self):
        r"""Gets the filters of this OpsSampleStrategy.

        **参数解释：** 数据采样的筛选条件。  **约束限制：** 不涉及  **取值范围：** 数组长度0-5。  **默认取值：** 空数组。

        :return: The filters of this OpsSampleStrategy.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsSampleFilter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this OpsSampleStrategy.

        **参数解释：** 数据采样的筛选条件。  **约束限制：** 不涉及  **取值范围：** 数组长度0-5。  **默认取值：** 空数组。

        :param filters: The filters of this OpsSampleStrategy.
        :type filters: list[:class:`huaweicloudsdkagentarts.v1.OpsSampleFilter`]
        """
        self._filters = filters

    @property
    def filter_sign(self):
        r"""Gets the filter_sign of this OpsSampleStrategy.

        **参数解释：** 连接标识，用于标明查询语句中条件之间且或者或的关系。 **约束限制：** 不涉及  **取值范围：** and，or **默认取值：** and

        :return: The filter_sign of this OpsSampleStrategy.
        :rtype: str
        """
        return self._filter_sign

    @filter_sign.setter
    def filter_sign(self, filter_sign):
        r"""Sets the filter_sign of this OpsSampleStrategy.

        **参数解释：** 连接标识，用于标明查询语句中条件之间且或者或的关系。 **约束限制：** 不涉及  **取值范围：** and，or **默认取值：** and

        :param filter_sign: The filter_sign of this OpsSampleStrategy.
        :type filter_sign: str
        """
        self._filter_sign = filter_sign

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
        if not isinstance(other, OpsSampleStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
