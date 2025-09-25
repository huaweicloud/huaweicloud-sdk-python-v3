# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopTransactionRequsetBody:

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
        'session_ids': 'list[int]'
    }

    attribute_map = {
        'node_id': 'node_id',
        'component_id': 'component_id',
        'session_ids': 'session_ids'
    }

    def __init__(self, node_id=None, component_id=None, session_ids=None):
        r"""StopTransactionRequsetBody

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**: 节点ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type node_id: str
        :param component_id: **参数解释**: 组件ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type component_id: str
        :param session_ids: **参数解释**: 查杀事务的ID列表。 **约束限制**: 不涉及。
        :type session_ids: list[int]
        """
        
        

        self._node_id = None
        self._component_id = None
        self._session_ids = None
        self.discriminator = None

        self.node_id = node_id
        self.component_id = component_id
        self.session_ids = session_ids

    @property
    def node_id(self):
        r"""Gets the node_id of this StopTransactionRequsetBody.

        **参数解释**: 节点ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The node_id of this StopTransactionRequsetBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this StopTransactionRequsetBody.

        **参数解释**: 节点ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param node_id: The node_id of this StopTransactionRequsetBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def component_id(self):
        r"""Gets the component_id of this StopTransactionRequsetBody.

        **参数解释**: 组件ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The component_id of this StopTransactionRequsetBody.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this StopTransactionRequsetBody.

        **参数解释**: 组件ID，仅支持非日志类型的CN或DN节点。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param component_id: The component_id of this StopTransactionRequsetBody.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def session_ids(self):
        r"""Gets the session_ids of this StopTransactionRequsetBody.

        **参数解释**: 查杀事务的ID列表。 **约束限制**: 不涉及。

        :return: The session_ids of this StopTransactionRequsetBody.
        :rtype: list[int]
        """
        return self._session_ids

    @session_ids.setter
    def session_ids(self, session_ids):
        r"""Sets the session_ids of this StopTransactionRequsetBody.

        **参数解释**: 查杀事务的ID列表。 **约束限制**: 不涉及。

        :param session_ids: The session_ids of this StopTransactionRequsetBody.
        :type session_ids: list[int]
        """
        self._session_ids = session_ids

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
        if not isinstance(other, StopTransactionRequsetBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
