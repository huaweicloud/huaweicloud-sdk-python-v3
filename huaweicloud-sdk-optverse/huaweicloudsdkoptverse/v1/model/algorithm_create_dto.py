# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgorithmCreateDto:

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
        'build_command': 'str',
        'env': 'str',
        'command': 'str',
        'description': 'str',
        'picture': 'str',
        'lang': 'ProgramLang'
    }

    attribute_map = {
        'name': 'name',
        'build_command': 'build_command',
        'env': 'env',
        'command': 'command',
        'description': 'description',
        'picture': 'picture',
        'lang': 'lang'
    }

    def __init__(self, name=None, build_command=None, env=None, command=None, description=None, picture=None, lang=None):
        r"""AlgorithmCreateDto

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 算法名称 **约束限制**： 不涉及 **取值范围**： 长度[0,128] **默认取值**： 不涉及 
        :type name: str
        :param build_command: **参数解释**： 算法构建命令 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 不涉及 
        :type build_command: str
        :param env: **参数解释**： 算法预处理命令，bash脚本，python为pip install等预处理过程。 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 不涉及 
        :type env: str
        :param command: **参数解释**： 算法默认启动指令 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 不涉及 
        :type command: str
        :param description: **参数解释**： 算法描述。 **约束限制**： 不涉及 **取值范围**： 长度[0,32768] **默认取值**： 不涉及 
        :type description: str
        :param picture: **参数解释**： 算法项目的图标 **约束限制**： 不涉及 **取值范围**： [0,65536] **默认取值**： 无 
        :type picture: str
        :param lang: 
        :type lang: :class:`huaweicloudsdkoptverse.v1.ProgramLang`
        """
        
        

        self._name = None
        self._build_command = None
        self._env = None
        self._command = None
        self._description = None
        self._picture = None
        self._lang = None
        self.discriminator = None

        self.name = name
        if build_command is not None:
            self.build_command = build_command
        if env is not None:
            self.env = env
        if command is not None:
            self.command = command
        if description is not None:
            self.description = description
        if picture is not None:
            self.picture = picture
        self.lang = lang

    @property
    def name(self):
        r"""Gets the name of this AlgorithmCreateDto.

        **参数解释**： 算法名称 **约束限制**： 不涉及 **取值范围**： 长度[0,128] **默认取值**： 不涉及 

        :return: The name of this AlgorithmCreateDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlgorithmCreateDto.

        **参数解释**： 算法名称 **约束限制**： 不涉及 **取值范围**： 长度[0,128] **默认取值**： 不涉及 

        :param name: The name of this AlgorithmCreateDto.
        :type name: str
        """
        self._name = name

    @property
    def build_command(self):
        r"""Gets the build_command of this AlgorithmCreateDto.

        **参数解释**： 算法构建命令 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 不涉及 

        :return: The build_command of this AlgorithmCreateDto.
        :rtype: str
        """
        return self._build_command

    @build_command.setter
    def build_command(self, build_command):
        r"""Sets the build_command of this AlgorithmCreateDto.

        **参数解释**： 算法构建命令 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 不涉及 

        :param build_command: The build_command of this AlgorithmCreateDto.
        :type build_command: str
        """
        self._build_command = build_command

    @property
    def env(self):
        r"""Gets the env of this AlgorithmCreateDto.

        **参数解释**： 算法预处理命令，bash脚本，python为pip install等预处理过程。 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 不涉及 

        :return: The env of this AlgorithmCreateDto.
        :rtype: str
        """
        return self._env

    @env.setter
    def env(self, env):
        r"""Sets the env of this AlgorithmCreateDto.

        **参数解释**： 算法预处理命令，bash脚本，python为pip install等预处理过程。 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 不涉及 

        :param env: The env of this AlgorithmCreateDto.
        :type env: str
        """
        self._env = env

    @property
    def command(self):
        r"""Gets the command of this AlgorithmCreateDto.

        **参数解释**： 算法默认启动指令 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 不涉及 

        :return: The command of this AlgorithmCreateDto.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this AlgorithmCreateDto.

        **参数解释**： 算法默认启动指令 **约束限制**： 不涉及 **取值范围**： 长度[0,256] **默认取值**： 不涉及 

        :param command: The command of this AlgorithmCreateDto.
        :type command: str
        """
        self._command = command

    @property
    def description(self):
        r"""Gets the description of this AlgorithmCreateDto.

        **参数解释**： 算法描述。 **约束限制**： 不涉及 **取值范围**： 长度[0,32768] **默认取值**： 不涉及 

        :return: The description of this AlgorithmCreateDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlgorithmCreateDto.

        **参数解释**： 算法描述。 **约束限制**： 不涉及 **取值范围**： 长度[0,32768] **默认取值**： 不涉及 

        :param description: The description of this AlgorithmCreateDto.
        :type description: str
        """
        self._description = description

    @property
    def picture(self):
        r"""Gets the picture of this AlgorithmCreateDto.

        **参数解释**： 算法项目的图标 **约束限制**： 不涉及 **取值范围**： [0,65536] **默认取值**： 无 

        :return: The picture of this AlgorithmCreateDto.
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        r"""Sets the picture of this AlgorithmCreateDto.

        **参数解释**： 算法项目的图标 **约束限制**： 不涉及 **取值范围**： [0,65536] **默认取值**： 无 

        :param picture: The picture of this AlgorithmCreateDto.
        :type picture: str
        """
        self._picture = picture

    @property
    def lang(self):
        r"""Gets the lang of this AlgorithmCreateDto.

        :return: The lang of this AlgorithmCreateDto.
        :rtype: :class:`huaweicloudsdkoptverse.v1.ProgramLang`
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        r"""Sets the lang of this AlgorithmCreateDto.

        :param lang: The lang of this AlgorithmCreateDto.
        :type lang: :class:`huaweicloudsdkoptverse.v1.ProgramLang`
        """
        self._lang = lang

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
        if not isinstance(other, AlgorithmCreateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
