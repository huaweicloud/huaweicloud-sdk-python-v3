# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostVulsRequest:

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
        'host_id': 'str',
        'type': 'str',
        'vul_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'handle_status': 'str',
        'status': 'str',
        'repair_priority': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'type': 'type',
        'vul_name': 'vul_name',
        'limit': 'limit',
        'offset': 'offset',
        'handle_status': 'handle_status',
        'status': 'status',
        'repair_priority': 'repair_priority'
    }

    def __init__(self, enterprise_project_id=None, host_id=None, type=None, vul_name=None, limit=None, offset=None, handle_status=None, status=None, repair_priority=None):
        r"""ListHostVulsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param host_id: 服务器id
        :type host_id: str
        :param type: 漏洞类型，默认为linux_vul，包括如下：   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞
        :type type: str
        :param vul_name: 漏洞名称
        :type vul_name: str
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param handle_status: 处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理
        :type handle_status: str
        :param status: 漏洞状态，包含如下：   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复
        :type status: str
        :param repair_priority: 修复优先级,包含如下 - Critical 紧急  - High 高  - Medium 中  - Low 低
        :type repair_priority: str
        """
        
        

        self._enterprise_project_id = None
        self._host_id = None
        self._type = None
        self._vul_name = None
        self._limit = None
        self._offset = None
        self._handle_status = None
        self._status = None
        self._repair_priority = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.host_id = host_id
        if type is not None:
            self.type = type
        if vul_name is not None:
            self.vul_name = vul_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if handle_status is not None:
            self.handle_status = handle_status
        if status is not None:
            self.status = status
        if repair_priority is not None:
            self.repair_priority = repair_priority

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListHostVulsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListHostVulsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListHostVulsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListHostVulsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ListHostVulsRequest.

        服务器id

        :return: The host_id of this ListHostVulsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListHostVulsRequest.

        服务器id

        :param host_id: The host_id of this ListHostVulsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def type(self):
        r"""Gets the type of this ListHostVulsRequest.

        漏洞类型，默认为linux_vul，包括如下：   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞

        :return: The type of this ListHostVulsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListHostVulsRequest.

        漏洞类型，默认为linux_vul，包括如下：   - linux_vul : 漏洞类型-linux漏洞   - windows_vul : 漏洞类型-windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞

        :param type: The type of this ListHostVulsRequest.
        :type type: str
        """
        self._type = type

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ListHostVulsRequest.

        漏洞名称

        :return: The vul_name of this ListHostVulsRequest.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ListHostVulsRequest.

        漏洞名称

        :param vul_name: The vul_name of this ListHostVulsRequest.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def limit(self):
        r"""Gets the limit of this ListHostVulsRequest.

        每页显示个数

        :return: The limit of this ListHostVulsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHostVulsRequest.

        每页显示个数

        :param limit: The limit of this ListHostVulsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListHostVulsRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListHostVulsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHostVulsRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListHostVulsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListHostVulsRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :return: The handle_status of this ListHostVulsRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListHostVulsRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :param handle_status: The handle_status of this ListHostVulsRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def status(self):
        r"""Gets the status of this ListHostVulsRequest.

        漏洞状态，包含如下：   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :return: The status of this ListHostVulsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListHostVulsRequest.

        漏洞状态，包含如下：   - vul_status_unfix : 未处理   - vul_status_ignored : 已忽略   - vul_status_verified : 验证中   - vul_status_fixing : 修复中   - vul_status_fixed : 修复成功   - vul_status_reboot : 修复成功待重启   - vul_status_failed : 修复失败   - vul_status_fix_after_reboot : 请重启主机再次修复

        :param status: The status of this ListHostVulsRequest.
        :type status: str
        """
        self._status = status

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this ListHostVulsRequest.

        修复优先级,包含如下 - Critical 紧急  - High 高  - Medium 中  - Low 低

        :return: The repair_priority of this ListHostVulsRequest.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this ListHostVulsRequest.

        修复优先级,包含如下 - Critical 紧急  - High 高  - Medium 中  - Low 低

        :param repair_priority: The repair_priority of this ListHostVulsRequest.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

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
        if not isinstance(other, ListHostVulsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
