# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'uid': 'str',
        'annotations': 'dict(str, str)',
        'creation_timestamp': 'str',
        'update_timestamp': 'str',
        'owner_references': 'NodeMetadataOwnerReferences'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'annotations': 'annotations',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp',
        'owner_references': 'ownerReferences'
    }

    def __init__(self, name=None, uid=None, annotations=None, creation_timestamp=None, update_timestamp=None, owner_references=None):
        r"""NodeMetadata

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 节点名称 **约束限制**： - 命名规则：以小写字母开头，由小写字母、数字、中划线(-)、点(.)组成，长度范围1-56位，且不能以中划线(-)结尾。 - 若name未指定或指定为空字符串，则按照默认规则生成节点名称。默认规则为：“集群名称-随机字符串”，若集群名称过长，则只取前36个字符。 - 若节点数量(count)大于1时，则按照默认规则会在用户输入的节点名称末尾添加随机字符串。默认规则为：“用户输入名称-随机字符串”，若用户输入的节点名称长度范围超过50位时，系统截取前50位，并在末尾添加随机字符串。  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type name: str
        :param uid: **参数解释**： 节点ID，资源唯一标识。 **约束限制**： 创建成功后自动生成，填写无效 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type uid: str
        :param annotations: **参数解释**： CCE自有节点注解，非Kubernetes原生annotations，格式为key/value键值对。 &gt; Annotations不用于标识和选择对象。Annotations中的元数据可以是small或large，structured或unstructured，并且可以包括标签不允许使用的字符。  **约束限制**： 仅用于查询，不支持请求时传入，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及  示例： &#x60;&#x60;&#x60; \&quot;annotations\&quot;: {   \&quot;key1\&quot; : \&quot;value1\&quot;,   \&quot;key2\&quot; : \&quot;value2\&quot; } &#x60;&#x60;&#x60; 
        :type annotations: dict(str, str)
        :param creation_timestamp: **参数解释**： 节点创建时间。 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type creation_timestamp: str
        :param update_timestamp: **参数解释**： 节点更新时间。 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type update_timestamp: str
        :param owner_references: 
        :type owner_references: :class:`huaweicloudsdkcce.v3.NodeMetadataOwnerReferences`
        """
        
        

        self._name = None
        self._uid = None
        self._annotations = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self._owner_references = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if annotations is not None:
            self.annotations = annotations
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp
        if owner_references is not None:
            self.owner_references = owner_references

    @property
    def name(self):
        r"""Gets the name of this NodeMetadata.

        **参数解释**： 节点名称 **约束限制**： - 命名规则：以小写字母开头，由小写字母、数字、中划线(-)、点(.)组成，长度范围1-56位，且不能以中划线(-)结尾。 - 若name未指定或指定为空字符串，则按照默认规则生成节点名称。默认规则为：“集群名称-随机字符串”，若集群名称过长，则只取前36个字符。 - 若节点数量(count)大于1时，则按照默认规则会在用户输入的节点名称末尾添加随机字符串。默认规则为：“用户输入名称-随机字符串”，若用户输入的节点名称长度范围超过50位时，系统截取前50位，并在末尾添加随机字符串。  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The name of this NodeMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NodeMetadata.

        **参数解释**： 节点名称 **约束限制**： - 命名规则：以小写字母开头，由小写字母、数字、中划线(-)、点(.)组成，长度范围1-56位，且不能以中划线(-)结尾。 - 若name未指定或指定为空字符串，则按照默认规则生成节点名称。默认规则为：“集群名称-随机字符串”，若集群名称过长，则只取前36个字符。 - 若节点数量(count)大于1时，则按照默认规则会在用户输入的节点名称末尾添加随机字符串。默认规则为：“用户输入名称-随机字符串”，若用户输入的节点名称长度范围超过50位时，系统截取前50位，并在末尾添加随机字符串。  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param name: The name of this NodeMetadata.
        :type name: str
        """
        self._name = name

    @property
    def uid(self):
        r"""Gets the uid of this NodeMetadata.

        **参数解释**： 节点ID，资源唯一标识。 **约束限制**： 创建成功后自动生成，填写无效 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The uid of this NodeMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this NodeMetadata.

        **参数解释**： 节点ID，资源唯一标识。 **约束限制**： 创建成功后自动生成，填写无效 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param uid: The uid of this NodeMetadata.
        :type uid: str
        """
        self._uid = uid

    @property
    def annotations(self):
        r"""Gets the annotations of this NodeMetadata.

        **参数解释**： CCE自有节点注解，非Kubernetes原生annotations，格式为key/value键值对。 > Annotations不用于标识和选择对象。Annotations中的元数据可以是small或large，structured或unstructured，并且可以包括标签不允许使用的字符。  **约束限制**： 仅用于查询，不支持请求时传入，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及  示例： ``` \"annotations\": {   \"key1\" : \"value1\",   \"key2\" : \"value2\" } ``` 

        :return: The annotations of this NodeMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this NodeMetadata.

        **参数解释**： CCE自有节点注解，非Kubernetes原生annotations，格式为key/value键值对。 > Annotations不用于标识和选择对象。Annotations中的元数据可以是small或large，structured或unstructured，并且可以包括标签不允许使用的字符。  **约束限制**： 仅用于查询，不支持请求时传入，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及  示例： ``` \"annotations\": {   \"key1\" : \"value1\",   \"key2\" : \"value2\" } ``` 

        :param annotations: The annotations of this NodeMetadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this NodeMetadata.

        **参数解释**： 节点创建时间。 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The creation_timestamp of this NodeMetadata.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this NodeMetadata.

        **参数解释**： 节点创建时间。 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param creation_timestamp: The creation_timestamp of this NodeMetadata.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        r"""Gets the update_timestamp of this NodeMetadata.

        **参数解释**： 节点更新时间。 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The update_timestamp of this NodeMetadata.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        r"""Sets the update_timestamp of this NodeMetadata.

        **参数解释**： 节点更新时间。 **约束限制**： 创建成功后自动生成，填写无效。 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param update_timestamp: The update_timestamp of this NodeMetadata.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

    @property
    def owner_references(self):
        r"""Gets the owner_references of this NodeMetadata.

        :return: The owner_references of this NodeMetadata.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeMetadataOwnerReferences`
        """
        return self._owner_references

    @owner_references.setter
    def owner_references(self, owner_references):
        r"""Sets the owner_references of this NodeMetadata.

        :param owner_references: The owner_references of this NodeMetadata.
        :type owner_references: :class:`huaweicloudsdkcce.v3.NodeMetadataOwnerReferences`
        """
        self._owner_references = owner_references

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
        if not isinstance(other, NodeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
