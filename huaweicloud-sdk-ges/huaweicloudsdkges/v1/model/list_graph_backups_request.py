# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGraphBackupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'graph_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'graph_id': 'graph_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, graph_id=None, limit=None, offset=None):
        """ListGraphBackupsRequest

        The model defined in huaweicloud sdk

        :param graph_id: 图ID。
        :type graph_id: str
        :param limit: 每页资源数量的最大值，默认为10。
        :type limit: int
        :param offset: 本次请求的起始位置，默认为0。
        :type offset: int
        """
        
        

        self._graph_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.graph_id = graph_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def graph_id(self):
        """Gets the graph_id of this ListGraphBackupsRequest.

        图ID。

        :return: The graph_id of this ListGraphBackupsRequest.
        :rtype: str
        """
        return self._graph_id

    @graph_id.setter
    def graph_id(self, graph_id):
        """Sets the graph_id of this ListGraphBackupsRequest.

        图ID。

        :param graph_id: The graph_id of this ListGraphBackupsRequest.
        :type graph_id: str
        """
        self._graph_id = graph_id

    @property
    def limit(self):
        """Gets the limit of this ListGraphBackupsRequest.

        每页资源数量的最大值，默认为10。

        :return: The limit of this ListGraphBackupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListGraphBackupsRequest.

        每页资源数量的最大值，默认为10。

        :param limit: The limit of this ListGraphBackupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListGraphBackupsRequest.

        本次请求的起始位置，默认为0。

        :return: The offset of this ListGraphBackupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListGraphBackupsRequest.

        本次请求的起始位置，默认为0。

        :param offset: The offset of this ListGraphBackupsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListGraphBackupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
