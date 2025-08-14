# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportAntiVirusResultRequest:

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
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'handle_status': 'str',
        'severity_list': 'list[str]',
        'asset_value': 'str',
        'malware_name': 'str',
        'file_path': 'str',
        'export_size': 'int',
        'file_hash': 'str',
        'task_name': 'str',
        'manual_isolate': 'bool',
        'body': 'ExportAntiVirusResultRequestBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'handle_status': 'handle_status',
        'severity_list': 'severity_list',
        'asset_value': 'asset_value',
        'malware_name': 'malware_name',
        'file_path': 'file_path',
        'export_size': 'export_size',
        'file_hash': 'file_hash',
        'task_name': 'task_name',
        'manual_isolate': 'manual_isolate',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, host_name=None, private_ip=None, public_ip=None, handle_status=None, severity_list=None, asset_value=None, malware_name=None, file_path=None, export_size=None, file_hash=None, task_name=None, manual_isolate=None, body=None):
        r"""ExportAntiVirusResultRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param private_ip: **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param handle_status: 处置状态，包含如下:   - unhandled：未处理   - handled：已处理
        :type handle_status: str
        :param severity_list: 威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命
        :type severity_list: list[str]
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param malware_name: 病毒名称
        :type malware_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param export_size: 导出条数
        :type export_size: int
        :param file_hash: 文件hash，当前为sha256
        :type file_hash: str
        :param task_name: 任务名称
        :type task_name: str
        :param manual_isolate: 是否使用手动隔离按钮
        :type manual_isolate: bool
        :param body: Body of the ExportAntiVirusResultRequest
        :type body: :class:`huaweicloudsdkhss.v5.ExportAntiVirusResultRequestBody`
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._handle_status = None
        self._severity_list = None
        self._asset_value = None
        self._malware_name = None
        self._file_path = None
        self._export_size = None
        self._file_hash = None
        self._task_name = None
        self._manual_isolate = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if handle_status is not None:
            self.handle_status = handle_status
        if severity_list is not None:
            self.severity_list = severity_list
        if asset_value is not None:
            self.asset_value = asset_value
        if malware_name is not None:
            self.malware_name = malware_name
        if file_path is not None:
            self.file_path = file_path
        if export_size is not None:
            self.export_size = export_size
        if file_hash is not None:
            self.file_hash = file_hash
        if task_name is not None:
            self.task_name = task_name
        if manual_isolate is not None:
            self.manual_isolate = manual_isolate
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExportAntiVirusResultRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ExportAntiVirusResultRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExportAntiVirusResultRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ExportAntiVirusResultRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ExportAntiVirusResultRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ExportAntiVirusResultRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ExportAntiVirusResultRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ExportAntiVirusResultRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ExportAntiVirusResultRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ExportAntiVirusResultRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ExportAntiVirusResultRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ExportAntiVirusResultRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host_name(self):
        r"""Gets the host_name of this ExportAntiVirusResultRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ExportAntiVirusResultRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ExportAntiVirusResultRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ExportAntiVirusResultRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ExportAntiVirusResultRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The private_ip of this ExportAntiVirusResultRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ExportAntiVirusResultRequest.

        **参数解释**: 服务器私有IP **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param private_ip: The private_ip of this ExportAntiVirusResultRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ExportAntiVirusResultRequest.

        服务器公网IP

        :return: The public_ip of this ExportAntiVirusResultRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ExportAntiVirusResultRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ExportAntiVirusResultRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ExportAntiVirusResultRequest.

        处置状态，包含如下:   - unhandled：未处理   - handled：已处理

        :return: The handle_status of this ExportAntiVirusResultRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ExportAntiVirusResultRequest.

        处置状态，包含如下:   - unhandled：未处理   - handled：已处理

        :param handle_status: The handle_status of this ExportAntiVirusResultRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def severity_list(self):
        r"""Gets the severity_list of this ExportAntiVirusResultRequest.

        威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命

        :return: The severity_list of this ExportAntiVirusResultRequest.
        :rtype: list[str]
        """
        return self._severity_list

    @severity_list.setter
    def severity_list(self, severity_list):
        r"""Sets the severity_list of this ExportAntiVirusResultRequest.

        威胁等级，包含如下:   - Low：低危   - Medium：中危   - High：高危   - Critical：致命

        :param severity_list: The severity_list of this ExportAntiVirusResultRequest.
        :type severity_list: list[str]
        """
        self._severity_list = severity_list

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ExportAntiVirusResultRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ExportAntiVirusResultRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ExportAntiVirusResultRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ExportAntiVirusResultRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def malware_name(self):
        r"""Gets the malware_name of this ExportAntiVirusResultRequest.

        病毒名称

        :return: The malware_name of this ExportAntiVirusResultRequest.
        :rtype: str
        """
        return self._malware_name

    @malware_name.setter
    def malware_name(self, malware_name):
        r"""Sets the malware_name of this ExportAntiVirusResultRequest.

        病毒名称

        :param malware_name: The malware_name of this ExportAntiVirusResultRequest.
        :type malware_name: str
        """
        self._malware_name = malware_name

    @property
    def file_path(self):
        r"""Gets the file_path of this ExportAntiVirusResultRequest.

        文件路径

        :return: The file_path of this ExportAntiVirusResultRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ExportAntiVirusResultRequest.

        文件路径

        :param file_path: The file_path of this ExportAntiVirusResultRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def export_size(self):
        r"""Gets the export_size of this ExportAntiVirusResultRequest.

        导出条数

        :return: The export_size of this ExportAntiVirusResultRequest.
        :rtype: int
        """
        return self._export_size

    @export_size.setter
    def export_size(self, export_size):
        r"""Sets the export_size of this ExportAntiVirusResultRequest.

        导出条数

        :param export_size: The export_size of this ExportAntiVirusResultRequest.
        :type export_size: int
        """
        self._export_size = export_size

    @property
    def file_hash(self):
        r"""Gets the file_hash of this ExportAntiVirusResultRequest.

        文件hash，当前为sha256

        :return: The file_hash of this ExportAntiVirusResultRequest.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        r"""Sets the file_hash of this ExportAntiVirusResultRequest.

        文件hash，当前为sha256

        :param file_hash: The file_hash of this ExportAntiVirusResultRequest.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def task_name(self):
        r"""Gets the task_name of this ExportAntiVirusResultRequest.

        任务名称

        :return: The task_name of this ExportAntiVirusResultRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ExportAntiVirusResultRequest.

        任务名称

        :param task_name: The task_name of this ExportAntiVirusResultRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def manual_isolate(self):
        r"""Gets the manual_isolate of this ExportAntiVirusResultRequest.

        是否使用手动隔离按钮

        :return: The manual_isolate of this ExportAntiVirusResultRequest.
        :rtype: bool
        """
        return self._manual_isolate

    @manual_isolate.setter
    def manual_isolate(self, manual_isolate):
        r"""Sets the manual_isolate of this ExportAntiVirusResultRequest.

        是否使用手动隔离按钮

        :param manual_isolate: The manual_isolate of this ExportAntiVirusResultRequest.
        :type manual_isolate: bool
        """
        self._manual_isolate = manual_isolate

    @property
    def body(self):
        r"""Gets the body of this ExportAntiVirusResultRequest.

        :return: The body of this ExportAntiVirusResultRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.ExportAntiVirusResultRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ExportAntiVirusResultRequest.

        :param body: The body of this ExportAntiVirusResultRequest.
        :type body: :class:`huaweicloudsdkhss.v5.ExportAntiVirusResultRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ExportAntiVirusResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
