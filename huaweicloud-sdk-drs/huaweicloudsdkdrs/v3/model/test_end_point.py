# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestEndPoint:

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
        'net_type': 'str',
        'db_type': 'str',
        'ip': 'str',
        'db_port': 'int',
        'inst_id': 'str',
        'db_user': 'str',
        'db_password': 'str',
        'ssl_link': 'bool',
        'ssl_cert_key': 'str',
        'ssl_cert_name': 'str',
        'ssl_cert_check_sum': 'str',
        'ssl_cert_password': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'end_point_type': 'str',
        'region': 'str',
        'project_id': 'str',
        'db_name': 'str',
        'kafka_security_config': 'KafkaSecurity'
    }

    attribute_map = {
        'id': 'id',
        'net_type': 'net_type',
        'db_type': 'db_type',
        'ip': 'ip',
        'db_port': 'db_port',
        'inst_id': 'inst_id',
        'db_user': 'db_user',
        'db_password': 'db_password',
        'ssl_link': 'ssl_link',
        'ssl_cert_key': 'ssl_cert_key',
        'ssl_cert_name': 'ssl_cert_name',
        'ssl_cert_check_sum': 'ssl_cert_check_sum',
        'ssl_cert_password': 'ssl_cert_password',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'end_point_type': 'end_point_type',
        'region': 'region',
        'project_id': 'project_id',
        'db_name': 'db_name',
        'kafka_security_config': 'kafka_security_config'
    }

    def __init__(self, id=None, net_type=None, db_type=None, ip=None, db_port=None, inst_id=None, db_user=None, db_password=None, ssl_link=None, ssl_cert_key=None, ssl_cert_name=None, ssl_cert_check_sum=None, ssl_cert_password=None, vpc_id=None, subnet_id=None, end_point_type=None, region=None, project_id=None, db_name=None, kafka_security_config=None):
        """TestEndPoint

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param net_type: 网络类型
        :type net_type: str
        :param db_type: 数据库类型
        :type db_type: str
        :param ip: 数据库IP
        :type ip: str
        :param db_port: 数据库端口，Mongo、DDS必填为0。
        :type db_port: int
        :param inst_id: RDS实例id，RDS实例必填。
        :type inst_id: str
        :param db_user: 数据库帐号。
        :type db_user: str
        :param db_password: 数据库密码。
        :type db_password: str
        :param ssl_link: 是否SSL安全连接。
        :type ssl_link: bool
        :param ssl_cert_key: SSL证书内容，base64加密后的值，源库安全连接必选。
        :type ssl_cert_key: str
        :param ssl_cert_name: SSL证书名字，源库安全连接必选。
        :type ssl_cert_name: str
        :param ssl_cert_check_sum: SSL证书内容checksum值，证书经过sha256加密后的值，后端校验，源库安全连接必选。
        :type ssl_cert_check_sum: str
        :param ssl_cert_password: SSL证书密码，证书文件后缀为.p12，需要密码。
        :type ssl_cert_password: str
        :param vpc_id: vpcid，数据库为RDS时必选。
        :type vpc_id: str
        :param subnet_id: subnetid，数据库为RDS必选。
        :type subnet_id: str
        :param end_point_type: 源库：so,目标库：ta
        :type end_point_type: str
        :param region: rds实例region，数据库为RDS时必填。
        :type region: str
        :param project_id: 用户所处region的projectId。
        :type project_id: str
        :param db_name: 数据库用户名，DDS的账号认证数据库，Oracle的serviceName。
        :type db_name: str
        :param kafka_security_config: 
        :type kafka_security_config: :class:`huaweicloudsdkdrs.v3.KafkaSecurity`
        """
        
        

        self._id = None
        self._net_type = None
        self._db_type = None
        self._ip = None
        self._db_port = None
        self._inst_id = None
        self._db_user = None
        self._db_password = None
        self._ssl_link = None
        self._ssl_cert_key = None
        self._ssl_cert_name = None
        self._ssl_cert_check_sum = None
        self._ssl_cert_password = None
        self._vpc_id = None
        self._subnet_id = None
        self._end_point_type = None
        self._region = None
        self._project_id = None
        self._db_name = None
        self._kafka_security_config = None
        self.discriminator = None

        self.id = id
        self.net_type = net_type
        self.db_type = db_type
        self.ip = ip
        if db_port is not None:
            self.db_port = db_port
        if inst_id is not None:
            self.inst_id = inst_id
        self.db_user = db_user
        self.db_password = db_password
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
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        self.end_point_type = end_point_type
        if region is not None:
            self.region = region
        if project_id is not None:
            self.project_id = project_id
        if db_name is not None:
            self.db_name = db_name
        if kafka_security_config is not None:
            self.kafka_security_config = kafka_security_config

    @property
    def id(self):
        """Gets the id of this TestEndPoint.

        任务ID

        :return: The id of this TestEndPoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestEndPoint.

        任务ID

        :param id: The id of this TestEndPoint.
        :type id: str
        """
        self._id = id

    @property
    def net_type(self):
        """Gets the net_type of this TestEndPoint.

        网络类型

        :return: The net_type of this TestEndPoint.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        """Sets the net_type of this TestEndPoint.

        网络类型

        :param net_type: The net_type of this TestEndPoint.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def db_type(self):
        """Gets the db_type of this TestEndPoint.

        数据库类型

        :return: The db_type of this TestEndPoint.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        """Sets the db_type of this TestEndPoint.

        数据库类型

        :param db_type: The db_type of this TestEndPoint.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def ip(self):
        """Gets the ip of this TestEndPoint.

        数据库IP

        :return: The ip of this TestEndPoint.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this TestEndPoint.

        数据库IP

        :param ip: The ip of this TestEndPoint.
        :type ip: str
        """
        self._ip = ip

    @property
    def db_port(self):
        """Gets the db_port of this TestEndPoint.

        数据库端口，Mongo、DDS必填为0。

        :return: The db_port of this TestEndPoint.
        :rtype: int
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        """Sets the db_port of this TestEndPoint.

        数据库端口，Mongo、DDS必填为0。

        :param db_port: The db_port of this TestEndPoint.
        :type db_port: int
        """
        self._db_port = db_port

    @property
    def inst_id(self):
        """Gets the inst_id of this TestEndPoint.

        RDS实例id，RDS实例必填。

        :return: The inst_id of this TestEndPoint.
        :rtype: str
        """
        return self._inst_id

    @inst_id.setter
    def inst_id(self, inst_id):
        """Sets the inst_id of this TestEndPoint.

        RDS实例id，RDS实例必填。

        :param inst_id: The inst_id of this TestEndPoint.
        :type inst_id: str
        """
        self._inst_id = inst_id

    @property
    def db_user(self):
        """Gets the db_user of this TestEndPoint.

        数据库帐号。

        :return: The db_user of this TestEndPoint.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        """Sets the db_user of this TestEndPoint.

        数据库帐号。

        :param db_user: The db_user of this TestEndPoint.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def db_password(self):
        """Gets the db_password of this TestEndPoint.

        数据库密码。

        :return: The db_password of this TestEndPoint.
        :rtype: str
        """
        return self._db_password

    @db_password.setter
    def db_password(self, db_password):
        """Sets the db_password of this TestEndPoint.

        数据库密码。

        :param db_password: The db_password of this TestEndPoint.
        :type db_password: str
        """
        self._db_password = db_password

    @property
    def ssl_link(self):
        """Gets the ssl_link of this TestEndPoint.

        是否SSL安全连接。

        :return: The ssl_link of this TestEndPoint.
        :rtype: bool
        """
        return self._ssl_link

    @ssl_link.setter
    def ssl_link(self, ssl_link):
        """Sets the ssl_link of this TestEndPoint.

        是否SSL安全连接。

        :param ssl_link: The ssl_link of this TestEndPoint.
        :type ssl_link: bool
        """
        self._ssl_link = ssl_link

    @property
    def ssl_cert_key(self):
        """Gets the ssl_cert_key of this TestEndPoint.

        SSL证书内容，base64加密后的值，源库安全连接必选。

        :return: The ssl_cert_key of this TestEndPoint.
        :rtype: str
        """
        return self._ssl_cert_key

    @ssl_cert_key.setter
    def ssl_cert_key(self, ssl_cert_key):
        """Sets the ssl_cert_key of this TestEndPoint.

        SSL证书内容，base64加密后的值，源库安全连接必选。

        :param ssl_cert_key: The ssl_cert_key of this TestEndPoint.
        :type ssl_cert_key: str
        """
        self._ssl_cert_key = ssl_cert_key

    @property
    def ssl_cert_name(self):
        """Gets the ssl_cert_name of this TestEndPoint.

        SSL证书名字，源库安全连接必选。

        :return: The ssl_cert_name of this TestEndPoint.
        :rtype: str
        """
        return self._ssl_cert_name

    @ssl_cert_name.setter
    def ssl_cert_name(self, ssl_cert_name):
        """Sets the ssl_cert_name of this TestEndPoint.

        SSL证书名字，源库安全连接必选。

        :param ssl_cert_name: The ssl_cert_name of this TestEndPoint.
        :type ssl_cert_name: str
        """
        self._ssl_cert_name = ssl_cert_name

    @property
    def ssl_cert_check_sum(self):
        """Gets the ssl_cert_check_sum of this TestEndPoint.

        SSL证书内容checksum值，证书经过sha256加密后的值，后端校验，源库安全连接必选。

        :return: The ssl_cert_check_sum of this TestEndPoint.
        :rtype: str
        """
        return self._ssl_cert_check_sum

    @ssl_cert_check_sum.setter
    def ssl_cert_check_sum(self, ssl_cert_check_sum):
        """Sets the ssl_cert_check_sum of this TestEndPoint.

        SSL证书内容checksum值，证书经过sha256加密后的值，后端校验，源库安全连接必选。

        :param ssl_cert_check_sum: The ssl_cert_check_sum of this TestEndPoint.
        :type ssl_cert_check_sum: str
        """
        self._ssl_cert_check_sum = ssl_cert_check_sum

    @property
    def ssl_cert_password(self):
        """Gets the ssl_cert_password of this TestEndPoint.

        SSL证书密码，证书文件后缀为.p12，需要密码。

        :return: The ssl_cert_password of this TestEndPoint.
        :rtype: str
        """
        return self._ssl_cert_password

    @ssl_cert_password.setter
    def ssl_cert_password(self, ssl_cert_password):
        """Sets the ssl_cert_password of this TestEndPoint.

        SSL证书密码，证书文件后缀为.p12，需要密码。

        :param ssl_cert_password: The ssl_cert_password of this TestEndPoint.
        :type ssl_cert_password: str
        """
        self._ssl_cert_password = ssl_cert_password

    @property
    def vpc_id(self):
        """Gets the vpc_id of this TestEndPoint.

        vpcid，数据库为RDS时必选。

        :return: The vpc_id of this TestEndPoint.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this TestEndPoint.

        vpcid，数据库为RDS时必选。

        :param vpc_id: The vpc_id of this TestEndPoint.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this TestEndPoint.

        subnetid，数据库为RDS必选。

        :return: The subnet_id of this TestEndPoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this TestEndPoint.

        subnetid，数据库为RDS必选。

        :param subnet_id: The subnet_id of this TestEndPoint.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def end_point_type(self):
        """Gets the end_point_type of this TestEndPoint.

        源库：so,目标库：ta

        :return: The end_point_type of this TestEndPoint.
        :rtype: str
        """
        return self._end_point_type

    @end_point_type.setter
    def end_point_type(self, end_point_type):
        """Sets the end_point_type of this TestEndPoint.

        源库：so,目标库：ta

        :param end_point_type: The end_point_type of this TestEndPoint.
        :type end_point_type: str
        """
        self._end_point_type = end_point_type

    @property
    def region(self):
        """Gets the region of this TestEndPoint.

        rds实例region，数据库为RDS时必填。

        :return: The region of this TestEndPoint.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TestEndPoint.

        rds实例region，数据库为RDS时必填。

        :param region: The region of this TestEndPoint.
        :type region: str
        """
        self._region = region

    @property
    def project_id(self):
        """Gets the project_id of this TestEndPoint.

        用户所处region的projectId。

        :return: The project_id of this TestEndPoint.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TestEndPoint.

        用户所处region的projectId。

        :param project_id: The project_id of this TestEndPoint.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def db_name(self):
        """Gets the db_name of this TestEndPoint.

        数据库用户名，DDS的账号认证数据库，Oracle的serviceName。

        :return: The db_name of this TestEndPoint.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this TestEndPoint.

        数据库用户名，DDS的账号认证数据库，Oracle的serviceName。

        :param db_name: The db_name of this TestEndPoint.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def kafka_security_config(self):
        """Gets the kafka_security_config of this TestEndPoint.

        :return: The kafka_security_config of this TestEndPoint.
        :rtype: :class:`huaweicloudsdkdrs.v3.KafkaSecurity`
        """
        return self._kafka_security_config

    @kafka_security_config.setter
    def kafka_security_config(self, kafka_security_config):
        """Sets the kafka_security_config of this TestEndPoint.

        :param kafka_security_config: The kafka_security_config of this TestEndPoint.
        :type kafka_security_config: :class:`huaweicloudsdkdrs.v3.KafkaSecurity`
        """
        self._kafka_security_config = kafka_security_config

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
        if not isinstance(other, TestEndPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
