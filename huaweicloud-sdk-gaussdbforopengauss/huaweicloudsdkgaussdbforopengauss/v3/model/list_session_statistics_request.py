# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSessionStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'dimension': 'str',
        'offset': 'int',
        'limit': 'int',
        'order_field': 'str',
        'order': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'dimension': 'dimension',
        'offset': 'offset',
        'limit': 'limit',
        'order_field': 'order_field',
        'order': 'order'
    }

    def __init__(self, x_language=None, instance_id=None, dimension=None, offset=None, limit=None, order_field=None, order=None):
        r"""ListSessionStatisticsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**:   - zh-cn   - en-us  **默认取值**: en-us
        :type x_language: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param dimension: **参数解释**  统计维度。 **约束限制**: 不涉及。 **取值范围** - usename：用户名。 - client_addr：访问来源。 - datname：数据库名。  **默认取值**: 不涉及。 
        :type dimension: str
        :param offset: **参数解释** 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围** [0, 2^31-1] **默认取值** 默认为0（偏移0条数据，表示从第一条数据开始查询）。 
        :type offset: int
        :param limit: **参数解释** 查询记录数。 **约束限制**: 不涉及。 **取值范围** [1, 100] **默认取值** 默认为100。 
        :type limit: int
        :param order_field: **参数解释** 实时会话统计排序字段。 **约束限制**: 不涉及。 **取值范围** - active_num：活跃会话数。 - total_num：总会话数。  **默认取值**: 不涉及。 
        :type order_field: str
        :param order: **参数解释** 实时会话统计排序方式。 **约束限制**: 不涉及。 **取值范围** - ASC：根据order_field值升序。 - DESC：根据order_field值降序。  **默认取值** ASC 
        :type order: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._dimension = None
        self._offset = None
        self._limit = None
        self._order_field = None
        self._order = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.dimension = dimension
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_field is not None:
            self.order_field = order_field
        if order is not None:
            self.order = order

    @property
    def x_language(self):
        r"""Gets the x_language of this ListSessionStatisticsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**:   - zh-cn   - en-us  **默认取值**: en-us

        :return: The x_language of this ListSessionStatisticsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListSessionStatisticsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**:   - zh-cn   - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ListSessionStatisticsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSessionStatisticsRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ListSessionStatisticsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSessionStatisticsRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListSessionStatisticsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def dimension(self):
        r"""Gets the dimension of this ListSessionStatisticsRequest.

        **参数解释**  统计维度。 **约束限制**: 不涉及。 **取值范围** - usename：用户名。 - client_addr：访问来源。 - datname：数据库名。  **默认取值**: 不涉及。 

        :return: The dimension of this ListSessionStatisticsRequest.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        r"""Sets the dimension of this ListSessionStatisticsRequest.

        **参数解释**  统计维度。 **约束限制**: 不涉及。 **取值范围** - usename：用户名。 - client_addr：访问来源。 - datname：数据库名。  **默认取值**: 不涉及。 

        :param dimension: The dimension of this ListSessionStatisticsRequest.
        :type dimension: str
        """
        self._dimension = dimension

    @property
    def offset(self):
        r"""Gets the offset of this ListSessionStatisticsRequest.

        **参数解释** 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围** [0, 2^31-1] **默认取值** 默认为0（偏移0条数据，表示从第一条数据开始查询）。 

        :return: The offset of this ListSessionStatisticsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSessionStatisticsRequest.

        **参数解释** 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 不涉及。 **取值范围** [0, 2^31-1] **默认取值** 默认为0（偏移0条数据，表示从第一条数据开始查询）。 

        :param offset: The offset of this ListSessionStatisticsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSessionStatisticsRequest.

        **参数解释** 查询记录数。 **约束限制**: 不涉及。 **取值范围** [1, 100] **默认取值** 默认为100。 

        :return: The limit of this ListSessionStatisticsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSessionStatisticsRequest.

        **参数解释** 查询记录数。 **约束限制**: 不涉及。 **取值范围** [1, 100] **默认取值** 默认为100。 

        :param limit: The limit of this ListSessionStatisticsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_field(self):
        r"""Gets the order_field of this ListSessionStatisticsRequest.

        **参数解释** 实时会话统计排序字段。 **约束限制**: 不涉及。 **取值范围** - active_num：活跃会话数。 - total_num：总会话数。  **默认取值**: 不涉及。 

        :return: The order_field of this ListSessionStatisticsRequest.
        :rtype: str
        """
        return self._order_field

    @order_field.setter
    def order_field(self, order_field):
        r"""Sets the order_field of this ListSessionStatisticsRequest.

        **参数解释** 实时会话统计排序字段。 **约束限制**: 不涉及。 **取值范围** - active_num：活跃会话数。 - total_num：总会话数。  **默认取值**: 不涉及。 

        :param order_field: The order_field of this ListSessionStatisticsRequest.
        :type order_field: str
        """
        self._order_field = order_field

    @property
    def order(self):
        r"""Gets the order of this ListSessionStatisticsRequest.

        **参数解释** 实时会话统计排序方式。 **约束限制**: 不涉及。 **取值范围** - ASC：根据order_field值升序。 - DESC：根据order_field值降序。  **默认取值** ASC 

        :return: The order of this ListSessionStatisticsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListSessionStatisticsRequest.

        **参数解释** 实时会话统计排序方式。 **约束限制**: 不涉及。 **取值范围** - ASC：根据order_field值升序。 - DESC：根据order_field值降序。  **默认取值** ASC 

        :param order: The order of this ListSessionStatisticsRequest.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ListSessionStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
