# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TraceTopologyLine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_node_id': 'int',
        'end_node_id': 'int',
        'span_id': 'str',
        'client_info': 'TraceTopologyLineInfo',
        'server_info': 'TraceTopologyLineInfo',
        'id': 'str',
        'hint': 'str'
    }

    attribute_map = {
        'start_node_id': 'start_node_id',
        'end_node_id': 'end_node_id',
        'span_id': 'span_id',
        'client_info': 'client_info',
        'server_info': 'server_info',
        'id': 'id',
        'hint': 'hint'
    }

    def __init__(self, start_node_id=None, end_node_id=None, span_id=None, client_info=None, server_info=None, id=None, hint=None):
        """TraceTopologyLine

        The model defined in huaweicloud sdk

        :param start_node_id: 开始节点id。
        :type start_node_id: int
        :param end_node_id: 结束节点id。
        :type end_node_id: int
        :param span_id: 调用跨度id。
        :type span_id: str
        :param client_info: 
        :type client_info: :class:`huaweicloudsdkapm.v1.TraceTopologyLineInfo`
        :param server_info: 
        :type server_info: :class:`huaweicloudsdkapm.v1.TraceTopologyLineInfo`
        :param id: id。
        :type id: str
        :param hint: 获取一条线的提示信息。
        :type hint: str
        """
        
        

        self._start_node_id = None
        self._end_node_id = None
        self._span_id = None
        self._client_info = None
        self._server_info = None
        self._id = None
        self._hint = None
        self.discriminator = None

        if start_node_id is not None:
            self.start_node_id = start_node_id
        if end_node_id is not None:
            self.end_node_id = end_node_id
        if span_id is not None:
            self.span_id = span_id
        if client_info is not None:
            self.client_info = client_info
        if server_info is not None:
            self.server_info = server_info
        if id is not None:
            self.id = id
        if hint is not None:
            self.hint = hint

    @property
    def start_node_id(self):
        """Gets the start_node_id of this TraceTopologyLine.

        开始节点id。

        :return: The start_node_id of this TraceTopologyLine.
        :rtype: int
        """
        return self._start_node_id

    @start_node_id.setter
    def start_node_id(self, start_node_id):
        """Sets the start_node_id of this TraceTopologyLine.

        开始节点id。

        :param start_node_id: The start_node_id of this TraceTopologyLine.
        :type start_node_id: int
        """
        self._start_node_id = start_node_id

    @property
    def end_node_id(self):
        """Gets the end_node_id of this TraceTopologyLine.

        结束节点id。

        :return: The end_node_id of this TraceTopologyLine.
        :rtype: int
        """
        return self._end_node_id

    @end_node_id.setter
    def end_node_id(self, end_node_id):
        """Sets the end_node_id of this TraceTopologyLine.

        结束节点id。

        :param end_node_id: The end_node_id of this TraceTopologyLine.
        :type end_node_id: int
        """
        self._end_node_id = end_node_id

    @property
    def span_id(self):
        """Gets the span_id of this TraceTopologyLine.

        调用跨度id。

        :return: The span_id of this TraceTopologyLine.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        """Sets the span_id of this TraceTopologyLine.

        调用跨度id。

        :param span_id: The span_id of this TraceTopologyLine.
        :type span_id: str
        """
        self._span_id = span_id

    @property
    def client_info(self):
        """Gets the client_info of this TraceTopologyLine.

        :return: The client_info of this TraceTopologyLine.
        :rtype: :class:`huaweicloudsdkapm.v1.TraceTopologyLineInfo`
        """
        return self._client_info

    @client_info.setter
    def client_info(self, client_info):
        """Sets the client_info of this TraceTopologyLine.

        :param client_info: The client_info of this TraceTopologyLine.
        :type client_info: :class:`huaweicloudsdkapm.v1.TraceTopologyLineInfo`
        """
        self._client_info = client_info

    @property
    def server_info(self):
        """Gets the server_info of this TraceTopologyLine.

        :return: The server_info of this TraceTopologyLine.
        :rtype: :class:`huaweicloudsdkapm.v1.TraceTopologyLineInfo`
        """
        return self._server_info

    @server_info.setter
    def server_info(self, server_info):
        """Sets the server_info of this TraceTopologyLine.

        :param server_info: The server_info of this TraceTopologyLine.
        :type server_info: :class:`huaweicloudsdkapm.v1.TraceTopologyLineInfo`
        """
        self._server_info = server_info

    @property
    def id(self):
        """Gets the id of this TraceTopologyLine.

        id。

        :return: The id of this TraceTopologyLine.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TraceTopologyLine.

        id。

        :param id: The id of this TraceTopologyLine.
        :type id: str
        """
        self._id = id

    @property
    def hint(self):
        """Gets the hint of this TraceTopologyLine.

        获取一条线的提示信息。

        :return: The hint of this TraceTopologyLine.
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        """Sets the hint of this TraceTopologyLine.

        获取一条线的提示信息。

        :param hint: The hint of this TraceTopologyLine.
        :type hint: str
        """
        self._hint = hint

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
        if not isinstance(other, TraceTopologyLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
