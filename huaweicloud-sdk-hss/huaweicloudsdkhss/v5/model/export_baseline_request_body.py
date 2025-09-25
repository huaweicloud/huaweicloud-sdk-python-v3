# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportBaselineRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'export_size': 'int',
        'group_id': 'str',
        'check_name': 'str',
        'standard': 'str',
        'scan_result': 'str',
        'severity': 'str',
        'host_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'export_headers': 'list[list[str]]'
    }

    attribute_map = {
        'category': 'category',
        'export_size': 'export_size',
        'group_id': 'group_id',
        'check_name': 'check_name',
        'standard': 'standard',
        'scan_result': 'scan_result',
        'severity': 'severity',
        'host_id': 'host_id',
        'limit': 'limit',
        'offset': 'offset',
        'export_headers': 'export_headers'
    }

    def __init__(self, category=None, export_size=None, group_id=None, check_name=None, standard=None, scan_result=None, severity=None, host_id=None, limit=None, offset=None, export_headers=None):
        r"""ExportBaselineRequestBody

        The model defined in huaweicloud sdk

        :param category: **参数解释**： 导出类型 **约束限制**： 不涉及 **取值范围**： - risk-config : 基线配置检测 - password-complexity : 口令复杂度检测 - weak-password : 弱口令检测  **默认取值**： risk-config
        :type category: str
        :param export_size: **参数解释** 导出数据条数 **约束限制** 不涉及 **取值范围**  取值 1 - 200000  **默认取值** 100000
        :type export_size: int
        :param group_id: **参数解释**： 策略组id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位  **默认取值**: 不涉及 
        :type group_id: str
        :param check_name: **参数解释**： 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **约束限制**： 不涉及 **取值范围**： 字符长度0-256位  **默认取值**: 不涉及 
        :type check_name: str
        :param standard: **参数解释**： 标准类型 **约束限制**： 不涉及 **取值范围**： - cn_standard ： 等保合规标准 - hw_standard ： 云安全实践标准 - cis_standard ： 通用安全标准  **默认取值**: 不涉及 
        :type standard: str
        :param scan_result: **参数解释**： 检查结果 **约束限制**： 不涉及 **取值范围** - pass : 检查通过 - failed : 检查未通过(已废弃) - unhandled: 未通过  **默认取值** 不涉及 
        :type scan_result: str
        :param severity: **参数解释**： 风险等级 **约束限制**： 不涉及 **取值范围** - Security: 无风险 - Low : 低危 - Medium : 中危 - High: 高危  **默认取值** 不涉及 
        :type severity: str
        :param host_id: **参数解释**： 主机ID，不赋值时，查租户所有主机 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位  **默认取值**: 不涉及 
        :type host_id: str
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param export_headers: 导出配置检测数据的表头信息列表
        :type export_headers: list[list[str]]
        """
        
        

        self._category = None
        self._export_size = None
        self._group_id = None
        self._check_name = None
        self._standard = None
        self._scan_result = None
        self._severity = None
        self._host_id = None
        self._limit = None
        self._offset = None
        self._export_headers = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if export_size is not None:
            self.export_size = export_size
        if group_id is not None:
            self.group_id = group_id
        if check_name is not None:
            self.check_name = check_name
        if standard is not None:
            self.standard = standard
        if scan_result is not None:
            self.scan_result = scan_result
        if severity is not None:
            self.severity = severity
        if host_id is not None:
            self.host_id = host_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.export_headers = export_headers

    @property
    def category(self):
        r"""Gets the category of this ExportBaselineRequestBody.

        **参数解释**： 导出类型 **约束限制**： 不涉及 **取值范围**： - risk-config : 基线配置检测 - password-complexity : 口令复杂度检测 - weak-password : 弱口令检测  **默认取值**： risk-config

        :return: The category of this ExportBaselineRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ExportBaselineRequestBody.

        **参数解释**： 导出类型 **约束限制**： 不涉及 **取值范围**： - risk-config : 基线配置检测 - password-complexity : 口令复杂度检测 - weak-password : 弱口令检测  **默认取值**： risk-config

        :param category: The category of this ExportBaselineRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def export_size(self):
        r"""Gets the export_size of this ExportBaselineRequestBody.

        **参数解释** 导出数据条数 **约束限制** 不涉及 **取值范围**  取值 1 - 200000  **默认取值** 100000

        :return: The export_size of this ExportBaselineRequestBody.
        :rtype: int
        """
        return self._export_size

    @export_size.setter
    def export_size(self, export_size):
        r"""Sets the export_size of this ExportBaselineRequestBody.

        **参数解释** 导出数据条数 **约束限制** 不涉及 **取值范围**  取值 1 - 200000  **默认取值** 100000

        :param export_size: The export_size of this ExportBaselineRequestBody.
        :type export_size: int
        """
        self._export_size = export_size

    @property
    def group_id(self):
        r"""Gets the group_id of this ExportBaselineRequestBody.

        **参数解释**： 策略组id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位  **默认取值**: 不涉及 

        :return: The group_id of this ExportBaselineRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ExportBaselineRequestBody.

        **参数解释**： 策略组id **约束限制**： 不涉及 **取值范围**： 字符长度0-128位  **默认取值**: 不涉及 

        :param group_id: The group_id of this ExportBaselineRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def check_name(self):
        r"""Gets the check_name of this ExportBaselineRequestBody.

        **参数解释**： 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **约束限制**： 不涉及 **取值范围**： 字符长度0-256位  **默认取值**: 不涉及 

        :return: The check_name of this ExportBaselineRequestBody.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ExportBaselineRequestBody.

        **参数解释**： 配置检查（基线）的名称，例如SSH、CentOS 7、Windows **约束限制**： 不涉及 **取值范围**： 字符长度0-256位  **默认取值**: 不涉及 

        :param check_name: The check_name of this ExportBaselineRequestBody.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def standard(self):
        r"""Gets the standard of this ExportBaselineRequestBody.

        **参数解释**： 标准类型 **约束限制**： 不涉及 **取值范围**： - cn_standard ： 等保合规标准 - hw_standard ： 云安全实践标准 - cis_standard ： 通用安全标准  **默认取值**: 不涉及 

        :return: The standard of this ExportBaselineRequestBody.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ExportBaselineRequestBody.

        **参数解释**： 标准类型 **约束限制**： 不涉及 **取值范围**： - cn_standard ： 等保合规标准 - hw_standard ： 云安全实践标准 - cis_standard ： 通用安全标准  **默认取值**: 不涉及 

        :param standard: The standard of this ExportBaselineRequestBody.
        :type standard: str
        """
        self._standard = standard

    @property
    def scan_result(self):
        r"""Gets the scan_result of this ExportBaselineRequestBody.

        **参数解释**： 检查结果 **约束限制**： 不涉及 **取值范围** - pass : 检查通过 - failed : 检查未通过(已废弃) - unhandled: 未通过  **默认取值** 不涉及 

        :return: The scan_result of this ExportBaselineRequestBody.
        :rtype: str
        """
        return self._scan_result

    @scan_result.setter
    def scan_result(self, scan_result):
        r"""Sets the scan_result of this ExportBaselineRequestBody.

        **参数解释**： 检查结果 **约束限制**： 不涉及 **取值范围** - pass : 检查通过 - failed : 检查未通过(已废弃) - unhandled: 未通过  **默认取值** 不涉及 

        :param scan_result: The scan_result of this ExportBaselineRequestBody.
        :type scan_result: str
        """
        self._scan_result = scan_result

    @property
    def severity(self):
        r"""Gets the severity of this ExportBaselineRequestBody.

        **参数解释**： 风险等级 **约束限制**： 不涉及 **取值范围** - Security: 无风险 - Low : 低危 - Medium : 中危 - High: 高危  **默认取值** 不涉及 

        :return: The severity of this ExportBaselineRequestBody.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ExportBaselineRequestBody.

        **参数解释**： 风险等级 **约束限制**： 不涉及 **取值范围** - Security: 无风险 - Low : 低危 - Medium : 中危 - High: 高危  **默认取值** 不涉及 

        :param severity: The severity of this ExportBaselineRequestBody.
        :type severity: str
        """
        self._severity = severity

    @property
    def host_id(self):
        r"""Gets the host_id of this ExportBaselineRequestBody.

        **参数解释**： 主机ID，不赋值时，查租户所有主机 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位  **默认取值**: 不涉及 

        :return: The host_id of this ExportBaselineRequestBody.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ExportBaselineRequestBody.

        **参数解释**： 主机ID，不赋值时，查租户所有主机 **约束限制**： 不涉及 **取值范围**： 字符长度0-64位  **默认取值**: 不涉及 

        :param host_id: The host_id of this ExportBaselineRequestBody.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def limit(self):
        r"""Gets the limit of this ExportBaselineRequestBody.

        每页显示个数

        :return: The limit of this ExportBaselineRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ExportBaselineRequestBody.

        每页显示个数

        :param limit: The limit of this ExportBaselineRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ExportBaselineRequestBody.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ExportBaselineRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ExportBaselineRequestBody.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ExportBaselineRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def export_headers(self):
        r"""Gets the export_headers of this ExportBaselineRequestBody.

        导出配置检测数据的表头信息列表

        :return: The export_headers of this ExportBaselineRequestBody.
        :rtype: list[list[str]]
        """
        return self._export_headers

    @export_headers.setter
    def export_headers(self, export_headers):
        r"""Sets the export_headers of this ExportBaselineRequestBody.

        导出配置检测数据的表头信息列表

        :param export_headers: The export_headers of this ExportBaselineRequestBody.
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
        if not isinstance(other, ExportBaselineRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
