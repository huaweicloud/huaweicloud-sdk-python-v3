# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataconnectionsRequest:

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
        'name': 'str',
        'type': 'str',
        'limit': 'str',
        'offset': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'name': 'name',
        'type': 'type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, name=None, type=None, limit=None, offset=None):
        """ListDataconnectionsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param name: 数据连接名称
        :type name: str
        :param type: 数据连接类型,有HIVE,MYSQL,ORALCLE,DWS,HBASE等。
        :type type: str
        :param limit: 数据条数限制
        :type limit: str
        :param offset: 偏移量
        :type offset: str
        """
        
        

        self._workspace = None
        self._name = None
        self._type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this ListDataconnectionsRequest.

        工作空间id

        :return: The workspace of this ListDataconnectionsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListDataconnectionsRequest.

        工作空间id

        :param workspace: The workspace of this ListDataconnectionsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def name(self):
        """Gets the name of this ListDataconnectionsRequest.

        数据连接名称

        :return: The name of this ListDataconnectionsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDataconnectionsRequest.

        数据连接名称

        :param name: The name of this ListDataconnectionsRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ListDataconnectionsRequest.

        数据连接类型,有HIVE,MYSQL,ORALCLE,DWS,HBASE等。

        :return: The type of this ListDataconnectionsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListDataconnectionsRequest.

        数据连接类型,有HIVE,MYSQL,ORALCLE,DWS,HBASE等。

        :param type: The type of this ListDataconnectionsRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        """Gets the limit of this ListDataconnectionsRequest.

        数据条数限制

        :return: The limit of this ListDataconnectionsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDataconnectionsRequest.

        数据条数限制

        :param limit: The limit of this ListDataconnectionsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDataconnectionsRequest.

        偏移量

        :return: The offset of this ListDataconnectionsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDataconnectionsRequest.

        偏移量

        :param offset: The offset of this ListDataconnectionsRequest.
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
        if not isinstance(other, ListDataconnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
