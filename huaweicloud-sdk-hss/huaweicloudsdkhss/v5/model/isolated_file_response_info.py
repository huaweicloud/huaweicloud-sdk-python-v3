# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsolatedFileResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_type': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'file_hash': 'str',
        'file_path': 'str',
        'file_attr': 'str',
        'isolation_status': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'asset_value': 'str',
        'update_time': 'int',
        'agent_version': 'str',
        'isolate_source': 'str',
        'event_name': 'str',
        'agent_event_info': 'IsolateEventResponseInfo',
        'antivirus_result_info': 'AntivirusResultDetailInfo'
    }

    attribute_map = {
        'os_type': 'os_type',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'file_hash': 'file_hash',
        'file_path': 'file_path',
        'file_attr': 'file_attr',
        'isolation_status': 'isolation_status',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'asset_value': 'asset_value',
        'update_time': 'update_time',
        'agent_version': 'agent_version',
        'isolate_source': 'isolate_source',
        'event_name': 'event_name',
        'agent_event_info': 'agent_event_info',
        'antivirus_result_info': 'antivirus_result_info'
    }

    def __init__(self, os_type=None, host_id=None, host_name=None, file_hash=None, file_path=None, file_attr=None, isolation_status=None, private_ip=None, public_ip=None, asset_value=None, update_time=None, agent_version=None, isolate_source=None, event_name=None, agent_event_info=None, antivirus_result_info=None):
        r"""IsolatedFileResponseInfo

        The model defined in huaweicloud sdk

        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 
        :type os_type: str
        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param file_hash: **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 
        :type file_hash: str
        :param file_path: **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 
        :type file_path: str
        :param file_attr: **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 
        :type file_attr: str
        :param isolation_status: 隔离状态，包含如下:   - isolated : 已隔离   - restored : 已恢复   - isolating : 已下发隔离任务   - restoring : 已下发恢复任务
        :type isolation_status: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param update_time: 更新时间，毫秒
        :type update_time: int
        :param agent_version: agent版本
        :type agent_version: str
        :param isolate_source: 隔离来源，包含如下:   - event : 安全告警事件   - antivirus : 病毒查杀
        :type isolate_source: str
        :param event_name: **参数解释**： 事件名称 **取值范围**： 字符长度1-256位 
        :type event_name: str
        :param agent_event_info: 
        :type agent_event_info: :class:`huaweicloudsdkhss.v5.IsolateEventResponseInfo`
        :param antivirus_result_info: 
        :type antivirus_result_info: :class:`huaweicloudsdkhss.v5.AntivirusResultDetailInfo`
        """
        
        

        self._os_type = None
        self._host_id = None
        self._host_name = None
        self._file_hash = None
        self._file_path = None
        self._file_attr = None
        self._isolation_status = None
        self._private_ip = None
        self._public_ip = None
        self._asset_value = None
        self._update_time = None
        self._agent_version = None
        self._isolate_source = None
        self._event_name = None
        self._agent_event_info = None
        self._antivirus_result_info = None
        self.discriminator = None

        self.os_type = os_type
        self.host_id = host_id
        self.host_name = host_name
        self.file_hash = file_hash
        self.file_path = file_path
        self.file_attr = file_attr
        self.isolation_status = isolation_status
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.asset_value = asset_value
        self.update_time = update_time
        self.agent_version = agent_version
        self.isolate_source = isolate_source
        self.event_name = event_name
        self.agent_event_info = agent_event_info
        self.antivirus_result_info = antivirus_result_info

    @property
    def os_type(self):
        r"""Gets the os_type of this IsolatedFileResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :return: The os_type of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this IsolatedFileResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :param os_type: The os_type of this IsolatedFileResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def host_id(self):
        r"""Gets the host_id of this IsolatedFileResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this IsolatedFileResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this IsolatedFileResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this IsolatedFileResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this IsolatedFileResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this IsolatedFileResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def file_hash(self):
        r"""Gets the file_hash of this IsolatedFileResponseInfo.

        **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 

        :return: The file_hash of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        r"""Sets the file_hash of this IsolatedFileResponseInfo.

        **参数解释**： 文件哈希 **取值范围**： 字符长度1-256位 

        :param file_hash: The file_hash of this IsolatedFileResponseInfo.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def file_path(self):
        r"""Gets the file_path of this IsolatedFileResponseInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :return: The file_path of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this IsolatedFileResponseInfo.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :param file_path: The file_path of this IsolatedFileResponseInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_attr(self):
        r"""Gets the file_attr of this IsolatedFileResponseInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 

        :return: The file_attr of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._file_attr

    @file_attr.setter
    def file_attr(self, file_attr):
        r"""Sets the file_attr of this IsolatedFileResponseInfo.

        **参数解释**： 文件属性 **取值范围**： 字符长度1-256位 

        :param file_attr: The file_attr of this IsolatedFileResponseInfo.
        :type file_attr: str
        """
        self._file_attr = file_attr

    @property
    def isolation_status(self):
        r"""Gets the isolation_status of this IsolatedFileResponseInfo.

        隔离状态，包含如下:   - isolated : 已隔离   - restored : 已恢复   - isolating : 已下发隔离任务   - restoring : 已下发恢复任务

        :return: The isolation_status of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._isolation_status

    @isolation_status.setter
    def isolation_status(self, isolation_status):
        r"""Sets the isolation_status of this IsolatedFileResponseInfo.

        隔离状态，包含如下:   - isolated : 已隔离   - restored : 已恢复   - isolating : 已下发隔离任务   - restoring : 已下发恢复任务

        :param isolation_status: The isolation_status of this IsolatedFileResponseInfo.
        :type isolation_status: str
        """
        self._isolation_status = isolation_status

    @property
    def private_ip(self):
        r"""Gets the private_ip of this IsolatedFileResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this IsolatedFileResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this IsolatedFileResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this IsolatedFileResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this IsolatedFileResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this IsolatedFileResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def asset_value(self):
        r"""Gets the asset_value of this IsolatedFileResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this IsolatedFileResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this IsolatedFileResponseInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def update_time(self):
        r"""Gets the update_time of this IsolatedFileResponseInfo.

        更新时间，毫秒

        :return: The update_time of this IsolatedFileResponseInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this IsolatedFileResponseInfo.

        更新时间，毫秒

        :param update_time: The update_time of this IsolatedFileResponseInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def agent_version(self):
        r"""Gets the agent_version of this IsolatedFileResponseInfo.

        agent版本

        :return: The agent_version of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this IsolatedFileResponseInfo.

        agent版本

        :param agent_version: The agent_version of this IsolatedFileResponseInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def isolate_source(self):
        r"""Gets the isolate_source of this IsolatedFileResponseInfo.

        隔离来源，包含如下:   - event : 安全告警事件   - antivirus : 病毒查杀

        :return: The isolate_source of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._isolate_source

    @isolate_source.setter
    def isolate_source(self, isolate_source):
        r"""Sets the isolate_source of this IsolatedFileResponseInfo.

        隔离来源，包含如下:   - event : 安全告警事件   - antivirus : 病毒查杀

        :param isolate_source: The isolate_source of this IsolatedFileResponseInfo.
        :type isolate_source: str
        """
        self._isolate_source = isolate_source

    @property
    def event_name(self):
        r"""Gets the event_name of this IsolatedFileResponseInfo.

        **参数解释**： 事件名称 **取值范围**： 字符长度1-256位 

        :return: The event_name of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this IsolatedFileResponseInfo.

        **参数解释**： 事件名称 **取值范围**： 字符长度1-256位 

        :param event_name: The event_name of this IsolatedFileResponseInfo.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def agent_event_info(self):
        r"""Gets the agent_event_info of this IsolatedFileResponseInfo.

        :return: The agent_event_info of this IsolatedFileResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.IsolateEventResponseInfo`
        """
        return self._agent_event_info

    @agent_event_info.setter
    def agent_event_info(self, agent_event_info):
        r"""Sets the agent_event_info of this IsolatedFileResponseInfo.

        :param agent_event_info: The agent_event_info of this IsolatedFileResponseInfo.
        :type agent_event_info: :class:`huaweicloudsdkhss.v5.IsolateEventResponseInfo`
        """
        self._agent_event_info = agent_event_info

    @property
    def antivirus_result_info(self):
        r"""Gets the antivirus_result_info of this IsolatedFileResponseInfo.

        :return: The antivirus_result_info of this IsolatedFileResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.AntivirusResultDetailInfo`
        """
        return self._antivirus_result_info

    @antivirus_result_info.setter
    def antivirus_result_info(self, antivirus_result_info):
        r"""Sets the antivirus_result_info of this IsolatedFileResponseInfo.

        :param antivirus_result_info: The antivirus_result_info of this IsolatedFileResponseInfo.
        :type antivirus_result_info: :class:`huaweicloudsdkhss.v5.AntivirusResultDetailInfo`
        """
        self._antivirus_result_info = antivirus_result_info

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
        if not isinstance(other, IsolatedFileResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
