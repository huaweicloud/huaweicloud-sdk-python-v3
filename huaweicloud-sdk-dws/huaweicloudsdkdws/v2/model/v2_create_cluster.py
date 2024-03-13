# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2CreateCluster:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'flavor': 'str',
        'num_cn': 'int',
        'num_node': 'int',
        'db_name': 'str',
        'db_password': 'str',
        'db_port': 'int',
        'dss_pool_id': 'str',
        'availability_zones': 'list[str]',
        'tags': 'list[Tags]',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'public_ip': 'PublicIp',
        'datastore_version': 'str',
        'master_key_id': 'str',
        'master_key_name': 'str',
        'crypt_algorithm': 'str',
        'volume': 'Volume',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'flavor': 'flavor',
        'num_cn': 'num_cn',
        'num_node': 'num_node',
        'db_name': 'db_name',
        'db_password': 'db_password',
        'db_port': 'db_port',
        'dss_pool_id': 'dss_pool_id',
        'availability_zones': 'availability_zones',
        'tags': 'tags',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'public_ip': 'public_ip',
        'datastore_version': 'datastore_version',
        'master_key_id': 'master_key_id',
        'master_key_name': 'master_key_name',
        'crypt_algorithm': 'crypt_algorithm',
        'volume': 'volume',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, flavor=None, num_cn=None, num_node=None, db_name=None, db_password=None, db_port=None, dss_pool_id=None, availability_zones=None, tags=None, vpc_id=None, subnet_id=None, security_group_id=None, public_ip=None, datastore_version=None, master_key_id=None, master_key_name=None, crypt_algorithm=None, volume=None, enterprise_project_id=None):
        """V2CreateCluster

        The model defined in huaweicloud sdk

        :param name: 集群名称，要求唯一性，必须以字母开头并只包含字母、数字、中划线或下划线，长度为4~64个字符。
        :type name: str
        :param flavor: 集群规格名称。节点类型详情请参见数据仓库类型数据仓库类型。
        :type flavor: str
        :param num_cn: 集群CN数量，取值范围为2~集群节点数，最大值为20，默认值为3。
        :type num_cn: int
        :param num_node: 集群节点数量，集群模式取值范围为3~256，实时数仓（单机模式）取值为1。
        :type num_node: int
        :param db_name: 管理员用户名称。用户命名要求如下： 只能由小写字母、数字或下划线组成。 必须由小写字母或下划线开头。 长度为1~63个字符。用户名不能为DWS数据库的关键字。
        :type db_name: str
        :param db_password: 管理员用户密码。 12~32个字符 至少包含以下字符中的3种：大写字母、小写字母、数字和特殊字符（~!?,.:;-_(){}[]/&lt;&gt;@#%^&amp;*+|\\&#x3D;）。不能与用户名或倒序的用户名相同。
        :type db_password: str
        :param db_port: 集群数据库端口，取值范围为8000~30000，默认值：8000。
        :type db_port: int
        :param dss_pool_id: 专属存储池ID
        :type dss_pool_id: str
        :param availability_zones: 可用区列表。集群可用区选择详情请参见地区和终端节点地区和终端节点。
        :type availability_zones: list[str]
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdkdws.v2.Tags`]
        :param vpc_id: 指定虚拟私有云ID，用于集群网络配置。
        :type vpc_id: str
        :param subnet_id: 指定子网ID，用于集群网络配置。
        :type subnet_id: str
        :param security_group_id: 指定安全组ID，用于集群网络配置。
        :type security_group_id: str
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkdws.v2.PublicIp`
        :param datastore_version: 集群版本
        :type datastore_version: str
        :param master_key_id: 密钥ID
        :type master_key_id: str
        :param master_key_name: 密钥名称
        :type master_key_name: str
        :param crypt_algorithm: 加密算法
        :type crypt_algorithm: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkdws.v2.Volume`
        :param enterprise_project_id: 企业项目ID，对集群指定企业项目，如果未指定，则使用默认企业项目“default”的ID，即0。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._flavor = None
        self._num_cn = None
        self._num_node = None
        self._db_name = None
        self._db_password = None
        self._db_port = None
        self._dss_pool_id = None
        self._availability_zones = None
        self._tags = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._public_ip = None
        self._datastore_version = None
        self._master_key_id = None
        self._master_key_name = None
        self._crypt_algorithm = None
        self._volume = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        self.flavor = flavor
        self.num_cn = num_cn
        self.num_node = num_node
        self.db_name = db_name
        self.db_password = db_password
        self.db_port = db_port
        if dss_pool_id is not None:
            self.dss_pool_id = dss_pool_id
        self.availability_zones = availability_zones
        if tags is not None:
            self.tags = tags
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if public_ip is not None:
            self.public_ip = public_ip
        self.datastore_version = datastore_version
        if master_key_id is not None:
            self.master_key_id = master_key_id
        if master_key_name is not None:
            self.master_key_name = master_key_name
        if crypt_algorithm is not None:
            self.crypt_algorithm = crypt_algorithm
        if volume is not None:
            self.volume = volume
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        """Gets the name of this V2CreateCluster.

        集群名称，要求唯一性，必须以字母开头并只包含字母、数字、中划线或下划线，长度为4~64个字符。

        :return: The name of this V2CreateCluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2CreateCluster.

        集群名称，要求唯一性，必须以字母开头并只包含字母、数字、中划线或下划线，长度为4~64个字符。

        :param name: The name of this V2CreateCluster.
        :type name: str
        """
        self._name = name

    @property
    def flavor(self):
        """Gets the flavor of this V2CreateCluster.

        集群规格名称。节点类型详情请参见数据仓库类型数据仓库类型。

        :return: The flavor of this V2CreateCluster.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this V2CreateCluster.

        集群规格名称。节点类型详情请参见数据仓库类型数据仓库类型。

        :param flavor: The flavor of this V2CreateCluster.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def num_cn(self):
        """Gets the num_cn of this V2CreateCluster.

        集群CN数量，取值范围为2~集群节点数，最大值为20，默认值为3。

        :return: The num_cn of this V2CreateCluster.
        :rtype: int
        """
        return self._num_cn

    @num_cn.setter
    def num_cn(self, num_cn):
        """Sets the num_cn of this V2CreateCluster.

        集群CN数量，取值范围为2~集群节点数，最大值为20，默认值为3。

        :param num_cn: The num_cn of this V2CreateCluster.
        :type num_cn: int
        """
        self._num_cn = num_cn

    @property
    def num_node(self):
        """Gets the num_node of this V2CreateCluster.

        集群节点数量，集群模式取值范围为3~256，实时数仓（单机模式）取值为1。

        :return: The num_node of this V2CreateCluster.
        :rtype: int
        """
        return self._num_node

    @num_node.setter
    def num_node(self, num_node):
        """Sets the num_node of this V2CreateCluster.

        集群节点数量，集群模式取值范围为3~256，实时数仓（单机模式）取值为1。

        :param num_node: The num_node of this V2CreateCluster.
        :type num_node: int
        """
        self._num_node = num_node

    @property
    def db_name(self):
        """Gets the db_name of this V2CreateCluster.

        管理员用户名称。用户命名要求如下： 只能由小写字母、数字或下划线组成。 必须由小写字母或下划线开头。 长度为1~63个字符。用户名不能为DWS数据库的关键字。

        :return: The db_name of this V2CreateCluster.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this V2CreateCluster.

        管理员用户名称。用户命名要求如下： 只能由小写字母、数字或下划线组成。 必须由小写字母或下划线开头。 长度为1~63个字符。用户名不能为DWS数据库的关键字。

        :param db_name: The db_name of this V2CreateCluster.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def db_password(self):
        """Gets the db_password of this V2CreateCluster.

        管理员用户密码。 12~32个字符 至少包含以下字符中的3种：大写字母、小写字母、数字和特殊字符（~!?,.:;-_(){}[]/<>@#%^&*+|\\=）。不能与用户名或倒序的用户名相同。

        :return: The db_password of this V2CreateCluster.
        :rtype: str
        """
        return self._db_password

    @db_password.setter
    def db_password(self, db_password):
        """Sets the db_password of this V2CreateCluster.

        管理员用户密码。 12~32个字符 至少包含以下字符中的3种：大写字母、小写字母、数字和特殊字符（~!?,.:;-_(){}[]/<>@#%^&*+|\\=）。不能与用户名或倒序的用户名相同。

        :param db_password: The db_password of this V2CreateCluster.
        :type db_password: str
        """
        self._db_password = db_password

    @property
    def db_port(self):
        """Gets the db_port of this V2CreateCluster.

        集群数据库端口，取值范围为8000~30000，默认值：8000。

        :return: The db_port of this V2CreateCluster.
        :rtype: int
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        """Sets the db_port of this V2CreateCluster.

        集群数据库端口，取值范围为8000~30000，默认值：8000。

        :param db_port: The db_port of this V2CreateCluster.
        :type db_port: int
        """
        self._db_port = db_port

    @property
    def dss_pool_id(self):
        """Gets the dss_pool_id of this V2CreateCluster.

        专属存储池ID

        :return: The dss_pool_id of this V2CreateCluster.
        :rtype: str
        """
        return self._dss_pool_id

    @dss_pool_id.setter
    def dss_pool_id(self, dss_pool_id):
        """Sets the dss_pool_id of this V2CreateCluster.

        专属存储池ID

        :param dss_pool_id: The dss_pool_id of this V2CreateCluster.
        :type dss_pool_id: str
        """
        self._dss_pool_id = dss_pool_id

    @property
    def availability_zones(self):
        """Gets the availability_zones of this V2CreateCluster.

        可用区列表。集群可用区选择详情请参见地区和终端节点地区和终端节点。

        :return: The availability_zones of this V2CreateCluster.
        :rtype: list[str]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        """Sets the availability_zones of this V2CreateCluster.

        可用区列表。集群可用区选择详情请参见地区和终端节点地区和终端节点。

        :param availability_zones: The availability_zones of this V2CreateCluster.
        :type availability_zones: list[str]
        """
        self._availability_zones = availability_zones

    @property
    def tags(self):
        """Gets the tags of this V2CreateCluster.

        标签列表

        :return: The tags of this V2CreateCluster.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Tags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V2CreateCluster.

        标签列表

        :param tags: The tags of this V2CreateCluster.
        :type tags: list[:class:`huaweicloudsdkdws.v2.Tags`]
        """
        self._tags = tags

    @property
    def vpc_id(self):
        """Gets the vpc_id of this V2CreateCluster.

        指定虚拟私有云ID，用于集群网络配置。

        :return: The vpc_id of this V2CreateCluster.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this V2CreateCluster.

        指定虚拟私有云ID，用于集群网络配置。

        :param vpc_id: The vpc_id of this V2CreateCluster.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this V2CreateCluster.

        指定子网ID，用于集群网络配置。

        :return: The subnet_id of this V2CreateCluster.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this V2CreateCluster.

        指定子网ID，用于集群网络配置。

        :param subnet_id: The subnet_id of this V2CreateCluster.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this V2CreateCluster.

        指定安全组ID，用于集群网络配置。

        :return: The security_group_id of this V2CreateCluster.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this V2CreateCluster.

        指定安全组ID，用于集群网络配置。

        :param security_group_id: The security_group_id of this V2CreateCluster.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def public_ip(self):
        """Gets the public_ip of this V2CreateCluster.

        :return: The public_ip of this V2CreateCluster.
        :rtype: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this V2CreateCluster.

        :param public_ip: The public_ip of this V2CreateCluster.
        :type public_ip: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def datastore_version(self):
        """Gets the datastore_version of this V2CreateCluster.

        集群版本

        :return: The datastore_version of this V2CreateCluster.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        """Sets the datastore_version of this V2CreateCluster.

        集群版本

        :param datastore_version: The datastore_version of this V2CreateCluster.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def master_key_id(self):
        """Gets the master_key_id of this V2CreateCluster.

        密钥ID

        :return: The master_key_id of this V2CreateCluster.
        :rtype: str
        """
        return self._master_key_id

    @master_key_id.setter
    def master_key_id(self, master_key_id):
        """Sets the master_key_id of this V2CreateCluster.

        密钥ID

        :param master_key_id: The master_key_id of this V2CreateCluster.
        :type master_key_id: str
        """
        self._master_key_id = master_key_id

    @property
    def master_key_name(self):
        """Gets the master_key_name of this V2CreateCluster.

        密钥名称

        :return: The master_key_name of this V2CreateCluster.
        :rtype: str
        """
        return self._master_key_name

    @master_key_name.setter
    def master_key_name(self, master_key_name):
        """Sets the master_key_name of this V2CreateCluster.

        密钥名称

        :param master_key_name: The master_key_name of this V2CreateCluster.
        :type master_key_name: str
        """
        self._master_key_name = master_key_name

    @property
    def crypt_algorithm(self):
        """Gets the crypt_algorithm of this V2CreateCluster.

        加密算法

        :return: The crypt_algorithm of this V2CreateCluster.
        :rtype: str
        """
        return self._crypt_algorithm

    @crypt_algorithm.setter
    def crypt_algorithm(self, crypt_algorithm):
        """Sets the crypt_algorithm of this V2CreateCluster.

        加密算法

        :param crypt_algorithm: The crypt_algorithm of this V2CreateCluster.
        :type crypt_algorithm: str
        """
        self._crypt_algorithm = crypt_algorithm

    @property
    def volume(self):
        """Gets the volume of this V2CreateCluster.

        :return: The volume of this V2CreateCluster.
        :rtype: :class:`huaweicloudsdkdws.v2.Volume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this V2CreateCluster.

        :param volume: The volume of this V2CreateCluster.
        :type volume: :class:`huaweicloudsdkdws.v2.Volume`
        """
        self._volume = volume

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this V2CreateCluster.

        企业项目ID，对集群指定企业项目，如果未指定，则使用默认企业项目“default”的ID，即0。

        :return: The enterprise_project_id of this V2CreateCluster.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this V2CreateCluster.

        企业项目ID，对集群指定企业项目，如果未指定，则使用默认企业项目“default”的ID，即0。

        :param enterprise_project_id: The enterprise_project_id of this V2CreateCluster.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, V2CreateCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
