# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CnComponentInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_name': 'str',
        'node_id': 'str',
        'component_id': 'str'
    }

    attribute_map = {
        'node_name': 'node_name',
        'node_id': 'node_id',
        'component_id': 'component_id'
    }

    def __init__(self, node_name=None, node_id=None, component_id=None):
        r"""CnComponentInfoResult

        The model defined in huaweicloud sdk

        :param node_name: **参数解释**: 节点名称。 **取值范围**: 不涉及。 
        :type node_name: str
        :param node_id: **参数解释**: 节点ID。 **取值范围**: 不涉及。 
        :type node_id: str
        :param component_id: **参数解释**: 组件ID。 **取值范围**: 不涉及。 
        :type component_id: str
        """
        
        

        self._node_name = None
        self._node_id = None
        self._component_id = None
        self.discriminator = None

        if node_name is not None:
            self.node_name = node_name
        if node_id is not None:
            self.node_id = node_id
        if component_id is not None:
            self.component_id = component_id

    @property
    def node_name(self):
        r"""Gets the node_name of this CnComponentInfoResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。 

        :return: The node_name of this CnComponentInfoResult.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this CnComponentInfoResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。 

        :param node_name: The node_name of this CnComponentInfoResult.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def node_id(self):
        r"""Gets the node_id of this CnComponentInfoResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。 

        :return: The node_id of this CnComponentInfoResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this CnComponentInfoResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。 

        :param node_id: The node_id of this CnComponentInfoResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def component_id(self):
        r"""Gets the component_id of this CnComponentInfoResult.

        **参数解释**: 组件ID。 **取值范围**: 不涉及。 

        :return: The component_id of this CnComponentInfoResult.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this CnComponentInfoResult.

        **参数解释**: 组件ID。 **取值范围**: 不涉及。 

        :param component_id: The component_id of this CnComponentInfoResult.
        :type component_id: str
        """
        self._component_id = component_id

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
        if not isinstance(other, CnComponentInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
