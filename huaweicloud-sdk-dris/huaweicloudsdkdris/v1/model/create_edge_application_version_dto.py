# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeApplicationVersionDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'description': 'str',
        'container_settings': 'ContainerSettingsDTO',
        'command': 'object',
        'args': 'object'
    }

    attribute_map = {
        'version': 'version',
        'description': 'description',
        'container_settings': 'container_settings',
        'command': 'command',
        'args': 'args'
    }

    def __init__(self, version=None, description=None, container_settings=None, command=None, args=None):
        """CreateEdgeApplicationVersionDTO

        The model defined in huaweicloud sdk

        :param version: **参数说明**：应用版本。
        :type version: str
        :param description: **参数说明**：应用描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文引号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。
        :type description: str
        :param container_settings: 
        :type container_settings: :class:`huaweicloudsdkdris.v1.ContainerSettingsDTO`
        :param command: **参数说明**：启动命令。
        :type command: object
        :param args: **参数说明**：启动参数。
        :type args: object
        """
        
        

        self._version = None
        self._description = None
        self._container_settings = None
        self._command = None
        self._args = None
        self.discriminator = None

        self.version = version
        if description is not None:
            self.description = description
        self.container_settings = container_settings
        if command is not None:
            self.command = command
        if args is not None:
            self.args = args

    @property
    def version(self):
        """Gets the version of this CreateEdgeApplicationVersionDTO.

        **参数说明**：应用版本。

        :return: The version of this CreateEdgeApplicationVersionDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateEdgeApplicationVersionDTO.

        **参数说明**：应用版本。

        :param version: The version of this CreateEdgeApplicationVersionDTO.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        """Gets the description of this CreateEdgeApplicationVersionDTO.

        **参数说明**：应用描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文引号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :return: The description of this CreateEdgeApplicationVersionDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEdgeApplicationVersionDTO.

        **参数说明**：应用描述。  **取值范围**：只允许中文、字母、数字、下划线（_）、中文分号（；）、中文冒号（：）、中文问号（？）、中文感叹号（！）中文逗号（，）、中文句号（。）、英文引号（;）、英文冒号（:）、英文逗号（,）、英文句号（.）、英文问号（?）、英文感叹号（!）、顿号（、）、连接符（-）的组合。

        :param description: The description of this CreateEdgeApplicationVersionDTO.
        :type description: str
        """
        self._description = description

    @property
    def container_settings(self):
        """Gets the container_settings of this CreateEdgeApplicationVersionDTO.

        :return: The container_settings of this CreateEdgeApplicationVersionDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.ContainerSettingsDTO`
        """
        return self._container_settings

    @container_settings.setter
    def container_settings(self, container_settings):
        """Sets the container_settings of this CreateEdgeApplicationVersionDTO.

        :param container_settings: The container_settings of this CreateEdgeApplicationVersionDTO.
        :type container_settings: :class:`huaweicloudsdkdris.v1.ContainerSettingsDTO`
        """
        self._container_settings = container_settings

    @property
    def command(self):
        """Gets the command of this CreateEdgeApplicationVersionDTO.

        **参数说明**：启动命令。

        :return: The command of this CreateEdgeApplicationVersionDTO.
        :rtype: object
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this CreateEdgeApplicationVersionDTO.

        **参数说明**：启动命令。

        :param command: The command of this CreateEdgeApplicationVersionDTO.
        :type command: object
        """
        self._command = command

    @property
    def args(self):
        """Gets the args of this CreateEdgeApplicationVersionDTO.

        **参数说明**：启动参数。

        :return: The args of this CreateEdgeApplicationVersionDTO.
        :rtype: object
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this CreateEdgeApplicationVersionDTO.

        **参数说明**：启动参数。

        :param args: The args of this CreateEdgeApplicationVersionDTO.
        :type args: object
        """
        self._args = args

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateEdgeApplicationVersionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
