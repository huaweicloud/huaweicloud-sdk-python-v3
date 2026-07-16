# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Os:

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
        'image_type': 'str',
        'auto_match': 'str'
    }

    attribute_map = {
        'name': 'name',
        'image_id': 'imageId',
        'image_type': 'imageType',
        'auto_match': 'autoMatch'
    }

    def __init__(self, name=None, image_id=None, image_type=None, auto_match=None):
        r"""Os

        The model defined in huaweicloud sdk

        :param name: **参数解释**：操作系统名称和版本，如EulorOS 2.5。指定私有镜像时可不指定。 **取值范围**：不涉及。
        :type name: str
        :param image_id: **参数解释**：操作系统镜像id。 **取值范围**：不涉及。
        :type image_id: str
        :param image_type: **参数解释**：操作系统镜像类型。设置私有镜像时必须指定。默认为预置镜像，无需指定该字段。 **取值范围**：可选值如下： - private：私有镜像 - \&quot;\&quot;：不指定类型即预置镜像。
        :type image_type: str
        :param auto_match: **参数解释**：操作系统镜像自动匹配配置。当配置该参数时将会自动选择最优镜像，同时该参数会自动清空。 **取值范围**：操作系统名称和版本，如EulorOS 2.5。
        :type auto_match: str
        """
        
        

        self._name = None
        self._image_id = None
        self._image_type = None
        self._auto_match = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if image_id is not None:
            self.image_id = image_id
        if image_type is not None:
            self.image_type = image_type
        if auto_match is not None:
            self.auto_match = auto_match

    @property
    def name(self):
        r"""Gets the name of this Os.

        **参数解释**：操作系统名称和版本，如EulorOS 2.5。指定私有镜像时可不指定。 **取值范围**：不涉及。

        :return: The name of this Os.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Os.

        **参数解释**：操作系统名称和版本，如EulorOS 2.5。指定私有镜像时可不指定。 **取值范围**：不涉及。

        :param name: The name of this Os.
        :type name: str
        """
        self._name = name

    @property
    def image_id(self):
        r"""Gets the image_id of this Os.

        **参数解释**：操作系统镜像id。 **取值范围**：不涉及。

        :return: The image_id of this Os.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this Os.

        **参数解释**：操作系统镜像id。 **取值范围**：不涉及。

        :param image_id: The image_id of this Os.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_type(self):
        r"""Gets the image_type of this Os.

        **参数解释**：操作系统镜像类型。设置私有镜像时必须指定。默认为预置镜像，无需指定该字段。 **取值范围**：可选值如下： - private：私有镜像 - \"\"：不指定类型即预置镜像。

        :return: The image_type of this Os.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this Os.

        **参数解释**：操作系统镜像类型。设置私有镜像时必须指定。默认为预置镜像，无需指定该字段。 **取值范围**：可选值如下： - private：私有镜像 - \"\"：不指定类型即预置镜像。

        :param image_type: The image_type of this Os.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def auto_match(self):
        r"""Gets the auto_match of this Os.

        **参数解释**：操作系统镜像自动匹配配置。当配置该参数时将会自动选择最优镜像，同时该参数会自动清空。 **取值范围**：操作系统名称和版本，如EulorOS 2.5。

        :return: The auto_match of this Os.
        :rtype: str
        """
        return self._auto_match

    @auto_match.setter
    def auto_match(self, auto_match):
        r"""Sets the auto_match of this Os.

        **参数解释**：操作系统镜像自动匹配配置。当配置该参数时将会自动选择最优镜像，同时该参数会自动清空。 **取值范围**：操作系统名称和版本，如EulorOS 2.5。

        :param auto_match: The auto_match of this Os.
        :type auto_match: str
        """
        self._auto_match = auto_match

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
        if not isinstance(other, Os):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
