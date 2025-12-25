# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'file_type': 'str',
        'node_id': 'str',
        'param': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_type': 'file_type',
        'node_id': 'node_id',
        'param': 'param',
        'type': 'type'
    }

    def __init__(self, file_name=None, file_type=None, node_id=None, param=None, type=None):
        r"""FileConfiguration

        The model defined in huaweicloud sdk

        :param file_name: 文件名称
        :type file_name: str
        :param file_type: **参数解释**: 文件类型 - JVM JVM配置文件类型 - LOG4J2 Log4j2日志配置文件类型 - YML YAML配置文件类型  **约束限制** 不涉及 **取值范围**: - JVM - LOG4J2 - YML   **默认值** 不涉及
        :type file_type: str
        :param node_id: 节点ID
        :type node_id: str
        :param param: 参数
        :type param: dict(str, str)
        :param type: **参数解释**: 配置类型 - HISTORY 历史版本 - CURRENT_SAVE 当前保存 - CURRENT_APPLY 当前使用  **约束限制** 不涉及 **取值范围**: - HISTORY - CURRENT_SAVE - CURRENT_APPLY  **默认值** 不涉及
        :type type: str
        """
        
        

        self._file_name = None
        self._file_type = None
        self._node_id = None
        self._param = None
        self._type = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        self.file_type = file_type
        if node_id is not None:
            self.node_id = node_id
        self.param = param
        if type is not None:
            self.type = type

    @property
    def file_name(self):
        r"""Gets the file_name of this FileConfiguration.

        文件名称

        :return: The file_name of this FileConfiguration.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this FileConfiguration.

        文件名称

        :param file_name: The file_name of this FileConfiguration.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        r"""Gets the file_type of this FileConfiguration.

        **参数解释**: 文件类型 - JVM JVM配置文件类型 - LOG4J2 Log4j2日志配置文件类型 - YML YAML配置文件类型  **约束限制** 不涉及 **取值范围**: - JVM - LOG4J2 - YML   **默认值** 不涉及

        :return: The file_type of this FileConfiguration.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this FileConfiguration.

        **参数解释**: 文件类型 - JVM JVM配置文件类型 - LOG4J2 Log4j2日志配置文件类型 - YML YAML配置文件类型  **约束限制** 不涉及 **取值范围**: - JVM - LOG4J2 - YML   **默认值** 不涉及

        :param file_type: The file_type of this FileConfiguration.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def node_id(self):
        r"""Gets the node_id of this FileConfiguration.

        节点ID

        :return: The node_id of this FileConfiguration.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this FileConfiguration.

        节点ID

        :param node_id: The node_id of this FileConfiguration.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def param(self):
        r"""Gets the param of this FileConfiguration.

        参数

        :return: The param of this FileConfiguration.
        :rtype: dict(str, str)
        """
        return self._param

    @param.setter
    def param(self, param):
        r"""Sets the param of this FileConfiguration.

        参数

        :param param: The param of this FileConfiguration.
        :type param: dict(str, str)
        """
        self._param = param

    @property
    def type(self):
        r"""Gets the type of this FileConfiguration.

        **参数解释**: 配置类型 - HISTORY 历史版本 - CURRENT_SAVE 当前保存 - CURRENT_APPLY 当前使用  **约束限制** 不涉及 **取值范围**: - HISTORY - CURRENT_SAVE - CURRENT_APPLY  **默认值** 不涉及

        :return: The type of this FileConfiguration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FileConfiguration.

        **参数解释**: 配置类型 - HISTORY 历史版本 - CURRENT_SAVE 当前保存 - CURRENT_APPLY 当前使用  **约束限制** 不涉及 **取值范围**: - HISTORY - CURRENT_SAVE - CURRENT_APPLY  **默认值** 不涉及

        :param type: The type of this FileConfiguration.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, FileConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
