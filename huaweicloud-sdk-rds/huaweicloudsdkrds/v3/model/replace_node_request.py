# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplaceNodeRequest:

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
        'node_id': 'str',
        'replace_action': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'replace_action': 'replace_action'
    }

    def __init__(self, instance_id=None, node_id=None, replace_action=None):
        r"""ReplaceNodeRequest

        The model defined in huaweicloud sdk

        :param instance_id: 只读实例ID。
        :type instance_id: str
        :param node_id: 只读实例的节点ID。
        :type node_id: str
        :param replace_action: 替换动作，取值范围： REPLACE: 节点顶替 REPLACE_ROLLBACK: 节点顶替回切
        :type replace_action: str
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._replace_action = None
        self.discriminator = None

        self.instance_id = instance_id
        self.node_id = node_id
        self.replace_action = replace_action

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ReplaceNodeRequest.

        只读实例ID。

        :return: The instance_id of this ReplaceNodeRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ReplaceNodeRequest.

        只读实例ID。

        :param instance_id: The instance_id of this ReplaceNodeRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ReplaceNodeRequest.

        只读实例的节点ID。

        :return: The node_id of this ReplaceNodeRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ReplaceNodeRequest.

        只读实例的节点ID。

        :param node_id: The node_id of this ReplaceNodeRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def replace_action(self):
        r"""Gets the replace_action of this ReplaceNodeRequest.

        替换动作，取值范围： REPLACE: 节点顶替 REPLACE_ROLLBACK: 节点顶替回切

        :return: The replace_action of this ReplaceNodeRequest.
        :rtype: str
        """
        return self._replace_action

    @replace_action.setter
    def replace_action(self, replace_action):
        r"""Sets the replace_action of this ReplaceNodeRequest.

        替换动作，取值范围： REPLACE: 节点顶替 REPLACE_ROLLBACK: 节点顶替回切

        :param replace_action: The replace_action of this ReplaceNodeRequest.
        :type replace_action: str
        """
        self._replace_action = replace_action

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
        if not isinstance(other, ReplaceNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
