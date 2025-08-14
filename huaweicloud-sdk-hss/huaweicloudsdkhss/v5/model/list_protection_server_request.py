# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectionServerRequest:

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
        'host_name': 'str',
        'os_type': 'str',
        'host_ip': 'str',
        'host_status': 'str',
        'last_days': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_name': 'host_name',
        'os_type': 'os_type',
        'host_ip': 'host_ip',
        'host_status': 'host_status',
        'last_days': 'last_days'
    }

    def __init__(self, region=None, enterprise_project_id=None, offset=None, limit=None, host_name=None, os_type=None, host_ip=None, host_status=None, last_days=None):
        r"""ListProtectionServerRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 取值0-2000000 **默认取值**: 0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param os_type: **参数解释**: 操作系统类型 **约束限制**: 不涉及 **取值范围**: 包含如下2种。   - Linux ：Linux。   - Windows ：Windows。 字符长度0-64 **默认取值**: 不涉及 
        :type os_type: str
        :param host_ip: **参数解释**: 服务器IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 
        :type host_ip: str
        :param host_status: **参数解释**: 主机状态 **约束限制**: 不涉及 **取值范围**: 包含如下3种。   - 不传参默认为全部。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。 **默认取值**: 不涉及 
        :type host_status: str
        :param last_days: **参数解释**: 查询时间范围天数 **约束限制**: 不涉及 **取值范围**: 长度1-30。若不填，则默认查询一天内的防护事件和已有备份数。 **默认取值**: 不涉及 
        :type last_days: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._host_name = None
        self._os_type = None
        self._host_ip = None
        self._host_status = None
        self._last_days = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if host_name is not None:
            self.host_name = host_name
        if os_type is not None:
            self.os_type = os_type
        if host_ip is not None:
            self.host_ip = host_ip
        if host_status is not None:
            self.host_status = host_status
        if last_days is not None:
            self.last_days = last_days

    @property
    def region(self):
        r"""Gets the region of this ListProtectionServerRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The region of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListProtectionServerRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param region: The region of this ListProtectionServerRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListProtectionServerRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListProtectionServerRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListProtectionServerRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListProtectionServerRequest.

        **参数解释**: 指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 取值0-2000000 **默认取值**: 0 

        :return: The offset of this ListProtectionServerRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProtectionServerRequest.

        **参数解释**: 指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 取值0-2000000 **默认取值**: 0 

        :param offset: The offset of this ListProtectionServerRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListProtectionServerRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListProtectionServerRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProtectionServerRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListProtectionServerRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host_name(self):
        r"""Gets the host_name of this ListProtectionServerRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListProtectionServerRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListProtectionServerRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def os_type(self):
        r"""Gets the os_type of this ListProtectionServerRequest.

        **参数解释**: 操作系统类型 **约束限制**: 不涉及 **取值范围**: 包含如下2种。   - Linux ：Linux。   - Windows ：Windows。 字符长度0-64 **默认取值**: 不涉及 

        :return: The os_type of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListProtectionServerRequest.

        **参数解释**: 操作系统类型 **约束限制**: 不涉及 **取值范围**: 包含如下2种。   - Linux ：Linux。   - Windows ：Windows。 字符长度0-64 **默认取值**: 不涉及 

        :param os_type: The os_type of this ListProtectionServerRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListProtectionServerRequest.

        **参数解释**: 服务器IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 

        :return: The host_ip of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListProtectionServerRequest.

        **参数解释**: 服务器IP地址 **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 

        :param host_ip: The host_ip of this ListProtectionServerRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_status(self):
        r"""Gets the host_status of this ListProtectionServerRequest.

        **参数解释**: 主机状态 **约束限制**: 不涉及 **取值范围**: 包含如下3种。   - 不传参默认为全部。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。 **默认取值**: 不涉及 

        :return: The host_status of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ListProtectionServerRequest.

        **参数解释**: 主机状态 **约束限制**: 不涉及 **取值范围**: 包含如下3种。   - 不传参默认为全部。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。 **默认取值**: 不涉及 

        :param host_status: The host_status of this ListProtectionServerRequest.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def last_days(self):
        r"""Gets the last_days of this ListProtectionServerRequest.

        **参数解释**: 查询时间范围天数 **约束限制**: 不涉及 **取值范围**: 长度1-30。若不填，则默认查询一天内的防护事件和已有备份数。 **默认取值**: 不涉及 

        :return: The last_days of this ListProtectionServerRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListProtectionServerRequest.

        **参数解释**: 查询时间范围天数 **约束限制**: 不涉及 **取值范围**: 长度1-30。若不填，则默认查询一天内的防护事件和已有备份数。 **默认取值**: 不涉及 

        :param last_days: The last_days of this ListProtectionServerRequest.
        :type last_days: int
        """
        self._last_days = last_days

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
        if not isinstance(other, ListProtectionServerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
