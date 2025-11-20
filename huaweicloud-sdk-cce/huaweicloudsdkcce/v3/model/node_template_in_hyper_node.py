# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeTemplateInHyperNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'az': 'str',
        'os': 'str',
        'login': 'Login',
        'root_volume': 'Volume',
        'data_volumes': 'list[Volume]',
        'storage': 'Storage',
        'k8s_tags': 'dict(str, str)',
        'runtime': 'Runtime',
        'extend_param': 'NodeExtendParam',
        'hostname_config': 'HostnameConfig'
    }

    attribute_map = {
        'az': 'az',
        'os': 'os',
        'login': 'login',
        'root_volume': 'rootVolume',
        'data_volumes': 'dataVolumes',
        'storage': 'storage',
        'k8s_tags': 'k8sTags',
        'runtime': 'runtime',
        'extend_param': 'extendParam',
        'hostname_config': 'hostnameConfig'
    }

    def __init__(self, az=None, os=None, login=None, root_volume=None, data_volumes=None, storage=None, k8s_tags=None, runtime=None, extend_param=None, hostname_config=None):
        r"""NodeTemplateInHyperNode

        The model defined in huaweicloud sdk

        :param az: **参数解释**： 超节点下节点所在的可用区。 [CCE支持的可用区请参考[地区和终端节点](https://console.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://console-intl.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws_hk)
        :type az: str
        :param os: **参数解释**： 超节点下节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](node-os.xml)。
        :type os: str
        :param login: 
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkcce.v3.Volume`
        :param data_volumes: **参数解释**： 节点的数据盘参数。
        :type data_volumes: list[:class:`huaweicloudsdkcce.v3.Volume`]
        :param storage: 
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        :param k8s_tags: **参数解释**： 超节点创建时下发到节点上的 k8s 标签，格式为key/value键值对。此接口中仅为展示作用。 示例： &#x60;&#x60;&#x60; \&quot;k8sTags\&quot;: {   \&quot;key\&quot;: \&quot;value\&quot; } &#x60;&#x60;&#x60;
        :type k8s_tags: dict(str, str)
        :param runtime: 
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.NodeExtendParam`
        :param hostname_config: 
        :type hostname_config: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        """
        
        

        self._az = None
        self._os = None
        self._login = None
        self._root_volume = None
        self._data_volumes = None
        self._storage = None
        self._k8s_tags = None
        self._runtime = None
        self._extend_param = None
        self._hostname_config = None
        self.discriminator = None

        if az is not None:
            self.az = az
        if os is not None:
            self.os = os
        if login is not None:
            self.login = login
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if storage is not None:
            self.storage = storage
        if k8s_tags is not None:
            self.k8s_tags = k8s_tags
        if runtime is not None:
            self.runtime = runtime
        if extend_param is not None:
            self.extend_param = extend_param
        if hostname_config is not None:
            self.hostname_config = hostname_config

    @property
    def az(self):
        r"""Gets the az of this NodeTemplateInHyperNode.

        **参数解释**： 超节点下节点所在的可用区。 [CCE支持的可用区请参考[地区和终端节点](https://console.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://console-intl.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws_hk)

        :return: The az of this NodeTemplateInHyperNode.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this NodeTemplateInHyperNode.

        **参数解释**： 超节点下节点所在的可用区。 [CCE支持的可用区请参考[地区和终端节点](https://console.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws) [CCE支持的可用区请参考[地区和终端节点](https://console-intl.huaweicloud.com/apiexplorer/#/endpoint/CCE)。](tag:hws_hk)

        :param az: The az of this NodeTemplateInHyperNode.
        :type az: str
        """
        self._az = az

    @property
    def os(self):
        r"""Gets the os of this NodeTemplateInHyperNode.

        **参数解释**： 超节点下节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](node-os.xml)。

        :return: The os of this NodeTemplateInHyperNode.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this NodeTemplateInHyperNode.

        **参数解释**： 超节点下节点的操作系统类型。具体支持的操作系统请参见[节点操作系统说明](node-os.xml)。

        :param os: The os of this NodeTemplateInHyperNode.
        :type os: str
        """
        self._os = os

    @property
    def login(self):
        r"""Gets the login of this NodeTemplateInHyperNode.

        :return: The login of this NodeTemplateInHyperNode.
        :rtype: :class:`huaweicloudsdkcce.v3.Login`
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this NodeTemplateInHyperNode.

        :param login: The login of this NodeTemplateInHyperNode.
        :type login: :class:`huaweicloudsdkcce.v3.Login`
        """
        self._login = login

    @property
    def root_volume(self):
        r"""Gets the root_volume of this NodeTemplateInHyperNode.

        :return: The root_volume of this NodeTemplateInHyperNode.
        :rtype: :class:`huaweicloudsdkcce.v3.Volume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this NodeTemplateInHyperNode.

        :param root_volume: The root_volume of this NodeTemplateInHyperNode.
        :type root_volume: :class:`huaweicloudsdkcce.v3.Volume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this NodeTemplateInHyperNode.

        **参数解释**： 节点的数据盘参数。

        :return: The data_volumes of this NodeTemplateInHyperNode.
        :rtype: list[:class:`huaweicloudsdkcce.v3.Volume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this NodeTemplateInHyperNode.

        **参数解释**： 节点的数据盘参数。

        :param data_volumes: The data_volumes of this NodeTemplateInHyperNode.
        :type data_volumes: list[:class:`huaweicloudsdkcce.v3.Volume`]
        """
        self._data_volumes = data_volumes

    @property
    def storage(self):
        r"""Gets the storage of this NodeTemplateInHyperNode.

        :return: The storage of this NodeTemplateInHyperNode.
        :rtype: :class:`huaweicloudsdkcce.v3.Storage`
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        r"""Sets the storage of this NodeTemplateInHyperNode.

        :param storage: The storage of this NodeTemplateInHyperNode.
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        """
        self._storage = storage

    @property
    def k8s_tags(self):
        r"""Gets the k8s_tags of this NodeTemplateInHyperNode.

        **参数解释**： 超节点创建时下发到节点上的 k8s 标签，格式为key/value键值对。此接口中仅为展示作用。 示例： ``` \"k8sTags\": {   \"key\": \"value\" } ```

        :return: The k8s_tags of this NodeTemplateInHyperNode.
        :rtype: dict(str, str)
        """
        return self._k8s_tags

    @k8s_tags.setter
    def k8s_tags(self, k8s_tags):
        r"""Sets the k8s_tags of this NodeTemplateInHyperNode.

        **参数解释**： 超节点创建时下发到节点上的 k8s 标签，格式为key/value键值对。此接口中仅为展示作用。 示例： ``` \"k8sTags\": {   \"key\": \"value\" } ```

        :param k8s_tags: The k8s_tags of this NodeTemplateInHyperNode.
        :type k8s_tags: dict(str, str)
        """
        self._k8s_tags = k8s_tags

    @property
    def runtime(self):
        r"""Gets the runtime of this NodeTemplateInHyperNode.

        :return: The runtime of this NodeTemplateInHyperNode.
        :rtype: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this NodeTemplateInHyperNode.

        :param runtime: The runtime of this NodeTemplateInHyperNode.
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        self._runtime = runtime

    @property
    def extend_param(self):
        r"""Gets the extend_param of this NodeTemplateInHyperNode.

        :return: The extend_param of this NodeTemplateInHyperNode.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this NodeTemplateInHyperNode.

        :param extend_param: The extend_param of this NodeTemplateInHyperNode.
        :type extend_param: :class:`huaweicloudsdkcce.v3.NodeExtendParam`
        """
        self._extend_param = extend_param

    @property
    def hostname_config(self):
        r"""Gets the hostname_config of this NodeTemplateInHyperNode.

        :return: The hostname_config of this NodeTemplateInHyperNode.
        :rtype: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        """
        return self._hostname_config

    @hostname_config.setter
    def hostname_config(self, hostname_config):
        r"""Sets the hostname_config of this NodeTemplateInHyperNode.

        :param hostname_config: The hostname_config of this NodeTemplateInHyperNode.
        :type hostname_config: :class:`huaweicloudsdkcce.v3.HostnameConfig`
        """
        self._hostname_config = hostname_config

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
        if not isinstance(other, NodeTemplateInHyperNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
