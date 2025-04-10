# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmQueryClusterInstanceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configuration_status': 'str',
        'params_group_id': 'str',
        'type': 'str',
        'role': 'str',
        'subnetid': 'str',
        'securegroup': 'str',
        'vpc': 'str',
        'azcode': 'str',
        'region': 'str',
        'created': 'str',
        'updated': 'str',
        'name': 'str',
        'id': 'str',
        'flavor': 'CdmQueryClusterInstanceDetailFlavor',
        'datastore': 'Datastore',
        'dbuser': 'str',
        'pay_model': 'int',
        'public_ip': 'str',
        'traffic_ip': 'str',
        'traffic_ipv6': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'configuration_status': 'configurationStatus',
        'params_group_id': 'paramsGroupId',
        'type': 'type',
        'role': 'role',
        'subnetid': 'subnetid',
        'securegroup': 'securegroup',
        'vpc': 'vpc',
        'azcode': 'azcode',
        'region': 'region',
        'created': 'created',
        'updated': 'updated',
        'name': 'name',
        'id': 'id',
        'flavor': 'flavor',
        'datastore': 'datastore',
        'dbuser': 'dbuser',
        'pay_model': 'payModel',
        'public_ip': 'publicIp',
        'traffic_ip': 'trafficIp',
        'traffic_ipv6': 'trafficIpv6',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, configuration_status=None, params_group_id=None, type=None, role=None, subnetid=None, securegroup=None, vpc=None, azcode=None, region=None, created=None, updated=None, name=None, id=None, flavor=None, datastore=None, dbuser=None, pay_model=None, public_ip=None, traffic_ip=None, traffic_ipv6=None, cluster_id=None):
        r"""CdmQueryClusterInstanceDetail

        The model defined in huaweicloud sdk

        :param configuration_status: 节点配置状态： - In-Sync：配置已同步。 - Applying：配置中。 - Sync-Failure：配置失败。
        :type configuration_status: str
        :param params_group_id: 配置ID
        :type params_group_id: str
        :param type: 配置服务类型，这里为cdm
        :type type: str
        :param role: 实例模式，这里为Standalone
        :type role: str
        :param subnetid: 实例的子网ID
        :type subnetid: str
        :param securegroup: 安全组ID
        :type securegroup: str
        :param vpc: 实例的VPC ID
        :type vpc: str
        :param azcode: 可用区名称
        :type azcode: str
        :param region: 局点名称
        :type region: str
        :param created: 实例创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ
        :type created: str
        :param updated: 实例更新时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ
        :type updated: str
        :param name: 实例名称
        :type name: str
        :param id: 实例ID
        :type id: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkcdm.v1.CdmQueryClusterInstanceDetailFlavor`
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcdm.v1.Datastore`
        :param dbuser: 数据库用户，这里为cdm。
        :type dbuser: str
        :param pay_model: 付费模式： - 0：按需 - 1：包周期
        :type pay_model: int
        :param public_ip: 集群绑定的公网地址
        :type public_ip: str
        :param traffic_ip: 集群的内网地址
        :type traffic_ip: str
        :param traffic_ipv6: 集群的内网IPv6地址
        :type traffic_ipv6: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        """
        
        

        self._configuration_status = None
        self._params_group_id = None
        self._type = None
        self._role = None
        self._subnetid = None
        self._securegroup = None
        self._vpc = None
        self._azcode = None
        self._region = None
        self._created = None
        self._updated = None
        self._name = None
        self._id = None
        self._flavor = None
        self._datastore = None
        self._dbuser = None
        self._pay_model = None
        self._public_ip = None
        self._traffic_ip = None
        self._traffic_ipv6 = None
        self._cluster_id = None
        self.discriminator = None

        if configuration_status is not None:
            self.configuration_status = configuration_status
        if params_group_id is not None:
            self.params_group_id = params_group_id
        if type is not None:
            self.type = type
        if role is not None:
            self.role = role
        if subnetid is not None:
            self.subnetid = subnetid
        if securegroup is not None:
            self.securegroup = securegroup
        if vpc is not None:
            self.vpc = vpc
        if azcode is not None:
            self.azcode = azcode
        if region is not None:
            self.region = region
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if flavor is not None:
            self.flavor = flavor
        if datastore is not None:
            self.datastore = datastore
        if dbuser is not None:
            self.dbuser = dbuser
        if pay_model is not None:
            self.pay_model = pay_model
        if public_ip is not None:
            self.public_ip = public_ip
        if traffic_ip is not None:
            self.traffic_ip = traffic_ip
        if traffic_ipv6 is not None:
            self.traffic_ipv6 = traffic_ipv6
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def configuration_status(self):
        r"""Gets the configuration_status of this CdmQueryClusterInstanceDetail.

        节点配置状态： - In-Sync：配置已同步。 - Applying：配置中。 - Sync-Failure：配置失败。

        :return: The configuration_status of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._configuration_status

    @configuration_status.setter
    def configuration_status(self, configuration_status):
        r"""Sets the configuration_status of this CdmQueryClusterInstanceDetail.

        节点配置状态： - In-Sync：配置已同步。 - Applying：配置中。 - Sync-Failure：配置失败。

        :param configuration_status: The configuration_status of this CdmQueryClusterInstanceDetail.
        :type configuration_status: str
        """
        self._configuration_status = configuration_status

    @property
    def params_group_id(self):
        r"""Gets the params_group_id of this CdmQueryClusterInstanceDetail.

        配置ID

        :return: The params_group_id of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._params_group_id

    @params_group_id.setter
    def params_group_id(self, params_group_id):
        r"""Sets the params_group_id of this CdmQueryClusterInstanceDetail.

        配置ID

        :param params_group_id: The params_group_id of this CdmQueryClusterInstanceDetail.
        :type params_group_id: str
        """
        self._params_group_id = params_group_id

    @property
    def type(self):
        r"""Gets the type of this CdmQueryClusterInstanceDetail.

        配置服务类型，这里为cdm

        :return: The type of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CdmQueryClusterInstanceDetail.

        配置服务类型，这里为cdm

        :param type: The type of this CdmQueryClusterInstanceDetail.
        :type type: str
        """
        self._type = type

    @property
    def role(self):
        r"""Gets the role of this CdmQueryClusterInstanceDetail.

        实例模式，这里为Standalone

        :return: The role of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this CdmQueryClusterInstanceDetail.

        实例模式，这里为Standalone

        :param role: The role of this CdmQueryClusterInstanceDetail.
        :type role: str
        """
        self._role = role

    @property
    def subnetid(self):
        r"""Gets the subnetid of this CdmQueryClusterInstanceDetail.

        实例的子网ID

        :return: The subnetid of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._subnetid

    @subnetid.setter
    def subnetid(self, subnetid):
        r"""Sets the subnetid of this CdmQueryClusterInstanceDetail.

        实例的子网ID

        :param subnetid: The subnetid of this CdmQueryClusterInstanceDetail.
        :type subnetid: str
        """
        self._subnetid = subnetid

    @property
    def securegroup(self):
        r"""Gets the securegroup of this CdmQueryClusterInstanceDetail.

        安全组ID

        :return: The securegroup of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._securegroup

    @securegroup.setter
    def securegroup(self, securegroup):
        r"""Sets the securegroup of this CdmQueryClusterInstanceDetail.

        安全组ID

        :param securegroup: The securegroup of this CdmQueryClusterInstanceDetail.
        :type securegroup: str
        """
        self._securegroup = securegroup

    @property
    def vpc(self):
        r"""Gets the vpc of this CdmQueryClusterInstanceDetail.

        实例的VPC ID

        :return: The vpc of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this CdmQueryClusterInstanceDetail.

        实例的VPC ID

        :param vpc: The vpc of this CdmQueryClusterInstanceDetail.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def azcode(self):
        r"""Gets the azcode of this CdmQueryClusterInstanceDetail.

        可用区名称

        :return: The azcode of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._azcode

    @azcode.setter
    def azcode(self, azcode):
        r"""Sets the azcode of this CdmQueryClusterInstanceDetail.

        可用区名称

        :param azcode: The azcode of this CdmQueryClusterInstanceDetail.
        :type azcode: str
        """
        self._azcode = azcode

    @property
    def region(self):
        r"""Gets the region of this CdmQueryClusterInstanceDetail.

        局点名称

        :return: The region of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CdmQueryClusterInstanceDetail.

        局点名称

        :param region: The region of this CdmQueryClusterInstanceDetail.
        :type region: str
        """
        self._region = region

    @property
    def created(self):
        r"""Gets the created of this CdmQueryClusterInstanceDetail.

        实例创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :return: The created of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this CdmQueryClusterInstanceDetail.

        实例创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :param created: The created of this CdmQueryClusterInstanceDetail.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this CdmQueryClusterInstanceDetail.

        实例更新时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :return: The updated of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this CdmQueryClusterInstanceDetail.

        实例更新时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :param updated: The updated of this CdmQueryClusterInstanceDetail.
        :type updated: str
        """
        self._updated = updated

    @property
    def name(self):
        r"""Gets the name of this CdmQueryClusterInstanceDetail.

        实例名称

        :return: The name of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CdmQueryClusterInstanceDetail.

        实例名称

        :param name: The name of this CdmQueryClusterInstanceDetail.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this CdmQueryClusterInstanceDetail.

        实例ID

        :return: The id of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CdmQueryClusterInstanceDetail.

        实例ID

        :param id: The id of this CdmQueryClusterInstanceDetail.
        :type id: str
        """
        self._id = id

    @property
    def flavor(self):
        r"""Gets the flavor of this CdmQueryClusterInstanceDetail.

        :return: The flavor of this CdmQueryClusterInstanceDetail.
        :rtype: :class:`huaweicloudsdkcdm.v1.CdmQueryClusterInstanceDetailFlavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CdmQueryClusterInstanceDetail.

        :param flavor: The flavor of this CdmQueryClusterInstanceDetail.
        :type flavor: :class:`huaweicloudsdkcdm.v1.CdmQueryClusterInstanceDetailFlavor`
        """
        self._flavor = flavor

    @property
    def datastore(self):
        r"""Gets the datastore of this CdmQueryClusterInstanceDetail.

        :return: The datastore of this CdmQueryClusterInstanceDetail.
        :rtype: :class:`huaweicloudsdkcdm.v1.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this CdmQueryClusterInstanceDetail.

        :param datastore: The datastore of this CdmQueryClusterInstanceDetail.
        :type datastore: :class:`huaweicloudsdkcdm.v1.Datastore`
        """
        self._datastore = datastore

    @property
    def dbuser(self):
        r"""Gets the dbuser of this CdmQueryClusterInstanceDetail.

        数据库用户，这里为cdm。

        :return: The dbuser of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._dbuser

    @dbuser.setter
    def dbuser(self, dbuser):
        r"""Sets the dbuser of this CdmQueryClusterInstanceDetail.

        数据库用户，这里为cdm。

        :param dbuser: The dbuser of this CdmQueryClusterInstanceDetail.
        :type dbuser: str
        """
        self._dbuser = dbuser

    @property
    def pay_model(self):
        r"""Gets the pay_model of this CdmQueryClusterInstanceDetail.

        付费模式： - 0：按需 - 1：包周期

        :return: The pay_model of this CdmQueryClusterInstanceDetail.
        :rtype: int
        """
        return self._pay_model

    @pay_model.setter
    def pay_model(self, pay_model):
        r"""Sets the pay_model of this CdmQueryClusterInstanceDetail.

        付费模式： - 0：按需 - 1：包周期

        :param pay_model: The pay_model of this CdmQueryClusterInstanceDetail.
        :type pay_model: int
        """
        self._pay_model = pay_model

    @property
    def public_ip(self):
        r"""Gets the public_ip of this CdmQueryClusterInstanceDetail.

        集群绑定的公网地址

        :return: The public_ip of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this CdmQueryClusterInstanceDetail.

        集群绑定的公网地址

        :param public_ip: The public_ip of this CdmQueryClusterInstanceDetail.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def traffic_ip(self):
        r"""Gets the traffic_ip of this CdmQueryClusterInstanceDetail.

        集群的内网地址

        :return: The traffic_ip of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._traffic_ip

    @traffic_ip.setter
    def traffic_ip(self, traffic_ip):
        r"""Sets the traffic_ip of this CdmQueryClusterInstanceDetail.

        集群的内网地址

        :param traffic_ip: The traffic_ip of this CdmQueryClusterInstanceDetail.
        :type traffic_ip: str
        """
        self._traffic_ip = traffic_ip

    @property
    def traffic_ipv6(self):
        r"""Gets the traffic_ipv6 of this CdmQueryClusterInstanceDetail.

        集群的内网IPv6地址

        :return: The traffic_ipv6 of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._traffic_ipv6

    @traffic_ipv6.setter
    def traffic_ipv6(self, traffic_ipv6):
        r"""Sets the traffic_ipv6 of this CdmQueryClusterInstanceDetail.

        集群的内网IPv6地址

        :param traffic_ipv6: The traffic_ipv6 of this CdmQueryClusterInstanceDetail.
        :type traffic_ipv6: str
        """
        self._traffic_ipv6 = traffic_ipv6

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CdmQueryClusterInstanceDetail.

        集群ID

        :return: The cluster_id of this CdmQueryClusterInstanceDetail.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CdmQueryClusterInstanceDetail.

        集群ID

        :param cluster_id: The cluster_id of this CdmQueryClusterInstanceDetail.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, CdmQueryClusterInstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
