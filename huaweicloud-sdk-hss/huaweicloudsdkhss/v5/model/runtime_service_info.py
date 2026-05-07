# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuntimeServiceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'runtime_type': 'str',
        'runtime_version': 'str',
        'storage_driver': 'list[str]'
    }

    attribute_map = {
        'runtime_type': 'runtime_type',
        'runtime_version': 'runtime_version',
        'storage_driver': 'storage_driver'
    }

    def __init__(self, runtime_type=None, runtime_version=None, storage_driver=None):
        r"""RuntimeServiceInfo

        The model defined in huaweicloud sdk

        :param runtime_type: **参数解释** 运行时类型 **取值范围** - docker：docker运行时。 - containerd：containerd运行时。 - podman：podman运行时。 - isulad：isulad运行时。 - crio：crio运行时。 - unknown：未知运行时。 
        :type runtime_type: str
        :param runtime_version: **参数解释** 运行时版本 **取值范围** 字符长度0-128 
        :type runtime_version: str
        :param storage_driver: **参数解释** 运行时存储驱动数组 **取值范围** 数组范围0-20 
        :type storage_driver: list[str]
        """
        
        

        self._runtime_type = None
        self._runtime_version = None
        self._storage_driver = None
        self.discriminator = None

        if runtime_type is not None:
            self.runtime_type = runtime_type
        if runtime_version is not None:
            self.runtime_version = runtime_version
        if storage_driver is not None:
            self.storage_driver = storage_driver

    @property
    def runtime_type(self):
        r"""Gets the runtime_type of this RuntimeServiceInfo.

        **参数解释** 运行时类型 **取值范围** - docker：docker运行时。 - containerd：containerd运行时。 - podman：podman运行时。 - isulad：isulad运行时。 - crio：crio运行时。 - unknown：未知运行时。 

        :return: The runtime_type of this RuntimeServiceInfo.
        :rtype: str
        """
        return self._runtime_type

    @runtime_type.setter
    def runtime_type(self, runtime_type):
        r"""Sets the runtime_type of this RuntimeServiceInfo.

        **参数解释** 运行时类型 **取值范围** - docker：docker运行时。 - containerd：containerd运行时。 - podman：podman运行时。 - isulad：isulad运行时。 - crio：crio运行时。 - unknown：未知运行时。 

        :param runtime_type: The runtime_type of this RuntimeServiceInfo.
        :type runtime_type: str
        """
        self._runtime_type = runtime_type

    @property
    def runtime_version(self):
        r"""Gets the runtime_version of this RuntimeServiceInfo.

        **参数解释** 运行时版本 **取值范围** 字符长度0-128 

        :return: The runtime_version of this RuntimeServiceInfo.
        :rtype: str
        """
        return self._runtime_version

    @runtime_version.setter
    def runtime_version(self, runtime_version):
        r"""Sets the runtime_version of this RuntimeServiceInfo.

        **参数解释** 运行时版本 **取值范围** 字符长度0-128 

        :param runtime_version: The runtime_version of this RuntimeServiceInfo.
        :type runtime_version: str
        """
        self._runtime_version = runtime_version

    @property
    def storage_driver(self):
        r"""Gets the storage_driver of this RuntimeServiceInfo.

        **参数解释** 运行时存储驱动数组 **取值范围** 数组范围0-20 

        :return: The storage_driver of this RuntimeServiceInfo.
        :rtype: list[str]
        """
        return self._storage_driver

    @storage_driver.setter
    def storage_driver(self, storage_driver):
        r"""Sets the storage_driver of this RuntimeServiceInfo.

        **参数解释** 运行时存储驱动数组 **取值范围** 数组范围0-20 

        :param storage_driver: The storage_driver of this RuntimeServiceInfo.
        :type storage_driver: list[str]
        """
        self._storage_driver = storage_driver

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
        if not isinstance(other, RuntimeServiceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
