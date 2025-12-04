# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReduceNodeOpenRequest:

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
        'node_ids': 'list[str]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_ids': 'node_ids'
    }

    def __init__(self, instance_id=None, node_ids=None):
        r"""ReduceNodeOpenRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例id。
        :type instance_id: str
        :param node_ids: 节点id列表。
        :type node_ids: list[str]
        """
        
        

        self._instance_id = None
        self._node_ids = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if node_ids is not None:
            self.node_ids = node_ids

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ReduceNodeOpenRequest.

        实例id。

        :return: The instance_id of this ReduceNodeOpenRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ReduceNodeOpenRequest.

        实例id。

        :param instance_id: The instance_id of this ReduceNodeOpenRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_ids(self):
        r"""Gets the node_ids of this ReduceNodeOpenRequest.

        节点id列表。

        :return: The node_ids of this ReduceNodeOpenRequest.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this ReduceNodeOpenRequest.

        节点id列表。

        :param node_ids: The node_ids of this ReduceNodeOpenRequest.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

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
        if not isinstance(other, ReduceNodeOpenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
