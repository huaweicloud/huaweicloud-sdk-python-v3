# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerSettingsReqDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configs': 'ContainerConfigsReqDTO',
        'custom_envs': 'object',
        'extra_hosts': 'object'
    }

    attribute_map = {
        'configs': 'configs',
        'custom_envs': 'custom_envs',
        'extra_hosts': 'extra_hosts'
    }

    def __init__(self, configs=None, custom_envs=None, extra_hosts=None):
        r"""ContainerSettingsReqDTO

        The model defined in huaweicloud sdk

        :param configs: 
        :type configs: :class:`huaweicloudsdkiotedge.v2.ContainerConfigsReqDTO`
        :param custom_envs: 自定义环境变量
        :type custom_envs: object
        :param extra_hosts: 域名解析配置集合。示例：[{\&quot;hostname\&quot;:\&quot;endpoint\&quot;,\&quot;ip\&quot;:\&quot;127.0.0.1\&quot;}]
        :type extra_hosts: object
        """
        
        

        self._configs = None
        self._custom_envs = None
        self._extra_hosts = None
        self.discriminator = None

        if configs is not None:
            self.configs = configs
        if custom_envs is not None:
            self.custom_envs = custom_envs
        if extra_hosts is not None:
            self.extra_hosts = extra_hosts

    @property
    def configs(self):
        r"""Gets the configs of this ContainerSettingsReqDTO.

        :return: The configs of this ContainerSettingsReqDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.ContainerConfigsReqDTO`
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        r"""Sets the configs of this ContainerSettingsReqDTO.

        :param configs: The configs of this ContainerSettingsReqDTO.
        :type configs: :class:`huaweicloudsdkiotedge.v2.ContainerConfigsReqDTO`
        """
        self._configs = configs

    @property
    def custom_envs(self):
        r"""Gets the custom_envs of this ContainerSettingsReqDTO.

        自定义环境变量

        :return: The custom_envs of this ContainerSettingsReqDTO.
        :rtype: object
        """
        return self._custom_envs

    @custom_envs.setter
    def custom_envs(self, custom_envs):
        r"""Sets the custom_envs of this ContainerSettingsReqDTO.

        自定义环境变量

        :param custom_envs: The custom_envs of this ContainerSettingsReqDTO.
        :type custom_envs: object
        """
        self._custom_envs = custom_envs

    @property
    def extra_hosts(self):
        r"""Gets the extra_hosts of this ContainerSettingsReqDTO.

        域名解析配置集合。示例：[{\"hostname\":\"endpoint\",\"ip\":\"127.0.0.1\"}]

        :return: The extra_hosts of this ContainerSettingsReqDTO.
        :rtype: object
        """
        return self._extra_hosts

    @extra_hosts.setter
    def extra_hosts(self, extra_hosts):
        r"""Sets the extra_hosts of this ContainerSettingsReqDTO.

        域名解析配置集合。示例：[{\"hostname\":\"endpoint\",\"ip\":\"127.0.0.1\"}]

        :param extra_hosts: The extra_hosts of this ContainerSettingsReqDTO.
        :type extra_hosts: object
        """
        self._extra_hosts = extra_hosts

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
        if not isinstance(other, ContainerSettingsReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
