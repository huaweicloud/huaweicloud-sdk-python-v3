# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportSecurityCheckInfoResponseInfo:

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
        'host_name': 'str',
        'host_public_ip': 'str',
        'host_private_ip': 'str',
        'check_type': 'str',
        'check_name': 'str',
        'standard': 'str',
        'check_rule_name': 'str',
        'executable_file_path': 'str',
        'severity': 'str',
        'scan_result': 'str',
        'status': 'str',
        'check_rule_desc': 'str',
        'audit': 'str',
        'remediation': 'str',
        'check_info_list': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_public_ip': 'host_public_ip',
        'host_private_ip': 'host_private_ip',
        'check_type': 'check_type',
        'check_name': 'check_name',
        'standard': 'standard',
        'check_rule_name': 'check_rule_name',
        'executable_file_path': 'executable_file_path',
        'severity': 'severity',
        'scan_result': 'scan_result',
        'status': 'status',
        'check_rule_desc': 'check_rule_desc',
        'audit': 'audit',
        'remediation': 'remediation',
        'check_info_list': 'check_info_list',
        'create_time': 'create_time'
    }

    def __init__(self, host_id=None, host_name=None, host_public_ip=None, host_private_ip=None, check_type=None, check_name=None, standard=None, check_rule_name=None, executable_file_path=None, severity=None, scan_result=None, status=None, check_rule_desc=None, audit=None, remediation=None, check_info_list=None, create_time=None):
        r"""ExportSecurityCheckInfoResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: 服务器ID
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_public_ip: 服务器公网IP
        :type host_public_ip: str
        :param host_private_ip: 服务器私网IP
        :type host_private_ip: str
        :param check_type: 配置检查（基线）的类型,Linux系统支持的基线一般check_type和check_name相同,例如SSH、CentOS 7。 Windows系统支持的基线一般check_type和check_name不相同，例如check_name为Windows的配置检查（基线），它的check_type包含Windows Server 2019 R2、Windows Server 2016 R2等。
        :type check_type: str
        :param check_name: 配置检查（基线）的名称，例如SSH、CentOS 7、Windows
        :type check_name: str
        :param standard: 基线标准 - cn_standard#等保合规标准 - hw_standard#云安全实践标准
        :type standard: str
        :param check_rule_name: 检查项（检查规则）名称
        :type check_rule_name: str
        :param executable_file_path: 配置检查（基线）的路径信息
        :type executable_file_path: str
        :param severity: 风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危
        :type severity: str
        :param scan_result: 检测结果  - pass - failed
        :type scan_result: str
        :param status: 状态  - safe : 无需处理 - ignored : 已忽略 - unhandled : 未处理
        :type status: str
        :param check_rule_desc: 规则描述
        :type check_rule_desc: str
        :param audit: 审计描述
        :type audit: str
        :param remediation: 修改建议
        :type remediation: str
        :param check_info_list: 检测用例信息
        :type check_info_list: str
        :param create_time: 首次扫描时间，时间戳单位：毫秒
        :type create_time: int
        """
        
        

        self._host_id = None
        self._host_name = None
        self._host_public_ip = None
        self._host_private_ip = None
        self._check_type = None
        self._check_name = None
        self._standard = None
        self._check_rule_name = None
        self._executable_file_path = None
        self._severity = None
        self._scan_result = None
        self._status = None
        self._check_rule_desc = None
        self._audit = None
        self._remediation = None
        self._check_info_list = None
        self._create_time = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_public_ip is not None:
            self.host_public_ip = host_public_ip
        if host_private_ip is not None:
            self.host_private_ip = host_private_ip
        if check_type is not None:
            self.check_type = check_type
        if check_name is not None:
            self.check_name = check_name
        if standard is not None:
            self.standard = standard
        if check_rule_name is not None:
            self.check_rule_name = check_rule_name
        if executable_file_path is not None:
            self.executable_file_path = executable_file_path
        if severity is not None:
            self.severity = severity
        if scan_result is not None:
            self.scan_result = scan_result
        if status is not None:
            self.status = status
        if check_rule_desc is not None:
            self.check_rule_desc = check_rule_desc
        if audit is not None:
            self.audit = audit
        if remediation is not None:
            self.remediation = remediation
        if check_info_list is not None:
            self.check_info_list = check_info_list
        if create_time is not None:
            self.create_time = create_time

    @property
    def host_id(self):
        r"""Gets the host_id of this ExportSecurityCheckInfoResponseInfo.

        服务器ID

        :return: The host_id of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ExportSecurityCheckInfoResponseInfo.

        服务器ID

        :param host_id: The host_id of this ExportSecurityCheckInfoResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ExportSecurityCheckInfoResponseInfo.

        服务器名称

        :return: The host_name of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ExportSecurityCheckInfoResponseInfo.

        服务器名称

        :param host_name: The host_name of this ExportSecurityCheckInfoResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_public_ip(self):
        r"""Gets the host_public_ip of this ExportSecurityCheckInfoResponseInfo.

        服务器公网IP

        :return: The host_public_ip of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._host_public_ip

    @host_public_ip.setter
    def host_public_ip(self, host_public_ip):
        r"""Sets the host_public_ip of this ExportSecurityCheckInfoResponseInfo.

        服务器公网IP

        :param host_public_ip: The host_public_ip of this ExportSecurityCheckInfoResponseInfo.
        :type host_public_ip: str
        """
        self._host_public_ip = host_public_ip

    @property
    def host_private_ip(self):
        r"""Gets the host_private_ip of this ExportSecurityCheckInfoResponseInfo.

        服务器私网IP

        :return: The host_private_ip of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._host_private_ip

    @host_private_ip.setter
    def host_private_ip(self, host_private_ip):
        r"""Sets the host_private_ip of this ExportSecurityCheckInfoResponseInfo.

        服务器私网IP

        :param host_private_ip: The host_private_ip of this ExportSecurityCheckInfoResponseInfo.
        :type host_private_ip: str
        """
        self._host_private_ip = host_private_ip

    @property
    def check_type(self):
        r"""Gets the check_type of this ExportSecurityCheckInfoResponseInfo.

        配置检查（基线）的类型,Linux系统支持的基线一般check_type和check_name相同,例如SSH、CentOS 7。 Windows系统支持的基线一般check_type和check_name不相同，例如check_name为Windows的配置检查（基线），它的check_type包含Windows Server 2019 R2、Windows Server 2016 R2等。

        :return: The check_type of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this ExportSecurityCheckInfoResponseInfo.

        配置检查（基线）的类型,Linux系统支持的基线一般check_type和check_name相同,例如SSH、CentOS 7。 Windows系统支持的基线一般check_type和check_name不相同，例如check_name为Windows的配置检查（基线），它的check_type包含Windows Server 2019 R2、Windows Server 2016 R2等。

        :param check_type: The check_type of this ExportSecurityCheckInfoResponseInfo.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def check_name(self):
        r"""Gets the check_name of this ExportSecurityCheckInfoResponseInfo.

        配置检查（基线）的名称，例如SSH、CentOS 7、Windows

        :return: The check_name of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ExportSecurityCheckInfoResponseInfo.

        配置检查（基线）的名称，例如SSH、CentOS 7、Windows

        :param check_name: The check_name of this ExportSecurityCheckInfoResponseInfo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def standard(self):
        r"""Gets the standard of this ExportSecurityCheckInfoResponseInfo.

        基线标准 - cn_standard#等保合规标准 - hw_standard#云安全实践标准

        :return: The standard of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ExportSecurityCheckInfoResponseInfo.

        基线标准 - cn_standard#等保合规标准 - hw_standard#云安全实践标准

        :param standard: The standard of this ExportSecurityCheckInfoResponseInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def check_rule_name(self):
        r"""Gets the check_rule_name of this ExportSecurityCheckInfoResponseInfo.

        检查项（检查规则）名称

        :return: The check_rule_name of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._check_rule_name

    @check_rule_name.setter
    def check_rule_name(self, check_rule_name):
        r"""Sets the check_rule_name of this ExportSecurityCheckInfoResponseInfo.

        检查项（检查规则）名称

        :param check_rule_name: The check_rule_name of this ExportSecurityCheckInfoResponseInfo.
        :type check_rule_name: str
        """
        self._check_rule_name = check_rule_name

    @property
    def executable_file_path(self):
        r"""Gets the executable_file_path of this ExportSecurityCheckInfoResponseInfo.

        配置检查（基线）的路径信息

        :return: The executable_file_path of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._executable_file_path

    @executable_file_path.setter
    def executable_file_path(self, executable_file_path):
        r"""Sets the executable_file_path of this ExportSecurityCheckInfoResponseInfo.

        配置检查（基线）的路径信息

        :param executable_file_path: The executable_file_path of this ExportSecurityCheckInfoResponseInfo.
        :type executable_file_path: str
        """
        self._executable_file_path = executable_file_path

    @property
    def severity(self):
        r"""Gets the severity of this ExportSecurityCheckInfoResponseInfo.

        风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危

        :return: The severity of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ExportSecurityCheckInfoResponseInfo.

        风险等级，包含如下:   - Low : 低危   - Medium : 中危   - High : 高危

        :param severity: The severity of this ExportSecurityCheckInfoResponseInfo.
        :type severity: str
        """
        self._severity = severity

    @property
    def scan_result(self):
        r"""Gets the scan_result of this ExportSecurityCheckInfoResponseInfo.

        检测结果  - pass - failed

        :return: The scan_result of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._scan_result

    @scan_result.setter
    def scan_result(self, scan_result):
        r"""Sets the scan_result of this ExportSecurityCheckInfoResponseInfo.

        检测结果  - pass - failed

        :param scan_result: The scan_result of this ExportSecurityCheckInfoResponseInfo.
        :type scan_result: str
        """
        self._scan_result = scan_result

    @property
    def status(self):
        r"""Gets the status of this ExportSecurityCheckInfoResponseInfo.

        状态  - safe : 无需处理 - ignored : 已忽略 - unhandled : 未处理

        :return: The status of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportSecurityCheckInfoResponseInfo.

        状态  - safe : 无需处理 - ignored : 已忽略 - unhandled : 未处理

        :param status: The status of this ExportSecurityCheckInfoResponseInfo.
        :type status: str
        """
        self._status = status

    @property
    def check_rule_desc(self):
        r"""Gets the check_rule_desc of this ExportSecurityCheckInfoResponseInfo.

        规则描述

        :return: The check_rule_desc of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._check_rule_desc

    @check_rule_desc.setter
    def check_rule_desc(self, check_rule_desc):
        r"""Sets the check_rule_desc of this ExportSecurityCheckInfoResponseInfo.

        规则描述

        :param check_rule_desc: The check_rule_desc of this ExportSecurityCheckInfoResponseInfo.
        :type check_rule_desc: str
        """
        self._check_rule_desc = check_rule_desc

    @property
    def audit(self):
        r"""Gets the audit of this ExportSecurityCheckInfoResponseInfo.

        审计描述

        :return: The audit of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._audit

    @audit.setter
    def audit(self, audit):
        r"""Sets the audit of this ExportSecurityCheckInfoResponseInfo.

        审计描述

        :param audit: The audit of this ExportSecurityCheckInfoResponseInfo.
        :type audit: str
        """
        self._audit = audit

    @property
    def remediation(self):
        r"""Gets the remediation of this ExportSecurityCheckInfoResponseInfo.

        修改建议

        :return: The remediation of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        r"""Sets the remediation of this ExportSecurityCheckInfoResponseInfo.

        修改建议

        :param remediation: The remediation of this ExportSecurityCheckInfoResponseInfo.
        :type remediation: str
        """
        self._remediation = remediation

    @property
    def check_info_list(self):
        r"""Gets the check_info_list of this ExportSecurityCheckInfoResponseInfo.

        检测用例信息

        :return: The check_info_list of this ExportSecurityCheckInfoResponseInfo.
        :rtype: str
        """
        return self._check_info_list

    @check_info_list.setter
    def check_info_list(self, check_info_list):
        r"""Sets the check_info_list of this ExportSecurityCheckInfoResponseInfo.

        检测用例信息

        :param check_info_list: The check_info_list of this ExportSecurityCheckInfoResponseInfo.
        :type check_info_list: str
        """
        self._check_info_list = check_info_list

    @property
    def create_time(self):
        r"""Gets the create_time of this ExportSecurityCheckInfoResponseInfo.

        首次扫描时间，时间戳单位：毫秒

        :return: The create_time of this ExportSecurityCheckInfoResponseInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ExportSecurityCheckInfoResponseInfo.

        首次扫描时间，时间戳单位：毫秒

        :param create_time: The create_time of this ExportSecurityCheckInfoResponseInfo.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ExportSecurityCheckInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
