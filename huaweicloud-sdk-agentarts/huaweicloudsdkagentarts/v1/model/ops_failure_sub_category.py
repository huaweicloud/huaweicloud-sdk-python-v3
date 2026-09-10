# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsFailureSubCategory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_sub_category_name': 'str',
        'affected_session_count': 'int'
    }

    attribute_map = {
        'error_sub_category_name': 'error_sub_category_name',
        'affected_session_count': 'affected_session_count'
    }

    def __init__(self, error_sub_category_name=None, affected_session_count=None):
        r"""OpsFailureSubCategory

        The model defined in huaweicloud sdk

        :param error_sub_category_name: **参数解释：** 故障类别名称。  **取值范围：** 长度1-128个字符。
        :type error_sub_category_name: str
        :param affected_session_count: **参数解释：** 故障影响的会话个数。  **取值范围：** 大小为0到10000。
        :type affected_session_count: int
        """
        
        

        self._error_sub_category_name = None
        self._affected_session_count = None
        self.discriminator = None

        if error_sub_category_name is not None:
            self.error_sub_category_name = error_sub_category_name
        if affected_session_count is not None:
            self.affected_session_count = affected_session_count

    @property
    def error_sub_category_name(self):
        r"""Gets the error_sub_category_name of this OpsFailureSubCategory.

        **参数解释：** 故障类别名称。  **取值范围：** 长度1-128个字符。

        :return: The error_sub_category_name of this OpsFailureSubCategory.
        :rtype: str
        """
        return self._error_sub_category_name

    @error_sub_category_name.setter
    def error_sub_category_name(self, error_sub_category_name):
        r"""Sets the error_sub_category_name of this OpsFailureSubCategory.

        **参数解释：** 故障类别名称。  **取值范围：** 长度1-128个字符。

        :param error_sub_category_name: The error_sub_category_name of this OpsFailureSubCategory.
        :type error_sub_category_name: str
        """
        self._error_sub_category_name = error_sub_category_name

    @property
    def affected_session_count(self):
        r"""Gets the affected_session_count of this OpsFailureSubCategory.

        **参数解释：** 故障影响的会话个数。  **取值范围：** 大小为0到10000。

        :return: The affected_session_count of this OpsFailureSubCategory.
        :rtype: int
        """
        return self._affected_session_count

    @affected_session_count.setter
    def affected_session_count(self, affected_session_count):
        r"""Sets the affected_session_count of this OpsFailureSubCategory.

        **参数解释：** 故障影响的会话个数。  **取值范围：** 大小为0到10000。

        :param affected_session_count: The affected_session_count of this OpsFailureSubCategory.
        :type affected_session_count: int
        """
        self._affected_session_count = affected_session_count

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
        if not isinstance(other, OpsFailureSubCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
