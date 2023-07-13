# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistorySessionsResponse(SdkResponse):

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
        'session_list': 'list[OperateHistorySession]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'session_list': 'session_list'
    }

    def __init__(self, total_count=None, session_list=None):
        """ListHistorySessionsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总记录数
        :type total_count: int
        :param session_list: 会话列表
        :type session_list: list[:class:`huaweicloudsdkosm.v2.OperateHistorySession`]
        """
        
        super(ListHistorySessionsResponse, self).__init__()

        self._total_count = None
        self._session_list = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if session_list is not None:
            self.session_list = session_list

    @property
    def total_count(self):
        """Gets the total_count of this ListHistorySessionsResponse.

        总记录数

        :return: The total_count of this ListHistorySessionsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListHistorySessionsResponse.

        总记录数

        :param total_count: The total_count of this ListHistorySessionsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def session_list(self):
        """Gets the session_list of this ListHistorySessionsResponse.

        会话列表

        :return: The session_list of this ListHistorySessionsResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.OperateHistorySession`]
        """
        return self._session_list

    @session_list.setter
    def session_list(self, session_list):
        """Sets the session_list of this ListHistorySessionsResponse.

        会话列表

        :param session_list: The session_list of this ListHistorySessionsResponse.
        :type session_list: list[:class:`huaweicloudsdkosm.v2.OperateHistorySession`]
        """
        self._session_list = session_list

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
        if not isinstance(other, ListHistorySessionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
