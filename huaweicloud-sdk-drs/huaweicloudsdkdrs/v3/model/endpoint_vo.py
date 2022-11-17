# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'obj_id': 'str',
        'instance_name': 'str',
        'db_type': 'str',
        'db_user': 'str',
        'db_password': 'str',
        'manage_ip': 'str',
        'traffic_ip': 'str',
        'db_port': 'int',
        'region': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'ip': 'str',
        'public_ip': 'str',
        'az_code': 'str',
        'security_group_id': 'str',
        'subnet_id': 'str',
        'vpc_id': 'str',
        'volume_size': 'int',
        'full_trans_user_pwd': 'str',
        'increment_trans_user_pwd': 'str',
        'ssl_link': 'bool',
        'ssl_cert_key': 'str',
        'ssl_cert_name': 'str',
        'ssl_cert_check_sum': 'str',
        'ssl_cert_password': 'str',
        'db_version': 'str',
        'mongo_ha_mode': 'str',
        'project_id': 'str',
        'cluster_mode': 'str',
        'instance_id': 'str',
        'db_name': 'str',
        'topic': 'str',
        'safe_mode': 'int',
        'kerberos_vo': 'KerberosVO',
        'multi_write_db_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'obj_id': 'obj_id',
        'instance_name': 'instance_name',
        'db_type': 'db_type',
        'db_user': 'db_user',
        'db_password': 'db_password',
        'manage_ip': 'manage_ip',
        'traffic_ip': 'traffic_ip',
        'db_port': 'db_port',
        'region': 'region',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'ip': 'ip',
        'public_ip': 'public_ip',
        'az_code': 'az_code',
        'security_group_id': 'security_group_id',
        'subnet_id': 'subnet_id',
        'vpc_id': 'vpc_id',
        'volume_size': 'volume_size',
        'full_trans_user_pwd': 'full_trans_user_pwd',
        'increment_trans_user_pwd': 'increment_trans_user_pwd',
        'ssl_link': 'ssl_link',
        'ssl_cert_key': 'ssl_cert_key',
        'ssl_cert_name': 'ssl_cert_name',
        'ssl_cert_check_sum': 'ssl_cert_check_sum',
        'ssl_cert_password': 'ssl_cert_password',
        'db_version': 'db_version',
        'mongo_ha_mode': 'mongo_ha_mode',
        'project_id': 'project_id',
        'cluster_mode': 'cluster_mode',
        'instance_id': 'instance_id',
        'db_name': 'db_name',
        'topic': 'topic',
        'safe_mode': 'safe_mode',
        'kerberos_vo': 'kerberos_vo',
        'multi_write_db_id': 'multi_write_db_id'
    }

    def __init__(self, id=None, obj_id=None, instance_name=None, db_type=None, db_user=None, db_password=None, manage_ip=None, traffic_ip=None, db_port=None, region=None, created_at=None, updated_at=None, ip=None, public_ip=None, az_code=None, security_group_id=None, subnet_id=None, vpc_id=None, volume_size=None, full_trans_user_pwd=None, increment_trans_user_pwd=None, ssl_link=None, ssl_cert_key=None, ssl_cert_name=None, ssl_cert_check_sum=None, ssl_cert_password=None, db_version=None, mongo_ha_mode=None, project_id=None, cluster_mode=None, instance_id=None, db_name=None, topic=None, safe_mode=None, kerberos_vo=None, multi_write_db_id=None):
        """EndpointVO

        The model defined in huaweicloud sdk

        :param id: 数据库id。
        :type id: str
        :param obj_id: 对象id。
        :type obj_id: str
        :param instance_name: RDS实例名称。
        :type instance_name: str
        :param db_type: 数据库类型
        :type db_type: str
        :param db_user: 数据库用户。
        :type db_user: str
        :param db_password: 数据库密码。
        :type db_password: str
        :param manage_ip: 管理IP。
        :type manage_ip: str
        :param traffic_ip: 流量IP。
        :type traffic_ip: str
        :param db_port: 数据库端口。
        :type db_port: int
        :param region: RDS实例所在region。
        :type region: str
        :param created_at: 创建日期，格式yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;
        :type created_at: str
        :param updated_at: 修改日期，格式yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;
        :type updated_at: str
        :param ip: 迁移实例所在的私有IP。
        :type ip: str
        :param public_ip: 迁移实例所在的公网IP。
        :type public_ip: str
        :param az_code: 可用区azCode。
        :type az_code: str
        :param security_group_id: 源库所在的安全组id。
        :type security_group_id: str
        :param subnet_id: 源库所在的子网id。
        :type subnet_id: str
        :param vpc_id: 源库所在的虚拟私有云id。
        :type vpc_id: str
        :param volume_size: 迁移实例的磁盘大小。
        :type volume_size: int
        :param full_trans_user_pwd: 全量迁移用户密码，密文。
        :type full_trans_user_pwd: str
        :param increment_trans_user_pwd: 增量迁移用户密码，密文。
        :type increment_trans_user_pwd: str
        :param ssl_link: 是否SSL安全连接。
        :type ssl_link: bool
        :param ssl_cert_key: SSL证书内容。
        :type ssl_cert_key: str
        :param ssl_cert_name: SSL证书名字。
        :type ssl_cert_name: str
        :param ssl_cert_check_sum: SSL证书内容checksum值。
        :type ssl_cert_check_sum: str
        :param ssl_cert_password: SSL证书密码，密文。
        :type ssl_cert_password: str
        :param db_version: 数据库版本。
        :type db_version: str
        :param mongo_ha_mode: mongoHa模式。 - Sharding 集群 - ReplicaSet 副本集 - ReplicaSingle 单节点
        :type mongo_ha_mode: str
        :param project_id: RDS实例projectId。
        :type project_id: str
        :param cluster_mode: 集群模式。 - Single：单节点RDS - Ha：主备RDS - GR：金融版RDS - Sharding：mongodb 集群或DDM的模式，均默认为分片 - Sharding4.0+：mongodb 集群版本4.0+，默认为不分片 - ReplicaSet：mongodb 副本集,Replica RDS只读副本 - ReplicaSingle：mongodb 单节点 - Cluster：集群 - Independent：gaussdbv5 independent模式 - Combined：gaussdbv5 Combined模式 - Distributed ：分布式taurus - NoSharding：非集群模式
        :type cluster_mode: str
        :param instance_id: RDS实例id。
        :type instance_id: str
        :param db_name: Oracle服务名serviceName。
        :type db_name: str
        :param topic: mrskafka topic名称。
        :type topic: str
        :param safe_mode: MRSkafka是否开启kerberos认证 - 0非安全认证 - 1安全认证
        :type safe_mode: int
        :param kerberos_vo: 
        :type kerberos_vo: :class:`huaweicloudsdkdrs.v3.KerberosVO`
        :param multi_write_db_id: 多写数据库Id。
        :type multi_write_db_id: str
        """
        
        

        self._id = None
        self._obj_id = None
        self._instance_name = None
        self._db_type = None
        self._db_user = None
        self._db_password = None
        self._manage_ip = None
        self._traffic_ip = None
        self._db_port = None
        self._region = None
        self._created_at = None
        self._updated_at = None
        self._ip = None
        self._public_ip = None
        self._az_code = None
        self._security_group_id = None
        self._subnet_id = None
        self._vpc_id = None
        self._volume_size = None
        self._full_trans_user_pwd = None
        self._increment_trans_user_pwd = None
        self._ssl_link = None
        self._ssl_cert_key = None
        self._ssl_cert_name = None
        self._ssl_cert_check_sum = None
        self._ssl_cert_password = None
        self._db_version = None
        self._mongo_ha_mode = None
        self._project_id = None
        self._cluster_mode = None
        self._instance_id = None
        self._db_name = None
        self._topic = None
        self._safe_mode = None
        self._kerberos_vo = None
        self._multi_write_db_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if obj_id is not None:
            self.obj_id = obj_id
        if instance_name is not None:
            self.instance_name = instance_name
        if db_type is not None:
            self.db_type = db_type
        if db_user is not None:
            self.db_user = db_user
        if db_password is not None:
            self.db_password = db_password
        if manage_ip is not None:
            self.manage_ip = manage_ip
        if traffic_ip is not None:
            self.traffic_ip = traffic_ip
        if db_port is not None:
            self.db_port = db_port
        if region is not None:
            self.region = region
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if ip is not None:
            self.ip = ip
        if public_ip is not None:
            self.public_ip = public_ip
        if az_code is not None:
            self.az_code = az_code
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if volume_size is not None:
            self.volume_size = volume_size
        if full_trans_user_pwd is not None:
            self.full_trans_user_pwd = full_trans_user_pwd
        if increment_trans_user_pwd is not None:
            self.increment_trans_user_pwd = increment_trans_user_pwd
        if ssl_link is not None:
            self.ssl_link = ssl_link
        if ssl_cert_key is not None:
            self.ssl_cert_key = ssl_cert_key
        if ssl_cert_name is not None:
            self.ssl_cert_name = ssl_cert_name
        if ssl_cert_check_sum is not None:
            self.ssl_cert_check_sum = ssl_cert_check_sum
        if ssl_cert_password is not None:
            self.ssl_cert_password = ssl_cert_password
        if db_version is not None:
            self.db_version = db_version
        if mongo_ha_mode is not None:
            self.mongo_ha_mode = mongo_ha_mode
        if project_id is not None:
            self.project_id = project_id
        if cluster_mode is not None:
            self.cluster_mode = cluster_mode
        if instance_id is not None:
            self.instance_id = instance_id
        if db_name is not None:
            self.db_name = db_name
        if topic is not None:
            self.topic = topic
        if safe_mode is not None:
            self.safe_mode = safe_mode
        if kerberos_vo is not None:
            self.kerberos_vo = kerberos_vo
        if multi_write_db_id is not None:
            self.multi_write_db_id = multi_write_db_id

    @property
    def id(self):
        """Gets the id of this EndpointVO.

        数据库id。

        :return: The id of this EndpointVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointVO.

        数据库id。

        :param id: The id of this EndpointVO.
        :type id: str
        """
        self._id = id

    @property
    def obj_id(self):
        """Gets the obj_id of this EndpointVO.

        对象id。

        :return: The obj_id of this EndpointVO.
        :rtype: str
        """
        return self._obj_id

    @obj_id.setter
    def obj_id(self, obj_id):
        """Sets the obj_id of this EndpointVO.

        对象id。

        :param obj_id: The obj_id of this EndpointVO.
        :type obj_id: str
        """
        self._obj_id = obj_id

    @property
    def instance_name(self):
        """Gets the instance_name of this EndpointVO.

        RDS实例名称。

        :return: The instance_name of this EndpointVO.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this EndpointVO.

        RDS实例名称。

        :param instance_name: The instance_name of this EndpointVO.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def db_type(self):
        """Gets the db_type of this EndpointVO.

        数据库类型

        :return: The db_type of this EndpointVO.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this EndpointVO.

        数据库类型

        :param db_type: The db_type of this EndpointVO.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def db_user(self):
        """Gets the db_user of this EndpointVO.

        数据库用户。

        :return: The db_user of this EndpointVO.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        """Sets the db_user of this EndpointVO.

        数据库用户。

        :param db_user: The db_user of this EndpointVO.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def db_password(self):
        """Gets the db_password of this EndpointVO.

        数据库密码。

        :return: The db_password of this EndpointVO.
        :rtype: str
        """
        return self._db_password

    @db_password.setter
    def db_password(self, db_password):
        """Sets the db_password of this EndpointVO.

        数据库密码。

        :param db_password: The db_password of this EndpointVO.
        :type db_password: str
        """
        self._db_password = db_password

    @property
    def manage_ip(self):
        """Gets the manage_ip of this EndpointVO.

        管理IP。

        :return: The manage_ip of this EndpointVO.
        :rtype: str
        """
        return self._manage_ip

    @manage_ip.setter
    def manage_ip(self, manage_ip):
        """Sets the manage_ip of this EndpointVO.

        管理IP。

        :param manage_ip: The manage_ip of this EndpointVO.
        :type manage_ip: str
        """
        self._manage_ip = manage_ip

    @property
    def traffic_ip(self):
        """Gets the traffic_ip of this EndpointVO.

        流量IP。

        :return: The traffic_ip of this EndpointVO.
        :rtype: str
        """
        return self._traffic_ip

    @traffic_ip.setter
    def traffic_ip(self, traffic_ip):
        """Sets the traffic_ip of this EndpointVO.

        流量IP。

        :param traffic_ip: The traffic_ip of this EndpointVO.
        :type traffic_ip: str
        """
        self._traffic_ip = traffic_ip

    @property
    def db_port(self):
        """Gets the db_port of this EndpointVO.

        数据库端口。

        :return: The db_port of this EndpointVO.
        :rtype: int
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        """Sets the db_port of this EndpointVO.

        数据库端口。

        :param db_port: The db_port of this EndpointVO.
        :type db_port: int
        """
        self._db_port = db_port

    @property
    def region(self):
        """Gets the region of this EndpointVO.

        RDS实例所在region。

        :return: The region of this EndpointVO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this EndpointVO.

        RDS实例所在region。

        :param region: The region of this EndpointVO.
        :type region: str
        """
        self._region = region

    @property
    def created_at(self):
        """Gets the created_at of this EndpointVO.

        创建日期，格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The created_at of this EndpointVO.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EndpointVO.

        创建日期，格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :param created_at: The created_at of this EndpointVO.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EndpointVO.

        修改日期，格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The updated_at of this EndpointVO.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EndpointVO.

        修改日期，格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :param updated_at: The updated_at of this EndpointVO.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def ip(self):
        """Gets the ip of this EndpointVO.

        迁移实例所在的私有IP。

        :return: The ip of this EndpointVO.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this EndpointVO.

        迁移实例所在的私有IP。

        :param ip: The ip of this EndpointVO.
        :type ip: str
        """
        self._ip = ip

    @property
    def public_ip(self):
        """Gets the public_ip of this EndpointVO.

        迁移实例所在的公网IP。

        :return: The public_ip of this EndpointVO.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this EndpointVO.

        迁移实例所在的公网IP。

        :param public_ip: The public_ip of this EndpointVO.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def az_code(self):
        """Gets the az_code of this EndpointVO.

        可用区azCode。

        :return: The az_code of this EndpointVO.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this EndpointVO.

        可用区azCode。

        :param az_code: The az_code of this EndpointVO.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def security_group_id(self):
        """Gets the security_group_id of this EndpointVO.

        源库所在的安全组id。

        :return: The security_group_id of this EndpointVO.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this EndpointVO.

        源库所在的安全组id。

        :param security_group_id: The security_group_id of this EndpointVO.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this EndpointVO.

        源库所在的子网id。

        :return: The subnet_id of this EndpointVO.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this EndpointVO.

        源库所在的子网id。

        :param subnet_id: The subnet_id of this EndpointVO.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this EndpointVO.

        源库所在的虚拟私有云id。

        :return: The vpc_id of this EndpointVO.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this EndpointVO.

        源库所在的虚拟私有云id。

        :param vpc_id: The vpc_id of this EndpointVO.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def volume_size(self):
        """Gets the volume_size of this EndpointVO.

        迁移实例的磁盘大小。

        :return: The volume_size of this EndpointVO.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this EndpointVO.

        迁移实例的磁盘大小。

        :param volume_size: The volume_size of this EndpointVO.
        :type volume_size: int
        """
        self._volume_size = volume_size

    @property
    def full_trans_user_pwd(self):
        """Gets the full_trans_user_pwd of this EndpointVO.

        全量迁移用户密码，密文。

        :return: The full_trans_user_pwd of this EndpointVO.
        :rtype: str
        """
        return self._full_trans_user_pwd

    @full_trans_user_pwd.setter
    def full_trans_user_pwd(self, full_trans_user_pwd):
        """Sets the full_trans_user_pwd of this EndpointVO.

        全量迁移用户密码，密文。

        :param full_trans_user_pwd: The full_trans_user_pwd of this EndpointVO.
        :type full_trans_user_pwd: str
        """
        self._full_trans_user_pwd = full_trans_user_pwd

    @property
    def increment_trans_user_pwd(self):
        """Gets the increment_trans_user_pwd of this EndpointVO.

        增量迁移用户密码，密文。

        :return: The increment_trans_user_pwd of this EndpointVO.
        :rtype: str
        """
        return self._increment_trans_user_pwd

    @increment_trans_user_pwd.setter
    def increment_trans_user_pwd(self, increment_trans_user_pwd):
        """Sets the increment_trans_user_pwd of this EndpointVO.

        增量迁移用户密码，密文。

        :param increment_trans_user_pwd: The increment_trans_user_pwd of this EndpointVO.
        :type increment_trans_user_pwd: str
        """
        self._increment_trans_user_pwd = increment_trans_user_pwd

    @property
    def ssl_link(self):
        """Gets the ssl_link of this EndpointVO.

        是否SSL安全连接。

        :return: The ssl_link of this EndpointVO.
        :rtype: bool
        """
        return self._ssl_link

    @ssl_link.setter
    def ssl_link(self, ssl_link):
        """Sets the ssl_link of this EndpointVO.

        是否SSL安全连接。

        :param ssl_link: The ssl_link of this EndpointVO.
        :type ssl_link: bool
        """
        self._ssl_link = ssl_link

    @property
    def ssl_cert_key(self):
        """Gets the ssl_cert_key of this EndpointVO.

        SSL证书内容。

        :return: The ssl_cert_key of this EndpointVO.
        :rtype: str
        """
        return self._ssl_cert_key

    @ssl_cert_key.setter
    def ssl_cert_key(self, ssl_cert_key):
        """Sets the ssl_cert_key of this EndpointVO.

        SSL证书内容。

        :param ssl_cert_key: The ssl_cert_key of this EndpointVO.
        :type ssl_cert_key: str
        """
        self._ssl_cert_key = ssl_cert_key

    @property
    def ssl_cert_name(self):
        """Gets the ssl_cert_name of this EndpointVO.

        SSL证书名字。

        :return: The ssl_cert_name of this EndpointVO.
        :rtype: str
        """
        return self._ssl_cert_name

    @ssl_cert_name.setter
    def ssl_cert_name(self, ssl_cert_name):
        """Sets the ssl_cert_name of this EndpointVO.

        SSL证书名字。

        :param ssl_cert_name: The ssl_cert_name of this EndpointVO.
        :type ssl_cert_name: str
        """
        self._ssl_cert_name = ssl_cert_name

    @property
    def ssl_cert_check_sum(self):
        """Gets the ssl_cert_check_sum of this EndpointVO.

        SSL证书内容checksum值。

        :return: The ssl_cert_check_sum of this EndpointVO.
        :rtype: str
        """
        return self._ssl_cert_check_sum

    @ssl_cert_check_sum.setter
    def ssl_cert_check_sum(self, ssl_cert_check_sum):
        """Sets the ssl_cert_check_sum of this EndpointVO.

        SSL证书内容checksum值。

        :param ssl_cert_check_sum: The ssl_cert_check_sum of this EndpointVO.
        :type ssl_cert_check_sum: str
        """
        self._ssl_cert_check_sum = ssl_cert_check_sum

    @property
    def ssl_cert_password(self):
        """Gets the ssl_cert_password of this EndpointVO.

        SSL证书密码，密文。

        :return: The ssl_cert_password of this EndpointVO.
        :rtype: str
        """
        return self._ssl_cert_password

    @ssl_cert_password.setter
    def ssl_cert_password(self, ssl_cert_password):
        """Sets the ssl_cert_password of this EndpointVO.

        SSL证书密码，密文。

        :param ssl_cert_password: The ssl_cert_password of this EndpointVO.
        :type ssl_cert_password: str
        """
        self._ssl_cert_password = ssl_cert_password

    @property
    def db_version(self):
        """Gets the db_version of this EndpointVO.

        数据库版本。

        :return: The db_version of this EndpointVO.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """Sets the db_version of this EndpointVO.

        数据库版本。

        :param db_version: The db_version of this EndpointVO.
        :type db_version: str
        """
        self._db_version = db_version

    @property
    def mongo_ha_mode(self):
        """Gets the mongo_ha_mode of this EndpointVO.

        mongoHa模式。 - Sharding 集群 - ReplicaSet 副本集 - ReplicaSingle 单节点

        :return: The mongo_ha_mode of this EndpointVO.
        :rtype: str
        """
        return self._mongo_ha_mode

    @mongo_ha_mode.setter
    def mongo_ha_mode(self, mongo_ha_mode):
        """Sets the mongo_ha_mode of this EndpointVO.

        mongoHa模式。 - Sharding 集群 - ReplicaSet 副本集 - ReplicaSingle 单节点

        :param mongo_ha_mode: The mongo_ha_mode of this EndpointVO.
        :type mongo_ha_mode: str
        """
        self._mongo_ha_mode = mongo_ha_mode

    @property
    def project_id(self):
        """Gets the project_id of this EndpointVO.

        RDS实例projectId。

        :return: The project_id of this EndpointVO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this EndpointVO.

        RDS实例projectId。

        :param project_id: The project_id of this EndpointVO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def cluster_mode(self):
        """Gets the cluster_mode of this EndpointVO.

        集群模式。 - Single：单节点RDS - Ha：主备RDS - GR：金融版RDS - Sharding：mongodb 集群或DDM的模式，均默认为分片 - Sharding4.0+：mongodb 集群版本4.0+，默认为不分片 - ReplicaSet：mongodb 副本集,Replica RDS只读副本 - ReplicaSingle：mongodb 单节点 - Cluster：集群 - Independent：gaussdbv5 independent模式 - Combined：gaussdbv5 Combined模式 - Distributed ：分布式taurus - NoSharding：非集群模式

        :return: The cluster_mode of this EndpointVO.
        :rtype: str
        """
        return self._cluster_mode

    @cluster_mode.setter
    def cluster_mode(self, cluster_mode):
        """Sets the cluster_mode of this EndpointVO.

        集群模式。 - Single：单节点RDS - Ha：主备RDS - GR：金融版RDS - Sharding：mongodb 集群或DDM的模式，均默认为分片 - Sharding4.0+：mongodb 集群版本4.0+，默认为不分片 - ReplicaSet：mongodb 副本集,Replica RDS只读副本 - ReplicaSingle：mongodb 单节点 - Cluster：集群 - Independent：gaussdbv5 independent模式 - Combined：gaussdbv5 Combined模式 - Distributed ：分布式taurus - NoSharding：非集群模式

        :param cluster_mode: The cluster_mode of this EndpointVO.
        :type cluster_mode: str
        """
        self._cluster_mode = cluster_mode

    @property
    def instance_id(self):
        """Gets the instance_id of this EndpointVO.

        RDS实例id。

        :return: The instance_id of this EndpointVO.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this EndpointVO.

        RDS实例id。

        :param instance_id: The instance_id of this EndpointVO.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def db_name(self):
        """Gets the db_name of this EndpointVO.

        Oracle服务名serviceName。

        :return: The db_name of this EndpointVO.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this EndpointVO.

        Oracle服务名serviceName。

        :param db_name: The db_name of this EndpointVO.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def topic(self):
        """Gets the topic of this EndpointVO.

        mrskafka topic名称。

        :return: The topic of this EndpointVO.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this EndpointVO.

        mrskafka topic名称。

        :param topic: The topic of this EndpointVO.
        :type topic: str
        """
        self._topic = topic

    @property
    def safe_mode(self):
        """Gets the safe_mode of this EndpointVO.

        MRSkafka是否开启kerberos认证 - 0非安全认证 - 1安全认证

        :return: The safe_mode of this EndpointVO.
        :rtype: int
        """
        return self._safe_mode

    @safe_mode.setter
    def safe_mode(self, safe_mode):
        """Sets the safe_mode of this EndpointVO.

        MRSkafka是否开启kerberos认证 - 0非安全认证 - 1安全认证

        :param safe_mode: The safe_mode of this EndpointVO.
        :type safe_mode: int
        """
        self._safe_mode = safe_mode

    @property
    def kerberos_vo(self):
        """Gets the kerberos_vo of this EndpointVO.

        :return: The kerberos_vo of this EndpointVO.
        :rtype: :class:`huaweicloudsdkdrs.v3.KerberosVO`
        """
        return self._kerberos_vo

    @kerberos_vo.setter
    def kerberos_vo(self, kerberos_vo):
        """Sets the kerberos_vo of this EndpointVO.

        :param kerberos_vo: The kerberos_vo of this EndpointVO.
        :type kerberos_vo: :class:`huaweicloudsdkdrs.v3.KerberosVO`
        """
        self._kerberos_vo = kerberos_vo

    @property
    def multi_write_db_id(self):
        """Gets the multi_write_db_id of this EndpointVO.

        多写数据库Id。

        :return: The multi_write_db_id of this EndpointVO.
        :rtype: str
        """
        return self._multi_write_db_id

    @multi_write_db_id.setter
    def multi_write_db_id(self, multi_write_db_id):
        """Sets the multi_write_db_id of this EndpointVO.

        多写数据库Id。

        :param multi_write_db_id: The multi_write_db_id of this EndpointVO.
        :type multi_write_db_id: str
        """
        self._multi_write_db_id = multi_write_db_id

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
        if not isinstance(other, EndpointVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
