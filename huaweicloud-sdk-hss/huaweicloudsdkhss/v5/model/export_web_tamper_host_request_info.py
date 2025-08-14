# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportWebTamperHostRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_id_list': 'list[str]',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'agent_id': 'str',
        'os_type': 'str',
        'asset_value': 'str',
        'group_name': 'str',
        'protect_status': 'str',
        'agent_status': 'str',
        'rasp_protect_status': 'str',
        'wtp_status': 'str',
        'offset': 'int',
        'limit': 'int',
        'export_size': 'int',
        'export_headers': 'list[list[str]]'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_id_list': 'host_id_list',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'agent_id': 'agent_id',
        'os_type': 'os_type',
        'asset_value': 'asset_value',
        'group_name': 'group_name',
        'protect_status': 'protect_status',
        'agent_status': 'agent_status',
        'rasp_protect_status': 'rasp_protect_status',
        'wtp_status': 'wtp_status',
        'offset': 'offset',
        'limit': 'limit',
        'export_size': 'export_size',
        'export_headers': 'export_headers'
    }

    def __init__(self, host_id=None, host_id_list=None, host_name=None, public_ip=None, private_ip=None, agent_id=None, os_type=None, asset_value=None, group_name=None, protect_status=None, agent_status=None, rasp_protect_status=None, wtp_status=None, offset=None, limit=None, export_size=None, export_headers=None):
        r"""ExportWebTamperHostRequestInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_id_list: 主机ID数组
        :type host_id_list: list[str]
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param agent_id: **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_id: str
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 
        :type os_type: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param group_name: **参数解释**: 服务器组名称 **取值范围**: 字符长度0-256位 
        :type group_name: str
        :param protect_status: 防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。
        :type protect_status: str
        :param agent_status: Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。
        :type agent_status: str
        :param rasp_protect_status: 动态网页防篡改防护状态   - opened : 防护中   - closed : 未防护
        :type rasp_protect_status: str
        :param wtp_status: 防护状态   - closed : 未防护   - opened : 防护中   - open_failed : 防护失败   - opening : 正在开启   - partial_protection : 部分防护
        :type wtp_status: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param export_size: 导出数据条数
        :type export_size: int
        :param export_headers: 导出表头集合
        :type export_headers: list[list[str]]
        """
        
        

        self._host_id = None
        self._host_id_list = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._agent_id = None
        self._os_type = None
        self._asset_value = None
        self._group_name = None
        self._protect_status = None
        self._agent_status = None
        self._rasp_protect_status = None
        self._wtp_status = None
        self._offset = None
        self._limit = None
        self._export_size = None
        self._export_headers = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_id_list is not None:
            self.host_id_list = host_id_list
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if agent_id is not None:
            self.agent_id = agent_id
        if os_type is not None:
            self.os_type = os_type
        if asset_value is not None:
            self.asset_value = asset_value
        if group_name is not None:
            self.group_name = group_name
        if protect_status is not None:
            self.protect_status = protect_status
        if agent_status is not None:
            self.agent_status = agent_status
        if rasp_protect_status is not None:
            self.rasp_protect_status = rasp_protect_status
        if wtp_status is not None:
            self.wtp_status = wtp_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if export_size is not None:
            self.export_size = export_size
        if export_headers is not None:
            self.export_headers = export_headers

    @property
    def host_id(self):
        r"""Gets the host_id of this ExportWebTamperHostRequestInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ExportWebTamperHostRequestInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this ExportWebTamperHostRequestInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this ExportWebTamperHostRequestInfo.

        主机ID数组

        :return: The host_id_list of this ExportWebTamperHostRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this ExportWebTamperHostRequestInfo.

        主机ID数组

        :param host_id_list: The host_id_list of this ExportWebTamperHostRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def host_name(self):
        r"""Gets the host_name of this ExportWebTamperHostRequestInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ExportWebTamperHostRequestInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this ExportWebTamperHostRequestInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ExportWebTamperHostRequestInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ExportWebTamperHostRequestInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this ExportWebTamperHostRequestInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ExportWebTamperHostRequestInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ExportWebTamperHostRequestInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this ExportWebTamperHostRequestInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ExportWebTamperHostRequestInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_id of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ExportWebTamperHostRequestInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this ExportWebTamperHostRequestInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def os_type(self):
        r"""Gets the os_type of this ExportWebTamperHostRequestInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :return: The os_type of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ExportWebTamperHostRequestInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :param os_type: The os_type of this ExportWebTamperHostRequestInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ExportWebTamperHostRequestInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ExportWebTamperHostRequestInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ExportWebTamperHostRequestInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def group_name(self):
        r"""Gets the group_name of this ExportWebTamperHostRequestInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符长度0-256位 

        :return: The group_name of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ExportWebTamperHostRequestInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符长度0-256位 

        :param group_name: The group_name of this ExportWebTamperHostRequestInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ExportWebTamperHostRequestInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :return: The protect_status of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ExportWebTamperHostRequestInfo.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :param protect_status: The protect_status of this ExportWebTamperHostRequestInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ExportWebTamperHostRequestInfo.

        Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。

        :return: The agent_status of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ExportWebTamperHostRequestInfo.

        Agent状态，包含如下6种。   - installed ：已安装。   - not_installed ：未安装。   - online ：在线。   - offline ：离线。   - install_failed ：安装失败。   - installing ：安装中。   - not_online ：不在线的（除了在线以外的所有状态，仅作为查询条件）。

        :param agent_status: The agent_status of this ExportWebTamperHostRequestInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def rasp_protect_status(self):
        r"""Gets the rasp_protect_status of this ExportWebTamperHostRequestInfo.

        动态网页防篡改防护状态   - opened : 防护中   - closed : 未防护

        :return: The rasp_protect_status of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._rasp_protect_status

    @rasp_protect_status.setter
    def rasp_protect_status(self, rasp_protect_status):
        r"""Sets the rasp_protect_status of this ExportWebTamperHostRequestInfo.

        动态网页防篡改防护状态   - opened : 防护中   - closed : 未防护

        :param rasp_protect_status: The rasp_protect_status of this ExportWebTamperHostRequestInfo.
        :type rasp_protect_status: str
        """
        self._rasp_protect_status = rasp_protect_status

    @property
    def wtp_status(self):
        r"""Gets the wtp_status of this ExportWebTamperHostRequestInfo.

        防护状态   - closed : 未防护   - opened : 防护中   - open_failed : 防护失败   - opening : 正在开启   - partial_protection : 部分防护

        :return: The wtp_status of this ExportWebTamperHostRequestInfo.
        :rtype: str
        """
        return self._wtp_status

    @wtp_status.setter
    def wtp_status(self, wtp_status):
        r"""Sets the wtp_status of this ExportWebTamperHostRequestInfo.

        防护状态   - closed : 未防护   - opened : 防护中   - open_failed : 防护失败   - opening : 正在开启   - partial_protection : 部分防护

        :param wtp_status: The wtp_status of this ExportWebTamperHostRequestInfo.
        :type wtp_status: str
        """
        self._wtp_status = wtp_status

    @property
    def offset(self):
        r"""Gets the offset of this ExportWebTamperHostRequestInfo.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ExportWebTamperHostRequestInfo.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ExportWebTamperHostRequestInfo.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ExportWebTamperHostRequestInfo.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ExportWebTamperHostRequestInfo.

        每页显示个数

        :return: The limit of this ExportWebTamperHostRequestInfo.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ExportWebTamperHostRequestInfo.

        每页显示个数

        :param limit: The limit of this ExportWebTamperHostRequestInfo.
        :type limit: int
        """
        self._limit = limit

    @property
    def export_size(self):
        r"""Gets the export_size of this ExportWebTamperHostRequestInfo.

        导出数据条数

        :return: The export_size of this ExportWebTamperHostRequestInfo.
        :rtype: int
        """
        return self._export_size

    @export_size.setter
    def export_size(self, export_size):
        r"""Sets the export_size of this ExportWebTamperHostRequestInfo.

        导出数据条数

        :param export_size: The export_size of this ExportWebTamperHostRequestInfo.
        :type export_size: int
        """
        self._export_size = export_size

    @property
    def export_headers(self):
        r"""Gets the export_headers of this ExportWebTamperHostRequestInfo.

        导出表头集合

        :return: The export_headers of this ExportWebTamperHostRequestInfo.
        :rtype: list[list[str]]
        """
        return self._export_headers

    @export_headers.setter
    def export_headers(self, export_headers):
        r"""Sets the export_headers of this ExportWebTamperHostRequestInfo.

        导出表头集合

        :param export_headers: The export_headers of this ExportWebTamperHostRequestInfo.
        :type export_headers: list[list[str]]
        """
        self._export_headers = export_headers

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
        if not isinstance(other, ExportWebTamperHostRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
