# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodeSessionsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'total_count': 'int',
        'sessions': 'list[ListNodeSessionsResultSessions]'
    }

    attribute_map = {
        'node_id': 'node_id',
        'total_count': 'total_count',
        'sessions': 'sessions'
    }

    def __init__(self, node_id=None, total_count=None, sessions=None):
        r"""ListNodeSessionsResult

        The model defined in huaweicloud sdk

        :param node_id: 节点ID。
        :type node_id: str
        :param total_count: 总会话数。
        :type total_count: int
        :param sessions: 节点会话详细信息列表。
        :type sessions: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListNodeSessionsResultSessions`]
        """
        
        

        self._node_id = None
        self._total_count = None
        self._sessions = None
        self.discriminator = None

        self.node_id = node_id
        if total_count is not None:
            self.total_count = total_count
        if sessions is not None:
            self.sessions = sessions

    @property
    def node_id(self):
        r"""Gets the node_id of this ListNodeSessionsResult.

        节点ID。

        :return: The node_id of this ListNodeSessionsResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListNodeSessionsResult.

        节点ID。

        :param node_id: The node_id of this ListNodeSessionsResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def total_count(self):
        r"""Gets the total_count of this ListNodeSessionsResult.

        总会话数。

        :return: The total_count of this ListNodeSessionsResult.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListNodeSessionsResult.

        总会话数。

        :param total_count: The total_count of this ListNodeSessionsResult.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def sessions(self):
        r"""Gets the sessions of this ListNodeSessionsResult.

        节点会话详细信息列表。

        :return: The sessions of this ListNodeSessionsResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListNodeSessionsResultSessions`]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        r"""Sets the sessions of this ListNodeSessionsResult.

        节点会话详细信息列表。

        :param sessions: The sessions of this ListNodeSessionsResult.
        :type sessions: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListNodeSessionsResultSessions`]
        """
        self._sessions = sessions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListNodeSessionsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
