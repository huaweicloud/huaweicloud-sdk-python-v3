# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportHandledVulnerabilitiesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_name': 'str',
        'repair_priority': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'is_affect_business': 'bool',
        'status': 'str',
        'asset_value': 'str',
        'label': 'str',
        'type': 'str',
        'group_name': 'str',
        'handle_cycle': 'str',
        'specific_vuls': 'list[ExportHandledVulnerabilitiesRequestBodySpecificVuls]',
        'export_size': 'int',
        'export_headers': 'list[list[str]]'
    }

    attribute_map = {
        'vul_name': 'vul_name',
        'repair_priority': 'repair_priority',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'is_affect_business': 'is_affect_business',
        'status': 'status',
        'asset_value': 'asset_value',
        'label': 'label',
        'type': 'type',
        'group_name': 'group_name',
        'handle_cycle': 'handle_cycle',
        'specific_vuls': 'specific_vuls',
        'export_size': 'export_size',
        'export_headers': 'export_headers'
    }

    def __init__(self, vul_name=None, repair_priority=None, host_name=None, host_ip=None, is_affect_business=None, status=None, asset_value=None, label=None, type=None, group_name=None, handle_cycle=None, specific_vuls=None, export_size=None, export_headers=None):
        r"""ExportHandledVulnerabilitiesRequestBody

        The model defined in huaweicloud sdk

        :param vul_name: 漏洞名称
        :type vul_name: str
        :param repair_priority: 漏洞修复优先级,包含如下 - Critical 紧急  - High 高  - Medium 中  - Low 低
        :type repair_priority: str
        :param host_name: 主机名称
        :type host_name: str
        :param host_ip: 主机ip
        :type host_ip: str
        :param is_affect_business: 是否影响业务
        :type is_affect_business: bool
        :param status: 漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复
        :type status: str
        :param asset_value: 资产重要性 important:重要 common：一般 test：测试
        :type asset_value: str
        :param label: 漏洞标签
        :type label: str
        :param type: 漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞
        :type type: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param handle_cycle: 需要查询的漏洞处置周期：   - today：查询今日处理的数据   - all：查询所有已处理数据
        :type handle_cycle: str
        :param specific_vuls: 指定要导出的漏洞数据
        :type specific_vuls: list[:class:`huaweicloudsdkhss.v5.ExportHandledVulnerabilitiesRequestBodySpecificVuls`]
        :param export_size: 导出数据条数
        :type export_size: int
        :param export_headers: 导出漏洞数据的表头信息列表
        :type export_headers: list[list[str]]
        """
        
        

        self._vul_name = None
        self._repair_priority = None
        self._host_name = None
        self._host_ip = None
        self._is_affect_business = None
        self._status = None
        self._asset_value = None
        self._label = None
        self._type = None
        self._group_name = None
        self._handle_cycle = None
        self._specific_vuls = None
        self._export_size = None
        self._export_headers = None
        self.discriminator = None

        if vul_name is not None:
            self.vul_name = vul_name
        if repair_priority is not None:
            self.repair_priority = repair_priority
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if is_affect_business is not None:
            self.is_affect_business = is_affect_business
        if status is not None:
            self.status = status
        if asset_value is not None:
            self.asset_value = asset_value
        if label is not None:
            self.label = label
        if type is not None:
            self.type = type
        if group_name is not None:
            self.group_name = group_name
        if handle_cycle is not None:
            self.handle_cycle = handle_cycle
        if specific_vuls is not None:
            self.specific_vuls = specific_vuls
        if export_size is not None:
            self.export_size = export_size
        self.export_headers = export_headers

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ExportHandledVulnerabilitiesRequestBody.

        漏洞名称

        :return: The vul_name of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ExportHandledVulnerabilitiesRequestBody.

        漏洞名称

        :param vul_name: The vul_name of this ExportHandledVulnerabilitiesRequestBody.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this ExportHandledVulnerabilitiesRequestBody.

        漏洞修复优先级,包含如下 - Critical 紧急  - High 高  - Medium 中  - Low 低

        :return: The repair_priority of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this ExportHandledVulnerabilitiesRequestBody.

        漏洞修复优先级,包含如下 - Critical 紧急  - High 高  - Medium 中  - Low 低

        :param repair_priority: The repair_priority of this ExportHandledVulnerabilitiesRequestBody.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

    @property
    def host_name(self):
        r"""Gets the host_name of this ExportHandledVulnerabilitiesRequestBody.

        主机名称

        :return: The host_name of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ExportHandledVulnerabilitiesRequestBody.

        主机名称

        :param host_name: The host_name of this ExportHandledVulnerabilitiesRequestBody.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ExportHandledVulnerabilitiesRequestBody.

        主机ip

        :return: The host_ip of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ExportHandledVulnerabilitiesRequestBody.

        主机ip

        :param host_ip: The host_ip of this ExportHandledVulnerabilitiesRequestBody.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def is_affect_business(self):
        r"""Gets the is_affect_business of this ExportHandledVulnerabilitiesRequestBody.

        是否影响业务

        :return: The is_affect_business of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: bool
        """
        return self._is_affect_business

    @is_affect_business.setter
    def is_affect_business(self, is_affect_business):
        r"""Sets the is_affect_business of this ExportHandledVulnerabilitiesRequestBody.

        是否影响业务

        :param is_affect_business: The is_affect_business of this ExportHandledVulnerabilitiesRequestBody.
        :type is_affect_business: bool
        """
        self._is_affect_business = is_affect_business

    @property
    def status(self):
        r"""Gets the status of this ExportHandledVulnerabilitiesRequestBody.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :return: The status of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportHandledVulnerabilitiesRequestBody.

        漏洞状态   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :param status: The status of this ExportHandledVulnerabilitiesRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ExportHandledVulnerabilitiesRequestBody.

        资产重要性 important:重要 common：一般 test：测试

        :return: The asset_value of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ExportHandledVulnerabilitiesRequestBody.

        资产重要性 important:重要 common：一般 test：测试

        :param asset_value: The asset_value of this ExportHandledVulnerabilitiesRequestBody.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def label(self):
        r"""Gets the label of this ExportHandledVulnerabilitiesRequestBody.

        漏洞标签

        :return: The label of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ExportHandledVulnerabilitiesRequestBody.

        漏洞标签

        :param label: The label of this ExportHandledVulnerabilitiesRequestBody.
        :type label: str
        """
        self._label = label

    @property
    def type(self):
        r"""Gets the type of this ExportHandledVulnerabilitiesRequestBody.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞

        :return: The type of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExportHandledVulnerabilitiesRequestBody.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞

        :param type: The type of this ExportHandledVulnerabilitiesRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def group_name(self):
        r"""Gets the group_name of this ExportHandledVulnerabilitiesRequestBody.

        服务器组名称

        :return: The group_name of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ExportHandledVulnerabilitiesRequestBody.

        服务器组名称

        :param group_name: The group_name of this ExportHandledVulnerabilitiesRequestBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def handle_cycle(self):
        r"""Gets the handle_cycle of this ExportHandledVulnerabilitiesRequestBody.

        需要查询的漏洞处置周期：   - today：查询今日处理的数据   - all：查询所有已处理数据

        :return: The handle_cycle of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: str
        """
        return self._handle_cycle

    @handle_cycle.setter
    def handle_cycle(self, handle_cycle):
        r"""Sets the handle_cycle of this ExportHandledVulnerabilitiesRequestBody.

        需要查询的漏洞处置周期：   - today：查询今日处理的数据   - all：查询所有已处理数据

        :param handle_cycle: The handle_cycle of this ExportHandledVulnerabilitiesRequestBody.
        :type handle_cycle: str
        """
        self._handle_cycle = handle_cycle

    @property
    def specific_vuls(self):
        r"""Gets the specific_vuls of this ExportHandledVulnerabilitiesRequestBody.

        指定要导出的漏洞数据

        :return: The specific_vuls of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ExportHandledVulnerabilitiesRequestBodySpecificVuls`]
        """
        return self._specific_vuls

    @specific_vuls.setter
    def specific_vuls(self, specific_vuls):
        r"""Sets the specific_vuls of this ExportHandledVulnerabilitiesRequestBody.

        指定要导出的漏洞数据

        :param specific_vuls: The specific_vuls of this ExportHandledVulnerabilitiesRequestBody.
        :type specific_vuls: list[:class:`huaweicloudsdkhss.v5.ExportHandledVulnerabilitiesRequestBodySpecificVuls`]
        """
        self._specific_vuls = specific_vuls

    @property
    def export_size(self):
        r"""Gets the export_size of this ExportHandledVulnerabilitiesRequestBody.

        导出数据条数

        :return: The export_size of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: int
        """
        return self._export_size

    @export_size.setter
    def export_size(self, export_size):
        r"""Sets the export_size of this ExportHandledVulnerabilitiesRequestBody.

        导出数据条数

        :param export_size: The export_size of this ExportHandledVulnerabilitiesRequestBody.
        :type export_size: int
        """
        self._export_size = export_size

    @property
    def export_headers(self):
        r"""Gets the export_headers of this ExportHandledVulnerabilitiesRequestBody.

        导出漏洞数据的表头信息列表

        :return: The export_headers of this ExportHandledVulnerabilitiesRequestBody.
        :rtype: list[list[str]]
        """
        return self._export_headers

    @export_headers.setter
    def export_headers(self, export_headers):
        r"""Sets the export_headers of this ExportHandledVulnerabilitiesRequestBody.

        导出漏洞数据的表头信息列表

        :param export_headers: The export_headers of this ExportHandledVulnerabilitiesRequestBody.
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
        if not isinstance(other, ExportHandledVulnerabilitiesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
