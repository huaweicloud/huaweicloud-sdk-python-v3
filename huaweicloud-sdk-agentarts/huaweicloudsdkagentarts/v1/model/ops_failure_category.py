# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsFailureCategory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_category_name': 'str',
        'affected_session_count': 'int',
        'sub_categories': 'list[OpsFailureSubCategory]'
    }

    attribute_map = {
        'error_category_name': 'error_category_name',
        'affected_session_count': 'affected_session_count',
        'sub_categories': 'sub_categories'
    }

    def __init__(self, error_category_name=None, affected_session_count=None, sub_categories=None):
        r"""OpsFailureCategory

        The model defined in huaweicloud sdk

        :param error_category_name: **参数解释：** 故障类别名称。  **取值范围：** 长度1-128个字符。
        :type error_category_name: str
        :param affected_session_count: **参数解释：** 故障影响的会话个数。  **取值范围：** 大小为0到10000。
        :type affected_session_count: int
        :param sub_categories: **参数解释：** 子故障类别列表。  **取值范围：** 长度0-100的数组。
        :type sub_categories: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureSubCategory`]
        """
        
        

        self._error_category_name = None
        self._affected_session_count = None
        self._sub_categories = None
        self.discriminator = None

        if error_category_name is not None:
            self.error_category_name = error_category_name
        if affected_session_count is not None:
            self.affected_session_count = affected_session_count
        if sub_categories is not None:
            self.sub_categories = sub_categories

    @property
    def error_category_name(self):
        r"""Gets the error_category_name of this OpsFailureCategory.

        **参数解释：** 故障类别名称。  **取值范围：** 长度1-128个字符。

        :return: The error_category_name of this OpsFailureCategory.
        :rtype: str
        """
        return self._error_category_name

    @error_category_name.setter
    def error_category_name(self, error_category_name):
        r"""Sets the error_category_name of this OpsFailureCategory.

        **参数解释：** 故障类别名称。  **取值范围：** 长度1-128个字符。

        :param error_category_name: The error_category_name of this OpsFailureCategory.
        :type error_category_name: str
        """
        self._error_category_name = error_category_name

    @property
    def affected_session_count(self):
        r"""Gets the affected_session_count of this OpsFailureCategory.

        **参数解释：** 故障影响的会话个数。  **取值范围：** 大小为0到10000。

        :return: The affected_session_count of this OpsFailureCategory.
        :rtype: int
        """
        return self._affected_session_count

    @affected_session_count.setter
    def affected_session_count(self, affected_session_count):
        r"""Sets the affected_session_count of this OpsFailureCategory.

        **参数解释：** 故障影响的会话个数。  **取值范围：** 大小为0到10000。

        :param affected_session_count: The affected_session_count of this OpsFailureCategory.
        :type affected_session_count: int
        """
        self._affected_session_count = affected_session_count

    @property
    def sub_categories(self):
        r"""Gets the sub_categories of this OpsFailureCategory.

        **参数解释：** 子故障类别列表。  **取值范围：** 长度0-100的数组。

        :return: The sub_categories of this OpsFailureCategory.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureSubCategory`]
        """
        return self._sub_categories

    @sub_categories.setter
    def sub_categories(self, sub_categories):
        r"""Sets the sub_categories of this OpsFailureCategory.

        **参数解释：** 子故障类别列表。  **取值范围：** 长度0-100的数组。

        :param sub_categories: The sub_categories of this OpsFailureCategory.
        :type sub_categories: list[:class:`huaweicloudsdkagentarts.v1.OpsFailureSubCategory`]
        """
        self._sub_categories = sub_categories

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
        if not isinstance(other, OpsFailureCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
