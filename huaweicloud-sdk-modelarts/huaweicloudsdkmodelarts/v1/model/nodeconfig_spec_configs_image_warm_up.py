# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeconfigSpecConfigsImageWarmUp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'creation_timestamp': 'str',
        'type': 'str',
        'image': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'creation_timestamp': 'creationTimestamp',
        'type': 'type',
        'image': 'image'
    }

    def __init__(self, id=None, name=None, creation_timestamp=None, type=None, image=None):
        r"""NodeconfigSpecConfigsImageWarmUp

        The model defined in huaweicloud sdk

        :param id: **参数解释**：镜像预热任务ID。 **约束限制**：系统自动生成。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type id: str
        :param name: **参数解释**：镜像预热任务名称。 **约束限制**：由4~32位小写字母、数字或\&quot;-\&quot;组成。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param creation_timestamp: **参数解释**：镜像预热任务的创建时间。 **约束限制**：系统自动填充。 **取值范围**：RFC3339格式时间。 **默认取值**：不涉及。
        :type creation_timestamp: str
        :param type: **参数解释**：镜像类型。 **约束限制**：不涉及。 **取值范围**：SWR。 **默认取值**：不涉及。
        :type type: str
        :param image: **参数解释**：需要预热的镜像地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type image: str
        """
        
        

        self._id = None
        self._name = None
        self._creation_timestamp = None
        self._type = None
        self._image = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if type is not None:
            self.type = type
        if image is not None:
            self.image = image

    @property
    def id(self):
        r"""Gets the id of this NodeconfigSpecConfigsImageWarmUp.

        **参数解释**：镜像预热任务ID。 **约束限制**：系统自动生成。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The id of this NodeconfigSpecConfigsImageWarmUp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NodeconfigSpecConfigsImageWarmUp.

        **参数解释**：镜像预热任务ID。 **约束限制**：系统自动生成。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param id: The id of this NodeconfigSpecConfigsImageWarmUp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this NodeconfigSpecConfigsImageWarmUp.

        **参数解释**：镜像预热任务名称。 **约束限制**：由4~32位小写字母、数字或\"-\"组成。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this NodeconfigSpecConfigsImageWarmUp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NodeconfigSpecConfigsImageWarmUp.

        **参数解释**：镜像预热任务名称。 **约束限制**：由4~32位小写字母、数字或\"-\"组成。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this NodeconfigSpecConfigsImageWarmUp.
        :type name: str
        """
        self._name = name

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this NodeconfigSpecConfigsImageWarmUp.

        **参数解释**：镜像预热任务的创建时间。 **约束限制**：系统自动填充。 **取值范围**：RFC3339格式时间。 **默认取值**：不涉及。

        :return: The creation_timestamp of this NodeconfigSpecConfigsImageWarmUp.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this NodeconfigSpecConfigsImageWarmUp.

        **参数解释**：镜像预热任务的创建时间。 **约束限制**：系统自动填充。 **取值范围**：RFC3339格式时间。 **默认取值**：不涉及。

        :param creation_timestamp: The creation_timestamp of this NodeconfigSpecConfigsImageWarmUp.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def type(self):
        r"""Gets the type of this NodeconfigSpecConfigsImageWarmUp.

        **参数解释**：镜像类型。 **约束限制**：不涉及。 **取值范围**：SWR。 **默认取值**：不涉及。

        :return: The type of this NodeconfigSpecConfigsImageWarmUp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NodeconfigSpecConfigsImageWarmUp.

        **参数解释**：镜像类型。 **约束限制**：不涉及。 **取值范围**：SWR。 **默认取值**：不涉及。

        :param type: The type of this NodeconfigSpecConfigsImageWarmUp.
        :type type: str
        """
        self._type = type

    @property
    def image(self):
        r"""Gets the image of this NodeconfigSpecConfigsImageWarmUp.

        **参数解释**：需要预热的镜像地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The image of this NodeconfigSpecConfigsImageWarmUp.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this NodeconfigSpecConfigsImageWarmUp.

        **参数解释**：需要预热的镜像地址。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param image: The image of this NodeconfigSpecConfigsImageWarmUp.
        :type image: str
        """
        self._image = image

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
        if not isinstance(other, NodeconfigSpecConfigsImageWarmUp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
