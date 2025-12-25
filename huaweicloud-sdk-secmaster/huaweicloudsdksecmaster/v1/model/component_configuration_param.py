# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentConfigurationParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_id': 'str',
        'configuration_id': 'str',
        'file_name': 'str',
        'file_path': 'str',
        'file_type': 'str',
        'node_id': 'str',
        'param': 'str',
        'type': 'str',
        'version': 'int'
    }

    attribute_map = {
        'component_id': 'component_id',
        'configuration_id': 'configuration_id',
        'file_name': 'file_name',
        'file_path': 'file_path',
        'file_type': 'file_type',
        'node_id': 'node_id',
        'param': 'param',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, component_id=None, configuration_id=None, file_name=None, file_path=None, file_type=None, node_id=None, param=None, type=None, version=None):
        r"""ComponentConfigurationParam

        The model defined in huaweicloud sdk

        :param component_id: 组件id.
        :type component_id: str
        :param configuration_id: 配置ID
        :type configuration_id: str
        :param file_name: 文件名称
        :type file_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param file_type: **参数解释**: 文件类型 - JVM JVM配置文件类型 - LOG4J2 Log4j2日志配置文件类型 - YML YAML配置文件类型  **约束限制** 不涉及 **取值范围**: - JVM - LOG4J2 - YML   **默认值** 不涉及
        :type file_type: str
        :param node_id: 节点ID
        :type node_id: str
        :param param: 参数
        :type param: str
        :param type: **参数解释**: 配置类型 - HISTORY 历史版本 - CURRENT_SAVE 当前保存 - CURRENT_APPLY 当前使用  **约束限制** 不涉及 **取值范围**: - HISTORY - CURRENT_SAVE - CURRENT_APPLY  **默认值** 不涉及
        :type type: str
        :param version: 版本
        :type version: int
        """
        
        

        self._component_id = None
        self._configuration_id = None
        self._file_name = None
        self._file_path = None
        self._file_type = None
        self._node_id = None
        self._param = None
        self._type = None
        self._version = None
        self.discriminator = None

        if component_id is not None:
            self.component_id = component_id
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if file_type is not None:
            self.file_type = file_type
        if node_id is not None:
            self.node_id = node_id
        if param is not None:
            self.param = param
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def component_id(self):
        r"""Gets the component_id of this ComponentConfigurationParam.

        组件id.

        :return: The component_id of this ComponentConfigurationParam.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ComponentConfigurationParam.

        组件id.

        :param component_id: The component_id of this ComponentConfigurationParam.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def configuration_id(self):
        r"""Gets the configuration_id of this ComponentConfigurationParam.

        配置ID

        :return: The configuration_id of this ComponentConfigurationParam.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        r"""Sets the configuration_id of this ComponentConfigurationParam.

        配置ID

        :param configuration_id: The configuration_id of this ComponentConfigurationParam.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def file_name(self):
        r"""Gets the file_name of this ComponentConfigurationParam.

        文件名称

        :return: The file_name of this ComponentConfigurationParam.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ComponentConfigurationParam.

        文件名称

        :param file_name: The file_name of this ComponentConfigurationParam.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        r"""Gets the file_path of this ComponentConfigurationParam.

        文件路径

        :return: The file_path of this ComponentConfigurationParam.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ComponentConfigurationParam.

        文件路径

        :param file_path: The file_path of this ComponentConfigurationParam.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_type(self):
        r"""Gets the file_type of this ComponentConfigurationParam.

        **参数解释**: 文件类型 - JVM JVM配置文件类型 - LOG4J2 Log4j2日志配置文件类型 - YML YAML配置文件类型  **约束限制** 不涉及 **取值范围**: - JVM - LOG4J2 - YML   **默认值** 不涉及

        :return: The file_type of this ComponentConfigurationParam.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this ComponentConfigurationParam.

        **参数解释**: 文件类型 - JVM JVM配置文件类型 - LOG4J2 Log4j2日志配置文件类型 - YML YAML配置文件类型  **约束限制** 不涉及 **取值范围**: - JVM - LOG4J2 - YML   **默认值** 不涉及

        :param file_type: The file_type of this ComponentConfigurationParam.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def node_id(self):
        r"""Gets the node_id of this ComponentConfigurationParam.

        节点ID

        :return: The node_id of this ComponentConfigurationParam.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ComponentConfigurationParam.

        节点ID

        :param node_id: The node_id of this ComponentConfigurationParam.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def param(self):
        r"""Gets the param of this ComponentConfigurationParam.

        参数

        :return: The param of this ComponentConfigurationParam.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        r"""Sets the param of this ComponentConfigurationParam.

        参数

        :param param: The param of this ComponentConfigurationParam.
        :type param: str
        """
        self._param = param

    @property
    def type(self):
        r"""Gets the type of this ComponentConfigurationParam.

        **参数解释**: 配置类型 - HISTORY 历史版本 - CURRENT_SAVE 当前保存 - CURRENT_APPLY 当前使用  **约束限制** 不涉及 **取值范围**: - HISTORY - CURRENT_SAVE - CURRENT_APPLY  **默认值** 不涉及

        :return: The type of this ComponentConfigurationParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ComponentConfigurationParam.

        **参数解释**: 配置类型 - HISTORY 历史版本 - CURRENT_SAVE 当前保存 - CURRENT_APPLY 当前使用  **约束限制** 不涉及 **取值范围**: - HISTORY - CURRENT_SAVE - CURRENT_APPLY  **默认值** 不涉及

        :param type: The type of this ComponentConfigurationParam.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this ComponentConfigurationParam.

        版本

        :return: The version of this ComponentConfigurationParam.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ComponentConfigurationParam.

        版本

        :param version: The version of this ComponentConfigurationParam.
        :type version: int
        """
        self._version = version

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
        if not isinstance(other, ComponentConfigurationParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
