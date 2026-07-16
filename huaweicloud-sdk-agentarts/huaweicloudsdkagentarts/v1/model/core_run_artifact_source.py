# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunArtifactSource:

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
        r"""CoreRunArtifactSource

        The model defined in huaweicloud sdk

        :param url: **参数解释**: Agent镜像地址，用于运行时拉取镜像启动Agent服务，可以通过SWR控制台以及SWR的镜像查询接口获取对应的镜像地址。 **约束限制**: 必须是一个有效的SWR镜像地址。 **取值范围**: 长度为 1 - 2048 个字符。 **默认取值**: 不涉及。 
        :type url: str
        :param commands: **参数解释**: 启动镜像的命令，示例：python main.py --port&#x3D;8080。 **约束限制**: 不涉及。 **取值范围**: 最多 10 个元素，每个元素长度为 1 - 256 个字符。 **默认取值**: 不涉及。 
        :type commands: list[str]
        :param swr_instance_id: **参数解释**: SWR企业版实例ID。 **约束限制**: 不涉及。 **取值范围**: 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值**: 不涉及。
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
        r"""Gets the url of this CoreRunArtifactSource.

        **参数解释**: Agent镜像地址，用于运行时拉取镜像启动Agent服务，可以通过SWR控制台以及SWR的镜像查询接口获取对应的镜像地址。 **约束限制**: 必须是一个有效的SWR镜像地址。 **取值范围**: 长度为 1 - 2048 个字符。 **默认取值**: 不涉及。 

        :return: The url of this CoreRunArtifactSource.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CoreRunArtifactSource.

        **参数解释**: Agent镜像地址，用于运行时拉取镜像启动Agent服务，可以通过SWR控制台以及SWR的镜像查询接口获取对应的镜像地址。 **约束限制**: 必须是一个有效的SWR镜像地址。 **取值范围**: 长度为 1 - 2048 个字符。 **默认取值**: 不涉及。 

        :param url: The url of this CoreRunArtifactSource.
        :type url: str
        """
        self._url = url

    @property
    def commands(self):
        r"""Gets the commands of this CoreRunArtifactSource.

        **参数解释**: 启动镜像的命令，示例：python main.py --port=8080。 **约束限制**: 不涉及。 **取值范围**: 最多 10 个元素，每个元素长度为 1 - 256 个字符。 **默认取值**: 不涉及。 

        :return: The commands of this CoreRunArtifactSource.
        :rtype: list[str]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        r"""Sets the commands of this CoreRunArtifactSource.

        **参数解释**: 启动镜像的命令，示例：python main.py --port=8080。 **约束限制**: 不涉及。 **取值范围**: 最多 10 个元素，每个元素长度为 1 - 256 个字符。 **默认取值**: 不涉及。 

        :param commands: The commands of this CoreRunArtifactSource.
        :type commands: list[str]
        """
        self._commands = commands

    @property
    def swr_instance_id(self):
        r"""Gets the swr_instance_id of this CoreRunArtifactSource.

        **参数解释**: SWR企业版实例ID。 **约束限制**: 不涉及。 **取值范围**: 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值**: 不涉及。

        :return: The swr_instance_id of this CoreRunArtifactSource.
        :rtype: str
        """
        return self._swr_instance_id

    @swr_instance_id.setter
    def swr_instance_id(self, swr_instance_id):
        r"""Sets the swr_instance_id of this CoreRunArtifactSource.

        **参数解释**: SWR企业版实例ID。 **约束限制**: 不涉及。 **取值范围**: 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值**: 不涉及。

        :param swr_instance_id: The swr_instance_id of this CoreRunArtifactSource.
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
        if not isinstance(other, CoreRunArtifactSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
