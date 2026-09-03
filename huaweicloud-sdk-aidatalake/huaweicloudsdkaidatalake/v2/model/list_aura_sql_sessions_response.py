# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuraSqlSessionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'next_marker': 'str',
        'total': 'int',
        'sessions': 'list[SqlSessionInfo]'
    }

    attribute_map = {
        'next_marker': 'next_marker',
        'total': 'total',
        'sessions': 'sessions'
    }

    def __init__(self, next_marker=None, total=None, sessions=None):
        r"""ListAuraSqlSessionsResponse

        The model defined in huaweicloud sdk

        :param next_marker: **参数解释**：下一页查询marker值，若为空表示当前已是最后一页。 **取值范围**：不涉及。
        :type next_marker: str
        :param total: **参数解释**：总数。 **取值范围**：1~2147483647。
        :type total: int
        :param sessions: **参数解释**：Session列表。
        :type sessions: list[:class:`huaweicloudsdkaidatalake.v2.SqlSessionInfo`]
        """
        
        super().__init__()

        self._next_marker = None
        self._total = None
        self._sessions = None
        self.discriminator = None

        if next_marker is not None:
            self.next_marker = next_marker
        if total is not None:
            self.total = total
        if sessions is not None:
            self.sessions = sessions

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListAuraSqlSessionsResponse.

        **参数解释**：下一页查询marker值，若为空表示当前已是最后一页。 **取值范围**：不涉及。

        :return: The next_marker of this ListAuraSqlSessionsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListAuraSqlSessionsResponse.

        **参数解释**：下一页查询marker值，若为空表示当前已是最后一页。 **取值范围**：不涉及。

        :param next_marker: The next_marker of this ListAuraSqlSessionsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def total(self):
        r"""Gets the total of this ListAuraSqlSessionsResponse.

        **参数解释**：总数。 **取值范围**：1~2147483647。

        :return: The total of this ListAuraSqlSessionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAuraSqlSessionsResponse.

        **参数解释**：总数。 **取值范围**：1~2147483647。

        :param total: The total of this ListAuraSqlSessionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def sessions(self):
        r"""Gets the sessions of this ListAuraSqlSessionsResponse.

        **参数解释**：Session列表。

        :return: The sessions of this ListAuraSqlSessionsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.SqlSessionInfo`]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        r"""Sets the sessions of this ListAuraSqlSessionsResponse.

        **参数解释**：Session列表。

        :param sessions: The sessions of this ListAuraSqlSessionsResponse.
        :type sessions: list[:class:`huaweicloudsdkaidatalake.v2.SqlSessionInfo`]
        """
        self._sessions = sessions

    def to_dict(self):
        import warnings
        warnings.warn("ListAuraSqlSessionsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAuraSqlSessionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
