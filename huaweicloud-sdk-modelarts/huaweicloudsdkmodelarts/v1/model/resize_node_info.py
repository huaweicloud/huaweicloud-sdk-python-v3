# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeNodeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_uid': 'str',
        'delete_node_names': 'list[str]'
    }

    attribute_map = {
        'batch_uid': 'batchUID',
        'delete_node_names': 'deleteNodeNames'
    }

    def __init__(self, batch_uid=None, delete_node_names=None):
        r"""ResizeNodeInfo

        The model defined in huaweicloud sdk

        :param batch_uid: **参数解释**：节点批次ID，批次变更时需要，可以从节点的os.modelarts.node/batch.uid标签中获取。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type batch_uid: str
        :param delete_node_names: **参数解释**：批次缩容场景，指定要缩容的节点名称列表。 **约束限制**：不涉及。
        :type delete_node_names: list[str]
        """
        
        

        self._batch_uid = None
        self._delete_node_names = None
        self.discriminator = None

        if batch_uid is not None:
            self.batch_uid = batch_uid
        if delete_node_names is not None:
            self.delete_node_names = delete_node_names

    @property
    def batch_uid(self):
        r"""Gets the batch_uid of this ResizeNodeInfo.

        **参数解释**：节点批次ID，批次变更时需要，可以从节点的os.modelarts.node/batch.uid标签中获取。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The batch_uid of this ResizeNodeInfo.
        :rtype: str
        """
        return self._batch_uid

    @batch_uid.setter
    def batch_uid(self, batch_uid):
        r"""Sets the batch_uid of this ResizeNodeInfo.

        **参数解释**：节点批次ID，批次变更时需要，可以从节点的os.modelarts.node/batch.uid标签中获取。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param batch_uid: The batch_uid of this ResizeNodeInfo.
        :type batch_uid: str
        """
        self._batch_uid = batch_uid

    @property
    def delete_node_names(self):
        r"""Gets the delete_node_names of this ResizeNodeInfo.

        **参数解释**：批次缩容场景，指定要缩容的节点名称列表。 **约束限制**：不涉及。

        :return: The delete_node_names of this ResizeNodeInfo.
        :rtype: list[str]
        """
        return self._delete_node_names

    @delete_node_names.setter
    def delete_node_names(self, delete_node_names):
        r"""Sets the delete_node_names of this ResizeNodeInfo.

        **参数解释**：批次缩容场景，指定要缩容的节点名称列表。 **约束限制**：不涉及。

        :param delete_node_names: The delete_node_names of this ResizeNodeInfo.
        :type delete_node_names: list[str]
        """
        self._delete_node_names = delete_node_names

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
        if not isinstance(other, ResizeNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
