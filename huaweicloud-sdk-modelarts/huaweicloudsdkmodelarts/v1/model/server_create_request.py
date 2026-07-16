# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_pass': 'str',
        'arch': 'str',
        'availability_zone': 'str',
        'charging_info': 'ChargingInfo',
        'count': 'int',
        'enterprise_project_id': 'str',
        'flavor': 'str',
        'resource_flavor': 'str',
        'image_id': 'str',
        'key_pair_name': 'str',
        'name': 'str',
        'network': 'ServerNetwork',
        'root_volume': 'EvsVolume',
        'data_volume': 'ServerDataVolume',
        'server_type': 'str',
        'user_data': 'str',
        'hps_cluster_id': 'str'
    }

    attribute_map = {
        'admin_pass': 'admin_pass',
        'arch': 'arch',
        'availability_zone': 'availability_zone',
        'charging_info': 'charging_info',
        'count': 'count',
        'enterprise_project_id': 'enterprise_project_id',
        'flavor': 'flavor',
        'resource_flavor': 'resource_flavor',
        'image_id': 'image_id',
        'key_pair_name': 'key_pair_name',
        'name': 'name',
        'network': 'network',
        'root_volume': 'root_volume',
        'data_volume': 'data_volume',
        'server_type': 'server_type',
        'user_data': 'user_data',
        'hps_cluster_id': 'hps_cluster_id'
    }

    def __init__(self, admin_pass=None, arch=None, availability_zone=None, charging_info=None, count=None, enterprise_project_id=None, flavor=None, resource_flavor=None, image_id=None, key_pair_name=None, name=None, network=None, root_volume=None, data_volume=None, server_type=None, user_data=None, hps_cluster_id=None):
        r"""ServerCreateRequest

        The model defined in huaweicloud sdk

        :param admin_pass: **参数解释**：用于登录服务器的密码。admin_pass和key_pair_name必须二选一。密码规则： - 长度为8至26个字符 - 至少包含大写字母、小写字母、数字及特殊符号(!@%-_&#x3D;+[{}]:,./?)中的3种 - 不能与用户名或倒序的用户名相同 - 不能包含root或administrator及其逆序 **约束限制**：admin_pass和key_pair_name不能同时存在。 **取值范围**：长度为8至26个字符，满足上述密码规则。 **默认取值**：不涉及。
        :type admin_pass: str
        :param arch: **参数解释**：服务器规格架构类型。 **约束限制**：不涉及。 **取值范围**： - X86：CPU架构为X86 - ARM：CPU架构为ARM **默认取值**：不涉及。
        :type arch: str
        :param availability_zone: **参数解释**：服务器所在的可用区。 **约束限制**：不涉及。 **取值范围**：长度为1至256个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。
        :type availability_zone: str
        :param charging_info: 
        :type charging_info: :class:`huaweicloudsdkmodelarts.v1.ChargingInfo`
        :param count: **参数解释**：单次购买的服务器数量。 **约束限制**：不支持超节点。 **取值范围**：1至10。 **默认取值**：不涉及。
        :type count: int
        :param enterprise_project_id: **参数解释**：企业ID。 **约束限制**：不涉及。 **取值范围**：长度为1至36个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。
        :type enterprise_project_id: str
        :param flavor: **参数解释**：服务器规格名称。 **约束限制**：flavor和resource_flavor二选一。 **取值范围**：长度为1至128个字符。 **默认取值**：不涉及。
        :type flavor: str
        :param resource_flavor: **参数解释**：服务器资源规格名称。 **约束限制**：flavor和resource_flavor二选一。 **取值范围**：长度为1至256个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。
        :type resource_flavor: str
        :param image_id: **参数解释**：服务器镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为36个字符，符合UUID格式。 **默认取值**：不涉及。
        :type image_id: str
        :param key_pair_name: **参数解释**：服务器登录密钥对名称。admin_pass和key_pair_name必须二选一。注意超节点仅支持使用密钥对创建。 **约束限制**：admin_pass和key_pair_name不能同时存在。 **取值范围**：长度为1至64个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。
        :type key_pair_name: str
        :param name: **参数解释**：服务器名称。 **约束限制**：不涉及。 **取值范围**：长度为1至64个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。
        :type name: str
        :param network: 
        :type network: :class:`huaweicloudsdkmodelarts.v1.ServerNetwork`
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkmodelarts.v1.EvsVolume`
        :param data_volume: 
        :type data_volume: :class:`huaweicloudsdkmodelarts.v1.ServerDataVolume`
        :param server_type: **参数解释**：服务器类型。 **约束限制**：不涉及。 **取值范围**： - BMS：裸金属服务 - ECS：弹性云服务 - HPS：超节点服务 **默认取值**：不涉及。
        :type server_type: str
        :param user_data: **参数解释**： 创建云服务器过程中待注入实例自定义数据。支持注入文本、文本文件。 示例： base64编码前： * Linux服务器： &#x60;&#x60;&#x60;bash #!/bin/bash echo user_test &gt; /home/user.txt &#x60;&#x60;&#x60; base64编码后： * Linux服务器： &#x60;&#x60;&#x60;bash IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA&#x3D;&#x3D; &#x60;&#x60;&#x60; 了解更多实例自定义数据注入请参考[[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hc)[[用户数据注入](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hk)[ECS服务“通过实例自定义数据配置ECS实例”章节](tag:fcs,hcso)。 用户需明确user_data的使用效果，可能产生的影响和风险由用户自行承担。 **约束限制**： - user_data的值为base64编码之后的内容。 - 注入内容（编码之前的内容）最大长度为32K。  **取值范围**：不涉及。 **默认取值**：不涉及。
        :type user_data: str
        :param hps_cluster_id: **参数解释**：超节点集群网络信息。仅在创建超节点时需要该参数。 **约束限制**：仅用于创建HPS类型的服务器。 **取值范围**：长度为36个字符，符合UUID格式。 **默认取值**：不涉及。
        :type hps_cluster_id: str
        """
        
        

        self._admin_pass = None
        self._arch = None
        self._availability_zone = None
        self._charging_info = None
        self._count = None
        self._enterprise_project_id = None
        self._flavor = None
        self._resource_flavor = None
        self._image_id = None
        self._key_pair_name = None
        self._name = None
        self._network = None
        self._root_volume = None
        self._data_volume = None
        self._server_type = None
        self._user_data = None
        self._hps_cluster_id = None
        self.discriminator = None

        if admin_pass is not None:
            self.admin_pass = admin_pass
        if arch is not None:
            self.arch = arch
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if charging_info is not None:
            self.charging_info = charging_info
        if count is not None:
            self.count = count
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if flavor is not None:
            self.flavor = flavor
        if resource_flavor is not None:
            self.resource_flavor = resource_flavor
        self.image_id = image_id
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name
        self.name = name
        self.network = network
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volume is not None:
            self.data_volume = data_volume
        if server_type is not None:
            self.server_type = server_type
        if user_data is not None:
            self.user_data = user_data
        if hps_cluster_id is not None:
            self.hps_cluster_id = hps_cluster_id

    @property
    def admin_pass(self):
        r"""Gets the admin_pass of this ServerCreateRequest.

        **参数解释**：用于登录服务器的密码。admin_pass和key_pair_name必须二选一。密码规则： - 长度为8至26个字符 - 至少包含大写字母、小写字母、数字及特殊符号(!@%-_=+[{}]:,./?)中的3种 - 不能与用户名或倒序的用户名相同 - 不能包含root或administrator及其逆序 **约束限制**：admin_pass和key_pair_name不能同时存在。 **取值范围**：长度为8至26个字符，满足上述密码规则。 **默认取值**：不涉及。

        :return: The admin_pass of this ServerCreateRequest.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        r"""Sets the admin_pass of this ServerCreateRequest.

        **参数解释**：用于登录服务器的密码。admin_pass和key_pair_name必须二选一。密码规则： - 长度为8至26个字符 - 至少包含大写字母、小写字母、数字及特殊符号(!@%-_=+[{}]:,./?)中的3种 - 不能与用户名或倒序的用户名相同 - 不能包含root或administrator及其逆序 **约束限制**：admin_pass和key_pair_name不能同时存在。 **取值范围**：长度为8至26个字符，满足上述密码规则。 **默认取值**：不涉及。

        :param admin_pass: The admin_pass of this ServerCreateRequest.
        :type admin_pass: str
        """
        self._admin_pass = admin_pass

    @property
    def arch(self):
        r"""Gets the arch of this ServerCreateRequest.

        **参数解释**：服务器规格架构类型。 **约束限制**：不涉及。 **取值范围**： - X86：CPU架构为X86 - ARM：CPU架构为ARM **默认取值**：不涉及。

        :return: The arch of this ServerCreateRequest.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ServerCreateRequest.

        **参数解释**：服务器规格架构类型。 **约束限制**：不涉及。 **取值范围**： - X86：CPU架构为X86 - ARM：CPU架构为ARM **默认取值**：不涉及。

        :param arch: The arch of this ServerCreateRequest.
        :type arch: str
        """
        self._arch = arch

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ServerCreateRequest.

        **参数解释**：服务器所在的可用区。 **约束限制**：不涉及。 **取值范围**：长度为1至256个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :return: The availability_zone of this ServerCreateRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ServerCreateRequest.

        **参数解释**：服务器所在的可用区。 **约束限制**：不涉及。 **取值范围**：长度为1至256个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :param availability_zone: The availability_zone of this ServerCreateRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def charging_info(self):
        r"""Gets the charging_info of this ServerCreateRequest.

        :return: The charging_info of this ServerCreateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ChargingInfo`
        """
        return self._charging_info

    @charging_info.setter
    def charging_info(self, charging_info):
        r"""Sets the charging_info of this ServerCreateRequest.

        :param charging_info: The charging_info of this ServerCreateRequest.
        :type charging_info: :class:`huaweicloudsdkmodelarts.v1.ChargingInfo`
        """
        self._charging_info = charging_info

    @property
    def count(self):
        r"""Gets the count of this ServerCreateRequest.

        **参数解释**：单次购买的服务器数量。 **约束限制**：不支持超节点。 **取值范围**：1至10。 **默认取值**：不涉及。

        :return: The count of this ServerCreateRequest.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ServerCreateRequest.

        **参数解释**：单次购买的服务器数量。 **约束限制**：不支持超节点。 **取值范围**：1至10。 **默认取值**：不涉及。

        :param count: The count of this ServerCreateRequest.
        :type count: int
        """
        self._count = count

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ServerCreateRequest.

        **参数解释**：企业ID。 **约束限制**：不涉及。 **取值范围**：长度为1至36个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :return: The enterprise_project_id of this ServerCreateRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ServerCreateRequest.

        **参数解释**：企业ID。 **约束限制**：不涉及。 **取值范围**：长度为1至36个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :param enterprise_project_id: The enterprise_project_id of this ServerCreateRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def flavor(self):
        r"""Gets the flavor of this ServerCreateRequest.

        **参数解释**：服务器规格名称。 **约束限制**：flavor和resource_flavor二选一。 **取值范围**：长度为1至128个字符。 **默认取值**：不涉及。

        :return: The flavor of this ServerCreateRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ServerCreateRequest.

        **参数解释**：服务器规格名称。 **约束限制**：flavor和resource_flavor二选一。 **取值范围**：长度为1至128个字符。 **默认取值**：不涉及。

        :param flavor: The flavor of this ServerCreateRequest.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def resource_flavor(self):
        r"""Gets the resource_flavor of this ServerCreateRequest.

        **参数解释**：服务器资源规格名称。 **约束限制**：flavor和resource_flavor二选一。 **取值范围**：长度为1至256个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :return: The resource_flavor of this ServerCreateRequest.
        :rtype: str
        """
        return self._resource_flavor

    @resource_flavor.setter
    def resource_flavor(self, resource_flavor):
        r"""Sets the resource_flavor of this ServerCreateRequest.

        **参数解释**：服务器资源规格名称。 **约束限制**：flavor和resource_flavor二选一。 **取值范围**：长度为1至256个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :param resource_flavor: The resource_flavor of this ServerCreateRequest.
        :type resource_flavor: str
        """
        self._resource_flavor = resource_flavor

    @property
    def image_id(self):
        r"""Gets the image_id of this ServerCreateRequest.

        **参数解释**：服务器镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为36个字符，符合UUID格式。 **默认取值**：不涉及。

        :return: The image_id of this ServerCreateRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ServerCreateRequest.

        **参数解释**：服务器镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为36个字符，符合UUID格式。 **默认取值**：不涉及。

        :param image_id: The image_id of this ServerCreateRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def key_pair_name(self):
        r"""Gets the key_pair_name of this ServerCreateRequest.

        **参数解释**：服务器登录密钥对名称。admin_pass和key_pair_name必须二选一。注意超节点仅支持使用密钥对创建。 **约束限制**：admin_pass和key_pair_name不能同时存在。 **取值范围**：长度为1至64个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :return: The key_pair_name of this ServerCreateRequest.
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        r"""Sets the key_pair_name of this ServerCreateRequest.

        **参数解释**：服务器登录密钥对名称。admin_pass和key_pair_name必须二选一。注意超节点仅支持使用密钥对创建。 **约束限制**：admin_pass和key_pair_name不能同时存在。 **取值范围**：长度为1至64个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :param key_pair_name: The key_pair_name of this ServerCreateRequest.
        :type key_pair_name: str
        """
        self._key_pair_name = key_pair_name

    @property
    def name(self):
        r"""Gets the name of this ServerCreateRequest.

        **参数解释**：服务器名称。 **约束限制**：不涉及。 **取值范围**：长度为1至64个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :return: The name of this ServerCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServerCreateRequest.

        **参数解释**：服务器名称。 **约束限制**：不涉及。 **取值范围**：长度为1至64个字符，只能包含字母、数字、中划线、下划线和点。 **默认取值**：不涉及。

        :param name: The name of this ServerCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def network(self):
        r"""Gets the network of this ServerCreateRequest.

        :return: The network of this ServerCreateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServerNetwork`
        """
        return self._network

    @network.setter
    def network(self, network):
        r"""Sets the network of this ServerCreateRequest.

        :param network: The network of this ServerCreateRequest.
        :type network: :class:`huaweicloudsdkmodelarts.v1.ServerNetwork`
        """
        self._network = network

    @property
    def root_volume(self):
        r"""Gets the root_volume of this ServerCreateRequest.

        :return: The root_volume of this ServerCreateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.EvsVolume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this ServerCreateRequest.

        :param root_volume: The root_volume of this ServerCreateRequest.
        :type root_volume: :class:`huaweicloudsdkmodelarts.v1.EvsVolume`
        """
        self._root_volume = root_volume

    @property
    def data_volume(self):
        r"""Gets the data_volume of this ServerCreateRequest.

        :return: The data_volume of this ServerCreateRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServerDataVolume`
        """
        return self._data_volume

    @data_volume.setter
    def data_volume(self, data_volume):
        r"""Sets the data_volume of this ServerCreateRequest.

        :param data_volume: The data_volume of this ServerCreateRequest.
        :type data_volume: :class:`huaweicloudsdkmodelarts.v1.ServerDataVolume`
        """
        self._data_volume = data_volume

    @property
    def server_type(self):
        r"""Gets the server_type of this ServerCreateRequest.

        **参数解释**：服务器类型。 **约束限制**：不涉及。 **取值范围**： - BMS：裸金属服务 - ECS：弹性云服务 - HPS：超节点服务 **默认取值**：不涉及。

        :return: The server_type of this ServerCreateRequest.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ServerCreateRequest.

        **参数解释**：服务器类型。 **约束限制**：不涉及。 **取值范围**： - BMS：裸金属服务 - ECS：弹性云服务 - HPS：超节点服务 **默认取值**：不涉及。

        :param server_type: The server_type of this ServerCreateRequest.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def user_data(self):
        r"""Gets the user_data of this ServerCreateRequest.

        **参数解释**： 创建云服务器过程中待注入实例自定义数据。支持注入文本、文本文件。 示例： base64编码前： * Linux服务器： ```bash #!/bin/bash echo user_test > /home/user.txt ``` base64编码后： * Linux服务器： ```bash IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA== ``` 了解更多实例自定义数据注入请参考[[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hc)[[用户数据注入](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hk)[ECS服务“通过实例自定义数据配置ECS实例”章节](tag:fcs,hcso)。 用户需明确user_data的使用效果，可能产生的影响和风险由用户自行承担。 **约束限制**： - user_data的值为base64编码之后的内容。 - 注入内容（编码之前的内容）最大长度为32K。  **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The user_data of this ServerCreateRequest.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this ServerCreateRequest.

        **参数解释**： 创建云服务器过程中待注入实例自定义数据。支持注入文本、文本文件。 示例： base64编码前： * Linux服务器： ```bash #!/bin/bash echo user_test > /home/user.txt ``` base64编码后： * Linux服务器： ```bash IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA== ``` 了解更多实例自定义数据注入请参考[[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hc)[[用户数据注入](https://support.huaweicloud.com/intl/zh-cn/usermanual-ecs/zh-cn_topic_0032380449.html)](tag:hk)[ECS服务“通过实例自定义数据配置ECS实例”章节](tag:fcs,hcso)。 用户需明确user_data的使用效果，可能产生的影响和风险由用户自行承担。 **约束限制**： - user_data的值为base64编码之后的内容。 - 注入内容（编码之前的内容）最大长度为32K。  **取值范围**：不涉及。 **默认取值**：不涉及。

        :param user_data: The user_data of this ServerCreateRequest.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def hps_cluster_id(self):
        r"""Gets the hps_cluster_id of this ServerCreateRequest.

        **参数解释**：超节点集群网络信息。仅在创建超节点时需要该参数。 **约束限制**：仅用于创建HPS类型的服务器。 **取值范围**：长度为36个字符，符合UUID格式。 **默认取值**：不涉及。

        :return: The hps_cluster_id of this ServerCreateRequest.
        :rtype: str
        """
        return self._hps_cluster_id

    @hps_cluster_id.setter
    def hps_cluster_id(self, hps_cluster_id):
        r"""Sets the hps_cluster_id of this ServerCreateRequest.

        **参数解释**：超节点集群网络信息。仅在创建超节点时需要该参数。 **约束限制**：仅用于创建HPS类型的服务器。 **取值范围**：长度为36个字符，符合UUID格式。 **默认取值**：不涉及。

        :param hps_cluster_id: The hps_cluster_id of this ServerCreateRequest.
        :type hps_cluster_id: str
        """
        self._hps_cluster_id = hps_cluster_id

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
        if not isinstance(other, ServerCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
