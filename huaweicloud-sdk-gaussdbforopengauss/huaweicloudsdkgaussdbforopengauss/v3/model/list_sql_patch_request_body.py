# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlPatchRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'query_info': 'SqlPatchQueryInfoOption',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'query_info': 'query_info',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, query_info=None, offset=None, limit=None):
        r"""ListSqlPatchRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 实例ID，与路径参数instance_id一致。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param query_info: 
        :type query_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.SqlPatchQueryInfoOption`
        :param offset: **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围**: 大于等于0的整数。 **默认取值**: 0
        :type offset: int
        :param limit: **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: 最小值为1，最大值为1000。 **默认取值**: 20
        :type limit: int
        """
        
        

        self._instance_id = None
        self._query_info = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if query_info is not None:
            self.query_info = query_info
        self.offset = offset
        self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSqlPatchRequestBody.

        **参数解释**: 实例ID，与路径参数instance_id一致。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ListSqlPatchRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSqlPatchRequestBody.

        **参数解释**: 实例ID，与路径参数instance_id一致。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListSqlPatchRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def query_info(self):
        r"""Gets the query_info of this ListSqlPatchRequestBody.

        :return: The query_info of this ListSqlPatchRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.SqlPatchQueryInfoOption`
        """
        return self._query_info

    @query_info.setter
    def query_info(self, query_info):
        r"""Sets the query_info of this ListSqlPatchRequestBody.

        :param query_info: The query_info of this ListSqlPatchRequestBody.
        :type query_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.SqlPatchQueryInfoOption`
        """
        self._query_info = query_info

    @property
    def offset(self):
        r"""Gets the offset of this ListSqlPatchRequestBody.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围**: 大于等于0的整数。 **默认取值**: 0

        :return: The offset of this ListSqlPatchRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSqlPatchRequestBody.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围**: 大于等于0的整数。 **默认取值**: 0

        :param offset: The offset of this ListSqlPatchRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSqlPatchRequestBody.

        **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: 最小值为1，最大值为1000。 **默认取值**: 20

        :return: The limit of this ListSqlPatchRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSqlPatchRequestBody.

        **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: 最小值为1，最大值为1000。 **默认取值**: 20

        :param limit: The limit of this ListSqlPatchRequestBody.
        :type limit: int
        """
        self._limit = limit

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSqlPatchRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
