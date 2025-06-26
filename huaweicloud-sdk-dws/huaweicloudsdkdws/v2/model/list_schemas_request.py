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
        r"""ListSchemasRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param database_name: **参数解释**： 数据库名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type database_name: str
        :param sort_key: **参数解释**： 排序字段。 **约束限制**： 不涉及。 **取值范围**： schemaName：模式名称排序。 **默认取值**： 不涉及。
        :type sort_key: str
        :param sort_dir: **参数解释**： 排序字段。 **约束限制**： 不涉及。 **取值范围**： ASC：表示按升序排序。  DESC：表示按降序排序。 **默认取值**： 不涉及。
        :type sort_dir: str
        :param keywords: **参数解释**： 查询关键词。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type keywords: str
        :param limit: **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10
        :type limit: int
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0
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
        r"""Gets the cluster_id of this ListSchemasRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :return: The cluster_id of this ListSchemasRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListSchemasRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ListSchemasRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def database_name(self):
        r"""Gets the database_name of this ListSchemasRequest.

        **参数解释**： 数据库名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The database_name of this ListSchemasRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListSchemasRequest.

        **参数解释**： 数据库名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param database_name: The database_name of this ListSchemasRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListSchemasRequest.

        **参数解释**： 排序字段。 **约束限制**： 不涉及。 **取值范围**： schemaName：模式名称排序。 **默认取值**： 不涉及。

        :return: The sort_key of this ListSchemasRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListSchemasRequest.

        **参数解释**： 排序字段。 **约束限制**： 不涉及。 **取值范围**： schemaName：模式名称排序。 **默认取值**： 不涉及。

        :param sort_key: The sort_key of this ListSchemasRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListSchemasRequest.

        **参数解释**： 排序字段。 **约束限制**： 不涉及。 **取值范围**： ASC：表示按升序排序。  DESC：表示按降序排序。 **默认取值**： 不涉及。

        :return: The sort_dir of this ListSchemasRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListSchemasRequest.

        **参数解释**： 排序字段。 **约束限制**： 不涉及。 **取值范围**： ASC：表示按升序排序。  DESC：表示按降序排序。 **默认取值**： 不涉及。

        :param sort_dir: The sort_dir of this ListSchemasRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def keywords(self):
        r"""Gets the keywords of this ListSchemasRequest.

        **参数解释**： 查询关键词。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The keywords of this ListSchemasRequest.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this ListSchemasRequest.

        **参数解释**： 查询关键词。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param keywords: The keywords of this ListSchemasRequest.
        :type keywords: str
        """
        self._keywords = keywords

    @property
    def limit(self):
        r"""Gets the limit of this ListSchemasRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10

        :return: The limit of this ListSchemasRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSchemasRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10

        :param limit: The limit of this ListSchemasRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSchemasRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :return: The offset of this ListSchemasRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSchemasRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

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
