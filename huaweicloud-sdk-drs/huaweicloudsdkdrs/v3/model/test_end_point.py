# coding: utf-8

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
        'kafka_security_config': 'KafkaSecurity',
        'customized_dns': 'CustomizedDns'
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
        'kafka_security_config': 'kafka_security_config',
        'customized_dns': 'customized_dns'
    }

    def __init__(self, id=None, net_type=None, db_type=None, ip=None, db_port=None, inst_id=None, db_user=None, db_password=None, ssl_link=None, ssl_cert_key=None, ssl_cert_name=None, ssl_cert_check_sum=None, ssl_cert_password=None, vpc_id=None, subnet_id=None, end_point_type=None, region=None, project_id=None, db_name=None, kafka_security_config=None, customized_dns=None):
        r"""TestEndPoint

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  DRS任务ID，用于唯一标识一个数据复制任务，可从任务列表或任务详情页面获取。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type id: str
        :param net_type: **参数解释**：  任务使用的网络类型。  **约束限制**：  不涉及。  **取值范围**：  - vpn：虚拟专用网络 - vpc：虚拟私有云 - eip：弹性公网IP  **默认取值**：  不涉及
        :type net_type: str
        :param db_type: **参数解释**：  数据库类型，标识源库或目标库的数据库引擎种类。  **约束限制**：  不涉及。  **取值范围**：  - mysql：MySQL - mongodb：MongoDB - gaussdbv5：GaussDB分布式版 - postgresql：PostgreSQL - kafka：Kafka - gaussdbv5ha：GaussDB集中式版 - taurus：TaurusDB  **默认取值**：  不涉及
        :type db_type: str
        :param ip: **参数解释**：  数据库IP地址，用于指定连接数据库的服务器地址。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type ip: str
        :param db_port: **参数解释**：  数据库端口号，用于指定连接数据库的服务端口。  **约束限制**：  - db_type为MongoDB、DDS时端口必填取值为0。 - db_type为Oracle时为必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type db_port: int
        :param inst_id: **参数解释**：  RDS实例ID，用于标识华为云RDS数据库实例。  **约束限制**：  - 数据库为RDS实例时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type inst_id: str
        :param db_user: **参数解释**：  数据库帐号，用于连接数据库的用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type db_user: str
        :param db_password: **参数解释**：  数据库密码，用于连接数据库的认证密码。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type db_password: str
        :param ssl_link: **参数解释**：  是否使用SSL安全连接，指定数据库连接是否启用SSL加密传输。  **约束限制**：  - 该参数为true时，需填写SSL证书相关信息参数。  **取值范围**：  - true：使用SSL安全连接 - false：不使用SSL安全连接  **默认取值**：  不涉及
        :type ssl_link: bool
        :param ssl_cert_key: **参数解释**：  SSL证书内容，获取SSL证书后将内容通过BASE64加密后所得的字符串。  **约束限制**：  - ssl_link为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type ssl_cert_key: str
        :param ssl_cert_name: **参数解释**：  SSL证书名字。  **约束限制**：  - ssl_link为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type ssl_cert_name: str
        :param ssl_cert_check_sum: **参数解释**：  SSL证书内容checksum值，获取SSL证书后将内容经过SHA256加密后的值，后端校验用。  **约束限制**：  - ssl_link为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type ssl_cert_check_sum: str
        :param ssl_cert_password: **参数解释**：  SSL证书密码。  **约束限制**：  - 证书文件后缀为.p12时需要填写密码。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type ssl_cert_password: str
        :param vpc_id: **参数解释**：  虚拟私有云ID，用于标识数据库所在的VPC。  **约束限制**：  - 网络类型为VPC时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type vpc_id: str
        :param subnet_id: **参数解释**：  子网ID，用于标识数据库所在的子网。  **约束限制**：  - 网络类型为VPC时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type subnet_id: str
        :param end_point_type: **参数解释**：  数据库端点类型，标识该数据库在数据复制任务中是源端还是目标端。  **约束限制**：  不涉及。  **取值范围**：  - so：源库 - ta：目标库  **默认取值**：  so
        :type end_point_type: str
        :param region: **参数解释**：  RDS实例所在区域，用于标识数据库实例的地理区域。  **约束限制**：  - 数据库为RDS实例时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type region: str
        :param project_id: **参数解释**：  数据库实例所在Region的项目ID，数据库为云上实例时填写数据库实例所在Region下的项目ID，否则填写当前任务所在Region下的项目ID。获取方法请参见获取项目ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type project_id: str
        :param db_name: **参数解释**：  数据库名称，Oracle场景下为serviceName。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type db_name: str
        :param kafka_security_config: 
        :type kafka_security_config: :class:`huaweicloudsdkdrs.v3.KafkaSecurity`
        :param customized_dns: 
        :type customized_dns: :class:`huaweicloudsdkdrs.v3.CustomizedDns`
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
        self._customized_dns = None
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
        if customized_dns is not None:
            self.customized_dns = customized_dns

    @property
    def id(self):
        r"""Gets the id of this TestEndPoint.

        **参数解释**：  DRS任务ID，用于唯一标识一个数据复制任务，可从任务列表或任务详情页面获取。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The id of this TestEndPoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TestEndPoint.

        **参数解释**：  DRS任务ID，用于唯一标识一个数据复制任务，可从任务列表或任务详情页面获取。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param id: The id of this TestEndPoint.
        :type id: str
        """
        self._id = id

    @property
    def net_type(self):
        r"""Gets the net_type of this TestEndPoint.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  不涉及。  **取值范围**：  - vpn：虚拟专用网络 - vpc：虚拟私有云 - eip：弹性公网IP  **默认取值**：  不涉及

        :return: The net_type of this TestEndPoint.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        r"""Sets the net_type of this TestEndPoint.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  不涉及。  **取值范围**：  - vpn：虚拟专用网络 - vpc：虚拟私有云 - eip：弹性公网IP  **默认取值**：  不涉及

        :param net_type: The net_type of this TestEndPoint.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def db_type(self):
        r"""Gets the db_type of this TestEndPoint.

        **参数解释**：  数据库类型，标识源库或目标库的数据库引擎种类。  **约束限制**：  不涉及。  **取值范围**：  - mysql：MySQL - mongodb：MongoDB - gaussdbv5：GaussDB分布式版 - postgresql：PostgreSQL - kafka：Kafka - gaussdbv5ha：GaussDB集中式版 - taurus：TaurusDB  **默认取值**：  不涉及

        :return: The db_type of this TestEndPoint.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this TestEndPoint.

        **参数解释**：  数据库类型，标识源库或目标库的数据库引擎种类。  **约束限制**：  不涉及。  **取值范围**：  - mysql：MySQL - mongodb：MongoDB - gaussdbv5：GaussDB分布式版 - postgresql：PostgreSQL - kafka：Kafka - gaussdbv5ha：GaussDB集中式版 - taurus：TaurusDB  **默认取值**：  不涉及

        :param db_type: The db_type of this TestEndPoint.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def ip(self):
        r"""Gets the ip of this TestEndPoint.

        **参数解释**：  数据库IP地址，用于指定连接数据库的服务器地址。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The ip of this TestEndPoint.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this TestEndPoint.

        **参数解释**：  数据库IP地址，用于指定连接数据库的服务器地址。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param ip: The ip of this TestEndPoint.
        :type ip: str
        """
        self._ip = ip

    @property
    def db_port(self):
        r"""Gets the db_port of this TestEndPoint.

        **参数解释**：  数据库端口号，用于指定连接数据库的服务端口。  **约束限制**：  - db_type为MongoDB、DDS时端口必填取值为0。 - db_type为Oracle时为必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The db_port of this TestEndPoint.
        :rtype: int
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        r"""Sets the db_port of this TestEndPoint.

        **参数解释**：  数据库端口号，用于指定连接数据库的服务端口。  **约束限制**：  - db_type为MongoDB、DDS时端口必填取值为0。 - db_type为Oracle时为必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param db_port: The db_port of this TestEndPoint.
        :type db_port: int
        """
        self._db_port = db_port

    @property
    def inst_id(self):
        r"""Gets the inst_id of this TestEndPoint.

        **参数解释**：  RDS实例ID，用于标识华为云RDS数据库实例。  **约束限制**：  - 数据库为RDS实例时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The inst_id of this TestEndPoint.
        :rtype: str
        """
        return self._inst_id

    @inst_id.setter
    def inst_id(self, inst_id):
        r"""Sets the inst_id of this TestEndPoint.

        **参数解释**：  RDS实例ID，用于标识华为云RDS数据库实例。  **约束限制**：  - 数据库为RDS实例时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param inst_id: The inst_id of this TestEndPoint.
        :type inst_id: str
        """
        self._inst_id = inst_id

    @property
    def db_user(self):
        r"""Gets the db_user of this TestEndPoint.

        **参数解释**：  数据库帐号，用于连接数据库的用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The db_user of this TestEndPoint.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        r"""Sets the db_user of this TestEndPoint.

        **参数解释**：  数据库帐号，用于连接数据库的用户名。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param db_user: The db_user of this TestEndPoint.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def db_password(self):
        r"""Gets the db_password of this TestEndPoint.

        **参数解释**：  数据库密码，用于连接数据库的认证密码。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The db_password of this TestEndPoint.
        :rtype: str
        """
        return self._db_password

    @db_password.setter
    def db_password(self, db_password):
        r"""Sets the db_password of this TestEndPoint.

        **参数解释**：  数据库密码，用于连接数据库的认证密码。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param db_password: The db_password of this TestEndPoint.
        :type db_password: str
        """
        self._db_password = db_password

    @property
    def ssl_link(self):
        r"""Gets the ssl_link of this TestEndPoint.

        **参数解释**：  是否使用SSL安全连接，指定数据库连接是否启用SSL加密传输。  **约束限制**：  - 该参数为true时，需填写SSL证书相关信息参数。  **取值范围**：  - true：使用SSL安全连接 - false：不使用SSL安全连接  **默认取值**：  不涉及

        :return: The ssl_link of this TestEndPoint.
        :rtype: bool
        """
        return self._ssl_link

    @ssl_link.setter
    def ssl_link(self, ssl_link):
        r"""Sets the ssl_link of this TestEndPoint.

        **参数解释**：  是否使用SSL安全连接，指定数据库连接是否启用SSL加密传输。  **约束限制**：  - 该参数为true时，需填写SSL证书相关信息参数。  **取值范围**：  - true：使用SSL安全连接 - false：不使用SSL安全连接  **默认取值**：  不涉及

        :param ssl_link: The ssl_link of this TestEndPoint.
        :type ssl_link: bool
        """
        self._ssl_link = ssl_link

    @property
    def ssl_cert_key(self):
        r"""Gets the ssl_cert_key of this TestEndPoint.

        **参数解释**：  SSL证书内容，获取SSL证书后将内容通过BASE64加密后所得的字符串。  **约束限制**：  - ssl_link为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The ssl_cert_key of this TestEndPoint.
        :rtype: str
        """
        return self._ssl_cert_key

    @ssl_cert_key.setter
    def ssl_cert_key(self, ssl_cert_key):
        r"""Sets the ssl_cert_key of this TestEndPoint.

        **参数解释**：  SSL证书内容，获取SSL证书后将内容通过BASE64加密后所得的字符串。  **约束限制**：  - ssl_link为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param ssl_cert_key: The ssl_cert_key of this TestEndPoint.
        :type ssl_cert_key: str
        """
        self._ssl_cert_key = ssl_cert_key

    @property
    def ssl_cert_name(self):
        r"""Gets the ssl_cert_name of this TestEndPoint.

        **参数解释**：  SSL证书名字。  **约束限制**：  - ssl_link为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The ssl_cert_name of this TestEndPoint.
        :rtype: str
        """
        return self._ssl_cert_name

    @ssl_cert_name.setter
    def ssl_cert_name(self, ssl_cert_name):
        r"""Sets the ssl_cert_name of this TestEndPoint.

        **参数解释**：  SSL证书名字。  **约束限制**：  - ssl_link为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param ssl_cert_name: The ssl_cert_name of this TestEndPoint.
        :type ssl_cert_name: str
        """
        self._ssl_cert_name = ssl_cert_name

    @property
    def ssl_cert_check_sum(self):
        r"""Gets the ssl_cert_check_sum of this TestEndPoint.

        **参数解释**：  SSL证书内容checksum值，获取SSL证书后将内容经过SHA256加密后的值，后端校验用。  **约束限制**：  - ssl_link为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The ssl_cert_check_sum of this TestEndPoint.
        :rtype: str
        """
        return self._ssl_cert_check_sum

    @ssl_cert_check_sum.setter
    def ssl_cert_check_sum(self, ssl_cert_check_sum):
        r"""Sets the ssl_cert_check_sum of this TestEndPoint.

        **参数解释**：  SSL证书内容checksum值，获取SSL证书后将内容经过SHA256加密后的值，后端校验用。  **约束限制**：  - ssl_link为true时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param ssl_cert_check_sum: The ssl_cert_check_sum of this TestEndPoint.
        :type ssl_cert_check_sum: str
        """
        self._ssl_cert_check_sum = ssl_cert_check_sum

    @property
    def ssl_cert_password(self):
        r"""Gets the ssl_cert_password of this TestEndPoint.

        **参数解释**：  SSL证书密码。  **约束限制**：  - 证书文件后缀为.p12时需要填写密码。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The ssl_cert_password of this TestEndPoint.
        :rtype: str
        """
        return self._ssl_cert_password

    @ssl_cert_password.setter
    def ssl_cert_password(self, ssl_cert_password):
        r"""Sets the ssl_cert_password of this TestEndPoint.

        **参数解释**：  SSL证书密码。  **约束限制**：  - 证书文件后缀为.p12时需要填写密码。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param ssl_cert_password: The ssl_cert_password of this TestEndPoint.
        :type ssl_cert_password: str
        """
        self._ssl_cert_password = ssl_cert_password

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this TestEndPoint.

        **参数解释**：  虚拟私有云ID，用于标识数据库所在的VPC。  **约束限制**：  - 网络类型为VPC时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The vpc_id of this TestEndPoint.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this TestEndPoint.

        **参数解释**：  虚拟私有云ID，用于标识数据库所在的VPC。  **约束限制**：  - 网络类型为VPC时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param vpc_id: The vpc_id of this TestEndPoint.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this TestEndPoint.

        **参数解释**：  子网ID，用于标识数据库所在的子网。  **约束限制**：  - 网络类型为VPC时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The subnet_id of this TestEndPoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this TestEndPoint.

        **参数解释**：  子网ID，用于标识数据库所在的子网。  **约束限制**：  - 网络类型为VPC时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param subnet_id: The subnet_id of this TestEndPoint.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def end_point_type(self):
        r"""Gets the end_point_type of this TestEndPoint.

        **参数解释**：  数据库端点类型，标识该数据库在数据复制任务中是源端还是目标端。  **约束限制**：  不涉及。  **取值范围**：  - so：源库 - ta：目标库  **默认取值**：  so

        :return: The end_point_type of this TestEndPoint.
        :rtype: str
        """
        return self._end_point_type

    @end_point_type.setter
    def end_point_type(self, end_point_type):
        r"""Sets the end_point_type of this TestEndPoint.

        **参数解释**：  数据库端点类型，标识该数据库在数据复制任务中是源端还是目标端。  **约束限制**：  不涉及。  **取值范围**：  - so：源库 - ta：目标库  **默认取值**：  so

        :param end_point_type: The end_point_type of this TestEndPoint.
        :type end_point_type: str
        """
        self._end_point_type = end_point_type

    @property
    def region(self):
        r"""Gets the region of this TestEndPoint.

        **参数解释**：  RDS实例所在区域，用于标识数据库实例的地理区域。  **约束限制**：  - 数据库为RDS实例时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The region of this TestEndPoint.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this TestEndPoint.

        **参数解释**：  RDS实例所在区域，用于标识数据库实例的地理区域。  **约束限制**：  - 数据库为RDS实例时必填。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param region: The region of this TestEndPoint.
        :type region: str
        """
        self._region = region

    @property
    def project_id(self):
        r"""Gets the project_id of this TestEndPoint.

        **参数解释**：  数据库实例所在Region的项目ID，数据库为云上实例时填写数据库实例所在Region下的项目ID，否则填写当前任务所在Region下的项目ID。获取方法请参见获取项目ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The project_id of this TestEndPoint.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TestEndPoint.

        **参数解释**：  数据库实例所在Region的项目ID，数据库为云上实例时填写数据库实例所在Region下的项目ID，否则填写当前任务所在Region下的项目ID。获取方法请参见获取项目ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param project_id: The project_id of this TestEndPoint.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def db_name(self):
        r"""Gets the db_name of this TestEndPoint.

        **参数解释**：  数据库名称，Oracle场景下为serviceName。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The db_name of this TestEndPoint.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this TestEndPoint.

        **参数解释**：  数据库名称，Oracle场景下为serviceName。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param db_name: The db_name of this TestEndPoint.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def kafka_security_config(self):
        r"""Gets the kafka_security_config of this TestEndPoint.

        :return: The kafka_security_config of this TestEndPoint.
        :rtype: :class:`huaweicloudsdkdrs.v3.KafkaSecurity`
        """
        return self._kafka_security_config

    @kafka_security_config.setter
    def kafka_security_config(self, kafka_security_config):
        r"""Sets the kafka_security_config of this TestEndPoint.

        :param kafka_security_config: The kafka_security_config of this TestEndPoint.
        :type kafka_security_config: :class:`huaweicloudsdkdrs.v3.KafkaSecurity`
        """
        self._kafka_security_config = kafka_security_config

    @property
    def customized_dns(self):
        r"""Gets the customized_dns of this TestEndPoint.

        :return: The customized_dns of this TestEndPoint.
        :rtype: :class:`huaweicloudsdkdrs.v3.CustomizedDns`
        """
        return self._customized_dns

    @customized_dns.setter
    def customized_dns(self, customized_dns):
        r"""Sets the customized_dns of this TestEndPoint.

        :param customized_dns: The customized_dns of this TestEndPoint.
        :type customized_dns: :class:`huaweicloudsdkdrs.v3.CustomizedDns`
        """
        self._customized_dns = customized_dns

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
