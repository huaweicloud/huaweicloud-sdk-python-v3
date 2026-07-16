# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetNodesRequestNodeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os': 'str',
        'name': 'str',
        'image_id': 'str',
        'image_type': 'str',
        'runtime': 'str'
    }

    attribute_map = {
        'os': 'os',
        'name': 'name',
        'image_id': 'imageId',
        'image_type': 'imageType',
        'runtime': 'runtime'
    }

    def __init__(self, os=None, name=None, image_id=None, image_type=None, runtime=None):
        r"""ResetNodesRequestNodeConfig

        The model defined in huaweicloud sdk

        :param os: **参数解释**：节点的镜像名称，如果不设置则取name字段的值 **约束限制**：不涉及。
        :type os: str
        :param name: **参数解释**：节点的镜像名称，如果os字段不设置才取此字段的值。 **约束限制**：不涉及。
        :type name: str
        :param image_id: **参数解释**：节点的镜像ID。 **约束限制**：不涉及。
        :type image_id: str
        :param image_type: **参数解释**：节点的镜像类型。 **约束限制**：不涉及。
        :type image_type: str
        :param runtime: **参数解释**：节点的容器运行时。 **约束限制**：不涉及。 **取值范围**：只能是[docker, containerd]其中一个。
        :type runtime: str
        """
        
        

        self._os = None
        self._name = None
        self._image_id = None
        self._image_type = None
        self._runtime = None
        self.discriminator = None

        if os is not None:
            self.os = os
        if name is not None:
            self.name = name
        if image_id is not None:
            self.image_id = image_id
        if image_type is not None:
            self.image_type = image_type
        if runtime is not None:
            self.runtime = runtime

    @property
    def os(self):
        r"""Gets the os of this ResetNodesRequestNodeConfig.

        **参数解释**：节点的镜像名称，如果不设置则取name字段的值 **约束限制**：不涉及。

        :return: The os of this ResetNodesRequestNodeConfig.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this ResetNodesRequestNodeConfig.

        **参数解释**：节点的镜像名称，如果不设置则取name字段的值 **约束限制**：不涉及。

        :param os: The os of this ResetNodesRequestNodeConfig.
        :type os: str
        """
        self._os = os

    @property
    def name(self):
        r"""Gets the name of this ResetNodesRequestNodeConfig.

        **参数解释**：节点的镜像名称，如果os字段不设置才取此字段的值。 **约束限制**：不涉及。

        :return: The name of this ResetNodesRequestNodeConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResetNodesRequestNodeConfig.

        **参数解释**：节点的镜像名称，如果os字段不设置才取此字段的值。 **约束限制**：不涉及。

        :param name: The name of this ResetNodesRequestNodeConfig.
        :type name: str
        """
        self._name = name

    @property
    def image_id(self):
        r"""Gets the image_id of this ResetNodesRequestNodeConfig.

        **参数解释**：节点的镜像ID。 **约束限制**：不涉及。

        :return: The image_id of this ResetNodesRequestNodeConfig.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ResetNodesRequestNodeConfig.

        **参数解释**：节点的镜像ID。 **约束限制**：不涉及。

        :param image_id: The image_id of this ResetNodesRequestNodeConfig.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_type(self):
        r"""Gets the image_type of this ResetNodesRequestNodeConfig.

        **参数解释**：节点的镜像类型。 **约束限制**：不涉及。

        :return: The image_type of this ResetNodesRequestNodeConfig.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ResetNodesRequestNodeConfig.

        **参数解释**：节点的镜像类型。 **约束限制**：不涉及。

        :param image_type: The image_type of this ResetNodesRequestNodeConfig.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def runtime(self):
        r"""Gets the runtime of this ResetNodesRequestNodeConfig.

        **参数解释**：节点的容器运行时。 **约束限制**：不涉及。 **取值范围**：只能是[docker, containerd]其中一个。

        :return: The runtime of this ResetNodesRequestNodeConfig.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this ResetNodesRequestNodeConfig.

        **参数解释**：节点的容器运行时。 **约束限制**：不涉及。 **取值范围**：只能是[docker, containerd]其中一个。

        :param runtime: The runtime of this ResetNodesRequestNodeConfig.
        :type runtime: str
        """
        self._runtime = runtime

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
        if not isinstance(other, ResetNodesRequestNodeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
