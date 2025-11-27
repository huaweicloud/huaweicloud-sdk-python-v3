# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWebTamperProtectionContainerRequest:

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
        'protection_config_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'host_name': 'str',
        'host_id': 'str',
        'host_private_ip': 'str',
        'container_name': 'str',
        'container_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'protection_config_id': 'protection_config_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'host_private_ip': 'host_private_ip',
        'container_name': 'container_name',
        'container_id': 'container_id',
        'status': 'status'
    }

    def __init__(self, enterprise_project_id=None, protection_config_id=None, offset=None, limit=None, host_name=None, host_id=None, host_private_ip=None, container_name=None, container_id=None, status=None):
        r"""ListWebTamperProtectionContainerRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param protection_config_id: **参数解释**: 防护配置id **约束限制**: 不涉及。 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type protection_config_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_id: str
        :param host_private_ip: **参数解释**: 主机私有IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type host_private_ip: str
        :param container_name: **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type container_name: str
        :param container_id: **参数解释**: 受影响容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type container_id: str
        :param status: **参数解释**: 防护状态 **约束限制**: 不涉及 **取值范围**: - protected：防护中 - partial_protected：部分防护 - protect_failed：防护失败 **默认取值**: 不涉及 
        :type status: str
        """
        
        

        self._enterprise_project_id = None
        self._protection_config_id = None
        self._offset = None
        self._limit = None
        self._host_name = None
        self._host_id = None
        self._host_private_ip = None
        self._container_name = None
        self._container_id = None
        self._status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.protection_config_id = protection_config_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if host_private_ip is not None:
            self.host_private_ip = host_private_ip
        if container_name is not None:
            self.container_name = container_name
        if container_id is not None:
            self.container_id = container_id
        if status is not None:
            self.status = status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListWebTamperProtectionContainerRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListWebTamperProtectionContainerRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def protection_config_id(self):
        r"""Gets the protection_config_id of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 防护配置id **约束限制**: 不涉及。 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The protection_config_id of this ListWebTamperProtectionContainerRequest.
        :rtype: str
        """
        return self._protection_config_id

    @protection_config_id.setter
    def protection_config_id(self, protection_config_id):
        r"""Sets the protection_config_id of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 防护配置id **约束限制**: 不涉及。 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param protection_config_id: The protection_config_id of this ListWebTamperProtectionContainerRequest.
        :type protection_config_id: str
        """
        self._protection_config_id = protection_config_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListWebTamperProtectionContainerRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListWebTamperProtectionContainerRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListWebTamperProtectionContainerRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListWebTamperProtectionContainerRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host_name(self):
        r"""Gets the host_name of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_name of this ListWebTamperProtectionContainerRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListWebTamperProtectionContainerRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_id of this ListWebTamperProtectionContainerRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListWebTamperProtectionContainerRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_private_ip(self):
        r"""Gets the host_private_ip of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 主机私有IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The host_private_ip of this ListWebTamperProtectionContainerRequest.
        :rtype: str
        """
        return self._host_private_ip

    @host_private_ip.setter
    def host_private_ip(self, host_private_ip):
        r"""Sets the host_private_ip of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 主机私有IP **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param host_private_ip: The host_private_ip of this ListWebTamperProtectionContainerRequest.
        :type host_private_ip: str
        """
        self._host_private_ip = host_private_ip

    @property
    def container_name(self):
        r"""Gets the container_name of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The container_name of this ListWebTamperProtectionContainerRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param container_name: The container_name of this ListWebTamperProtectionContainerRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_id(self):
        r"""Gets the container_id of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 受影响容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The container_id of this ListWebTamperProtectionContainerRequest.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 受影响容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param container_id: The container_id of this ListWebTamperProtectionContainerRequest.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def status(self):
        r"""Gets the status of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 防护状态 **约束限制**: 不涉及 **取值范围**: - protected：防护中 - partial_protected：部分防护 - protect_failed：防护失败 **默认取值**: 不涉及 

        :return: The status of this ListWebTamperProtectionContainerRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListWebTamperProtectionContainerRequest.

        **参数解释**: 防护状态 **约束限制**: 不涉及 **取值范围**: - protected：防护中 - partial_protected：部分防护 - protect_failed：防护失败 **默认取值**: 不涉及 

        :param status: The status of this ListWebTamperProtectionContainerRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListWebTamperProtectionContainerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
