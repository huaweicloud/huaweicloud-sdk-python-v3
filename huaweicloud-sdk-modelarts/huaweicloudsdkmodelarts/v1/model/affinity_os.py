# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AffinityOS:

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
        'image_id': 'str',
        'preferred': 'bool',
        'eos': 'bool',
        'offline': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'image_id': 'imageId',
        'preferred': 'preferred',
        'eos': 'eos',
        'offline': 'offline'
    }

    def __init__(self, name=None, image_id=None, preferred=None, eos=None, offline=None):
        r"""AffinityOS

        The model defined in huaweicloud sdk

        :param name: **参数解释**：操作系统名称。 **取值范围**：不涉及。
        :type name: str
        :param image_id: **参数解释**：操作系统镜像id, 裸金属规格该字段不为空。 **取值范围**：不涉及。
        :type image_id: str
        :param preferred: **参数解释**：是否优选。 **取值范围**：不涉及。
        :type preferred: bool
        :param eos: **参数解释**：操作系统是否即将停止服务, end of service。 **取值范围**：不涉及。
        :type eos: bool
        :param offline: **参数解释**：操作系统是否下线。 **取值范围**：不涉及
        :type offline: bool
        """
        
        

        self._name = None
        self._image_id = None
        self._preferred = None
        self._eos = None
        self._offline = None
        self.discriminator = None

        self.name = name
        if image_id is not None:
            self.image_id = image_id
        if preferred is not None:
            self.preferred = preferred
        if eos is not None:
            self.eos = eos
        if offline is not None:
            self.offline = offline

    @property
    def name(self):
        r"""Gets the name of this AffinityOS.

        **参数解释**：操作系统名称。 **取值范围**：不涉及。

        :return: The name of this AffinityOS.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AffinityOS.

        **参数解释**：操作系统名称。 **取值范围**：不涉及。

        :param name: The name of this AffinityOS.
        :type name: str
        """
        self._name = name

    @property
    def image_id(self):
        r"""Gets the image_id of this AffinityOS.

        **参数解释**：操作系统镜像id, 裸金属规格该字段不为空。 **取值范围**：不涉及。

        :return: The image_id of this AffinityOS.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this AffinityOS.

        **参数解释**：操作系统镜像id, 裸金属规格该字段不为空。 **取值范围**：不涉及。

        :param image_id: The image_id of this AffinityOS.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def preferred(self):
        r"""Gets the preferred of this AffinityOS.

        **参数解释**：是否优选。 **取值范围**：不涉及。

        :return: The preferred of this AffinityOS.
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred):
        r"""Sets the preferred of this AffinityOS.

        **参数解释**：是否优选。 **取值范围**：不涉及。

        :param preferred: The preferred of this AffinityOS.
        :type preferred: bool
        """
        self._preferred = preferred

    @property
    def eos(self):
        r"""Gets the eos of this AffinityOS.

        **参数解释**：操作系统是否即将停止服务, end of service。 **取值范围**：不涉及。

        :return: The eos of this AffinityOS.
        :rtype: bool
        """
        return self._eos

    @eos.setter
    def eos(self, eos):
        r"""Sets the eos of this AffinityOS.

        **参数解释**：操作系统是否即将停止服务, end of service。 **取值范围**：不涉及。

        :param eos: The eos of this AffinityOS.
        :type eos: bool
        """
        self._eos = eos

    @property
    def offline(self):
        r"""Gets the offline of this AffinityOS.

        **参数解释**：操作系统是否下线。 **取值范围**：不涉及

        :return: The offline of this AffinityOS.
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        r"""Sets the offline of this AffinityOS.

        **参数解释**：操作系统是否下线。 **取值范围**：不涉及

        :param offline: The offline of this AffinityOS.
        :type offline: bool
        """
        self._offline = offline

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
        if not isinstance(other, AffinityOS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
