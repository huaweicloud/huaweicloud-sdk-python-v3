# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWaitEventRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'system': 'bool',
        'limit': 'int',
        'offset': 'int',
        'order_fields': 'list[list[str]]',
        'wait_event_query_info': 'WaitEventQueryInfo'
    }

    attribute_map = {
        'node_id': 'node_id',
        'system': 'system',
        'limit': 'limit',
        'offset': 'offset',
        'order_fields': 'order_fields',
        'wait_event_query_info': 'wait_event_query_info'
    }

    def __init__(self, node_id=None, system=None, limit=None, offset=None, order_fields=None, wait_event_query_info=None):
        r"""ListWaitEventRequestBody

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**: 节点ID，仅支持包含有CN或DN（主、备）组件的节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type node_id: str
        :param system: **参数解释**: 是否查询系统用户。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type system: bool
        :param limit: **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: [1，100]。 **默认取值**: 默认为10。
        :type limit: int
        :param offset: **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 不涉及。 **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。
        :type offset: int
        :param order_fields: **参数解释**: 排序字段列表，内部List&lt;String&gt;。 **约束限制**: 不涉及。
        :type order_fields: list[list[str]]
        :param wait_event_query_info: 
        :type wait_event_query_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.WaitEventQueryInfo`
        """
        
        

        self._node_id = None
        self._system = None
        self._limit = None
        self._offset = None
        self._order_fields = None
        self._wait_event_query_info = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if system is not None:
            self.system = system
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order_fields is not None:
            self.order_fields = order_fields
        if wait_event_query_info is not None:
            self.wait_event_query_info = wait_event_query_info

    @property
    def node_id(self):
        r"""Gets the node_id of this ListWaitEventRequestBody.

        **参数解释**: 节点ID，仅支持包含有CN或DN（主、备）组件的节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The node_id of this ListWaitEventRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListWaitEventRequestBody.

        **参数解释**: 节点ID，仅支持包含有CN或DN（主、备）组件的节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param node_id: The node_id of this ListWaitEventRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def system(self):
        r"""Gets the system of this ListWaitEventRequestBody.

        **参数解释**: 是否查询系统用户。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The system of this ListWaitEventRequestBody.
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        r"""Sets the system of this ListWaitEventRequestBody.

        **参数解释**: 是否查询系统用户。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param system: The system of this ListWaitEventRequestBody.
        :type system: bool
        """
        self._system = system

    @property
    def limit(self):
        r"""Gets the limit of this ListWaitEventRequestBody.

        **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: [1，100]。 **默认取值**: 默认为10。

        :return: The limit of this ListWaitEventRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWaitEventRequestBody.

        **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: [1，100]。 **默认取值**: 默认为10。

        :param limit: The limit of this ListWaitEventRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListWaitEventRequestBody.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 不涉及。 **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :return: The offset of this ListWaitEventRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWaitEventRequestBody.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 不涉及。 **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :param offset: The offset of this ListWaitEventRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def order_fields(self):
        r"""Gets the order_fields of this ListWaitEventRequestBody.

        **参数解释**: 排序字段列表，内部List<String>。 **约束限制**: 不涉及。

        :return: The order_fields of this ListWaitEventRequestBody.
        :rtype: list[list[str]]
        """
        return self._order_fields

    @order_fields.setter
    def order_fields(self, order_fields):
        r"""Sets the order_fields of this ListWaitEventRequestBody.

        **参数解释**: 排序字段列表，内部List<String>。 **约束限制**: 不涉及。

        :param order_fields: The order_fields of this ListWaitEventRequestBody.
        :type order_fields: list[list[str]]
        """
        self._order_fields = order_fields

    @property
    def wait_event_query_info(self):
        r"""Gets the wait_event_query_info of this ListWaitEventRequestBody.

        :return: The wait_event_query_info of this ListWaitEventRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.WaitEventQueryInfo`
        """
        return self._wait_event_query_info

    @wait_event_query_info.setter
    def wait_event_query_info(self, wait_event_query_info):
        r"""Sets the wait_event_query_info of this ListWaitEventRequestBody.

        :param wait_event_query_info: The wait_event_query_info of this ListWaitEventRequestBody.
        :type wait_event_query_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.WaitEventQueryInfo`
        """
        self._wait_event_query_info = wait_event_query_info

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
        if not isinstance(other, ListWaitEventRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
