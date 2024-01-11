# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSchemasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'database_name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'keywords': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'database_name': 'database_name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'keywords': 'keywords',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, cluster_id=None, database_name=None, sort_key=None, sort_dir=None, keywords=None, limit=None, offset=None):
        """ListSchemasRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param database_name: 数据库名称
        :type database_name: str
        :param sort_key: 排序字段
        :type sort_key: str
        :param sort_dir: 排序字段
        :type sort_dir: str
        :param keywords: 查询关键词
        :type keywords: str
        :param limit: 查询条数
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        """
        
        

        self._cluster_id = None
        self._database_name = None
        self._sort_key = None
        self._sort_dir = None
        self._keywords = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.database_name = database_name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if keywords is not None:
            self.keywords = keywords
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListSchemasRequest.

        集群ID

        :return: The cluster_id of this ListSchemasRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListSchemasRequest.

        集群ID

        :param cluster_id: The cluster_id of this ListSchemasRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def database_name(self):
        """Gets the database_name of this ListSchemasRequest.

        数据库名称

        :return: The database_name of this ListSchemasRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListSchemasRequest.

        数据库名称

        :param database_name: The database_name of this ListSchemasRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def sort_key(self):
        """Gets the sort_key of this ListSchemasRequest.

        排序字段

        :return: The sort_key of this ListSchemasRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListSchemasRequest.

        排序字段

        :param sort_key: The sort_key of this ListSchemasRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListSchemasRequest.

        排序字段

        :return: The sort_dir of this ListSchemasRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListSchemasRequest.

        排序字段

        :param sort_dir: The sort_dir of this ListSchemasRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def keywords(self):
        """Gets the keywords of this ListSchemasRequest.

        查询关键词

        :return: The keywords of this ListSchemasRequest.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this ListSchemasRequest.

        查询关键词

        :param keywords: The keywords of this ListSchemasRequest.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def limit(self):
        """Gets the limit of this ListSchemasRequest.

        查询条数

        :return: The limit of this ListSchemasRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSchemasRequest.

        查询条数

        :param limit: The limit of this ListSchemasRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSchemasRequest.

        偏移量

        :return: The offset of this ListSchemasRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSchemasRequest.

        偏移量

        :param offset: The offset of this ListSchemasRequest.
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
        if not isinstance(other, ListSchemasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
