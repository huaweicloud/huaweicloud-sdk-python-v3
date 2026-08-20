# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionModuleProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_manifest_version': 'str',
        'name': 'str',
        'description': 'str',
        'uuid': 'str',
        'operation_system': 'str',
        'image_source': 'str',
        'image': 'str',
        'icon': 'str',
        'environment_variables': 'dict(str, dict(str, str))',
        'execution': 'ExtensionExecution',
        'parameters': 'list[ExtensionParameter]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'build_manifest_version': 'build_manifestVersion',
        'name': 'name',
        'description': 'description',
        'uuid': 'uuid',
        'operation_system': 'operationSystem',
        'image_source': 'imageSource',
        'image': 'image',
        'icon': 'icon',
        'environment_variables': 'environmentVariables',
        'execution': 'execution',
        'parameters': 'parameters',
        'tags': 'tags'
    }

    def __init__(self, build_manifest_version=None, name=None, description=None, uuid=None, operation_system=None, image_source=None, image=None, icon=None, environment_variables=None, execution=None, parameters=None, tags=None):
        r"""ExtensionModuleProperties

        The model defined in huaweicloud sdk

        :param build_manifest_version: 构建清单版本
        :type build_manifest_version: str
        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param uuid: 任务uuid
        :type uuid: str
        :param operation_system: 操作系统
        :type operation_system: str
        :param image_source: 镜像来源
        :type image_source: str
        :param image: 镜像名
        :type image: str
        :param icon: 图标路径
        :type icon: str
        :param environment_variables: 环境变量，按region映射。键为变量类别(如registry/mirror)，值为region到配置命令的映射。
        :type environment_variables: dict(str, dict(str, str))
        :param execution: 
        :type execution: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionExecution`
        :param parameters: 用户可配置参数列表。
        :type parameters: list[:class:`huaweicloudsdkcodeartspipeline.v2.ExtensionParameter`]
        :param tags: 内部标签。
        :type tags: list[str]
        """
        
        

        self._build_manifest_version = None
        self._name = None
        self._description = None
        self._uuid = None
        self._operation_system = None
        self._image_source = None
        self._image = None
        self._icon = None
        self._environment_variables = None
        self._execution = None
        self._parameters = None
        self._tags = None
        self.discriminator = None

        if build_manifest_version is not None:
            self.build_manifest_version = build_manifest_version
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if uuid is not None:
            self.uuid = uuid
        if operation_system is not None:
            self.operation_system = operation_system
        if image_source is not None:
            self.image_source = image_source
        if image is not None:
            self.image = image
        if icon is not None:
            self.icon = icon
        if environment_variables is not None:
            self.environment_variables = environment_variables
        if execution is not None:
            self.execution = execution
        if parameters is not None:
            self.parameters = parameters
        if tags is not None:
            self.tags = tags

    @property
    def build_manifest_version(self):
        r"""Gets the build_manifest_version of this ExtensionModuleProperties.

        构建清单版本

        :return: The build_manifest_version of this ExtensionModuleProperties.
        :rtype: str
        """
        return self._build_manifest_version

    @build_manifest_version.setter
    def build_manifest_version(self, build_manifest_version):
        r"""Sets the build_manifest_version of this ExtensionModuleProperties.

        构建清单版本

        :param build_manifest_version: The build_manifest_version of this ExtensionModuleProperties.
        :type build_manifest_version: str
        """
        self._build_manifest_version = build_manifest_version

    @property
    def name(self):
        r"""Gets the name of this ExtensionModuleProperties.

        名称

        :return: The name of this ExtensionModuleProperties.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExtensionModuleProperties.

        名称

        :param name: The name of this ExtensionModuleProperties.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ExtensionModuleProperties.

        描述

        :return: The description of this ExtensionModuleProperties.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ExtensionModuleProperties.

        描述

        :param description: The description of this ExtensionModuleProperties.
        :type description: str
        """
        self._description = description

    @property
    def uuid(self):
        r"""Gets the uuid of this ExtensionModuleProperties.

        任务uuid

        :return: The uuid of this ExtensionModuleProperties.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this ExtensionModuleProperties.

        任务uuid

        :param uuid: The uuid of this ExtensionModuleProperties.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def operation_system(self):
        r"""Gets the operation_system of this ExtensionModuleProperties.

        操作系统

        :return: The operation_system of this ExtensionModuleProperties.
        :rtype: str
        """
        return self._operation_system

    @operation_system.setter
    def operation_system(self, operation_system):
        r"""Sets the operation_system of this ExtensionModuleProperties.

        操作系统

        :param operation_system: The operation_system of this ExtensionModuleProperties.
        :type operation_system: str
        """
        self._operation_system = operation_system

    @property
    def image_source(self):
        r"""Gets the image_source of this ExtensionModuleProperties.

        镜像来源

        :return: The image_source of this ExtensionModuleProperties.
        :rtype: str
        """
        return self._image_source

    @image_source.setter
    def image_source(self, image_source):
        r"""Sets the image_source of this ExtensionModuleProperties.

        镜像来源

        :param image_source: The image_source of this ExtensionModuleProperties.
        :type image_source: str
        """
        self._image_source = image_source

    @property
    def image(self):
        r"""Gets the image of this ExtensionModuleProperties.

        镜像名

        :return: The image of this ExtensionModuleProperties.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this ExtensionModuleProperties.

        镜像名

        :param image: The image of this ExtensionModuleProperties.
        :type image: str
        """
        self._image = image

    @property
    def icon(self):
        r"""Gets the icon of this ExtensionModuleProperties.

        图标路径

        :return: The icon of this ExtensionModuleProperties.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        r"""Sets the icon of this ExtensionModuleProperties.

        图标路径

        :param icon: The icon of this ExtensionModuleProperties.
        :type icon: str
        """
        self._icon = icon

    @property
    def environment_variables(self):
        r"""Gets the environment_variables of this ExtensionModuleProperties.

        环境变量，按region映射。键为变量类别(如registry/mirror)，值为region到配置命令的映射。

        :return: The environment_variables of this ExtensionModuleProperties.
        :rtype: dict(str, dict(str, str))
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        r"""Sets the environment_variables of this ExtensionModuleProperties.

        环境变量，按region映射。键为变量类别(如registry/mirror)，值为region到配置命令的映射。

        :param environment_variables: The environment_variables of this ExtensionModuleProperties.
        :type environment_variables: dict(str, dict(str, str))
        """
        self._environment_variables = environment_variables

    @property
    def execution(self):
        r"""Gets the execution of this ExtensionModuleProperties.

        :return: The execution of this ExtensionModuleProperties.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionExecution`
        """
        return self._execution

    @execution.setter
    def execution(self, execution):
        r"""Sets the execution of this ExtensionModuleProperties.

        :param execution: The execution of this ExtensionModuleProperties.
        :type execution: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionExecution`
        """
        self._execution = execution

    @property
    def parameters(self):
        r"""Gets the parameters of this ExtensionModuleProperties.

        用户可配置参数列表。

        :return: The parameters of this ExtensionModuleProperties.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.ExtensionParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ExtensionModuleProperties.

        用户可配置参数列表。

        :param parameters: The parameters of this ExtensionModuleProperties.
        :type parameters: list[:class:`huaweicloudsdkcodeartspipeline.v2.ExtensionParameter`]
        """
        self._parameters = parameters

    @property
    def tags(self):
        r"""Gets the tags of this ExtensionModuleProperties.

        内部标签。

        :return: The tags of this ExtensionModuleProperties.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ExtensionModuleProperties.

        内部标签。

        :param tags: The tags of this ExtensionModuleProperties.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, ExtensionModuleProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
