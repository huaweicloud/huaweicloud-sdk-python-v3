# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MeshSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str',
        'extend_params': 'MeshExtendParams',
        'ipv6_enable': 'bool',
        'tags': 'list[MeshTags]',
        'config': 'MeshConfig'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'extend_params': 'extendParams',
        'ipv6_enable': 'ipv6Enable',
        'tags': 'tags',
        'config': 'config'
    }

    def __init__(self, type=None, version=None, extend_params=None, ipv6_enable=None, tags=None, config=None):
        r"""MeshSpec

        The model defined in huaweicloud sdk

        :param type: 网格类型。 取值范围： - InCluster: 集群内控制平面形态，基础版网格取值为InCluster。目前仅支持该类型。
        :type type: str
        :param version: 网格版本。
        :type version: str
        :param extend_params: 
        :type extend_params: :class:`huaweicloudsdkasm.v1.MeshExtendParams`
        :param ipv6_enable: 网格是否支持IPV6
        :type ipv6_enable: bool
        :param tags: 网格资源标签。如果需要配置资源标签，请确认当前region的TMS服务已上线。
        :type tags: list[:class:`huaweicloudsdkasm.v1.MeshTags`]
        :param config: 
        :type config: :class:`huaweicloudsdkasm.v1.MeshConfig`
        """
        
        

        self._type = None
        self._version = None
        self._extend_params = None
        self._ipv6_enable = None
        self._tags = None
        self._config = None
        self.discriminator = None

        self.type = type
        self.version = version
        self.extend_params = extend_params
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable
        if tags is not None:
            self.tags = tags
        if config is not None:
            self.config = config

    @property
    def type(self):
        r"""Gets the type of this MeshSpec.

        网格类型。 取值范围： - InCluster: 集群内控制平面形态，基础版网格取值为InCluster。目前仅支持该类型。

        :return: The type of this MeshSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MeshSpec.

        网格类型。 取值范围： - InCluster: 集群内控制平面形态，基础版网格取值为InCluster。目前仅支持该类型。

        :param type: The type of this MeshSpec.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this MeshSpec.

        网格版本。

        :return: The version of this MeshSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this MeshSpec.

        网格版本。

        :param version: The version of this MeshSpec.
        :type version: str
        """
        self._version = version

    @property
    def extend_params(self):
        r"""Gets the extend_params of this MeshSpec.

        :return: The extend_params of this MeshSpec.
        :rtype: :class:`huaweicloudsdkasm.v1.MeshExtendParams`
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this MeshSpec.

        :param extend_params: The extend_params of this MeshSpec.
        :type extend_params: :class:`huaweicloudsdkasm.v1.MeshExtendParams`
        """
        self._extend_params = extend_params

    @property
    def ipv6_enable(self):
        r"""Gets the ipv6_enable of this MeshSpec.

        网格是否支持IPV6

        :return: The ipv6_enable of this MeshSpec.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        r"""Sets the ipv6_enable of this MeshSpec.

        网格是否支持IPV6

        :param ipv6_enable: The ipv6_enable of this MeshSpec.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

    @property
    def tags(self):
        r"""Gets the tags of this MeshSpec.

        网格资源标签。如果需要配置资源标签，请确认当前region的TMS服务已上线。

        :return: The tags of this MeshSpec.
        :rtype: list[:class:`huaweicloudsdkasm.v1.MeshTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this MeshSpec.

        网格资源标签。如果需要配置资源标签，请确认当前region的TMS服务已上线。

        :param tags: The tags of this MeshSpec.
        :type tags: list[:class:`huaweicloudsdkasm.v1.MeshTags`]
        """
        self._tags = tags

    @property
    def config(self):
        r"""Gets the config of this MeshSpec.

        :return: The config of this MeshSpec.
        :rtype: :class:`huaweicloudsdkasm.v1.MeshConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this MeshSpec.

        :param config: The config of this MeshSpec.
        :type config: :class:`huaweicloudsdkasm.v1.MeshConfig`
        """
        self._config = config

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
        if not isinstance(other, MeshSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
