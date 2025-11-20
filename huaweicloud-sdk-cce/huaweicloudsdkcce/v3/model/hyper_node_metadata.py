# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HyperNodeMetadata:

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
        'creation_timestamp': 'str',
        'update_timestamp': 'str',
        'owner_reference': 'HyperNodeMetadataOwnerReference'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp',
        'owner_reference': 'ownerReference'
    }

    def __init__(self, name=None, uid=None, creation_timestamp=None, update_timestamp=None, owner_reference=None):
        r"""HyperNodeMetadata

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 超节点名称 &gt; 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-56位，且不能以中划线(-)结尾。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type name: str
        :param uid: **参数解释**： 超节点ID，资源唯一标识，创建成功后自动生成，填写无效
        :type uid: str
        :param creation_timestamp: **参数解释**： 创建时间，创建成功后自动生成，填写无效
        :type creation_timestamp: str
        :param update_timestamp: **参数解释**： 更新时间，创建成功后自动生成，填写无效
        :type update_timestamp: str
        :param owner_reference: 
        :type owner_reference: :class:`huaweicloudsdkcce.v3.HyperNodeMetadataOwnerReference`
        """
        
        

        self._name = None
        self._uid = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self._owner_reference = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp
        if owner_reference is not None:
            self.owner_reference = owner_reference

    @property
    def name(self):
        r"""Gets the name of this HyperNodeMetadata.

        **参数解释**： 超节点名称 > 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-56位，且不能以中划线(-)结尾。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The name of this HyperNodeMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HyperNodeMetadata.

        **参数解释**： 超节点名称 > 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-56位，且不能以中划线(-)结尾。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param name: The name of this HyperNodeMetadata.
        :type name: str
        """
        self._name = name

    @property
    def uid(self):
        r"""Gets the uid of this HyperNodeMetadata.

        **参数解释**： 超节点ID，资源唯一标识，创建成功后自动生成，填写无效

        :return: The uid of this HyperNodeMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this HyperNodeMetadata.

        **参数解释**： 超节点ID，资源唯一标识，创建成功后自动生成，填写无效

        :param uid: The uid of this HyperNodeMetadata.
        :type uid: str
        """
        self._uid = uid

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this HyperNodeMetadata.

        **参数解释**： 创建时间，创建成功后自动生成，填写无效

        :return: The creation_timestamp of this HyperNodeMetadata.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this HyperNodeMetadata.

        **参数解释**： 创建时间，创建成功后自动生成，填写无效

        :param creation_timestamp: The creation_timestamp of this HyperNodeMetadata.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        r"""Gets the update_timestamp of this HyperNodeMetadata.

        **参数解释**： 更新时间，创建成功后自动生成，填写无效

        :return: The update_timestamp of this HyperNodeMetadata.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        r"""Sets the update_timestamp of this HyperNodeMetadata.

        **参数解释**： 更新时间，创建成功后自动生成，填写无效

        :param update_timestamp: The update_timestamp of this HyperNodeMetadata.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

    @property
    def owner_reference(self):
        r"""Gets the owner_reference of this HyperNodeMetadata.

        :return: The owner_reference of this HyperNodeMetadata.
        :rtype: :class:`huaweicloudsdkcce.v3.HyperNodeMetadataOwnerReference`
        """
        return self._owner_reference

    @owner_reference.setter
    def owner_reference(self, owner_reference):
        r"""Sets the owner_reference of this HyperNodeMetadata.

        :param owner_reference: The owner_reference of this HyperNodeMetadata.
        :type owner_reference: :class:`huaweicloudsdkcce.v3.HyperNodeMetadataOwnerReference`
        """
        self._owner_reference = owner_reference

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
        if not isinstance(other, HyperNodeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
