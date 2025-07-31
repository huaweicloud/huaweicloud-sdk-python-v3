# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportVulHandleHistoryRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'vul_id': 'str',
        'vul_type': 'str',
        'asset_value': 'str',
        'group_name': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'export_size': 'int',
        'export_header_list': 'list[list[str]]'
    }

    attribute_map = {
        'status': 'status',
        'vul_id': 'vul_id',
        'vul_type': 'vul_type',
        'asset_value': 'asset_value',
        'group_name': 'group_name',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'export_size': 'export_size',
        'export_header_list': 'export_header_list'
    }

    def __init__(self, status=None, vul_id=None, vul_type=None, asset_value=None, group_name=None, host_name=None, host_ip=None, export_size=None, export_header_list=None):
        r"""ExportVulHandleHistoryRequestBody

        The model defined in huaweicloud sdk

        :param status: 漏洞状态 vul_status_unfix : 未处理 vul_status_ignored : 已忽略 vul_status_verified : 验证中 vul_status_fixing : 修复中 vul_status_fixed : 修复成功 vul_status_reboot : 修复成功待重启 vul_status_failed : 修复失败 vul_status_fix_after_reboot : 请重启主机再次修复
        :type status: str
        :param vul_id: 漏洞ID
        :type vul_id: str
        :param vul_type: 漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞
        :type vul_type: str
        :param asset_value: 资产重要性，包含如下3种 important ：重要资产 common ：一般资产 test ：测试资产
        :type asset_value: str
        :param group_name: 服务器组
        :type group_name: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 服务器ip
        :type host_ip: str
        :param export_size: 导出数据条数
        :type export_size: int
        :param export_header_list: 导出漏洞数据的表头信息列表
        :type export_header_list: list[list[str]]
        """
        
        

        self._status = None
        self._vul_id = None
        self._vul_type = None
        self._asset_value = None
        self._group_name = None
        self._host_name = None
        self._host_ip = None
        self._export_size = None
        self._export_header_list = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_type is not None:
            self.vul_type = vul_type
        if asset_value is not None:
            self.asset_value = asset_value
        if group_name is not None:
            self.group_name = group_name
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if export_size is not None:
            self.export_size = export_size
        if export_header_list is not None:
            self.export_header_list = export_header_list

    @property
    def status(self):
        r"""Gets the status of this ExportVulHandleHistoryRequestBody.

        漏洞状态 vul_status_unfix : 未处理 vul_status_ignored : 已忽略 vul_status_verified : 验证中 vul_status_fixing : 修复中 vul_status_fixed : 修复成功 vul_status_reboot : 修复成功待重启 vul_status_failed : 修复失败 vul_status_fix_after_reboot : 请重启主机再次修复

        :return: The status of this ExportVulHandleHistoryRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportVulHandleHistoryRequestBody.

        漏洞状态 vul_status_unfix : 未处理 vul_status_ignored : 已忽略 vul_status_verified : 验证中 vul_status_fixing : 修复中 vul_status_fixed : 修复成功 vul_status_reboot : 修复成功待重启 vul_status_failed : 修复失败 vul_status_fix_after_reboot : 请重启主机再次修复

        :param status: The status of this ExportVulHandleHistoryRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ExportVulHandleHistoryRequestBody.

        漏洞ID

        :return: The vul_id of this ExportVulHandleHistoryRequestBody.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ExportVulHandleHistoryRequestBody.

        漏洞ID

        :param vul_id: The vul_id of this ExportVulHandleHistoryRequestBody.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_type(self):
        r"""Gets the vul_type of this ExportVulHandleHistoryRequestBody.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞

        :return: The vul_type of this ExportVulHandleHistoryRequestBody.
        :rtype: str
        """
        return self._vul_type

    @vul_type.setter
    def vul_type(self, vul_type):
        r"""Sets the vul_type of this ExportVulHandleHistoryRequestBody.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞

        :param vul_type: The vul_type of this ExportVulHandleHistoryRequestBody.
        :type vul_type: str
        """
        self._vul_type = vul_type

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ExportVulHandleHistoryRequestBody.

        资产重要性，包含如下3种 important ：重要资产 common ：一般资产 test ：测试资产

        :return: The asset_value of this ExportVulHandleHistoryRequestBody.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ExportVulHandleHistoryRequestBody.

        资产重要性，包含如下3种 important ：重要资产 common ：一般资产 test ：测试资产

        :param asset_value: The asset_value of this ExportVulHandleHistoryRequestBody.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def group_name(self):
        r"""Gets the group_name of this ExportVulHandleHistoryRequestBody.

        服务器组

        :return: The group_name of this ExportVulHandleHistoryRequestBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ExportVulHandleHistoryRequestBody.

        服务器组

        :param group_name: The group_name of this ExportVulHandleHistoryRequestBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ExportVulHandleHistoryRequestBody.

        服务器名称

        :return: The host_name of this ExportVulHandleHistoryRequestBody.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ExportVulHandleHistoryRequestBody.

        服务器名称

        :param host_name: The host_name of this ExportVulHandleHistoryRequestBody.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ExportVulHandleHistoryRequestBody.

        服务器ip

        :return: The host_ip of this ExportVulHandleHistoryRequestBody.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ExportVulHandleHistoryRequestBody.

        服务器ip

        :param host_ip: The host_ip of this ExportVulHandleHistoryRequestBody.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def export_size(self):
        r"""Gets the export_size of this ExportVulHandleHistoryRequestBody.

        导出数据条数

        :return: The export_size of this ExportVulHandleHistoryRequestBody.
        :rtype: int
        """
        return self._export_size

    @export_size.setter
    def export_size(self, export_size):
        r"""Sets the export_size of this ExportVulHandleHistoryRequestBody.

        导出数据条数

        :param export_size: The export_size of this ExportVulHandleHistoryRequestBody.
        :type export_size: int
        """
        self._export_size = export_size

    @property
    def export_header_list(self):
        r"""Gets the export_header_list of this ExportVulHandleHistoryRequestBody.

        导出漏洞数据的表头信息列表

        :return: The export_header_list of this ExportVulHandleHistoryRequestBody.
        :rtype: list[list[str]]
        """
        return self._export_header_list

    @export_header_list.setter
    def export_header_list(self, export_header_list):
        r"""Sets the export_header_list of this ExportVulHandleHistoryRequestBody.

        导出漏洞数据的表头信息列表

        :param export_header_list: The export_header_list of this ExportVulHandleHistoryRequestBody.
        :type export_header_list: list[list[str]]
        """
        self._export_header_list = export_header_list

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
        if not isinstance(other, ExportVulHandleHistoryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
