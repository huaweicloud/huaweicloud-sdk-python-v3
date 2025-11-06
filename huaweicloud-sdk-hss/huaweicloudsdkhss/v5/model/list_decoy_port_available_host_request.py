# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDecoyPortAvailableHostRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'ports': 'str',
        'os_type': 'str',
        'policy_id': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'ports': 'ports',
        'os_type': 'os_type',
        'policy_id': 'policy_id'
    }

    def __init__(self, region=None, enterprise_project_id=None, offset=None, limit=None, ports=None, os_type=None, policy_id=None):
        r"""ListDecoyPortAvailableHostRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param ports: 要设置的端口号,以,分割
        :type ports: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。
        :type os_type: str
        :param policy_id: 策略id
        :type policy_id: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._ports = None
        self._os_type = None
        self._policy_id = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if ports is not None:
            self.ports = ports
        self.os_type = os_type
        if policy_id is not None:
            self.policy_id = policy_id

    @property
    def region(self):
        r"""Gets the region of this ListDecoyPortAvailableHostRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListDecoyPortAvailableHostRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListDecoyPortAvailableHostRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListDecoyPortAvailableHostRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListDecoyPortAvailableHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListDecoyPortAvailableHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListDecoyPortAvailableHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListDecoyPortAvailableHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListDecoyPortAvailableHostRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListDecoyPortAvailableHostRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDecoyPortAvailableHostRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListDecoyPortAvailableHostRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDecoyPortAvailableHostRequest.

        每页显示个数

        :return: The limit of this ListDecoyPortAvailableHostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDecoyPortAvailableHostRequest.

        每页显示个数

        :param limit: The limit of this ListDecoyPortAvailableHostRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def ports(self):
        r"""Gets the ports of this ListDecoyPortAvailableHostRequest.

        要设置的端口号,以,分割

        :return: The ports of this ListDecoyPortAvailableHostRequest.
        :rtype: str
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        r"""Sets the ports of this ListDecoyPortAvailableHostRequest.

        要设置的端口号,以,分割

        :param ports: The ports of this ListDecoyPortAvailableHostRequest.
        :type ports: str
        """
        self._ports = ports

    @property
    def os_type(self):
        r"""Gets the os_type of this ListDecoyPortAvailableHostRequest.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :return: The os_type of this ListDecoyPortAvailableHostRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListDecoyPortAvailableHostRequest.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :param os_type: The os_type of this ListDecoyPortAvailableHostRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListDecoyPortAvailableHostRequest.

        策略id

        :return: The policy_id of this ListDecoyPortAvailableHostRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListDecoyPortAvailableHostRequest.

        策略id

        :param policy_id: The policy_id of this ListDecoyPortAvailableHostRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

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
        if not isinstance(other, ListDecoyPortAvailableHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
