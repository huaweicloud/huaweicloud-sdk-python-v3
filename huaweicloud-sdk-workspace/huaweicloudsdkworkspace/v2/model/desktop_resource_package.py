# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopResourcePackage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'package_type': 'str',
        'cpu': 'str',
        'architecture': 'str',
        'memory': 'str',
        'domain_ids': 'list[str]',
        'name': 'dict(str, str)',
        'description': 'dict(str, str)',
        'resource_packages': 'list[ResourcePackage]'
    }

    attribute_map = {
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'package_type': 'package_type',
        'cpu': 'cpu',
        'architecture': 'architecture',
        'memory': 'memory',
        'domain_ids': 'domain_ids',
        'name': 'name',
        'description': 'description',
        'resource_packages': 'resource_packages'
    }

    def __init__(self, cloud_service_type=None, resource_type=None, resource_spec_code=None, package_type=None, cpu=None, architecture=None, memory=None, domain_ids=None, name=None, description=None, resource_packages=None):
        r"""DesktopResourcePackage

        The model defined in huaweicloud sdk

        :param cloud_service_type: 云服务类型。
        :type cloud_service_type: str
        :param resource_type: 资源类型。
        :type resource_type: str
        :param resource_spec_code: 资源规格编码。
        :type resource_spec_code: str
        :param package_type: 规格。
        :type package_type: str
        :param cpu: cpu。
        :type cpu: str
        :param architecture: 产品架构：arm、x86。
        :type architecture: str
        :param memory: 内存。
        :type memory: str
        :param domain_ids: 该产品套餐支持的专有域id（domainId）。
        :type domain_ids: list[str]
        :param name: 产品名称&lt;语言，各语言对应的产品名&gt;。
        :type name: dict(str, str)
        :param description: 产品描述&lt;语言，各语言对应的产品名&gt;。
        :type description: dict(str, str)
        :param resource_packages: 按需套餐包规格列表。
        :type resource_packages: list[:class:`huaweicloudsdkworkspace.v2.ResourcePackage`]
        """
        
        

        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._package_type = None
        self._cpu = None
        self._architecture = None
        self._memory = None
        self._domain_ids = None
        self._name = None
        self._description = None
        self._resource_packages = None
        self.discriminator = None

        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if package_type is not None:
            self.package_type = package_type
        if cpu is not None:
            self.cpu = cpu
        if architecture is not None:
            self.architecture = architecture
        if memory is not None:
            self.memory = memory
        if domain_ids is not None:
            self.domain_ids = domain_ids
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if resource_packages is not None:
            self.resource_packages = resource_packages

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this DesktopResourcePackage.

        云服务类型。

        :return: The cloud_service_type of this DesktopResourcePackage.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this DesktopResourcePackage.

        云服务类型。

        :param cloud_service_type: The cloud_service_type of this DesktopResourcePackage.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this DesktopResourcePackage.

        资源类型。

        :return: The resource_type of this DesktopResourcePackage.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this DesktopResourcePackage.

        资源类型。

        :param resource_type: The resource_type of this DesktopResourcePackage.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this DesktopResourcePackage.

        资源规格编码。

        :return: The resource_spec_code of this DesktopResourcePackage.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this DesktopResourcePackage.

        资源规格编码。

        :param resource_spec_code: The resource_spec_code of this DesktopResourcePackage.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def package_type(self):
        r"""Gets the package_type of this DesktopResourcePackage.

        规格。

        :return: The package_type of this DesktopResourcePackage.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        r"""Sets the package_type of this DesktopResourcePackage.

        规格。

        :param package_type: The package_type of this DesktopResourcePackage.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def cpu(self):
        r"""Gets the cpu of this DesktopResourcePackage.

        cpu。

        :return: The cpu of this DesktopResourcePackage.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this DesktopResourcePackage.

        cpu。

        :param cpu: The cpu of this DesktopResourcePackage.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def architecture(self):
        r"""Gets the architecture of this DesktopResourcePackage.

        产品架构：arm、x86。

        :return: The architecture of this DesktopResourcePackage.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        r"""Sets the architecture of this DesktopResourcePackage.

        产品架构：arm、x86。

        :param architecture: The architecture of this DesktopResourcePackage.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def memory(self):
        r"""Gets the memory of this DesktopResourcePackage.

        内存。

        :return: The memory of this DesktopResourcePackage.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this DesktopResourcePackage.

        内存。

        :param memory: The memory of this DesktopResourcePackage.
        :type memory: str
        """
        self._memory = memory

    @property
    def domain_ids(self):
        r"""Gets the domain_ids of this DesktopResourcePackage.

        该产品套餐支持的专有域id（domainId）。

        :return: The domain_ids of this DesktopResourcePackage.
        :rtype: list[str]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        r"""Sets the domain_ids of this DesktopResourcePackage.

        该产品套餐支持的专有域id（domainId）。

        :param domain_ids: The domain_ids of this DesktopResourcePackage.
        :type domain_ids: list[str]
        """
        self._domain_ids = domain_ids

    @property
    def name(self):
        r"""Gets the name of this DesktopResourcePackage.

        产品名称<语言，各语言对应的产品名>。

        :return: The name of this DesktopResourcePackage.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DesktopResourcePackage.

        产品名称<语言，各语言对应的产品名>。

        :param name: The name of this DesktopResourcePackage.
        :type name: dict(str, str)
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this DesktopResourcePackage.

        产品描述<语言，各语言对应的产品名>。

        :return: The description of this DesktopResourcePackage.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DesktopResourcePackage.

        产品描述<语言，各语言对应的产品名>。

        :param description: The description of this DesktopResourcePackage.
        :type description: dict(str, str)
        """
        self._description = description

    @property
    def resource_packages(self):
        r"""Gets the resource_packages of this DesktopResourcePackage.

        按需套餐包规格列表。

        :return: The resource_packages of this DesktopResourcePackage.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ResourcePackage`]
        """
        return self._resource_packages

    @resource_packages.setter
    def resource_packages(self, resource_packages):
        r"""Sets the resource_packages of this DesktopResourcePackage.

        按需套餐包规格列表。

        :param resource_packages: The resource_packages of this DesktopResourcePackage.
        :type resource_packages: list[:class:`huaweicloudsdkworkspace.v2.ResourcePackage`]
        """
        self._resource_packages = resource_packages

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
        if not isinstance(other, DesktopResourcePackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
