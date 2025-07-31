# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAntiVirusHostRequest:

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
        'host_id': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'group_id': 'str',
        'scan_type': 'str',
        'start_type': 'str',
        'policy_id': 'str',
        'next_start_time': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'group_id': 'group_id',
        'scan_type': 'scan_type',
        'start_type': 'start_type',
        'policy_id': 'policy_id',
        'next_start_time': 'next_start_time'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, host_id=None, host_name=None, private_ip=None, public_ip=None, group_id=None, scan_type=None, start_type=None, policy_id=None, next_start_time=None):
        r"""ListAntiVirusHostRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param group_id: 服务器组ID
        :type group_id: str
        :param scan_type: 任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描
        :type scan_type: str
        :param start_type: 启动类型，包含如下:   - now ：立即启动   - period : 周期启动
        :type start_type: str
        :param policy_id: 策略ID
        :type policy_id: str
        :param next_start_time: 下次启动时间，毫秒
        :type next_start_time: int
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._host_id = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._group_id = None
        self._scan_type = None
        self._start_type = None
        self._policy_id = None
        self._next_start_time = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if group_id is not None:
            self.group_id = group_id
        self.scan_type = scan_type
        self.start_type = start_type
        if policy_id is not None:
            self.policy_id = policy_id
        if next_start_time is not None:
            self.next_start_time = next_start_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAntiVirusHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListAntiVirusHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAntiVirusHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListAntiVirusHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAntiVirusHostRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListAntiVirusHostRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAntiVirusHostRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListAntiVirusHostRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAntiVirusHostRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListAntiVirusHostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAntiVirusHostRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListAntiVirusHostRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host_id(self):
        r"""Gets the host_id of this ListAntiVirusHostRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListAntiVirusHostRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListAntiVirusHostRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListAntiVirusHostRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ListAntiVirusHostRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListAntiVirusHostRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListAntiVirusHostRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListAntiVirusHostRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListAntiVirusHostRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ListAntiVirusHostRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListAntiVirusHostRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListAntiVirusHostRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListAntiVirusHostRequest.

        服务器公网IP

        :return: The public_ip of this ListAntiVirusHostRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListAntiVirusHostRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListAntiVirusHostRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def group_id(self):
        r"""Gets the group_id of this ListAntiVirusHostRequest.

        服务器组ID

        :return: The group_id of this ListAntiVirusHostRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListAntiVirusHostRequest.

        服务器组ID

        :param group_id: The group_id of this ListAntiVirusHostRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def scan_type(self):
        r"""Gets the scan_type of this ListAntiVirusHostRequest.

        任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描

        :return: The scan_type of this ListAntiVirusHostRequest.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this ListAntiVirusHostRequest.

        任务类型，包含如下:   - quick ：快速扫描   - full : 全盘扫描   - custom : 自定义扫描

        :param scan_type: The scan_type of this ListAntiVirusHostRequest.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def start_type(self):
        r"""Gets the start_type of this ListAntiVirusHostRequest.

        启动类型，包含如下:   - now ：立即启动   - period : 周期启动

        :return: The start_type of this ListAntiVirusHostRequest.
        :rtype: str
        """
        return self._start_type

    @start_type.setter
    def start_type(self, start_type):
        r"""Sets the start_type of this ListAntiVirusHostRequest.

        启动类型，包含如下:   - now ：立即启动   - period : 周期启动

        :param start_type: The start_type of this ListAntiVirusHostRequest.
        :type start_type: str
        """
        self._start_type = start_type

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListAntiVirusHostRequest.

        策略ID

        :return: The policy_id of this ListAntiVirusHostRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListAntiVirusHostRequest.

        策略ID

        :param policy_id: The policy_id of this ListAntiVirusHostRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def next_start_time(self):
        r"""Gets the next_start_time of this ListAntiVirusHostRequest.

        下次启动时间，毫秒

        :return: The next_start_time of this ListAntiVirusHostRequest.
        :rtype: int
        """
        return self._next_start_time

    @next_start_time.setter
    def next_start_time(self, next_start_time):
        r"""Sets the next_start_time of this ListAntiVirusHostRequest.

        下次启动时间，毫秒

        :param next_start_time: The next_start_time of this ListAntiVirusHostRequest.
        :type next_start_time: int
        """
        self._next_start_time = next_start_time

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
        if not isinstance(other, ListAntiVirusHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
