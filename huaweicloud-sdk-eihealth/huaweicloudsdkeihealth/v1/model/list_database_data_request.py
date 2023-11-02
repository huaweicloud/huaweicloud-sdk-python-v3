# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'limit': 'int',
        'query': 'str',
        'offset': 'int',
        'database_id': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'limit': 'limit',
        'query': 'query',
        'offset': 'offset',
        'database_id': 'database_id',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, eihealth_project_id=None, limit=None, query=None, offset=None, database_id=None, sort_key=None, sort_dir=None):
        """ListDatabaseDataRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param limit: 返回记录限制
        :type limit: int
        :param query: 查询条件，例如START::gte::1|END::lte::5|TAG::like::a
        :type query: str
        :param offset: 偏移量
        :type offset: int
        :param database_id: 数据库实例id
        :type database_id: str
        :param sort_key: 排序字段
        :type sort_key: str
        :param sort_dir: 排序方向，升序或降序，即ASC 和DESC
        :type sort_dir: str
        """
        
        

        self._eihealth_project_id = None
        self._limit = None
        self._query = None
        self._offset = None
        self._database_id = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        if limit is not None:
            self.limit = limit
        if query is not None:
            self.query = query
        if offset is not None:
            self.offset = offset
        self.database_id = database_id
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ListDatabaseDataRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ListDatabaseDataRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ListDatabaseDataRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ListDatabaseDataRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def limit(self):
        """Gets the limit of this ListDatabaseDataRequest.

        返回记录限制

        :return: The limit of this ListDatabaseDataRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDatabaseDataRequest.

        返回记录限制

        :param limit: The limit of this ListDatabaseDataRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def query(self):
        """Gets the query of this ListDatabaseDataRequest.

        查询条件，例如START::gte::1|END::lte::5|TAG::like::a

        :return: The query of this ListDatabaseDataRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ListDatabaseDataRequest.

        查询条件，例如START::gte::1|END::lte::5|TAG::like::a

        :param query: The query of this ListDatabaseDataRequest.
        :type query: str
        """
        self._query = query

    @property
    def offset(self):
        """Gets the offset of this ListDatabaseDataRequest.

        偏移量

        :return: The offset of this ListDatabaseDataRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDatabaseDataRequest.

        偏移量

        :param offset: The offset of this ListDatabaseDataRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def database_id(self):
        """Gets the database_id of this ListDatabaseDataRequest.

        数据库实例id

        :return: The database_id of this ListDatabaseDataRequest.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """Sets the database_id of this ListDatabaseDataRequest.

        数据库实例id

        :param database_id: The database_id of this ListDatabaseDataRequest.
        :type database_id: str
        """
        self._database_id = database_id

    @property
    def sort_key(self):
        """Gets the sort_key of this ListDatabaseDataRequest.

        排序字段

        :return: The sort_key of this ListDatabaseDataRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListDatabaseDataRequest.

        排序字段

        :param sort_key: The sort_key of this ListDatabaseDataRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListDatabaseDataRequest.

        排序方向，升序或降序，即ASC 和DESC

        :return: The sort_dir of this ListDatabaseDataRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListDatabaseDataRequest.

        排序方向，升序或降序，即ASC 和DESC

        :param sort_dir: The sort_dir of this ListDatabaseDataRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListDatabaseDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
