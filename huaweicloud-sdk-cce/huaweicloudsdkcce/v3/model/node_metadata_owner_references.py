# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeMetadataOwnerReferences:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodepool_name': 'str',
        'nodepool_id': 'str',
        'hyper_node_name': 'str',
        'hyper_node_id': 'str'
    }

    attribute_map = {
        'nodepool_name': 'nodepoolName',
        'nodepool_id': 'nodepoolID',
        'hyper_node_name': 'hyperNodeName',
        'hyper_node_id': 'hyperNodeID'
    }

    def __init__(self, nodepool_name=None, nodepool_id=None, hyper_node_name=None, hyper_node_id=None):
        r"""NodeMetadataOwnerReferences

        The model defined in huaweicloud sdk

        :param nodepool_name: **参数解释**： 节点池名称 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type nodepool_name: str
        :param nodepool_id: **参数解释**： 节点池ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type nodepool_id: str
        :param hyper_node_name: **参数解释**： 超节点名称。如果节点不属于超节点，此字段不展示。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type hyper_node_name: str
        :param hyper_node_id: **参数解释**： 超节点ID。如果节点不属于超节点，此字段不展示。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type hyper_node_id: str
        """
        
        

        self._nodepool_name = None
        self._nodepool_id = None
        self._hyper_node_name = None
        self._hyper_node_id = None
        self.discriminator = None

        if nodepool_name is not None:
            self.nodepool_name = nodepool_name
        if nodepool_id is not None:
            self.nodepool_id = nodepool_id
        if hyper_node_name is not None:
            self.hyper_node_name = hyper_node_name
        if hyper_node_id is not None:
            self.hyper_node_id = hyper_node_id

    @property
    def nodepool_name(self):
        r"""Gets the nodepool_name of this NodeMetadataOwnerReferences.

        **参数解释**： 节点池名称 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The nodepool_name of this NodeMetadataOwnerReferences.
        :rtype: str
        """
        return self._nodepool_name

    @nodepool_name.setter
    def nodepool_name(self, nodepool_name):
        r"""Sets the nodepool_name of this NodeMetadataOwnerReferences.

        **参数解释**： 节点池名称 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param nodepool_name: The nodepool_name of this NodeMetadataOwnerReferences.
        :type nodepool_name: str
        """
        self._nodepool_name = nodepool_name

    @property
    def nodepool_id(self):
        r"""Gets the nodepool_id of this NodeMetadataOwnerReferences.

        **参数解释**： 节点池ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The nodepool_id of this NodeMetadataOwnerReferences.
        :rtype: str
        """
        return self._nodepool_id

    @nodepool_id.setter
    def nodepool_id(self, nodepool_id):
        r"""Sets the nodepool_id of this NodeMetadataOwnerReferences.

        **参数解释**： 节点池ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param nodepool_id: The nodepool_id of this NodeMetadataOwnerReferences.
        :type nodepool_id: str
        """
        self._nodepool_id = nodepool_id

    @property
    def hyper_node_name(self):
        r"""Gets the hyper_node_name of this NodeMetadataOwnerReferences.

        **参数解释**： 超节点名称。如果节点不属于超节点，此字段不展示。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The hyper_node_name of this NodeMetadataOwnerReferences.
        :rtype: str
        """
        return self._hyper_node_name

    @hyper_node_name.setter
    def hyper_node_name(self, hyper_node_name):
        r"""Sets the hyper_node_name of this NodeMetadataOwnerReferences.

        **参数解释**： 超节点名称。如果节点不属于超节点，此字段不展示。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param hyper_node_name: The hyper_node_name of this NodeMetadataOwnerReferences.
        :type hyper_node_name: str
        """
        self._hyper_node_name = hyper_node_name

    @property
    def hyper_node_id(self):
        r"""Gets the hyper_node_id of this NodeMetadataOwnerReferences.

        **参数解释**： 超节点ID。如果节点不属于超节点，此字段不展示。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The hyper_node_id of this NodeMetadataOwnerReferences.
        :rtype: str
        """
        return self._hyper_node_id

    @hyper_node_id.setter
    def hyper_node_id(self, hyper_node_id):
        r"""Sets the hyper_node_id of this NodeMetadataOwnerReferences.

        **参数解释**： 超节点ID。如果节点不属于超节点，此字段不展示。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param hyper_node_id: The hyper_node_id of this NodeMetadataOwnerReferences.
        :type hyper_node_id: str
        """
        self._hyper_node_id = hyper_node_id

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
        if not isinstance(other, NodeMetadataOwnerReferences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
