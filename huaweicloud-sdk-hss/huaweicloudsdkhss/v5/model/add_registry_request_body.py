# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddRegistryRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'registry_name': 'str',
        'registry_type': 'str',
        'api_version': 'str',
        'protocol': 'str',
        'registry_addr': 'str',
        'registry_username': 'str',
        'registry_password': 'str',
        'namespace': 'str',
        'connect_cluster_id': 'str',
        'get_scan_image_channel': 'str'
    }

    attribute_map = {
        'registry_name': 'registry_name',
        'registry_type': 'registry_type',
        'api_version': 'api_version',
        'protocol': 'protocol',
        'registry_addr': 'registry_addr',
        'registry_username': 'registry_username',
        'registry_password': 'registry_password',
        'namespace': 'namespace',
        'connect_cluster_id': 'connect_cluster_id',
        'get_scan_image_channel': 'get_scan_image_channel'
    }

    def __init__(self, registry_name=None, registry_type=None, api_version=None, protocol=None, registry_addr=None, registry_username=None, registry_password=None, namespace=None, connect_cluster_id=None, get_scan_image_channel=None):
        r"""AddRegistryRequestBody

        The model defined in huaweicloud sdk

        :param registry_name: **参数解释**： 仓库名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 
        :type registry_name: str
        :param registry_type: **参数解释**： 镜像仓类型 **约束限制**： 不涉及 **取值范围**：   - Harbor：Harbor镜像仓。   - Jfrog：Jfrog镜像仓。  **默认取值**： 不涉及 
        :type registry_type: str
        :param api_version: **参数解释**： 镜像仓接口版本 **约束限制**： 不涉及 **取值范围**：   - V1：V1版本。   - V2：V2版本。  **默认取值**： 不涉及 
        :type api_version: str
        :param protocol: **参数解释**： 协议类型 **约束限制**： 不涉及 **取值范围**：   - http：http协议。   - https：https协议。  **默认取值**： 不涉及 
        :type protocol: str
        :param registry_addr: **参数解释**： 镜像仓地址 **约束限制**： 网址/IP:端口。如：myharbor.com。 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 
        :type registry_addr: str
        :param registry_username: **参数解释**： 用于登录镜像仓的用户名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 
        :type registry_username: str
        :param registry_password: **参数解释**： 用于登录镜像仓的密码。仅用于访问镜像仓，HSS服务不会存储您的镜像仓密码。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 
        :type registry_password: str
        :param namespace: **参数解释**： 镜像仓项目,用来指定扫描组件要上传到的镜像仓目录。get_scan_image_channel为Other时需要填写。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 
        :type namespace: str
        :param connect_cluster_id: **参数解释**： 承载集群id。请选择一个已接入HSS的集群作为承载集群，镜像同步组件和扫描组件会以任务的方式运行在您所选的集群上，来帮助主机安全获取您的镜像数据和扫描镜像安全风险。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位  **默认取值**： 不涉及 
        :type connect_cluster_id: str
        :param get_scan_image_channel: **参数解释**： 获取扫描组件的方式 **约束限制**： 不涉及 **取值范围**： - Swr：访问swr获取扫描组件。 - Other：手动上传扫描组件到承载集群。选择此方式，需要调用接口/v5/{project_id}/image/registries/image-upload-command 获取扫描组件镜像上传指令。  **默认取值**： 不涉及 
        :type get_scan_image_channel: str
        """
        
        

        self._registry_name = None
        self._registry_type = None
        self._api_version = None
        self._protocol = None
        self._registry_addr = None
        self._registry_username = None
        self._registry_password = None
        self._namespace = None
        self._connect_cluster_id = None
        self._get_scan_image_channel = None
        self.discriminator = None

        self.registry_name = registry_name
        self.registry_type = registry_type
        self.api_version = api_version
        self.protocol = protocol
        self.registry_addr = registry_addr
        self.registry_username = registry_username
        self.registry_password = registry_password
        if namespace is not None:
            self.namespace = namespace
        self.connect_cluster_id = connect_cluster_id
        self.get_scan_image_channel = get_scan_image_channel

    @property
    def registry_name(self):
        r"""Gets the registry_name of this AddRegistryRequestBody.

        **参数解释**： 仓库名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :return: The registry_name of this AddRegistryRequestBody.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this AddRegistryRequestBody.

        **参数解释**： 仓库名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位 **默认取值**： 不涉及 

        :param registry_name: The registry_name of this AddRegistryRequestBody.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def registry_type(self):
        r"""Gets the registry_type of this AddRegistryRequestBody.

        **参数解释**： 镜像仓类型 **约束限制**： 不涉及 **取值范围**：   - Harbor：Harbor镜像仓。   - Jfrog：Jfrog镜像仓。  **默认取值**： 不涉及 

        :return: The registry_type of this AddRegistryRequestBody.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this AddRegistryRequestBody.

        **参数解释**： 镜像仓类型 **约束限制**： 不涉及 **取值范围**：   - Harbor：Harbor镜像仓。   - Jfrog：Jfrog镜像仓。  **默认取值**： 不涉及 

        :param registry_type: The registry_type of this AddRegistryRequestBody.
        :type registry_type: str
        """
        self._registry_type = registry_type

    @property
    def api_version(self):
        r"""Gets the api_version of this AddRegistryRequestBody.

        **参数解释**： 镜像仓接口版本 **约束限制**： 不涉及 **取值范围**：   - V1：V1版本。   - V2：V2版本。  **默认取值**： 不涉及 

        :return: The api_version of this AddRegistryRequestBody.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this AddRegistryRequestBody.

        **参数解释**： 镜像仓接口版本 **约束限制**： 不涉及 **取值范围**：   - V1：V1版本。   - V2：V2版本。  **默认取值**： 不涉及 

        :param api_version: The api_version of this AddRegistryRequestBody.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def protocol(self):
        r"""Gets the protocol of this AddRegistryRequestBody.

        **参数解释**： 协议类型 **约束限制**： 不涉及 **取值范围**：   - http：http协议。   - https：https协议。  **默认取值**： 不涉及 

        :return: The protocol of this AddRegistryRequestBody.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this AddRegistryRequestBody.

        **参数解释**： 协议类型 **约束限制**： 不涉及 **取值范围**：   - http：http协议。   - https：https协议。  **默认取值**： 不涉及 

        :param protocol: The protocol of this AddRegistryRequestBody.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def registry_addr(self):
        r"""Gets the registry_addr of this AddRegistryRequestBody.

        **参数解释**： 镜像仓地址 **约束限制**： 网址/IP:端口。如：myharbor.com。 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :return: The registry_addr of this AddRegistryRequestBody.
        :rtype: str
        """
        return self._registry_addr

    @registry_addr.setter
    def registry_addr(self, registry_addr):
        r"""Sets the registry_addr of this AddRegistryRequestBody.

        **参数解释**： 镜像仓地址 **约束限制**： 网址/IP:端口。如：myharbor.com。 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :param registry_addr: The registry_addr of this AddRegistryRequestBody.
        :type registry_addr: str
        """
        self._registry_addr = registry_addr

    @property
    def registry_username(self):
        r"""Gets the registry_username of this AddRegistryRequestBody.

        **参数解释**： 用于登录镜像仓的用户名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :return: The registry_username of this AddRegistryRequestBody.
        :rtype: str
        """
        return self._registry_username

    @registry_username.setter
    def registry_username(self, registry_username):
        r"""Sets the registry_username of this AddRegistryRequestBody.

        **参数解释**： 用于登录镜像仓的用户名。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :param registry_username: The registry_username of this AddRegistryRequestBody.
        :type registry_username: str
        """
        self._registry_username = registry_username

    @property
    def registry_password(self):
        r"""Gets the registry_password of this AddRegistryRequestBody.

        **参数解释**： 用于登录镜像仓的密码。仅用于访问镜像仓，HSS服务不会存储您的镜像仓密码。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :return: The registry_password of this AddRegistryRequestBody.
        :rtype: str
        """
        return self._registry_password

    @registry_password.setter
    def registry_password(self, registry_password):
        r"""Sets the registry_password of this AddRegistryRequestBody.

        **参数解释**： 用于登录镜像仓的密码。仅用于访问镜像仓，HSS服务不会存储您的镜像仓密码。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :param registry_password: The registry_password of this AddRegistryRequestBody.
        :type registry_password: str
        """
        self._registry_password = registry_password

    @property
    def namespace(self):
        r"""Gets the namespace of this AddRegistryRequestBody.

        **参数解释**： 镜像仓项目,用来指定扫描组件要上传到的镜像仓目录。get_scan_image_channel为Other时需要填写。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :return: The namespace of this AddRegistryRequestBody.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this AddRegistryRequestBody.

        **参数解释**： 镜像仓项目,用来指定扫描组件要上传到的镜像仓目录。get_scan_image_channel为Other时需要填写。 **约束限制**： 不涉及 **取值范围**： 字符长度1-128位  **默认取值**： 不涉及 

        :param namespace: The namespace of this AddRegistryRequestBody.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def connect_cluster_id(self):
        r"""Gets the connect_cluster_id of this AddRegistryRequestBody.

        **参数解释**： 承载集群id。请选择一个已接入HSS的集群作为承载集群，镜像同步组件和扫描组件会以任务的方式运行在您所选的集群上，来帮助主机安全获取您的镜像数据和扫描镜像安全风险。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位  **默认取值**： 不涉及 

        :return: The connect_cluster_id of this AddRegistryRequestBody.
        :rtype: str
        """
        return self._connect_cluster_id

    @connect_cluster_id.setter
    def connect_cluster_id(self, connect_cluster_id):
        r"""Sets the connect_cluster_id of this AddRegistryRequestBody.

        **参数解释**： 承载集群id。请选择一个已接入HSS的集群作为承载集群，镜像同步组件和扫描组件会以任务的方式运行在您所选的集群上，来帮助主机安全获取您的镜像数据和扫描镜像安全风险。 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位  **默认取值**： 不涉及 

        :param connect_cluster_id: The connect_cluster_id of this AddRegistryRequestBody.
        :type connect_cluster_id: str
        """
        self._connect_cluster_id = connect_cluster_id

    @property
    def get_scan_image_channel(self):
        r"""Gets the get_scan_image_channel of this AddRegistryRequestBody.

        **参数解释**： 获取扫描组件的方式 **约束限制**： 不涉及 **取值范围**： - Swr：访问swr获取扫描组件。 - Other：手动上传扫描组件到承载集群。选择此方式，需要调用接口/v5/{project_id}/image/registries/image-upload-command 获取扫描组件镜像上传指令。  **默认取值**： 不涉及 

        :return: The get_scan_image_channel of this AddRegistryRequestBody.
        :rtype: str
        """
        return self._get_scan_image_channel

    @get_scan_image_channel.setter
    def get_scan_image_channel(self, get_scan_image_channel):
        r"""Sets the get_scan_image_channel of this AddRegistryRequestBody.

        **参数解释**： 获取扫描组件的方式 **约束限制**： 不涉及 **取值范围**： - Swr：访问swr获取扫描组件。 - Other：手动上传扫描组件到承载集群。选择此方式，需要调用接口/v5/{project_id}/image/registries/image-upload-command 获取扫描组件镜像上传指令。  **默认取值**： 不涉及 

        :param get_scan_image_channel: The get_scan_image_channel of this AddRegistryRequestBody.
        :type get_scan_image_channel: str
        """
        self._get_scan_image_channel = get_scan_image_channel

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
        if not isinstance(other, AddRegistryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
