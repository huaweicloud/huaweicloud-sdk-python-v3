# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetEastWestFirewallResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'project_id': 'str',
        'status': 'int',
        'er_associated_subnet': 'SubnetInfo',
        'firewall_associated_subnets': 'list[SubnetInfo]',
        'er': 'ErInstance',
        'inspection_vpc': 'VpcDetail',
        'protect_infos': 'list[EwProtectResourceInfo]',
        'total': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'object_id': 'object_id',
        'project_id': 'project_id',
        'status': 'status',
        'er_associated_subnet': 'er_associated_subnet',
        'firewall_associated_subnets': 'firewall_associated_subnets',
        'er': 'er',
        'inspection_vpc': 'inspection_vpc',
        'protect_infos': 'protect_infos',
        'total': 'total',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, object_id=None, project_id=None, status=None, er_associated_subnet=None, firewall_associated_subnets=None, er=None, inspection_vpc=None, protect_infos=None, total=None, offset=None, limit=None):
        """GetEastWestFirewallResponseBody

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。
        :type object_id: str
        :param project_id: 租户project_id
        :type project_id: str
        :param status: 防护状态：0 未开启防护， 1 已开启防护
        :type status: int
        :param er_associated_subnet: 
        :type er_associated_subnet: :class:`huaweicloudsdkcfw.v1.SubnetInfo`
        :param firewall_associated_subnets: 云防火墙关联子网信息
        :type firewall_associated_subnets: list[:class:`huaweicloudsdkcfw.v1.SubnetInfo`]
        :param er: 
        :type er: :class:`huaweicloudsdkcfw.v1.ErInstance`
        :param inspection_vpc: 
        :type inspection_vpc: :class:`huaweicloudsdkcfw.v1.VpcDetail`
        :param protect_infos: 东西向防护资源信息
        :type protect_infos: list[:class:`huaweicloudsdkcfw.v1.EwProtectResourceInfo`]
        :param total: 防护VPC总数
        :type total: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        """
        
        

        self._object_id = None
        self._project_id = None
        self._status = None
        self._er_associated_subnet = None
        self._firewall_associated_subnets = None
        self._er = None
        self._inspection_vpc = None
        self._protect_infos = None
        self._total = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        if er_associated_subnet is not None:
            self.er_associated_subnet = er_associated_subnet
        if firewall_associated_subnets is not None:
            self.firewall_associated_subnets = firewall_associated_subnets
        if er is not None:
            self.er = er
        if inspection_vpc is not None:
            self.inspection_vpc = inspection_vpc
        if protect_infos is not None:
            self.protect_infos = protect_infos
        if total is not None:
            self.total = total
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def object_id(self):
        """Gets the object_id of this GetEastWestFirewallResponseBody.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :return: The object_id of this GetEastWestFirewallResponseBody.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this GetEastWestFirewallResponseBody.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用查询防火墙实例接口获得，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。具体可参考APIExlorer和帮助中心FAQ。

        :param object_id: The object_id of this GetEastWestFirewallResponseBody.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def project_id(self):
        """Gets the project_id of this GetEastWestFirewallResponseBody.

        租户project_id

        :return: The project_id of this GetEastWestFirewallResponseBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this GetEastWestFirewallResponseBody.

        租户project_id

        :param project_id: The project_id of this GetEastWestFirewallResponseBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        """Gets the status of this GetEastWestFirewallResponseBody.

        防护状态：0 未开启防护， 1 已开启防护

        :return: The status of this GetEastWestFirewallResponseBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetEastWestFirewallResponseBody.

        防护状态：0 未开启防护， 1 已开启防护

        :param status: The status of this GetEastWestFirewallResponseBody.
        :type status: int
        """
        self._status = status

    @property
    def er_associated_subnet(self):
        """Gets the er_associated_subnet of this GetEastWestFirewallResponseBody.

        :return: The er_associated_subnet of this GetEastWestFirewallResponseBody.
        :rtype: :class:`huaweicloudsdkcfw.v1.SubnetInfo`
        """
        return self._er_associated_subnet

    @er_associated_subnet.setter
    def er_associated_subnet(self, er_associated_subnet):
        """Sets the er_associated_subnet of this GetEastWestFirewallResponseBody.

        :param er_associated_subnet: The er_associated_subnet of this GetEastWestFirewallResponseBody.
        :type er_associated_subnet: :class:`huaweicloudsdkcfw.v1.SubnetInfo`
        """
        self._er_associated_subnet = er_associated_subnet

    @property
    def firewall_associated_subnets(self):
        """Gets the firewall_associated_subnets of this GetEastWestFirewallResponseBody.

        云防火墙关联子网信息

        :return: The firewall_associated_subnets of this GetEastWestFirewallResponseBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.SubnetInfo`]
        """
        return self._firewall_associated_subnets

    @firewall_associated_subnets.setter
    def firewall_associated_subnets(self, firewall_associated_subnets):
        """Sets the firewall_associated_subnets of this GetEastWestFirewallResponseBody.

        云防火墙关联子网信息

        :param firewall_associated_subnets: The firewall_associated_subnets of this GetEastWestFirewallResponseBody.
        :type firewall_associated_subnets: list[:class:`huaweicloudsdkcfw.v1.SubnetInfo`]
        """
        self._firewall_associated_subnets = firewall_associated_subnets

    @property
    def er(self):
        """Gets the er of this GetEastWestFirewallResponseBody.

        :return: The er of this GetEastWestFirewallResponseBody.
        :rtype: :class:`huaweicloudsdkcfw.v1.ErInstance`
        """
        return self._er

    @er.setter
    def er(self, er):
        """Sets the er of this GetEastWestFirewallResponseBody.

        :param er: The er of this GetEastWestFirewallResponseBody.
        :type er: :class:`huaweicloudsdkcfw.v1.ErInstance`
        """
        self._er = er

    @property
    def inspection_vpc(self):
        """Gets the inspection_vpc of this GetEastWestFirewallResponseBody.

        :return: The inspection_vpc of this GetEastWestFirewallResponseBody.
        :rtype: :class:`huaweicloudsdkcfw.v1.VpcDetail`
        """
        return self._inspection_vpc

    @inspection_vpc.setter
    def inspection_vpc(self, inspection_vpc):
        """Sets the inspection_vpc of this GetEastWestFirewallResponseBody.

        :param inspection_vpc: The inspection_vpc of this GetEastWestFirewallResponseBody.
        :type inspection_vpc: :class:`huaweicloudsdkcfw.v1.VpcDetail`
        """
        self._inspection_vpc = inspection_vpc

    @property
    def protect_infos(self):
        """Gets the protect_infos of this GetEastWestFirewallResponseBody.

        东西向防护资源信息

        :return: The protect_infos of this GetEastWestFirewallResponseBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.EwProtectResourceInfo`]
        """
        return self._protect_infos

    @protect_infos.setter
    def protect_infos(self, protect_infos):
        """Sets the protect_infos of this GetEastWestFirewallResponseBody.

        东西向防护资源信息

        :param protect_infos: The protect_infos of this GetEastWestFirewallResponseBody.
        :type protect_infos: list[:class:`huaweicloudsdkcfw.v1.EwProtectResourceInfo`]
        """
        self._protect_infos = protect_infos

    @property
    def total(self):
        """Gets the total of this GetEastWestFirewallResponseBody.

        防护VPC总数

        :return: The total of this GetEastWestFirewallResponseBody.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this GetEastWestFirewallResponseBody.

        防护VPC总数

        :param total: The total of this GetEastWestFirewallResponseBody.
        :type total: int
        """
        self._total = total

    @property
    def offset(self):
        """Gets the offset of this GetEastWestFirewallResponseBody.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this GetEastWestFirewallResponseBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GetEastWestFirewallResponseBody.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this GetEastWestFirewallResponseBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this GetEastWestFirewallResponseBody.

        每页显示个数

        :return: The limit of this GetEastWestFirewallResponseBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetEastWestFirewallResponseBody.

        每页显示个数

        :param limit: The limit of this GetEastWestFirewallResponseBody.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, GetEastWestFirewallResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
