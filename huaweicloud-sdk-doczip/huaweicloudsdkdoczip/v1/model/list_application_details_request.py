# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'query_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'tenant_id': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'query_type': 'query_type',
        'offset': 'offset',
        'limit': 'limit',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, application_id=None, query_type=None, offset=None, limit=None, tenant_id=None):
        r"""ListApplicationDetailsRequest

        The model defined in huaweicloud sdk

        :param application_id: **参数解释**： 应用ID。 **约束限制**： 不涉及。 **取值范围**： [1-256]个字符。 **默认取值**： 不涉及。
        :type application_id: str
        :param query_type: **参数解释**： 查询类型。 **约束限制**： 不涉及。 **取值范围**： - 0：应用基本信息。 - 1：系统配置信息。 - 2：文档块信息。 - 3：发布信息。 - 4：所有信息 **默认取值**： 0。
        :type query_type: str
        :param offset: **参数解释**： 页码。 **约束限制**： 仅当query_type为3或者4时该字段有效。 **取值范围**： 不涉及。 **默认取值**： 1。
        :type offset: int
        :param limit: **参数解释**： 单页数量。 **约束限制**： 仅当query_type为3或者4时该字段有效。 **取值范围**： [1-100]。 **默认取值**： 20。
        :type limit: int
        :param tenant_id: **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。
        :type tenant_id: str
        """
        
        

        self._application_id = None
        self._query_type = None
        self._offset = None
        self._limit = None
        self._tenant_id = None
        self.discriminator = None

        self.application_id = application_id
        if query_type is not None:
            self.query_type = query_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.tenant_id = tenant_id

    @property
    def application_id(self):
        r"""Gets the application_id of this ListApplicationDetailsRequest.

        **参数解释**： 应用ID。 **约束限制**： 不涉及。 **取值范围**： [1-256]个字符。 **默认取值**： 不涉及。

        :return: The application_id of this ListApplicationDetailsRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ListApplicationDetailsRequest.

        **参数解释**： 应用ID。 **约束限制**： 不涉及。 **取值范围**： [1-256]个字符。 **默认取值**： 不涉及。

        :param application_id: The application_id of this ListApplicationDetailsRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def query_type(self):
        r"""Gets the query_type of this ListApplicationDetailsRequest.

        **参数解释**： 查询类型。 **约束限制**： 不涉及。 **取值范围**： - 0：应用基本信息。 - 1：系统配置信息。 - 2：文档块信息。 - 3：发布信息。 - 4：所有信息 **默认取值**： 0。

        :return: The query_type of this ListApplicationDetailsRequest.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this ListApplicationDetailsRequest.

        **参数解释**： 查询类型。 **约束限制**： 不涉及。 **取值范围**： - 0：应用基本信息。 - 1：系统配置信息。 - 2：文档块信息。 - 3：发布信息。 - 4：所有信息 **默认取值**： 0。

        :param query_type: The query_type of this ListApplicationDetailsRequest.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def offset(self):
        r"""Gets the offset of this ListApplicationDetailsRequest.

        **参数解释**： 页码。 **约束限制**： 仅当query_type为3或者4时该字段有效。 **取值范围**： 不涉及。 **默认取值**： 1。

        :return: The offset of this ListApplicationDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListApplicationDetailsRequest.

        **参数解释**： 页码。 **约束限制**： 仅当query_type为3或者4时该字段有效。 **取值范围**： 不涉及。 **默认取值**： 1。

        :param offset: The offset of this ListApplicationDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListApplicationDetailsRequest.

        **参数解释**： 单页数量。 **约束限制**： 仅当query_type为3或者4时该字段有效。 **取值范围**： [1-100]。 **默认取值**： 20。

        :return: The limit of this ListApplicationDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListApplicationDetailsRequest.

        **参数解释**： 单页数量。 **约束限制**： 仅当query_type为3或者4时该字段有效。 **取值范围**： [1-100]。 **默认取值**： 20。

        :param limit: The limit of this ListApplicationDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ListApplicationDetailsRequest.

        **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。

        :return: The tenant_id of this ListApplicationDetailsRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ListApplicationDetailsRequest.

        **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。

        :param tenant_id: The tenant_id of this ListApplicationDetailsRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, ListApplicationDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
