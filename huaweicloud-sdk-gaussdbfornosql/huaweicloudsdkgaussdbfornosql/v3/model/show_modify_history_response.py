# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowModifyHistoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'histories': 'list[ConfigurationHistoryRsp]',
        'total_count': 'int'
    }

    attribute_map = {
        'histories': 'histories',
        'total_count': 'total_count'
    }

    def __init__(self, histories=None, total_count=None):
        r"""ShowModifyHistoryResponse

        The model defined in huaweicloud sdk

        :param histories: 实例参数的修改历史列表。
        :type histories: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ConfigurationHistoryRsp`]
        :param total_count: **参数解释：** 参数修改历史记录总条数。 **约束限制：** 默认返回参数历史修改记录总条数。若为参数名搜索，返回符合要求的记录总条数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type total_count: int
        """
        
        super().__init__()

        self._histories = None
        self._total_count = None
        self.discriminator = None

        if histories is not None:
            self.histories = histories
        if total_count is not None:
            self.total_count = total_count

    @property
    def histories(self):
        r"""Gets the histories of this ShowModifyHistoryResponse.

        实例参数的修改历史列表。

        :return: The histories of this ShowModifyHistoryResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ConfigurationHistoryRsp`]
        """
        return self._histories

    @histories.setter
    def histories(self, histories):
        r"""Sets the histories of this ShowModifyHistoryResponse.

        实例参数的修改历史列表。

        :param histories: The histories of this ShowModifyHistoryResponse.
        :type histories: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ConfigurationHistoryRsp`]
        """
        self._histories = histories

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowModifyHistoryResponse.

        **参数解释：** 参数修改历史记录总条数。 **约束限制：** 默认返回参数历史修改记录总条数。若为参数名搜索，返回符合要求的记录总条数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The total_count of this ShowModifyHistoryResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowModifyHistoryResponse.

        **参数解释：** 参数修改历史记录总条数。 **约束限制：** 默认返回参数历史修改记录总条数。若为参数名搜索，返回符合要求的记录总条数。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param total_count: The total_count of this ShowModifyHistoryResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowModifyHistoryResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowModifyHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
