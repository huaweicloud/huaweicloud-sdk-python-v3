# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWebTamperProtectionConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'type': 'str',
        'id': 'str',
        'web_app_name': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'protect_type': 'str',
        'status': 'str',
        'cluster_name': 'str',
        'cluster_id': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'host_private_ip': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'id': 'id',
        'web_app_name': 'web_app_name',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'protect_type': 'protect_type',
        'status': 'status',
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'host_private_ip': 'host_private_ip'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, type=None, id=None, web_app_name=None, image_name=None, image_version=None, protect_type=None, status=None, cluster_name=None, cluster_id=None, host_name=None, host_id=None, host_private_ip=None):
        r"""ListWebTamperProtectionConfigsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param type: **参数解释**: 网页防篡改类型 **约束限制**: 不涉及。 **取值范围**: - container_wtp：容器网页防篡改  **默认取值**: 不涉及 
        :type type: str
        :param id: **参数解释**: 网页防篡改配置ID **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type id: str
        :param web_app_name: **参数解释**: 网站应用的名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type web_app_name: str
        :param image_name: **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 
        :type image_name: str
        :param image_version: **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type image_version: str
        :param protect_type: **参数解释**: 防护类型 **约束限制**: 不涉及。 **取值范围**: - cluster：集群范围内防护 - host：主机范围内防护  **默认取值**: 不涉及 
        :type protect_type: str
        :param status: **参数解释**: 防护状态 **约束限制**: 不涉及。 **取值范围**: - not_protect：未防护 - protected：防护中 - partial_protected：部分防护 - protect_failed：防护失败 - redundant：防护冗余  **默认取值**: 不涉及 
        :type status: str
        :param cluster_name: **参数解释**: 集群名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type cluster_name: str
        :param cluster_id: **参数解释**： 集群id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 
        :type cluster_id: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_id: str
        :param host_private_ip: **参数解释**: 主机私有IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_private_ip: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._type = None
        self._id = None
        self._web_app_name = None
        self._image_name = None
        self._image_version = None
        self._protect_type = None
        self._status = None
        self._cluster_name = None
        self._cluster_id = None
        self._host_name = None
        self._host_id = None
        self._host_private_ip = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.type = type
        if id is not None:
            self.id = id
        if web_app_name is not None:
            self.web_app_name = web_app_name
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if protect_type is not None:
            self.protect_type = protect_type
        if status is not None:
            self.status = status
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if host_private_ip is not None:
            self.host_private_ip = host_private_ip

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListWebTamperProtectionConfigsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListWebTamperProtectionConfigsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListWebTamperProtectionConfigsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListWebTamperProtectionConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListWebTamperProtectionConfigsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        r"""Gets the type of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 网页防篡改类型 **约束限制**: 不涉及。 **取值范围**: - container_wtp：容器网页防篡改  **默认取值**: 不涉及 

        :return: The type of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 网页防篡改类型 **约束限制**: 不涉及。 **取值范围**: - container_wtp：容器网页防篡改  **默认取值**: 不涉及 

        :param type: The type of this ListWebTamperProtectionConfigsRequest.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        r"""Gets the id of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 网页防篡改配置ID **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The id of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 网页防篡改配置ID **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param id: The id of this ListWebTamperProtectionConfigsRequest.
        :type id: str
        """
        self._id = id

    @property
    def web_app_name(self):
        r"""Gets the web_app_name of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 网站应用的名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The web_app_name of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._web_app_name

    @web_app_name.setter
    def web_app_name(self, web_app_name):
        r"""Sets the web_app_name of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 网站应用的名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param web_app_name: The web_app_name of this ListWebTamperProtectionConfigsRequest.
        :type web_app_name: str
        """
        self._web_app_name = web_app_name

    @property
    def image_name(self):
        r"""Gets the image_name of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :return: The image_name of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :param image_name: The image_name of this ListWebTamperProtectionConfigsRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The image_version of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 镜像版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param image_version: The image_version of this ListWebTamperProtectionConfigsRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def protect_type(self):
        r"""Gets the protect_type of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 防护类型 **约束限制**: 不涉及。 **取值范围**: - cluster：集群范围内防护 - host：主机范围内防护  **默认取值**: 不涉及 

        :return: The protect_type of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        r"""Sets the protect_type of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 防护类型 **约束限制**: 不涉及。 **取值范围**: - cluster：集群范围内防护 - host：主机范围内防护  **默认取值**: 不涉及 

        :param protect_type: The protect_type of this ListWebTamperProtectionConfigsRequest.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def status(self):
        r"""Gets the status of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 防护状态 **约束限制**: 不涉及。 **取值范围**: - not_protect：未防护 - protected：防护中 - partial_protected：部分防护 - protect_failed：防护失败 - redundant：防护冗余  **默认取值**: 不涉及 

        :return: The status of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 防护状态 **约束限制**: 不涉及。 **取值范围**: - not_protect：未防护 - protected：防护中 - partial_protected：部分防护 - protect_failed：防护失败 - redundant：防护冗余  **默认取值**: 不涉及 

        :param status: The status of this ListWebTamperProtectionConfigsRequest.
        :type status: str
        """
        self._status = status

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 集群名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The cluster_name of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 集群名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param cluster_name: The cluster_name of this ListWebTamperProtectionConfigsRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListWebTamperProtectionConfigsRequest.

        **参数解释**： 集群id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 

        :return: The cluster_id of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListWebTamperProtectionConfigsRequest.

        **参数解释**： 集群id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位 **默认取值**： 不涉及 

        :param cluster_id: The cluster_id of this ListWebTamperProtectionConfigsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_name of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListWebTamperProtectionConfigsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_id of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListWebTamperProtectionConfigsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_private_ip(self):
        r"""Gets the host_private_ip of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 主机私有IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_private_ip of this ListWebTamperProtectionConfigsRequest.
        :rtype: str
        """
        return self._host_private_ip

    @host_private_ip.setter
    def host_private_ip(self, host_private_ip):
        r"""Sets the host_private_ip of this ListWebTamperProtectionConfigsRequest.

        **参数解释**: 主机私有IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_private_ip: The host_private_ip of this ListWebTamperProtectionConfigsRequest.
        :type host_private_ip: str
        """
        self._host_private_ip = host_private_ip

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
        if not isinstance(other, ListWebTamperProtectionConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
