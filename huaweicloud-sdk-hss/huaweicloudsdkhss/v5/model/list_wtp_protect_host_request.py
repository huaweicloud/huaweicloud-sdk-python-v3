# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWtpProtectHostRequest:

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
        'region': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'group_name': 'str',
        'os_type': 'str',
        'asset_value': 'str',
        'offset': 'int',
        'limit': 'int',
        'protect_status': 'str',
        'wtp_status': 'str',
        'agent_status': 'str',
        'rasp_status': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'region': 'region',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'group_name': 'group_name',
        'os_type': 'os_type',
        'asset_value': 'asset_value',
        'offset': 'offset',
        'limit': 'limit',
        'protect_status': 'protect_status',
        'wtp_status': 'wtp_status',
        'agent_status': 'agent_status',
        'rasp_status': 'rasp_status'
    }

    def __init__(self, enterprise_project_id=None, region=None, host_name=None, host_id=None, public_ip=None, private_ip=None, group_name=None, os_type=None, asset_value=None, offset=None, limit=None, protect_status=None, wtp_status=None, agent_status=None, rasp_status=None):
        r"""ListWtpProtectHostRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux：Linux。   - Windows：Windows。
        :type os_type: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param protect_status: **参数解释**: 网页防篡改防护开启状态 **约束限制**: 不涉及 **取值范围**: - opened ：已开启网页防篡改防护。  **默认取值**: 不涉及 
        :type protect_status: str
        :param wtp_status: **参数解释**: 网页防篡改详细防护状态 **约束限制**: 不涉及 **取值范围**: - opened : 防护中。 - opening : 开启中。 - open_failed : 防护失败。 - partial_protection : 部分防护。 - protection_interruption : 防护中断。  **默认取值**: 不涉及 
        :type wtp_status: str
        :param agent_status: **参数解释**: Agent状态 **约束限制**: 不涉及 **取值范围**: - not_installed : agent未安装。 - online : agent在线。 - offline : agent不在线。  **默认取值**: 不涉及 
        :type agent_status: str
        :param rasp_status: **参数解释**: 动态网页防篡改防护开启状态 **约束限制**: 不涉及 **取值范围**: - opened ：已开启动态网页防篡改防护。 - closed ：未开启动态网页防篡改防护。  **默认取值**: 不涉及 
        :type rasp_status: str
        """
        
        

        self._enterprise_project_id = None
        self._region = None
        self._host_name = None
        self._host_id = None
        self._public_ip = None
        self._private_ip = None
        self._group_name = None
        self._os_type = None
        self._asset_value = None
        self._offset = None
        self._limit = None
        self._protect_status = None
        self._wtp_status = None
        self._agent_status = None
        self._rasp_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if region is not None:
            self.region = region
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if group_name is not None:
            self.group_name = group_name
        if os_type is not None:
            self.os_type = os_type
        if asset_value is not None:
            self.asset_value = asset_value
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if protect_status is not None:
            self.protect_status = protect_status
        if wtp_status is not None:
            self.wtp_status = wtp_status
        if agent_status is not None:
            self.agent_status = agent_status
        if rasp_status is not None:
            self.rasp_status = rasp_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWtpProtectHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWtpProtectHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListWtpProtectHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def region(self):
        r"""Gets the region of this ListWtpProtectHostRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListWtpProtectHostRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListWtpProtectHostRequest.
        :type region: str
        """
        self._region = region

    @property
    def host_name(self):
        r"""Gets the host_name of this ListWtpProtectHostRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListWtpProtectHostRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListWtpProtectHostRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListWtpProtectHostRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListWtpProtectHostRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListWtpProtectHostRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListWtpProtectHostRequest.

        服务器公网IP

        :return: The public_ip of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListWtpProtectHostRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListWtpProtectHostRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListWtpProtectHostRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListWtpProtectHostRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ListWtpProtectHostRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def group_name(self):
        r"""Gets the group_name of this ListWtpProtectHostRequest.

        服务器组名称

        :return: The group_name of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListWtpProtectHostRequest.

        服务器组名称

        :param group_name: The group_name of this ListWtpProtectHostRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def os_type(self):
        r"""Gets the os_type of this ListWtpProtectHostRequest.

        操作系统类型，包含如下2种。   - Linux：Linux。   - Windows：Windows。

        :return: The os_type of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListWtpProtectHostRequest.

        操作系统类型，包含如下2种。   - Linux：Linux。   - Windows：Windows。

        :param os_type: The os_type of this ListWtpProtectHostRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListWtpProtectHostRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListWtpProtectHostRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ListWtpProtectHostRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def offset(self):
        r"""Gets the offset of this ListWtpProtectHostRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListWtpProtectHostRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWtpProtectHostRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListWtpProtectHostRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWtpProtectHostRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListWtpProtectHostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWtpProtectHostRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListWtpProtectHostRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ListWtpProtectHostRequest.

        **参数解释**: 网页防篡改防护开启状态 **约束限制**: 不涉及 **取值范围**: - opened ：已开启网页防篡改防护。  **默认取值**: 不涉及 

        :return: The protect_status of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ListWtpProtectHostRequest.

        **参数解释**: 网页防篡改防护开启状态 **约束限制**: 不涉及 **取值范围**: - opened ：已开启网页防篡改防护。  **默认取值**: 不涉及 

        :param protect_status: The protect_status of this ListWtpProtectHostRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def wtp_status(self):
        r"""Gets the wtp_status of this ListWtpProtectHostRequest.

        **参数解释**: 网页防篡改详细防护状态 **约束限制**: 不涉及 **取值范围**: - opened : 防护中。 - opening : 开启中。 - open_failed : 防护失败。 - partial_protection : 部分防护。 - protection_interruption : 防护中断。  **默认取值**: 不涉及 

        :return: The wtp_status of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._wtp_status

    @wtp_status.setter
    def wtp_status(self, wtp_status):
        r"""Sets the wtp_status of this ListWtpProtectHostRequest.

        **参数解释**: 网页防篡改详细防护状态 **约束限制**: 不涉及 **取值范围**: - opened : 防护中。 - opening : 开启中。 - open_failed : 防护失败。 - partial_protection : 部分防护。 - protection_interruption : 防护中断。  **默认取值**: 不涉及 

        :param wtp_status: The wtp_status of this ListWtpProtectHostRequest.
        :type wtp_status: str
        """
        self._wtp_status = wtp_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ListWtpProtectHostRequest.

        **参数解释**: Agent状态 **约束限制**: 不涉及 **取值范围**: - not_installed : agent未安装。 - online : agent在线。 - offline : agent不在线。  **默认取值**: 不涉及 

        :return: The agent_status of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ListWtpProtectHostRequest.

        **参数解释**: Agent状态 **约束限制**: 不涉及 **取值范围**: - not_installed : agent未安装。 - online : agent在线。 - offline : agent不在线。  **默认取值**: 不涉及 

        :param agent_status: The agent_status of this ListWtpProtectHostRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def rasp_status(self):
        r"""Gets the rasp_status of this ListWtpProtectHostRequest.

        **参数解释**: 动态网页防篡改防护开启状态 **约束限制**: 不涉及 **取值范围**: - opened ：已开启动态网页防篡改防护。 - closed ：未开启动态网页防篡改防护。  **默认取值**: 不涉及 

        :return: The rasp_status of this ListWtpProtectHostRequest.
        :rtype: str
        """
        return self._rasp_status

    @rasp_status.setter
    def rasp_status(self, rasp_status):
        r"""Sets the rasp_status of this ListWtpProtectHostRequest.

        **参数解释**: 动态网页防篡改防护开启状态 **约束限制**: 不涉及 **取值范围**: - opened ：已开启动态网页防篡改防护。 - closed ：未开启动态网页防篡改防护。  **默认取值**: 不涉及 

        :param rasp_status: The rasp_status of this ListWtpProtectHostRequest.
        :type rasp_status: str
        """
        self._rasp_status = rasp_status

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
        if not isinstance(other, ListWtpProtectHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
