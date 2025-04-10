# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesSessionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'sessions': 'list[ListInstancesSessionRespondBodySessions]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'sessions': 'sessions'
    }

    def __init__(self, total_count=None, sessions=None):
        r"""ListInstancesSessionResponse

        The model defined in huaweicloud sdk

        :param total_count: 符合查询条件的总会话数。
        :type total_count: int
        :param sessions: 实例会话详细信息列表。
        :type sessions: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesSessionRespondBodySessions`]
        """
        
        super(ListInstancesSessionResponse, self).__init__()

        self._total_count = None
        self._sessions = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if sessions is not None:
            self.sessions = sessions

    @property
    def total_count(self):
        r"""Gets the total_count of this ListInstancesSessionResponse.

        符合查询条件的总会话数。

        :return: The total_count of this ListInstancesSessionResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListInstancesSessionResponse.

        符合查询条件的总会话数。

        :param total_count: The total_count of this ListInstancesSessionResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def sessions(self):
        r"""Gets the sessions of this ListInstancesSessionResponse.

        实例会话详细信息列表。

        :return: The sessions of this ListInstancesSessionResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesSessionRespondBodySessions`]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        r"""Sets the sessions of this ListInstancesSessionResponse.

        实例会话详细信息列表。

        :param sessions: The sessions of this ListInstancesSessionResponse.
        :type sessions: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesSessionRespondBodySessions`]
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
        if not isinstance(other, ListInstancesSessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
