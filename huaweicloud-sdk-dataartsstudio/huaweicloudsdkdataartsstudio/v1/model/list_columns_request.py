# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListColumnsRequest:

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
        'connection_id': 'str',
        'table_id': 'str',
        'limit': 'str',
        'offset': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'connection_id': 'connection_id',
        'table_id': 'table_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, connection_id=None, table_id=None, limit=None, offset=None):
        """ListColumnsRequest

        The model defined in huaweicloud sdk

        :param workspace: 数据所在空间的id值
        :type workspace: str
        :param connection_id: 数据连接id
        :type connection_id: str
        :param table_id: 表id
        :type table_id: str
        :param limit: 数据条数限制
        :type limit: str
        :param offset: 偏移量
        :type offset: str
        """
        
        

        self._workspace = None
        self._connection_id = None
        self._table_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        self.connection_id = connection_id
        self.table_id = table_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this ListColumnsRequest.

        数据所在空间的id值

        :return: The workspace of this ListColumnsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListColumnsRequest.

        数据所在空间的id值

        :param workspace: The workspace of this ListColumnsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def connection_id(self):
        """Gets the connection_id of this ListColumnsRequest.

        数据连接id

        :return: The connection_id of this ListColumnsRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this ListColumnsRequest.

        数据连接id

        :param connection_id: The connection_id of this ListColumnsRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def table_id(self):
        """Gets the table_id of this ListColumnsRequest.

        表id

        :return: The table_id of this ListColumnsRequest.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this ListColumnsRequest.

        表id

        :param table_id: The table_id of this ListColumnsRequest.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def limit(self):
        """Gets the limit of this ListColumnsRequest.

        数据条数限制

        :return: The limit of this ListColumnsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListColumnsRequest.

        数据条数限制

        :param limit: The limit of this ListColumnsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListColumnsRequest.

        偏移量

        :return: The offset of this ListColumnsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListColumnsRequest.

        偏移量

        :param offset: The offset of this ListColumnsRequest.
        :type offset: str
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
        if not isinstance(other, ListColumnsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
