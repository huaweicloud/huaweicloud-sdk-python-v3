# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulnerabilitiesRequest:

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
        'limit': 'int',
        'offset': 'int',
        'repair_priority': 'str',
        'handle_status': 'str',
        'cve_id': 'str',
        'label_list': 'str',
        'status': 'str',
        'asset_value': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'limit': 'limit',
        'offset': 'offset',
        'repair_priority': 'repair_priority',
        'handle_status': 'handle_status',
        'cve_id': 'cve_id',
        'label_list': 'label_list',
        'status': 'status',
        'asset_value': 'asset_value',
        'group_name': 'group_name'
    }

    def __init__(self, enterprise_project_id=None, type=None, vul_id=None, vul_name=None, limit=None, offset=None, repair_priority=None, handle_status=None, cve_id=None, label_list=None, status=None, asset_value=None, group_name=None):
        """ListVulnerabilitiesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业租户ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param type: 漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞
        :type type: str
        :param vul_id: 漏洞ID
        :type vul_id: str
        :param vul_name: 漏洞名称
        :type vul_name: str
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param repair_priority: 修复优先级 Critical 紧急 High  高 Medium 中 Low 低
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
        """
        
        

        self._enterprise_project_id = None
        self._type = None
        self._vul_id = None
        self._vul_name = None
        self._limit = None
        self._offset = None
        self._repair_priority = None
        self._handle_status = None
        self._cve_id = None
        self._label_list = None
        self._status = None
        self._asset_value = None
        self._group_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
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

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListVulnerabilitiesRequest.

        企业租户ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListVulnerabilitiesRequest.

        企业租户ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListVulnerabilitiesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        """Gets the type of this ListVulnerabilitiesRequest.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞

        :return: The type of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListVulnerabilitiesRequest.

        漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞

        :param type: The type of this ListVulnerabilitiesRequest.
        :type type: str
        """
        self._type = type

    @property
    def vul_id(self):
        """Gets the vul_id of this ListVulnerabilitiesRequest.

        漏洞ID

        :return: The vul_id of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        """Sets the vul_id of this ListVulnerabilitiesRequest.

        漏洞ID

        :param vul_id: The vul_id of this ListVulnerabilitiesRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        """Gets the vul_name of this ListVulnerabilitiesRequest.

        漏洞名称

        :return: The vul_name of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        """Sets the vul_name of this ListVulnerabilitiesRequest.

        漏洞名称

        :param vul_name: The vul_name of this ListVulnerabilitiesRequest.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def limit(self):
        """Gets the limit of this ListVulnerabilitiesRequest.

        每页显示个数

        :return: The limit of this ListVulnerabilitiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVulnerabilitiesRequest.

        每页显示个数

        :param limit: The limit of this ListVulnerabilitiesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListVulnerabilitiesRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListVulnerabilitiesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVulnerabilitiesRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListVulnerabilitiesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def repair_priority(self):
        """Gets the repair_priority of this ListVulnerabilitiesRequest.

        修复优先级 Critical 紧急 High  高 Medium 中 Low 低

        :return: The repair_priority of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        """Sets the repair_priority of this ListVulnerabilitiesRequest.

        修复优先级 Critical 紧急 High  高 Medium 中 Low 低

        :param repair_priority: The repair_priority of this ListVulnerabilitiesRequest.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

    @property
    def handle_status(self):
        """Gets the handle_status of this ListVulnerabilitiesRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :return: The handle_status of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        """Sets the handle_status of this ListVulnerabilitiesRequest.

        处置状态，包含如下:   - unhandled ：未处理   - handled : 已处理

        :param handle_status: The handle_status of this ListVulnerabilitiesRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def cve_id(self):
        """Gets the cve_id of this ListVulnerabilitiesRequest.

        漏洞编号

        :return: The cve_id of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        """Sets the cve_id of this ListVulnerabilitiesRequest.

        漏洞编号

        :param cve_id: The cve_id of this ListVulnerabilitiesRequest.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def label_list(self):
        """Gets the label_list of this ListVulnerabilitiesRequest.

        漏洞标签

        :return: The label_list of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._label_list

    @label_list.setter
    def label_list(self, label_list):
        """Sets the label_list of this ListVulnerabilitiesRequest.

        漏洞标签

        :param label_list: The label_list of this ListVulnerabilitiesRequest.
        :type label_list: str
        """
        self._label_list = label_list

    @property
    def status(self):
        """Gets the status of this ListVulnerabilitiesRequest.

        漏洞状态

        :return: The status of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListVulnerabilitiesRequest.

        漏洞状态

        :param status: The status of this ListVulnerabilitiesRequest.
        :type status: str
        """
        self._status = status

    @property
    def asset_value(self):
        """Gets the asset_value of this ListVulnerabilitiesRequest.

        资产重要性 important common test

        :return: The asset_value of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        """Sets the asset_value of this ListVulnerabilitiesRequest.

        资产重要性 important common test

        :param asset_value: The asset_value of this ListVulnerabilitiesRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def group_name(self):
        """Gets the group_name of this ListVulnerabilitiesRequest.

        服务器组名称

        :return: The group_name of this ListVulnerabilitiesRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ListVulnerabilitiesRequest.

        服务器组名称

        :param group_name: The group_name of this ListVulnerabilitiesRequest.
        :type group_name: str
        """
        self._group_name = group_name

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
        if not isinstance(other, ListVulnerabilitiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
