# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterCheckBody:

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
        'flavor': 'str',
        'availability_zones': 'list[str]',
        'num_node': 'int',
        'security_group_id': 'str',
        'datastore_version': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'public_ip': 'OpenPublicIp',
        'cross_spec_restore': 'str',
        'volume': 'Volume',
        'old_cluster_hostname': 'str',
        'restore_point': 'RestorePoint',
        'tag_list': 'list[Tag]',
        'dss_pool_id': 'str',
        'db_port': 'str',
        'db_password': 'str',
        'db_name': 'str',
        'num_cn': 'int',
        'name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'flavor': 'flavor',
        'availability_zones': 'availability_zones',
        'num_node': 'num_node',
        'security_group_id': 'security_group_id',
        'datastore_version': 'datastore_version',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'public_ip': 'public_ip',
        'cross_spec_restore': 'cross_spec_restore',
        'volume': 'volume',
        'old_cluster_hostname': 'old_cluster_hostname',
        'restore_point': 'restore_point',
        'tag_list': 'tag_list',
        'dss_pool_id': 'dss_pool_id',
        'db_port': 'db_port',
        'db_password': 'db_password',
        'db_name': 'db_name',
        'num_cn': 'num_cn',
        'name': 'name'
    }

    def __init__(self, enterprise_project_id=None, flavor=None, availability_zones=None, num_node=None, security_group_id=None, datastore_version=None, vpc_id=None, subnet_id=None, public_ip=None, cross_spec_restore=None, volume=None, old_cluster_hostname=None, restore_point=None, tag_list=None, dss_pool_id=None, db_port=None, db_password=None, db_name=None, num_cn=None, name=None):
        r"""ClusterCheckBody

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**： 企业项目ID，对集群指定企业项目。如果未指定，则使用默认企业项目“default”的ID，即0。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0
        :type enterprise_project_id: str
        :param flavor: **参数解释**： 集群规格名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type flavor: str
        :param availability_zones: **参数解释**： 可用区列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type availability_zones: list[str]
        :param num_node: **参数解释**： 实例节点个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type num_node: int
        :param security_group_id: **参数解释**： 安全组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type security_group_id: str
        :param datastore_version: **参数解释**： 集群版本。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type datastore_version: str
        :param vpc_id: **参数解释**： 集群虚拟私有云ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type vpc_id: str
        :param subnet_id: **参数解释**： 集群子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type subnet_id: str
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkdws.v2.OpenPublicIp`
        :param cross_spec_restore: **参数解释**： 跨规格恢复信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type cross_spec_restore: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkdws.v2.Volume`
        :param old_cluster_hostname: **参数解释**： 旧主机名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type old_cluster_hostname: str
        :param restore_point: 
        :type restore_point: :class:`huaweicloudsdkdws.v2.RestorePoint`
        :param tag_list: **参数解释**： 标签列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type tag_list: list[:class:`huaweicloudsdkdws.v2.Tag`]
        :param dss_pool_id: **参数解释**： 存储池ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type dss_pool_id: str
        :param db_port: **参数解释**： 数据库端口。 **约束限制**： 不涉及。 **取值范围**： 8000~30000 **默认取值**： 8000
        :type db_port: str
        :param db_password: **参数解释**： 管理员密码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type db_password: str
        :param db_name: **参数解释**： 管理员用户。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： dbadmin
        :type db_name: str
        :param num_cn: **参数解释**： cn节点数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type num_cn: int
        :param name: **参数解释**： 集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        """
        
        

        self._enterprise_project_id = None
        self._flavor = None
        self._availability_zones = None
        self._num_node = None
        self._security_group_id = None
        self._datastore_version = None
        self._vpc_id = None
        self._subnet_id = None
        self._public_ip = None
        self._cross_spec_restore = None
        self._volume = None
        self._old_cluster_hostname = None
        self._restore_point = None
        self._tag_list = None
        self._dss_pool_id = None
        self._db_port = None
        self._db_password = None
        self._db_name = None
        self._num_cn = None
        self._name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.flavor = flavor
        self.availability_zones = availability_zones
        self.num_node = num_node
        if security_group_id is not None:
            self.security_group_id = security_group_id
        self.datastore_version = datastore_version
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if public_ip is not None:
            self.public_ip = public_ip
        if cross_spec_restore is not None:
            self.cross_spec_restore = cross_spec_restore
        if volume is not None:
            self.volume = volume
        if old_cluster_hostname is not None:
            self.old_cluster_hostname = old_cluster_hostname
        if restore_point is not None:
            self.restore_point = restore_point
        if tag_list is not None:
            self.tag_list = tag_list
        if dss_pool_id is not None:
            self.dss_pool_id = dss_pool_id
        if db_port is not None:
            self.db_port = db_port
        if db_password is not None:
            self.db_password = db_password
        if db_name is not None:
            self.db_name = db_name
        if num_cn is not None:
            self.num_cn = num_cn
        if name is not None:
            self.name = name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ClusterCheckBody.

        **参数解释**： 企业项目ID，对集群指定企业项目。如果未指定，则使用默认企业项目“default”的ID，即0。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0

        :return: The enterprise_project_id of this ClusterCheckBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ClusterCheckBody.

        **参数解释**： 企业项目ID，对集群指定企业项目。如果未指定，则使用默认企业项目“default”的ID，即0。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0

        :param enterprise_project_id: The enterprise_project_id of this ClusterCheckBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def flavor(self):
        r"""Gets the flavor of this ClusterCheckBody.

        **参数解释**： 集群规格名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The flavor of this ClusterCheckBody.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ClusterCheckBody.

        **参数解释**： 集群规格名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param flavor: The flavor of this ClusterCheckBody.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def availability_zones(self):
        r"""Gets the availability_zones of this ClusterCheckBody.

        **参数解释**： 可用区列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The availability_zones of this ClusterCheckBody.
        :rtype: list[str]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        r"""Sets the availability_zones of this ClusterCheckBody.

        **参数解释**： 可用区列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param availability_zones: The availability_zones of this ClusterCheckBody.
        :type availability_zones: list[str]
        """
        self._availability_zones = availability_zones

    @property
    def num_node(self):
        r"""Gets the num_node of this ClusterCheckBody.

        **参数解释**： 实例节点个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The num_node of this ClusterCheckBody.
        :rtype: int
        """
        return self._num_node

    @num_node.setter
    def num_node(self, num_node):
        r"""Sets the num_node of this ClusterCheckBody.

        **参数解释**： 实例节点个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param num_node: The num_node of this ClusterCheckBody.
        :type num_node: int
        """
        self._num_node = num_node

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ClusterCheckBody.

        **参数解释**： 安全组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The security_group_id of this ClusterCheckBody.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ClusterCheckBody.

        **参数解释**： 安全组ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param security_group_id: The security_group_id of this ClusterCheckBody.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def datastore_version(self):
        r"""Gets the datastore_version of this ClusterCheckBody.

        **参数解释**： 集群版本。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The datastore_version of this ClusterCheckBody.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        r"""Sets the datastore_version of this ClusterCheckBody.

        **参数解释**： 集群版本。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param datastore_version: The datastore_version of this ClusterCheckBody.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ClusterCheckBody.

        **参数解释**： 集群虚拟私有云ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The vpc_id of this ClusterCheckBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ClusterCheckBody.

        **参数解释**： 集群虚拟私有云ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param vpc_id: The vpc_id of this ClusterCheckBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ClusterCheckBody.

        **参数解释**： 集群子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The subnet_id of this ClusterCheckBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ClusterCheckBody.

        **参数解释**： 集群子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param subnet_id: The subnet_id of this ClusterCheckBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ClusterCheckBody.

        :return: The public_ip of this ClusterCheckBody.
        :rtype: :class:`huaweicloudsdkdws.v2.OpenPublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ClusterCheckBody.

        :param public_ip: The public_ip of this ClusterCheckBody.
        :type public_ip: :class:`huaweicloudsdkdws.v2.OpenPublicIp`
        """
        self._public_ip = public_ip

    @property
    def cross_spec_restore(self):
        r"""Gets the cross_spec_restore of this ClusterCheckBody.

        **参数解释**： 跨规格恢复信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The cross_spec_restore of this ClusterCheckBody.
        :rtype: str
        """
        return self._cross_spec_restore

    @cross_spec_restore.setter
    def cross_spec_restore(self, cross_spec_restore):
        r"""Sets the cross_spec_restore of this ClusterCheckBody.

        **参数解释**： 跨规格恢复信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param cross_spec_restore: The cross_spec_restore of this ClusterCheckBody.
        :type cross_spec_restore: str
        """
        self._cross_spec_restore = cross_spec_restore

    @property
    def volume(self):
        r"""Gets the volume of this ClusterCheckBody.

        :return: The volume of this ClusterCheckBody.
        :rtype: :class:`huaweicloudsdkdws.v2.Volume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this ClusterCheckBody.

        :param volume: The volume of this ClusterCheckBody.
        :type volume: :class:`huaweicloudsdkdws.v2.Volume`
        """
        self._volume = volume

    @property
    def old_cluster_hostname(self):
        r"""Gets the old_cluster_hostname of this ClusterCheckBody.

        **参数解释**： 旧主机名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The old_cluster_hostname of this ClusterCheckBody.
        :rtype: str
        """
        return self._old_cluster_hostname

    @old_cluster_hostname.setter
    def old_cluster_hostname(self, old_cluster_hostname):
        r"""Sets the old_cluster_hostname of this ClusterCheckBody.

        **参数解释**： 旧主机名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param old_cluster_hostname: The old_cluster_hostname of this ClusterCheckBody.
        :type old_cluster_hostname: str
        """
        self._old_cluster_hostname = old_cluster_hostname

    @property
    def restore_point(self):
        r"""Gets the restore_point of this ClusterCheckBody.

        :return: The restore_point of this ClusterCheckBody.
        :rtype: :class:`huaweicloudsdkdws.v2.RestorePoint`
        """
        return self._restore_point

    @restore_point.setter
    def restore_point(self, restore_point):
        r"""Sets the restore_point of this ClusterCheckBody.

        :param restore_point: The restore_point of this ClusterCheckBody.
        :type restore_point: :class:`huaweicloudsdkdws.v2.RestorePoint`
        """
        self._restore_point = restore_point

    @property
    def tag_list(self):
        r"""Gets the tag_list of this ClusterCheckBody.

        **参数解释**： 标签列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The tag_list of this ClusterCheckBody.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Tag`]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        r"""Sets the tag_list of this ClusterCheckBody.

        **参数解释**： 标签列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param tag_list: The tag_list of this ClusterCheckBody.
        :type tag_list: list[:class:`huaweicloudsdkdws.v2.Tag`]
        """
        self._tag_list = tag_list

    @property
    def dss_pool_id(self):
        r"""Gets the dss_pool_id of this ClusterCheckBody.

        **参数解释**： 存储池ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The dss_pool_id of this ClusterCheckBody.
        :rtype: str
        """
        return self._dss_pool_id

    @dss_pool_id.setter
    def dss_pool_id(self, dss_pool_id):
        r"""Sets the dss_pool_id of this ClusterCheckBody.

        **参数解释**： 存储池ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param dss_pool_id: The dss_pool_id of this ClusterCheckBody.
        :type dss_pool_id: str
        """
        self._dss_pool_id = dss_pool_id

    @property
    def db_port(self):
        r"""Gets the db_port of this ClusterCheckBody.

        **参数解释**： 数据库端口。 **约束限制**： 不涉及。 **取值范围**： 8000~30000 **默认取值**： 8000

        :return: The db_port of this ClusterCheckBody.
        :rtype: str
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        r"""Sets the db_port of this ClusterCheckBody.

        **参数解释**： 数据库端口。 **约束限制**： 不涉及。 **取值范围**： 8000~30000 **默认取值**： 8000

        :param db_port: The db_port of this ClusterCheckBody.
        :type db_port: str
        """
        self._db_port = db_port

    @property
    def db_password(self):
        r"""Gets the db_password of this ClusterCheckBody.

        **参数解释**： 管理员密码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The db_password of this ClusterCheckBody.
        :rtype: str
        """
        return self._db_password

    @db_password.setter
    def db_password(self, db_password):
        r"""Sets the db_password of this ClusterCheckBody.

        **参数解释**： 管理员密码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param db_password: The db_password of this ClusterCheckBody.
        :type db_password: str
        """
        self._db_password = db_password

    @property
    def db_name(self):
        r"""Gets the db_name of this ClusterCheckBody.

        **参数解释**： 管理员用户。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： dbadmin

        :return: The db_name of this ClusterCheckBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ClusterCheckBody.

        **参数解释**： 管理员用户。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： dbadmin

        :param db_name: The db_name of this ClusterCheckBody.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def num_cn(self):
        r"""Gets the num_cn of this ClusterCheckBody.

        **参数解释**： cn节点数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The num_cn of this ClusterCheckBody.
        :rtype: int
        """
        return self._num_cn

    @num_cn.setter
    def num_cn(self, num_cn):
        r"""Sets the num_cn of this ClusterCheckBody.

        **参数解释**： cn节点数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param num_cn: The num_cn of this ClusterCheckBody.
        :type num_cn: int
        """
        self._num_cn = num_cn

    @property
    def name(self):
        r"""Gets the name of this ClusterCheckBody.

        **参数解释**： 集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this ClusterCheckBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ClusterCheckBody.

        **参数解释**： 集群名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this ClusterCheckBody.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ClusterCheckBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
