# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'source_servers': 'list[SourceServersResponseBody]'
    }

    attribute_map = {
        'count': 'count',
        'source_servers': 'source_servers'
    }

    def __init__(self, count=None, source_servers=None):
        """ListServersResponse

        The model defined in huaweicloud sdk

        :param count: 符合查询条件的源端总数量，不受limit和offset影响
        :type count: int
        :param source_servers: 批量查询的源端服务器详列表
        :type source_servers: list[:class:`huaweicloudsdksms.v3.SourceServersResponseBody`]
        """
        
        super(ListServersResponse, self).__init__()

        self._count = None
        self._source_servers = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if source_servers is not None:
            self.source_servers = source_servers

    @property
    def count(self):
        """Gets the count of this ListServersResponse.

        符合查询条件的源端总数量，不受limit和offset影响

        :return: The count of this ListServersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListServersResponse.

        符合查询条件的源端总数量，不受limit和offset影响

        :param count: The count of this ListServersResponse.
        :type count: int
        """
        self._count = count

    @property
    def source_servers(self):
        """Gets the source_servers of this ListServersResponse.

        批量查询的源端服务器详列表

        :return: The source_servers of this ListServersResponse.
        :rtype: list[:class:`huaweicloudsdksms.v3.SourceServersResponseBody`]
        """
        return self._source_servers

    @source_servers.setter
    def source_servers(self, source_servers):
        """Sets the source_servers of this ListServersResponse.

        批量查询的源端服务器详列表

        :param source_servers: The source_servers of this ListServersResponse.
        :type source_servers: list[:class:`huaweicloudsdksms.v3.SourceServersResponseBody`]
        """
        self._source_servers = source_servers

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
        if not isinstance(other, ListServersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
