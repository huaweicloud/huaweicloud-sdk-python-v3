# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulHandleHistoryRequest:

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
        'status': 'list[str]',
        'vul_id': 'str',
        'vul_type': 'str',
        'asset_value': 'str',
        'group_name': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'cluster_id': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'status': 'status',
        'vul_id': 'vul_id',
        'vul_type': 'vul_type',
        'asset_value': 'asset_value',
        'group_name': 'group_name',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'cluster_id': 'cluster_id',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, status=None, vul_id=None, vul_type=None, asset_value=None, group_name=None, host_name=None, host_ip=None, cluster_id=None, sort_key=None, sort_dir=None, public_ip=None, private_ip=None, limit=None, offset=None):
        r"""ListVulHandleHistoryRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param status: 漏洞状态，包含如下：   - vul_status_unfix：未处理   - vul_status_ignored：已忽略   - vul_status_verified：验证中   - vul_status_fixing：修复中   - vul_status_fixed：修复成功   - vul_status_reboot：修复成功待重启   - vul_status_failed：修复失败   - vul_status_fix_after_reboot：请重启主机再次修复
        :type status: list[str]
        :param vul_id: 漏洞ID
        :type vul_id: str
        :param vul_type: 漏洞类型，包含如下:   - linux_vul：Linux漏洞   - windows_vul：Windows漏洞   - web_cms：Web-CMS漏洞   - app_vul：应用漏洞   - urgent_vul：应急漏洞
        :type vul_type: str
        :param asset_value: 资产重要性，包含如下:   - important：重要资产   - common：一般资产   - test：测试资产
        :type asset_value: str
        :param group_name: 服务器组
        :type group_name: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 服务器IP
        :type host_ip: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param sort_key: 排序字段，包含如下：   - handle_time：处置时间
        :type sort_key: str
        :param sort_dir: 排序顺序，若sort_key不为空，设置返回结果按照sort_key升序或降序排序，默认降序排序，包含如下：   - asc：升序   - desc：降序
        :type sort_dir: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param private_ip: 服务器私网IP
        :type private_ip: str
        :param limit: 每页个数
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._status = None
        self._vul_id = None
        self._vul_type = None
        self._asset_value = None
        self._group_name = None
        self._host_name = None
        self._host_ip = None
        self._cluster_id = None
        self._sort_key = None
        self._sort_dir = None
        self._public_ip = None
        self._private_ip = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
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
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        self.limit = limit
        self.offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVulHandleHistoryRequest.

        企业项目ID

        :return: The enterprise_project_id of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVulHandleHistoryRequest.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListVulHandleHistoryRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def status(self):
        r"""Gets the status of this ListVulHandleHistoryRequest.

        漏洞状态，包含如下：   - vul_status_unfix：未处理   - vul_status_ignored：已忽略   - vul_status_verified：验证中   - vul_status_fixing：修复中   - vul_status_fixed：修复成功   - vul_status_reboot：修复成功待重启   - vul_status_failed：修复失败   - vul_status_fix_after_reboot：请重启主机再次修复

        :return: The status of this ListVulHandleHistoryRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVulHandleHistoryRequest.

        漏洞状态，包含如下：   - vul_status_unfix：未处理   - vul_status_ignored：已忽略   - vul_status_verified：验证中   - vul_status_fixing：修复中   - vul_status_fixed：修复成功   - vul_status_reboot：修复成功待重启   - vul_status_failed：修复失败   - vul_status_fix_after_reboot：请重启主机再次修复

        :param status: The status of this ListVulHandleHistoryRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ListVulHandleHistoryRequest.

        漏洞ID

        :return: The vul_id of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ListVulHandleHistoryRequest.

        漏洞ID

        :param vul_id: The vul_id of this ListVulHandleHistoryRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_type(self):
        r"""Gets the vul_type of this ListVulHandleHistoryRequest.

        漏洞类型，包含如下:   - linux_vul：Linux漏洞   - windows_vul：Windows漏洞   - web_cms：Web-CMS漏洞   - app_vul：应用漏洞   - urgent_vul：应急漏洞

        :return: The vul_type of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._vul_type

    @vul_type.setter
    def vul_type(self, vul_type):
        r"""Sets the vul_type of this ListVulHandleHistoryRequest.

        漏洞类型，包含如下:   - linux_vul：Linux漏洞   - windows_vul：Windows漏洞   - web_cms：Web-CMS漏洞   - app_vul：应用漏洞   - urgent_vul：应急漏洞

        :param vul_type: The vul_type of this ListVulHandleHistoryRequest.
        :type vul_type: str
        """
        self._vul_type = vul_type

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListVulHandleHistoryRequest.

        资产重要性，包含如下:   - important：重要资产   - common：一般资产   - test：测试资产

        :return: The asset_value of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListVulHandleHistoryRequest.

        资产重要性，包含如下:   - important：重要资产   - common：一般资产   - test：测试资产

        :param asset_value: The asset_value of this ListVulHandleHistoryRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def group_name(self):
        r"""Gets the group_name of this ListVulHandleHistoryRequest.

        服务器组

        :return: The group_name of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListVulHandleHistoryRequest.

        服务器组

        :param group_name: The group_name of this ListVulHandleHistoryRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ListVulHandleHistoryRequest.

        服务器名称

        :return: The host_name of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListVulHandleHistoryRequest.

        服务器名称

        :param host_name: The host_name of this ListVulHandleHistoryRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListVulHandleHistoryRequest.

        服务器IP

        :return: The host_ip of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListVulHandleHistoryRequest.

        服务器IP

        :param host_ip: The host_ip of this ListVulHandleHistoryRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListVulHandleHistoryRequest.

        集群ID

        :return: The cluster_id of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListVulHandleHistoryRequest.

        集群ID

        :param cluster_id: The cluster_id of this ListVulHandleHistoryRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListVulHandleHistoryRequest.

        排序字段，包含如下：   - handle_time：处置时间

        :return: The sort_key of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListVulHandleHistoryRequest.

        排序字段，包含如下：   - handle_time：处置时间

        :param sort_key: The sort_key of this ListVulHandleHistoryRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListVulHandleHistoryRequest.

        排序顺序，若sort_key不为空，设置返回结果按照sort_key升序或降序排序，默认降序排序，包含如下：   - asc：升序   - desc：降序

        :return: The sort_dir of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListVulHandleHistoryRequest.

        排序顺序，若sort_key不为空，设置返回结果按照sort_key升序或降序排序，默认降序排序，包含如下：   - asc：升序   - desc：降序

        :param sort_dir: The sort_dir of this ListVulHandleHistoryRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListVulHandleHistoryRequest.

        服务器公网IP

        :return: The public_ip of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListVulHandleHistoryRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListVulHandleHistoryRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListVulHandleHistoryRequest.

        服务器私网IP

        :return: The private_ip of this ListVulHandleHistoryRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListVulHandleHistoryRequest.

        服务器私网IP

        :param private_ip: The private_ip of this ListVulHandleHistoryRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def limit(self):
        r"""Gets the limit of this ListVulHandleHistoryRequest.

        每页个数

        :return: The limit of this ListVulHandleHistoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVulHandleHistoryRequest.

        每页个数

        :param limit: The limit of this ListVulHandleHistoryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListVulHandleHistoryRequest.

        偏移量

        :return: The offset of this ListVulHandleHistoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVulHandleHistoryRequest.

        偏移量

        :param offset: The offset of this ListVulHandleHistoryRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListVulHandleHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
