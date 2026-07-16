# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunArtifactSourceResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'commands': 'list[str]',
        'swr_instance_id': 'str'
    }

    attribute_map = {
        'url': 'url',
        'commands': 'commands',
        'swr_instance_id': 'swr_instance_id'
    }

    def __init__(self, url=None, commands=None, swr_instance_id=None):
        r"""CoreRunArtifactSourceResp

        The model defined in huaweicloud sdk

        :param url: **参数解释**: Agent镜像地址，用于运行时拉取镜像启动Agent服务。 **取值范围**: 长度为 1 - 2048 个字符。 
        :type url: str
        :param commands: **参数解释**: 启动镜像的命令。 **取值范围**: 最多 10 个元素，每个元素长度为 1 - 256 个字符。 
        :type commands: list[str]
        :param swr_instance_id: **参数解释**: SWR企业版实例ID。 **取值范围**: 匹配标准的UUID格式。
        :type swr_instance_id: str
        """
        
        

        self._url = None
        self._commands = None
        self._swr_instance_id = None
        self.discriminator = None

        self.url = url
        if commands is not None:
            self.commands = commands
        if swr_instance_id is not None:
            self.swr_instance_id = swr_instance_id

    @property
    def url(self):
        r"""Gets the url of this CoreRunArtifactSourceResp.

        **参数解释**: Agent镜像地址，用于运行时拉取镜像启动Agent服务。 **取值范围**: 长度为 1 - 2048 个字符。 

        :return: The url of this CoreRunArtifactSourceResp.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CoreRunArtifactSourceResp.

        **参数解释**: Agent镜像地址，用于运行时拉取镜像启动Agent服务。 **取值范围**: 长度为 1 - 2048 个字符。 

        :param url: The url of this CoreRunArtifactSourceResp.
        :type url: str
        """
        self._url = url

    @property
    def commands(self):
        r"""Gets the commands of this CoreRunArtifactSourceResp.

        **参数解释**: 启动镜像的命令。 **取值范围**: 最多 10 个元素，每个元素长度为 1 - 256 个字符。 

        :return: The commands of this CoreRunArtifactSourceResp.
        :rtype: list[str]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        r"""Sets the commands of this CoreRunArtifactSourceResp.

        **参数解释**: 启动镜像的命令。 **取值范围**: 最多 10 个元素，每个元素长度为 1 - 256 个字符。 

        :param commands: The commands of this CoreRunArtifactSourceResp.
        :type commands: list[str]
        """
        self._commands = commands

    @property
    def swr_instance_id(self):
        r"""Gets the swr_instance_id of this CoreRunArtifactSourceResp.

        **参数解释**: SWR企业版实例ID。 **取值范围**: 匹配标准的UUID格式。

        :return: The swr_instance_id of this CoreRunArtifactSourceResp.
        :rtype: str
        """
        return self._swr_instance_id

    @swr_instance_id.setter
    def swr_instance_id(self, swr_instance_id):
        r"""Sets the swr_instance_id of this CoreRunArtifactSourceResp.

        **参数解释**: SWR企业版实例ID。 **取值范围**: 匹配标准的UUID格式。

        :param swr_instance_id: The swr_instance_id of this CoreRunArtifactSourceResp.
        :type swr_instance_id: str
        """
        self._swr_instance_id = swr_instance_id

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
        if not isinstance(other, CoreRunArtifactSourceResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
