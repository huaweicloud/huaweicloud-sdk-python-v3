# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportVulsRequest:

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
        'type': 'str',
        'vul_id': 'str',
        'vul_name': 'str',
        'host_id': 'str',
        'export_size': 'int',
        'category': 'str',
        'limit': 'int',
        'offset': 'int',
        'repair_priority': 'str',
        'handle_status': 'str',
        'cve_id': 'str',
        'label_list': 'str',
        'status': 'str',
        'asset_value': 'str',
        'group_name': 'str',
        'body': 'ExportVulRequestBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'host_id': 'host_id',
        'export_size': 'export_size',
        'category': 'category',
        'limit': 'limit',
        'offset': 'offset',
        'repair_priority': 'repair_priority',
        'handle_status': 'handle_status',
        'cve_id': 'cve_id',
        'label_list': 'label_list',
        'status': 'status',
        'asset_value': 'asset_value',
        'group_name': 'group_name',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, type=None, vul_id=None, vul_name=None, host_id=None, export_size=None, category=None, limit=None, offset=None, repair_priority=None, handle_status=None, cve_id=None, label_list=None, status=None, asset_value=None, group_name=None, body=None):
        r"""ExportVulsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param type: 漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞
        :type type: str
        :param vul_id: 漏洞ID
        :type vul_id: str
        :param vul_name: 漏洞名称
        :type vul_name: str
        :param host_id: 主机id，导出单台主机漏洞时会用到
        :type host_id: str
        :param export_size: 导出数据条数
        :type export_size: int
        :param category: 导出漏洞数据类别:   - vul ：漏洞   - host: 主机漏洞
        :type category: str
        :param limit: limit
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param repair_priority: 修复优先级 Critical：紧急 High：高 Medium：中 Low：低
        :type repair_priority: str
        :param handle_status: 处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理
        :type handle_status: str
        :param cve_id: 漏洞编号
        :type cve_id: str
        :param label_list: 漏洞标签
        :type label_list: str
        :param status: 漏洞状态
        :type status: str
        :param asset_value: 资产重要性 important common test
        :type asset_value: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param body: Body of the ExportVulsRequest
        :type body: :class:`huaweicloudsdkhss.v5.ExportVulRequestBody`
        """
        
        

        self._enterprise_project_id = None
        self._type = None
        self._vul_id = None
        self._vul_name = None
        self._host_id = None
        self._export_size = None
        self._category = None
        self._limit = None
        self._offset = None
        self._repair_priority = None
        self._handle_status = None
        self._cve_id = None
        self._label_list = None
        self._status = None
        self._asset_value = None
        self._group_name = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if host_id is not None:
            self.host_id = host_id
        self.export_size = export_size
        self.category = category
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if repair_priority is not None:
            self.repair_priority = repair_priority
        if handle_status is not None:
            self.handle_status = handle_status
        if cve_id is not None:
            self.cve_id = cve_id
        if label_list is not None:
            self.label_list = label_list
        if status is not None:
            self.status = status
        if asset_value is not None:
            self.asset_value = asset_value
        if group_name is not None:
            self.group_name = group_name
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ExportVulsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ExportVulsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ExportVulsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ExportVulsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this ExportVulsRequest.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞

        :return: The type of this ExportVulsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExportVulsRequest.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞

        :param type: The type of this ExportVulsRequest.
        :type type: str
        """
        self._type = type

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ExportVulsRequest.

        漏洞ID

        :return: The vul_id of this ExportVulsRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ExportVulsRequest.

        漏洞ID

        :param vul_id: The vul_id of this ExportVulsRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ExportVulsRequest.

        漏洞名称

        :return: The vul_name of this ExportVulsRequest.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ExportVulsRequest.

        漏洞名称

        :param vul_name: The vul_name of this ExportVulsRequest.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ExportVulsRequest.

        主机id，导出单台主机漏洞时会用到

        :return: The host_id of this ExportVulsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ExportVulsRequest.

        主机id，导出单台主机漏洞时会用到

        :param host_id: The host_id of this ExportVulsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def export_size(self):
        r"""Gets the export_size of this ExportVulsRequest.

        导出数据条数

        :return: The export_size of this ExportVulsRequest.
        :rtype: int
        """
        return self._export_size

    @export_size.setter
    def export_size(self, export_size):
        r"""Sets the export_size of this ExportVulsRequest.

        导出数据条数

        :param export_size: The export_size of this ExportVulsRequest.
        :type export_size: int
        """
        self._export_size = export_size

    @property
    def category(self):
        r"""Gets the category of this ExportVulsRequest.

        导出漏洞数据类别:   - vul ：漏洞   - host: 主机漏洞

        :return: The category of this ExportVulsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ExportVulsRequest.

        导出漏洞数据类别:   - vul ：漏洞   - host: 主机漏洞

        :param category: The category of this ExportVulsRequest.
        :type category: str
        """
        self._category = category

    @property
    def limit(self):
        r"""Gets the limit of this ExportVulsRequest.

        limit

        :return: The limit of this ExportVulsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ExportVulsRequest.

        limit

        :param limit: The limit of this ExportVulsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ExportVulsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ExportVulsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ExportVulsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ExportVulsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this ExportVulsRequest.

        修复优先级 Critical：紧急 High：高 Medium：中 Low：低

        :return: The repair_priority of this ExportVulsRequest.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this ExportVulsRequest.

        修复优先级 Critical：紧急 High：高 Medium：中 Low：低

        :param repair_priority: The repair_priority of this ExportVulsRequest.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ExportVulsRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :return: The handle_status of this ExportVulsRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ExportVulsRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :param handle_status: The handle_status of this ExportVulsRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def cve_id(self):
        r"""Gets the cve_id of this ExportVulsRequest.

        漏洞编号

        :return: The cve_id of this ExportVulsRequest.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        r"""Sets the cve_id of this ExportVulsRequest.

        漏洞编号

        :param cve_id: The cve_id of this ExportVulsRequest.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def label_list(self):
        r"""Gets the label_list of this ExportVulsRequest.

        漏洞标签

        :return: The label_list of this ExportVulsRequest.
        :rtype: str
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        r"""Sets the label_list of this ExportVulsRequest.

        漏洞标签

        :param label_list: The label_list of this ExportVulsRequest.
        :type label_list: str
        """
        self._label_list = label_list

    @property
    def status(self):
        r"""Gets the status of this ExportVulsRequest.

        漏洞状态

        :return: The status of this ExportVulsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportVulsRequest.

        漏洞状态

        :param status: The status of this ExportVulsRequest.
        :type status: str
        """
        self._status = status

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ExportVulsRequest.

        资产重要性 important common test

        :return: The asset_value of this ExportVulsRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ExportVulsRequest.

        资产重要性 important common test

        :param asset_value: The asset_value of this ExportVulsRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def group_name(self):
        r"""Gets the group_name of this ExportVulsRequest.

        服务器组名称

        :return: The group_name of this ExportVulsRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ExportVulsRequest.

        服务器组名称

        :param group_name: The group_name of this ExportVulsRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def body(self):
        r"""Gets the body of this ExportVulsRequest.

        :return: The body of this ExportVulsRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.ExportVulRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ExportVulsRequest.

        :param body: The body of this ExportVulsRequest.
        :type body: :class:`huaweicloudsdkhss.v5.ExportVulRequestBody`
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
        if not isinstance(other, ExportVulsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
