# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRedistributionSchemaRequest:

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
        'db_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'schema_name': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'db_name': 'db_name',
        'limit': 'limit',
        'offset': 'offset',
        'schema_name': 'schema_name'
    }

    def __init__(self, cluster_id=None, db_name=None, limit=None, offset=None, schema_name=None):
        r"""ListRedistributionSchemaRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param db_name: **参数解释**： 分页偏移量。 **约束限制**： 不涉及。 **取值范围**： ^[a-zA-Z0-9\\u4e00-\\u9fa5_.+&#x3D; :@!#-]{0,255}$ **默认取值**： null
        :type db_name: str
        :param limit: **参数解释**： 分页条数。 **约束限制**： 不涉及。 **取值范围**： 有效值：大于等于1。 **默认取值**： 10
        :type limit: int
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 有效值：大于等于0。 **默认取值**： 0
        :type offset: int
        :param schema_name: **参数解释**： schema名称。 **约束限制**： 不涉及。 **取值范围**： ^[a-zA-Z0-9\\u4e00-\\u9fa5_.+&#x3D; ,:@!#-]{0,2048}$ **默认取值**： null
        :type schema_name: str
        """
        
        

        self._cluster_id = None
        self._db_name = None
        self._limit = None
        self._offset = None
        self._schema_name = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.db_name = db_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if schema_name is not None:
            self.schema_name = schema_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListRedistributionSchemaRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The cluster_id of this ListRedistributionSchemaRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListRedistributionSchemaRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this ListRedistributionSchemaRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def db_name(self):
        r"""Gets the db_name of this ListRedistributionSchemaRequest.

        **参数解释**： 分页偏移量。 **约束限制**： 不涉及。 **取值范围**： ^[a-zA-Z0-9\\u4e00-\\u9fa5_.+= :@!#-]{0,255}$ **默认取值**： null

        :return: The db_name of this ListRedistributionSchemaRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListRedistributionSchemaRequest.

        **参数解释**： 分页偏移量。 **约束限制**： 不涉及。 **取值范围**： ^[a-zA-Z0-9\\u4e00-\\u9fa5_.+= :@!#-]{0,255}$ **默认取值**： null

        :param db_name: The db_name of this ListRedistributionSchemaRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def limit(self):
        r"""Gets the limit of this ListRedistributionSchemaRequest.

        **参数解释**： 分页条数。 **约束限制**： 不涉及。 **取值范围**： 有效值：大于等于1。 **默认取值**： 10

        :return: The limit of this ListRedistributionSchemaRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRedistributionSchemaRequest.

        **参数解释**： 分页条数。 **约束限制**： 不涉及。 **取值范围**： 有效值：大于等于1。 **默认取值**： 10

        :param limit: The limit of this ListRedistributionSchemaRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListRedistributionSchemaRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 有效值：大于等于0。 **默认取值**： 0

        :return: The offset of this ListRedistributionSchemaRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRedistributionSchemaRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 有效值：大于等于0。 **默认取值**： 0

        :param offset: The offset of this ListRedistributionSchemaRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ListRedistributionSchemaRequest.

        **参数解释**： schema名称。 **约束限制**： 不涉及。 **取值范围**： ^[a-zA-Z0-9\\u4e00-\\u9fa5_.+= ,:@!#-]{0,2048}$ **默认取值**： null

        :return: The schema_name of this ListRedistributionSchemaRequest.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ListRedistributionSchemaRequest.

        **参数解释**： schema名称。 **约束限制**： 不涉及。 **取值范围**： ^[a-zA-Z0-9\\u4e00-\\u9fa5_.+= ,:@!#-]{0,2048}$ **默认取值**： null

        :param schema_name: The schema_name of this ListRedistributionSchemaRequest.
        :type schema_name: str
        """
        self._schema_name = schema_name

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
        if not isinstance(other, ListRedistributionSchemaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
