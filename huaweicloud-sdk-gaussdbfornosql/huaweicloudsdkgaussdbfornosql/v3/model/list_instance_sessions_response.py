# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceSessionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_sessions': 'list[ListNodeSessionsResult]'
    }

    attribute_map = {
        'node_sessions': 'node_sessions'
    }

    def __init__(self, node_sessions=None):
        r"""ListInstanceSessionsResponse

        The model defined in huaweicloud sdk

        :param node_sessions: 节点的会话信息列表。
        :type node_sessions: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListNodeSessionsResult`]
        """
        
        super(ListInstanceSessionsResponse, self).__init__()

        self._node_sessions = None
        self.discriminator = None

        if node_sessions is not None:
            self.node_sessions = node_sessions

    @property
    def node_sessions(self):
        r"""Gets the node_sessions of this ListInstanceSessionsResponse.

        节点的会话信息列表。

        :return: The node_sessions of this ListInstanceSessionsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListNodeSessionsResult`]
        """
        return self._node_sessions

    @node_sessions.setter
    def node_sessions(self, node_sessions):
        r"""Sets the node_sessions of this ListInstanceSessionsResponse.

        节点的会话信息列表。

        :param node_sessions: The node_sessions of this ListInstanceSessionsResponse.
        :type node_sessions: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListNodeSessionsResult`]
        """
        self._node_sessions = node_sessions

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
        if not isinstance(other, ListInstanceSessionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
