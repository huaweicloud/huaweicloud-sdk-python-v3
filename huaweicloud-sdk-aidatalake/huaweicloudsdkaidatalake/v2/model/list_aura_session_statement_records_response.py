# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuraSessionStatementRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'records': 'list[SessionStatementRecord]',
        'current_count': 'int',
        'next_marker': 'str'
    }

    attribute_map = {
        'records': 'records',
        'current_count': 'current_count',
        'next_marker': 'next_marker'
    }

    def __init__(self, records=None, current_count=None, next_marker=None):
        r"""ListAuraSessionStatementRecordsResponse

        The model defined in huaweicloud sdk

        :param records: **参数解释**：本次查询记录。 **取值范围**：不涉及。
        :type records: list[:class:`huaweicloudsdkaidatalake.v2.SessionStatementRecord`]
        :param current_count: **参数解释**：本次查询记录总数。 **取值范围**：1~2147483647。
        :type current_count: int
        :param next_marker: **参数解释**：下一页查询marker值，若为空表示当前已是最后一页。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。
        :type next_marker: str
        """
        
        super().__init__()

        self._records = None
        self._current_count = None
        self._next_marker = None
        self.discriminator = None

        if records is not None:
            self.records = records
        if current_count is not None:
            self.current_count = current_count
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def records(self):
        r"""Gets the records of this ListAuraSessionStatementRecordsResponse.

        **参数解释**：本次查询记录。 **取值范围**：不涉及。

        :return: The records of this ListAuraSessionStatementRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.SessionStatementRecord`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListAuraSessionStatementRecordsResponse.

        **参数解释**：本次查询记录。 **取值范围**：不涉及。

        :param records: The records of this ListAuraSessionStatementRecordsResponse.
        :type records: list[:class:`huaweicloudsdkaidatalake.v2.SessionStatementRecord`]
        """
        self._records = records

    @property
    def current_count(self):
        r"""Gets the current_count of this ListAuraSessionStatementRecordsResponse.

        **参数解释**：本次查询记录总数。 **取值范围**：1~2147483647。

        :return: The current_count of this ListAuraSessionStatementRecordsResponse.
        :rtype: int
        """
        return self._current_count

    @current_count.setter
    def current_count(self, current_count):
        r"""Sets the current_count of this ListAuraSessionStatementRecordsResponse.

        **参数解释**：本次查询记录总数。 **取值范围**：1~2147483647。

        :param current_count: The current_count of this ListAuraSessionStatementRecordsResponse.
        :type current_count: int
        """
        self._current_count = current_count

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListAuraSessionStatementRecordsResponse.

        **参数解释**：下一页查询marker值，若为空表示当前已是最后一页。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。

        :return: The next_marker of this ListAuraSessionStatementRecordsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListAuraSessionStatementRecordsResponse.

        **参数解释**：下一页查询marker值，若为空表示当前已是最后一页。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。

        :param next_marker: The next_marker of this ListAuraSessionStatementRecordsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    def to_dict(self):
        import warnings
        warnings.warn("ListAuraSessionStatementRecordsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAuraSessionStatementRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
