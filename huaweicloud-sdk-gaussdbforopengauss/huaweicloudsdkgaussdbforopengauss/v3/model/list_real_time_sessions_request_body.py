# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRealTimeSessionsRequestBody:

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
        'component_id': 'str',
        'query_info': 'SessionQueryInfoOption'
    }

    attribute_map = {
        'node_id': 'node_id',
        'component_id': 'component_id',
        'query_info': 'query_info'
    }

    def __init__(self, node_id=None, component_id=None, query_info=None):
        r"""ListRealTimeSessionsRequestBody

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**： 节点ID。 **约束限制**： 仅支持非日志类型的CN或DN节点。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type node_id: str
        :param component_id: **参数解释**： 组件ID。 **约束限制**： 仅支持非日志类型的CN或DN节点。 **取值范围**： 不涉及。 **默认取值**: 不涉及。
        :type component_id: str
        :param query_info: 
        :type query_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.SessionQueryInfoOption`
        """
        
        

        self._node_id = None
        self._component_id = None
        self._query_info = None
        self.discriminator = None

        self.node_id = node_id
        self.component_id = component_id
        if query_info is not None:
            self.query_info = query_info

    @property
    def node_id(self):
        r"""Gets the node_id of this ListRealTimeSessionsRequestBody.

        **参数解释**： 节点ID。 **约束限制**： 仅支持非日志类型的CN或DN节点。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The node_id of this ListRealTimeSessionsRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListRealTimeSessionsRequestBody.

        **参数解释**： 节点ID。 **约束限制**： 仅支持非日志类型的CN或DN节点。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param node_id: The node_id of this ListRealTimeSessionsRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def component_id(self):
        r"""Gets the component_id of this ListRealTimeSessionsRequestBody.

        **参数解释**： 组件ID。 **约束限制**： 仅支持非日志类型的CN或DN节点。 **取值范围**： 不涉及。 **默认取值**: 不涉及。

        :return: The component_id of this ListRealTimeSessionsRequestBody.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ListRealTimeSessionsRequestBody.

        **参数解释**： 组件ID。 **约束限制**： 仅支持非日志类型的CN或DN节点。 **取值范围**： 不涉及。 **默认取值**: 不涉及。

        :param component_id: The component_id of this ListRealTimeSessionsRequestBody.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def query_info(self):
        r"""Gets the query_info of this ListRealTimeSessionsRequestBody.

        :return: The query_info of this ListRealTimeSessionsRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.SessionQueryInfoOption`
        """
        return self._query_info

    @query_info.setter
    def query_info(self, query_info):
        r"""Sets the query_info of this ListRealTimeSessionsRequestBody.

        :param query_info: The query_info of this ListRealTimeSessionsRequestBody.
        :type query_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.SessionQueryInfoOption`
        """
        self._query_info = query_info

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
        if not isinstance(other, ListRealTimeSessionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
