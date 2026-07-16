# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerImageResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'image_id': 'str',
        'name': 'str',
        'server_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'image_id': 'image_id',
        'name': 'name',
        'server_type': 'server_type',
        'status': 'status'
    }

    def __init__(self, arch=None, image_id=None, name=None, server_type=None, status=None):
        r"""ServerImageResponse

        The model defined in huaweicloud sdk

        :param arch: **参数解释**：服务器镜像架构类型。 **取值范围**： - ARM - X86
        :type arch: str
        :param image_id: **参数解释**：服务器镜像ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type image_id: str
        :param name: **参数解释**：服务器镜像名称。表示服务器镜像的名称。 **约束限制**：不涉及。 **取值范围**：1 - 256字符 **默认取值**：不涉及。
        :type name: str
        :param server_type: **参数解释**：服务器类型。 **取值范围**： - BMS：裸金属服务器 - ECS：弹性云服务器 - HPS：超节点服务器
        :type server_type: str
        :param status: **参数解释**：服务器镜像状态。 **取值范围**： - ACTIVE - INACTIVE
        :type status: str
        """
        
        

        self._arch = None
        self._image_id = None
        self._name = None
        self._server_type = None
        self._status = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        if image_id is not None:
            self.image_id = image_id
        if name is not None:
            self.name = name
        if server_type is not None:
            self.server_type = server_type
        if status is not None:
            self.status = status

    @property
    def arch(self):
        r"""Gets the arch of this ServerImageResponse.

        **参数解释**：服务器镜像架构类型。 **取值范围**： - ARM - X86

        :return: The arch of this ServerImageResponse.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ServerImageResponse.

        **参数解释**：服务器镜像架构类型。 **取值范围**： - ARM - X86

        :param arch: The arch of this ServerImageResponse.
        :type arch: str
        """
        self._arch = arch

    @property
    def image_id(self):
        r"""Gets the image_id of this ServerImageResponse.

        **参数解释**：服务器镜像ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The image_id of this ServerImageResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ServerImageResponse.

        **参数解释**：服务器镜像ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param image_id: The image_id of this ServerImageResponse.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def name(self):
        r"""Gets the name of this ServerImageResponse.

        **参数解释**：服务器镜像名称。表示服务器镜像的名称。 **约束限制**：不涉及。 **取值范围**：1 - 256字符 **默认取值**：不涉及。

        :return: The name of this ServerImageResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServerImageResponse.

        **参数解释**：服务器镜像名称。表示服务器镜像的名称。 **约束限制**：不涉及。 **取值范围**：1 - 256字符 **默认取值**：不涉及。

        :param name: The name of this ServerImageResponse.
        :type name: str
        """
        self._name = name

    @property
    def server_type(self):
        r"""Gets the server_type of this ServerImageResponse.

        **参数解释**：服务器类型。 **取值范围**： - BMS：裸金属服务器 - ECS：弹性云服务器 - HPS：超节点服务器

        :return: The server_type of this ServerImageResponse.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ServerImageResponse.

        **参数解释**：服务器类型。 **取值范围**： - BMS：裸金属服务器 - ECS：弹性云服务器 - HPS：超节点服务器

        :param server_type: The server_type of this ServerImageResponse.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def status(self):
        r"""Gets the status of this ServerImageResponse.

        **参数解释**：服务器镜像状态。 **取值范围**： - ACTIVE - INACTIVE

        :return: The status of this ServerImageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServerImageResponse.

        **参数解释**：服务器镜像状态。 **取值范围**： - ACTIVE - INACTIVE

        :param status: The status of this ServerImageResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ServerImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
