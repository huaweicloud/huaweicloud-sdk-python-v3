# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Endpoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'db_type': 'str',
        'az_code': 'str',
        'region': 'str',
        'inst_id': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'project_id': 'str',
        'db_name': 'str',
        'db_password': 'str',
        'db_port': 'int',
        'db_user': 'str',
        'inst_name': 'str',
        'ip': 'str',
        'mongo_ha_mode': 'str',
        'safe_mode': 'int',
        'ssl_cert_password': 'str',
        'ssl_cert_check_sum': 'str',
        'ssl_cert_key': 'str',
        'ssl_cert_name': 'str',
        'ssl_link': 'bool',
        'topic': 'str',
        'cluster_mode': 'str'
    }

    attribute_map = {
        'db_type': 'db_type',
        'az_code': 'az_code',
        'region': 'region',
        'inst_id': 'inst_id',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'project_id': 'project_id',
        'db_name': 'db_name',
        'db_password': 'db_password',
        'db_port': 'db_port',
        'db_user': 'db_user',
        'inst_name': 'inst_name',
        'ip': 'ip',
        'mongo_ha_mode': 'mongo_ha_mode',
        'safe_mode': 'safe_mode',
        'ssl_cert_password': 'ssl_cert_password',
        'ssl_cert_check_sum': 'ssl_cert_check_sum',
        'ssl_cert_key': 'ssl_cert_key',
        'ssl_cert_name': 'ssl_cert_name',
        'ssl_link': 'ssl_link',
        'topic': 'topic',
        'cluster_mode': 'cluster_mode'
    }

    def __init__(self, db_type=None, az_code=None, region=None, inst_id=None, vpc_id=None, subnet_id=None, security_group_id=None, project_id=None, db_name=None, db_password=None, db_port=None, db_user=None, inst_name=None, ip=None, mongo_ha_mode=None, safe_mode=None, ssl_cert_password=None, ssl_cert_check_sum=None, ssl_cert_key=None, ssl_cert_name=None, ssl_link=None, topic=None, cluster_mode=None):
        """Endpoint

        The model defined in huaweicloud sdk

        :param db_type: 数据库类型，测试连接之后修改调用时必填。
        :type db_type: str
        :param az_code: 数据库所在可用区azCode
        :type az_code: str
        :param region: RDS实例所在Region，数据库为RDS实例时必填（灾备场景下job_direction为down时source_endpoint中该值为必填，job_direction为up时target_endpoint中该值为必填）。
        :type region: str
        :param inst_id: RDS实例ID，数据库为RDS实例必填（灾备场景下job_direction为down时source_endpoint中该值为必填，job_direction为up时target_endpoint中该值为必填）。
        :type inst_id: str
        :param vpc_id: 数据库所在的虚拟私有云id
        :type vpc_id: str
        :param subnet_id: 数据库所在的子网id
        :type subnet_id: str
        :param security_group_id: 数据库所在的安全组id。
        :type security_group_id: str
        :param project_id: RDS实例projectId
        :type project_id: str
        :param db_name: 服务名serviceName，源库为oracle场景时必填。约束：不能超过128位，不能包含!&lt;&gt;&amp;&#39;\&quot;\\特殊字符。待还原数据库名称是指备份文件中包含的数据库名称，当您选择部分数据库恢复时，需要选择恢复一个或者多个数据库。
        :type db_name: str
        :param db_password: 数据库密码。
        :type db_password: str
        :param db_port: 数据库端口。约束：输入范围为1-65535之间的整数。
        :type db_port: int
        :param db_user: 数据库用户。
        :type db_user: str
        :param inst_name: RDS实例名称。
        :type inst_name: str
        :param ip: 数据库ip
        :type ip: str
        :param mongo_ha_mode: mongo ha模式。
        :type mongo_ha_mode: str
        :param safe_mode: MRS集群运行模式，取值： - 0普通集群 - 1安全集群
        :type safe_mode: int
        :param ssl_cert_password: SSL证书密码，证书文件后缀为.p12
        :type ssl_cert_password: str
        :param ssl_cert_check_sum: SSL证书内容checksum值，后端校验，源库安全连接必选。
        :type ssl_cert_check_sum: str
        :param ssl_cert_key: SSL证书内容，用base64加密
        :type ssl_cert_key: str
        :param ssl_cert_name: SSL证书名字
        :type ssl_cert_name: str
        :param ssl_link: 是否SSL安全连接。
        :type ssl_link: bool
        :param topic: kafka topic名称
        :type topic: str
        :param cluster_mode: MongDB集群4.0及以上版本，当集群实例无法获取到分片节点的IP时，source_endpoint中需要填写，值为：Sharding4.0+。
        :type cluster_mode: str
        """
        
        

        self._db_type = None
        self._az_code = None
        self._region = None
        self._inst_id = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._project_id = None
        self._db_name = None
        self._db_password = None
        self._db_port = None
        self._db_user = None
        self._inst_name = None
        self._ip = None
        self._mongo_ha_mode = None
        self._safe_mode = None
        self._ssl_cert_password = None
        self._ssl_cert_check_sum = None
        self._ssl_cert_key = None
        self._ssl_cert_name = None
        self._ssl_link = None
        self._topic = None
        self._cluster_mode = None
        self.discriminator = None

        if db_type is not None:
            self.db_type = db_type
        if az_code is not None:
            self.az_code = az_code
        if region is not None:
            self.region = region
        if inst_id is not None:
            self.inst_id = inst_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if project_id is not None:
            self.project_id = project_id
        if db_name is not None:
            self.db_name = db_name
        if db_password is not None:
            self.db_password = db_password
        if db_port is not None:
            self.db_port = db_port
        if db_user is not None:
            self.db_user = db_user
        if inst_name is not None:
            self.inst_name = inst_name
        if ip is not None:
            self.ip = ip
        if mongo_ha_mode is not None:
            self.mongo_ha_mode = mongo_ha_mode
        if safe_mode is not None:
            self.safe_mode = safe_mode
        if ssl_cert_password is not None:
            self.ssl_cert_password = ssl_cert_password
        if ssl_cert_check_sum is not None:
            self.ssl_cert_check_sum = ssl_cert_check_sum
        if ssl_cert_key is not None:
            self.ssl_cert_key = ssl_cert_key
        if ssl_cert_name is not None:
            self.ssl_cert_name = ssl_cert_name
        if ssl_link is not None:
            self.ssl_link = ssl_link
        if topic is not None:
            self.topic = topic
        if cluster_mode is not None:
            self.cluster_mode = cluster_mode

    @property
    def db_type(self):
        """Gets the db_type of this Endpoint.

        数据库类型，测试连接之后修改调用时必填。

        :return: The db_type of this Endpoint.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this Endpoint.

        数据库类型，测试连接之后修改调用时必填。

        :param db_type: The db_type of this Endpoint.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def az_code(self):
        """Gets the az_code of this Endpoint.

        数据库所在可用区azCode

        :return: The az_code of this Endpoint.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this Endpoint.

        数据库所在可用区azCode

        :param az_code: The az_code of this Endpoint.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def region(self):
        """Gets the region of this Endpoint.

        RDS实例所在Region，数据库为RDS实例时必填（灾备场景下job_direction为down时source_endpoint中该值为必填，job_direction为up时target_endpoint中该值为必填）。

        :return: The region of this Endpoint.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Endpoint.

        RDS实例所在Region，数据库为RDS实例时必填（灾备场景下job_direction为down时source_endpoint中该值为必填，job_direction为up时target_endpoint中该值为必填）。

        :param region: The region of this Endpoint.
        :type region: str
        """
        self._region = region

    @property
    def inst_id(self):
        """Gets the inst_id of this Endpoint.

        RDS实例ID，数据库为RDS实例必填（灾备场景下job_direction为down时source_endpoint中该值为必填，job_direction为up时target_endpoint中该值为必填）。

        :return: The inst_id of this Endpoint.
        :rtype: str
        """
        return self._inst_id

    @inst_id.setter
    def inst_id(self, inst_id):
        """Sets the inst_id of this Endpoint.

        RDS实例ID，数据库为RDS实例必填（灾备场景下job_direction为down时source_endpoint中该值为必填，job_direction为up时target_endpoint中该值为必填）。

        :param inst_id: The inst_id of this Endpoint.
        :type inst_id: str
        """
        self._inst_id = inst_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Endpoint.

        数据库所在的虚拟私有云id

        :return: The vpc_id of this Endpoint.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Endpoint.

        数据库所在的虚拟私有云id

        :param vpc_id: The vpc_id of this Endpoint.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this Endpoint.

        数据库所在的子网id

        :return: The subnet_id of this Endpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this Endpoint.

        数据库所在的子网id

        :param subnet_id: The subnet_id of this Endpoint.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this Endpoint.

        数据库所在的安全组id。

        :return: The security_group_id of this Endpoint.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this Endpoint.

        数据库所在的安全组id。

        :param security_group_id: The security_group_id of this Endpoint.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def project_id(self):
        """Gets the project_id of this Endpoint.

        RDS实例projectId

        :return: The project_id of this Endpoint.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Endpoint.

        RDS实例projectId

        :param project_id: The project_id of this Endpoint.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def db_name(self):
        """Gets the db_name of this Endpoint.

        服务名serviceName，源库为oracle场景时必填。约束：不能超过128位，不能包含!<>&'\"\\特殊字符。待还原数据库名称是指备份文件中包含的数据库名称，当您选择部分数据库恢复时，需要选择恢复一个或者多个数据库。

        :return: The db_name of this Endpoint.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this Endpoint.

        服务名serviceName，源库为oracle场景时必填。约束：不能超过128位，不能包含!<>&'\"\\特殊字符。待还原数据库名称是指备份文件中包含的数据库名称，当您选择部分数据库恢复时，需要选择恢复一个或者多个数据库。

        :param db_name: The db_name of this Endpoint.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def db_password(self):
        """Gets the db_password of this Endpoint.

        数据库密码。

        :return: The db_password of this Endpoint.
        :rtype: str
        """
        return self._db_password

    @db_password.setter
    def db_password(self, db_password):
        """Sets the db_password of this Endpoint.

        数据库密码。

        :param db_password: The db_password of this Endpoint.
        :type db_password: str
        """
        self._db_password = db_password

    @property
    def db_port(self):
        """Gets the db_port of this Endpoint.

        数据库端口。约束：输入范围为1-65535之间的整数。

        :return: The db_port of this Endpoint.
        :rtype: int
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        """Sets the db_port of this Endpoint.

        数据库端口。约束：输入范围为1-65535之间的整数。

        :param db_port: The db_port of this Endpoint.
        :type db_port: int
        """
        self._db_port = db_port

    @property
    def db_user(self):
        """Gets the db_user of this Endpoint.

        数据库用户。

        :return: The db_user of this Endpoint.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        """Sets the db_user of this Endpoint.

        数据库用户。

        :param db_user: The db_user of this Endpoint.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def inst_name(self):
        """Gets the inst_name of this Endpoint.

        RDS实例名称。

        :return: The inst_name of this Endpoint.
        :rtype: str
        """
        return self._inst_name

    @inst_name.setter
    def inst_name(self, inst_name):
        """Sets the inst_name of this Endpoint.

        RDS实例名称。

        :param inst_name: The inst_name of this Endpoint.
        :type inst_name: str
        """
        self._inst_name = inst_name

    @property
    def ip(self):
        """Gets the ip of this Endpoint.

        数据库ip

        :return: The ip of this Endpoint.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Endpoint.

        数据库ip

        :param ip: The ip of this Endpoint.
        :type ip: str
        """
        self._ip = ip

    @property
    def mongo_ha_mode(self):
        """Gets the mongo_ha_mode of this Endpoint.

        mongo ha模式。

        :return: The mongo_ha_mode of this Endpoint.
        :rtype: str
        """
        return self._mongo_ha_mode

    @mongo_ha_mode.setter
    def mongo_ha_mode(self, mongo_ha_mode):
        """Sets the mongo_ha_mode of this Endpoint.

        mongo ha模式。

        :param mongo_ha_mode: The mongo_ha_mode of this Endpoint.
        :type mongo_ha_mode: str
        """
        self._mongo_ha_mode = mongo_ha_mode

    @property
    def safe_mode(self):
        """Gets the safe_mode of this Endpoint.

        MRS集群运行模式，取值： - 0普通集群 - 1安全集群

        :return: The safe_mode of this Endpoint.
        :rtype: int
        """
        return self._safe_mode

    @safe_mode.setter
    def safe_mode(self, safe_mode):
        """Sets the safe_mode of this Endpoint.

        MRS集群运行模式，取值： - 0普通集群 - 1安全集群

        :param safe_mode: The safe_mode of this Endpoint.
        :type safe_mode: int
        """
        self._safe_mode = safe_mode

    @property
    def ssl_cert_password(self):
        """Gets the ssl_cert_password of this Endpoint.

        SSL证书密码，证书文件后缀为.p12

        :return: The ssl_cert_password of this Endpoint.
        :rtype: str
        """
        return self._ssl_cert_password

    @ssl_cert_password.setter
    def ssl_cert_password(self, ssl_cert_password):
        """Sets the ssl_cert_password of this Endpoint.

        SSL证书密码，证书文件后缀为.p12

        :param ssl_cert_password: The ssl_cert_password of this Endpoint.
        :type ssl_cert_password: str
        """
        self._ssl_cert_password = ssl_cert_password

    @property
    def ssl_cert_check_sum(self):
        """Gets the ssl_cert_check_sum of this Endpoint.

        SSL证书内容checksum值，后端校验，源库安全连接必选。

        :return: The ssl_cert_check_sum of this Endpoint.
        :rtype: str
        """
        return self._ssl_cert_check_sum

    @ssl_cert_check_sum.setter
    def ssl_cert_check_sum(self, ssl_cert_check_sum):
        """Sets the ssl_cert_check_sum of this Endpoint.

        SSL证书内容checksum值，后端校验，源库安全连接必选。

        :param ssl_cert_check_sum: The ssl_cert_check_sum of this Endpoint.
        :type ssl_cert_check_sum: str
        """
        self._ssl_cert_check_sum = ssl_cert_check_sum

    @property
    def ssl_cert_key(self):
        """Gets the ssl_cert_key of this Endpoint.

        SSL证书内容，用base64加密

        :return: The ssl_cert_key of this Endpoint.
        :rtype: str
        """
        return self._ssl_cert_key

    @ssl_cert_key.setter
    def ssl_cert_key(self, ssl_cert_key):
        """Sets the ssl_cert_key of this Endpoint.

        SSL证书内容，用base64加密

        :param ssl_cert_key: The ssl_cert_key of this Endpoint.
        :type ssl_cert_key: str
        """
        self._ssl_cert_key = ssl_cert_key

    @property
    def ssl_cert_name(self):
        """Gets the ssl_cert_name of this Endpoint.

        SSL证书名字

        :return: The ssl_cert_name of this Endpoint.
        :rtype: str
        """
        return self._ssl_cert_name

    @ssl_cert_name.setter
    def ssl_cert_name(self, ssl_cert_name):
        """Sets the ssl_cert_name of this Endpoint.

        SSL证书名字

        :param ssl_cert_name: The ssl_cert_name of this Endpoint.
        :type ssl_cert_name: str
        """
        self._ssl_cert_name = ssl_cert_name

    @property
    def ssl_link(self):
        """Gets the ssl_link of this Endpoint.

        是否SSL安全连接。

        :return: The ssl_link of this Endpoint.
        :rtype: bool
        """
        return self._ssl_link

    @ssl_link.setter
    def ssl_link(self, ssl_link):
        """Sets the ssl_link of this Endpoint.

        是否SSL安全连接。

        :param ssl_link: The ssl_link of this Endpoint.
        :type ssl_link: bool
        """
        self._ssl_link = ssl_link

    @property
    def topic(self):
        """Gets the topic of this Endpoint.

        kafka topic名称

        :return: The topic of this Endpoint.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this Endpoint.

        kafka topic名称

        :param topic: The topic of this Endpoint.
        :type topic: str
        """
        self._topic = topic

    @property
    def cluster_mode(self):
        """Gets the cluster_mode of this Endpoint.

        MongDB集群4.0及以上版本，当集群实例无法获取到分片节点的IP时，source_endpoint中需要填写，值为：Sharding4.0+。

        :return: The cluster_mode of this Endpoint.
        :rtype: str
        """
        return self._cluster_mode

    @cluster_mode.setter
    def cluster_mode(self, cluster_mode):
        """Sets the cluster_mode of this Endpoint.

        MongDB集群4.0及以上版本，当集群实例无法获取到分片节点的IP时，source_endpoint中需要填写，值为：Sharding4.0+。

        :param cluster_mode: The cluster_mode of this Endpoint.
        :type cluster_mode: str
        """
        self._cluster_mode = cluster_mode

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
        if not isinstance(other, Endpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
