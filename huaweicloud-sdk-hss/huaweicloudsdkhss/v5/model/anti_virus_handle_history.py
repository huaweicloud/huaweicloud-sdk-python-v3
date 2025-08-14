# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntiVirusHandleHistory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_id': 'str',
        'malware_type': 'str',
        'malware_name': 'str',
        'severity': 'str',
        'file_path': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'asset_value': 'str',
        'occur_time': 'int',
        'handle_status': 'str',
        'handle_method': 'str',
        'notes': 'str',
        'handle_time': 'int',
        'user_name': 'str'
    }

    attribute_map = {
        'result_id': 'result_id',
        'malware_type': 'malware_type',
        'malware_name': 'malware_name',
        'severity': 'severity',
        'file_path': 'file_path',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'asset_value': 'asset_value',
        'occur_time': 'occur_time',
        'handle_status': 'handle_status',
        'handle_method': 'handle_method',
        'notes': 'notes',
        'handle_time': 'handle_time',
        'user_name': 'user_name'
    }

    def __init__(self, result_id=None, malware_type=None, malware_name=None, severity=None, file_path=None, host_name=None, private_ip=None, public_ip=None, asset_value=None, occur_time=None, handle_status=None, handle_method=None, notes=None, handle_time=None, user_name=None):
        r"""AntiVirusHandleHistory

        The model defined in huaweicloud sdk

        :param result_id: 病毒查杀结果ID
        :type result_id: str
        :param malware_type: 病毒类型
        :type malware_type: str
        :param malware_name: 病毒名称
        :type malware_name: str
        :param severity: **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 
        :type severity: str
        :param file_path: **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 
        :type file_path: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param occur_time: **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 
        :type occur_time: int
        :param handle_status: **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 
        :type handle_status: str
        :param handle_method: 处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - isolate_and_kill：隔离文件
        :type handle_method: str
        :param notes: 备注信息
        :type notes: str
        :param handle_time: 处置时间
        :type handle_time: int
        :param user_name: 用户名
        :type user_name: str
        """
        
        

        self._result_id = None
        self._malware_type = None
        self._malware_name = None
        self._severity = None
        self._file_path = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._asset_value = None
        self._occur_time = None
        self._handle_status = None
        self._handle_method = None
        self._notes = None
        self._handle_time = None
        self._user_name = None
        self.discriminator = None

        if result_id is not None:
            self.result_id = result_id
        if malware_type is not None:
            self.malware_type = malware_type
        if malware_name is not None:
            self.malware_name = malware_name
        if severity is not None:
            self.severity = severity
        if file_path is not None:
            self.file_path = file_path
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if asset_value is not None:
            self.asset_value = asset_value
        if occur_time is not None:
            self.occur_time = occur_time
        if handle_status is not None:
            self.handle_status = handle_status
        if handle_method is not None:
            self.handle_method = handle_method
        if notes is not None:
            self.notes = notes
        if handle_time is not None:
            self.handle_time = handle_time
        if user_name is not None:
            self.user_name = user_name

    @property
    def result_id(self):
        r"""Gets the result_id of this AntiVirusHandleHistory.

        病毒查杀结果ID

        :return: The result_id of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        r"""Sets the result_id of this AntiVirusHandleHistory.

        病毒查杀结果ID

        :param result_id: The result_id of this AntiVirusHandleHistory.
        :type result_id: str
        """
        self._result_id = result_id

    @property
    def malware_type(self):
        r"""Gets the malware_type of this AntiVirusHandleHistory.

        病毒类型

        :return: The malware_type of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._malware_type

    @malware_type.setter
    def malware_type(self, malware_type):
        r"""Sets the malware_type of this AntiVirusHandleHistory.

        病毒类型

        :param malware_type: The malware_type of this AntiVirusHandleHistory.
        :type malware_type: str
        """
        self._malware_type = malware_type

    @property
    def malware_name(self):
        r"""Gets the malware_name of this AntiVirusHandleHistory.

        病毒名称

        :return: The malware_name of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._malware_name

    @malware_name.setter
    def malware_name(self, malware_name):
        r"""Sets the malware_name of this AntiVirusHandleHistory.

        病毒名称

        :param malware_name: The malware_name of this AntiVirusHandleHistory.
        :type malware_name: str
        """
        self._malware_name = malware_name

    @property
    def severity(self):
        r"""Gets the severity of this AntiVirusHandleHistory.

        **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 

        :return: The severity of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this AntiVirusHandleHistory.

        **参数解释**： 威胁等级 **取值范围**： - Security：安全 - Low：低危 - Medium：中危 - High：高危 - Critical：危急 

        :param severity: The severity of this AntiVirusHandleHistory.
        :type severity: str
        """
        self._severity = severity

    @property
    def file_path(self):
        r"""Gets the file_path of this AntiVirusHandleHistory.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :return: The file_path of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this AntiVirusHandleHistory.

        **参数解释**： 文件路径 **取值范围**： 字符长度1-256位 

        :param file_path: The file_path of this AntiVirusHandleHistory.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def host_name(self):
        r"""Gets the host_name of this AntiVirusHandleHistory.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this AntiVirusHandleHistory.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this AntiVirusHandleHistory.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this AntiVirusHandleHistory.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this AntiVirusHandleHistory.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this AntiVirusHandleHistory.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this AntiVirusHandleHistory.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this AntiVirusHandleHistory.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this AntiVirusHandleHistory.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def asset_value(self):
        r"""Gets the asset_value of this AntiVirusHandleHistory.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this AntiVirusHandleHistory.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this AntiVirusHandleHistory.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def occur_time(self):
        r"""Gets the occur_time of this AntiVirusHandleHistory.

        **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The occur_time of this AntiVirusHandleHistory.
        :rtype: int
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        r"""Sets the occur_time of this AntiVirusHandleHistory.

        **参数解释**： 发生时间，毫秒 **取值范围**： 最小值0，最大值9223372036854775807 

        :param occur_time: The occur_time of this AntiVirusHandleHistory.
        :type occur_time: int
        """
        self._occur_time = occur_time

    @property
    def handle_status(self):
        r"""Gets the handle_status of this AntiVirusHandleHistory.

        **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 

        :return: The handle_status of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this AntiVirusHandleHistory.

        **参数解释**： 处理状态 **取值范围**： - unhandled：未处理 - handled：已处理 

        :param handle_status: The handle_status of this AntiVirusHandleHistory.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def handle_method(self):
        r"""Gets the handle_method of this AntiVirusHandleHistory.

        处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - isolate_and_kill：隔离文件

        :return: The handle_method of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._handle_method

    @handle_method.setter
    def handle_method(self, handle_method):
        r"""Sets the handle_method of this AntiVirusHandleHistory.

        处理方式，包含如下:   - mark_as_handled：手动处理   - ignore：忽略   - add_to_alarm_whitelist：加入告警白名单   - isolate_and_kill：隔离文件

        :param handle_method: The handle_method of this AntiVirusHandleHistory.
        :type handle_method: str
        """
        self._handle_method = handle_method

    @property
    def notes(self):
        r"""Gets the notes of this AntiVirusHandleHistory.

        备注信息

        :return: The notes of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        r"""Sets the notes of this AntiVirusHandleHistory.

        备注信息

        :param notes: The notes of this AntiVirusHandleHistory.
        :type notes: str
        """
        self._notes = notes

    @property
    def handle_time(self):
        r"""Gets the handle_time of this AntiVirusHandleHistory.

        处置时间

        :return: The handle_time of this AntiVirusHandleHistory.
        :rtype: int
        """
        return self._handle_time

    @handle_time.setter
    def handle_time(self, handle_time):
        r"""Sets the handle_time of this AntiVirusHandleHistory.

        处置时间

        :param handle_time: The handle_time of this AntiVirusHandleHistory.
        :type handle_time: int
        """
        self._handle_time = handle_time

    @property
    def user_name(self):
        r"""Gets the user_name of this AntiVirusHandleHistory.

        用户名

        :return: The user_name of this AntiVirusHandleHistory.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this AntiVirusHandleHistory.

        用户名

        :param user_name: The user_name of this AntiVirusHandleHistory.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, AntiVirusHandleHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
