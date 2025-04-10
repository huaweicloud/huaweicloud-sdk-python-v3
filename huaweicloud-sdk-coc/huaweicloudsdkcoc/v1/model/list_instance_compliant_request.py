# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceCompliantRequest:

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
        'name': 'str',
        'instance_id': 'str',
        'ip': 'str',
        'eip': 'str',
        'operating_system': 'str',
        'region': 'str',
        'group': 'str',
        'compliant_status': 'str',
        'order_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_dir': 'str',
        'sort_key': 'str',
        'report_scene': 'str',
        'cce_info_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'instance_id': 'instance_id',
        'ip': 'ip',
        'eip': 'eip',
        'operating_system': 'operating_system',
        'region': 'region',
        'group': 'group',
        'compliant_status': 'compliant_status',
        'order_id': 'order_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'report_scene': 'report_scene',
        'cce_info_id': 'cce_info_id'
    }

    def __init__(self, enterprise_project_id=None, name=None, instance_id=None, ip=None, eip=None, operating_system=None, region=None, group=None, compliant_status=None, order_id=None, offset=None, limit=None, sort_dir=None, sort_key=None, report_scene=None, cce_info_id=None):
        r"""ListInstanceCompliantRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param name: 名称
        :type name: str
        :param instance_id: ECS实例id
        :type instance_id: str
        :param ip: 内网ip
        :type ip: str
        :param eip: 弹性公网ip
        :type eip: str
        :param operating_system: 操作系统 - HuaweiCloudEulerOS - CentOS - EulerOS
        :type operating_system: str
        :param region: 区域
        :type region: str
        :param group: 分组
        :type group: str
        :param compliant_status: 合规性状态 - non_compliant：不合规 - compliant：合规
        :type compliant_status: str
        :param order_id: 工单id
        :type order_id: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 每页数量
        :type limit: int
        :param sort_dir: 排序 - asc：升序 - desc：降序
        :type sort_dir: str
        :param sort_key: 排序字段 - report_time：报告时间
        :type sort_key: str
        :param report_scene: 报告场景 - CCE  - ECS
        :type report_scene: str
        :param cce_info_id: cce 集群信息id
        :type cce_info_id: str
        """
        
        

        self._enterprise_project_id = None
        self._name = None
        self._instance_id = None
        self._ip = None
        self._eip = None
        self._operating_system = None
        self._region = None
        self._group = None
        self._compliant_status = None
        self._order_id = None
        self._offset = None
        self._limit = None
        self._sort_dir = None
        self._sort_key = None
        self._report_scene = None
        self._cce_info_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if ip is not None:
            self.ip = ip
        if eip is not None:
            self.eip = eip
        if operating_system is not None:
            self.operating_system = operating_system
        if region is not None:
            self.region = region
        if group is not None:
            self.group = group
        if compliant_status is not None:
            self.compliant_status = compliant_status
        if order_id is not None:
            self.order_id = order_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if report_scene is not None:
            self.report_scene = report_scene
        if cce_info_id is not None:
            self.cce_info_id = cce_info_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListInstanceCompliantRequest.

        企业项目id

        :return: The enterprise_project_id of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListInstanceCompliantRequest.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListInstanceCompliantRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this ListInstanceCompliantRequest.

        名称

        :return: The name of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInstanceCompliantRequest.

        名称

        :param name: The name of this ListInstanceCompliantRequest.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceCompliantRequest.

        ECS实例id

        :return: The instance_id of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceCompliantRequest.

        ECS实例id

        :param instance_id: The instance_id of this ListInstanceCompliantRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def ip(self):
        r"""Gets the ip of this ListInstanceCompliantRequest.

        内网ip

        :return: The ip of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ListInstanceCompliantRequest.

        内网ip

        :param ip: The ip of this ListInstanceCompliantRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def eip(self):
        r"""Gets the eip of this ListInstanceCompliantRequest.

        弹性公网ip

        :return: The eip of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this ListInstanceCompliantRequest.

        弹性公网ip

        :param eip: The eip of this ListInstanceCompliantRequest.
        :type eip: str
        """
        self._eip = eip

    @property
    def operating_system(self):
        r"""Gets the operating_system of this ListInstanceCompliantRequest.

        操作系统 - HuaweiCloudEulerOS - CentOS - EulerOS

        :return: The operating_system of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        r"""Sets the operating_system of this ListInstanceCompliantRequest.

        操作系统 - HuaweiCloudEulerOS - CentOS - EulerOS

        :param operating_system: The operating_system of this ListInstanceCompliantRequest.
        :type operating_system: str
        """
        self._operating_system = operating_system

    @property
    def region(self):
        r"""Gets the region of this ListInstanceCompliantRequest.

        区域

        :return: The region of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListInstanceCompliantRequest.

        区域

        :param region: The region of this ListInstanceCompliantRequest.
        :type region: str
        """
        self._region = region

    @property
    def group(self):
        r"""Gets the group of this ListInstanceCompliantRequest.

        分组

        :return: The group of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ListInstanceCompliantRequest.

        分组

        :param group: The group of this ListInstanceCompliantRequest.
        :type group: str
        """
        self._group = group

    @property
    def compliant_status(self):
        r"""Gets the compliant_status of this ListInstanceCompliantRequest.

        合规性状态 - non_compliant：不合规 - compliant：合规

        :return: The compliant_status of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._compliant_status

    @compliant_status.setter
    def compliant_status(self, compliant_status):
        r"""Sets the compliant_status of this ListInstanceCompliantRequest.

        合规性状态 - non_compliant：不合规 - compliant：合规

        :param compliant_status: The compliant_status of this ListInstanceCompliantRequest.
        :type compliant_status: str
        """
        self._compliant_status = compliant_status

    @property
    def order_id(self):
        r"""Gets the order_id of this ListInstanceCompliantRequest.

        工单id

        :return: The order_id of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ListInstanceCompliantRequest.

        工单id

        :param order_id: The order_id of this ListInstanceCompliantRequest.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceCompliantRequest.

        偏移量

        :return: The offset of this ListInstanceCompliantRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceCompliantRequest.

        偏移量

        :param offset: The offset of this ListInstanceCompliantRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceCompliantRequest.

        每页数量

        :return: The limit of this ListInstanceCompliantRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceCompliantRequest.

        每页数量

        :param limit: The limit of this ListInstanceCompliantRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListInstanceCompliantRequest.

        排序 - asc：升序 - desc：降序

        :return: The sort_dir of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListInstanceCompliantRequest.

        排序 - asc：升序 - desc：降序

        :param sort_dir: The sort_dir of this ListInstanceCompliantRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListInstanceCompliantRequest.

        排序字段 - report_time：报告时间

        :return: The sort_key of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListInstanceCompliantRequest.

        排序字段 - report_time：报告时间

        :param sort_key: The sort_key of this ListInstanceCompliantRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def report_scene(self):
        r"""Gets the report_scene of this ListInstanceCompliantRequest.

        报告场景 - CCE  - ECS

        :return: The report_scene of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._report_scene

    @report_scene.setter
    def report_scene(self, report_scene):
        r"""Sets the report_scene of this ListInstanceCompliantRequest.

        报告场景 - CCE  - ECS

        :param report_scene: The report_scene of this ListInstanceCompliantRequest.
        :type report_scene: str
        """
        self._report_scene = report_scene

    @property
    def cce_info_id(self):
        r"""Gets the cce_info_id of this ListInstanceCompliantRequest.

        cce 集群信息id

        :return: The cce_info_id of this ListInstanceCompliantRequest.
        :rtype: str
        """
        return self._cce_info_id

    @cce_info_id.setter
    def cce_info_id(self, cce_info_id):
        r"""Sets the cce_info_id of this ListInstanceCompliantRequest.

        cce 集群信息id

        :param cce_info_id: The cce_info_id of this ListInstanceCompliantRequest.
        :type cce_info_id: str
        """
        self._cce_info_id = cce_info_id

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
        if not isinstance(other, ListInstanceCompliantRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
