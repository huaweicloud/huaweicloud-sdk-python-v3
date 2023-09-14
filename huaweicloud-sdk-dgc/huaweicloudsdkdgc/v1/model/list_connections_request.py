# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'connection_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'connection_name': 'connectionName'
    }

    def __init__(self, workspace=None, limit=None, offset=None, connection_name=None):
        """ListConnectionsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param limit: 分页参数：每页限定数量。范围[1,100]
        :type limit: int
        :param offset: 分页参数：页数
        :type offset: int
        :param connection_name: 连接名称.
        :type connection_name: str
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._connection_name = None
        self.discriminator = None

        if workspace is not None:
            self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if connection_name is not None:
            self.connection_name = connection_name

    @property
    def workspace(self):
        """Gets the workspace of this ListConnectionsRequest.

        工作空间id

        :return: The workspace of this ListConnectionsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListConnectionsRequest.

        工作空间id

        :param workspace: The workspace of this ListConnectionsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        """Gets the limit of this ListConnectionsRequest.

        分页参数：每页限定数量。范围[1,100]

        :return: The limit of this ListConnectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListConnectionsRequest.

        分页参数：每页限定数量。范围[1,100]

        :param limit: The limit of this ListConnectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListConnectionsRequest.

        分页参数：页数

        :return: The offset of this ListConnectionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListConnectionsRequest.

        分页参数：页数

        :param offset: The offset of this ListConnectionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def connection_name(self):
        """Gets the connection_name of this ListConnectionsRequest.

        连接名称.

        :return: The connection_name of this ListConnectionsRequest.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        """Sets the connection_name of this ListConnectionsRequest.

        连接名称.

        :param connection_name: The connection_name of this ListConnectionsRequest.
        :type connection_name: str
        """
        self._connection_name = connection_name

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
        if not isinstance(other, ListConnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
