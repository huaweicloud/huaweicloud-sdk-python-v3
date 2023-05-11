# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Content:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gauss100_version': 'str',
        'host': 'str',
        'port': 'str',
        'database_name': 'str',
        'redis_database': 'str',
        'user_name': 'str',
        'password': 'str',
        'mode': 'str',
        'cdc_mode': 'str',
        'multi_oracle_address': 'list[MultiOracleAddress]',
        'oracle_service_name': 'str',
        'ftp_connect_mode': 'str',
        'ftp_protocol': 'str',
        'address': 'str',
        'ak': 'str',
        'sk': 'str',
        'bucket_name': 'str',
        'https': 'bool',
        'url': 'str',
        'api_method': 'str',
        'auth_method': 'str',
        'api_auth_detail': 'ApiAuthDetail',
        'broker': 'str',
        'ssl': 'bool',
        'ssl_enable': 'bool',
        'ssl_username': 'str',
        'ssl_password': 'str',
        'mongodb_auth_source': 'str',
        'mongodb_cluster_enable': 'bool',
        'mongodb_replica_set': 'str',
        'encoding': 'str',
        'mysql_timeout': 'int',
        'trust_store_password': 'str',
        'trust_store': 'str',
        'trust_store_file_type': 'str',
        'ssl_auth_method': 'str',
        'key_store': 'str',
        'key_store_file_type': 'str',
        'key_store_password': 'str',
        'key_store_key_password': 'str',
        'dis_tunnel_name': 'str',
        'dis_data_type': 'str',
        'dis_setting_type': 'str',
        'dis_endpoint': 'str',
        'dis_region': 'str',
        'dis_source_project_id': 'str',
        'hl7_position': 'str',
        'hl7_whitelist_enable': 'bool',
        'hl7_whitelist': 'str',
        'ldap_security_auth_type': 'str',
        'rabbitmq_virtual_host': 'str',
        'rabbitmq_ssl_protocol': 'str',
        'sap_client': 'str',
        'sap_sysnr': 'str',
        'snmp_network_protocol': 'str',
        'snmp_version': 'int',
        'snmp_community': 'str',
        'ibmmq_ccs_id': 'str',
        'ibmmq_queue_manager': 'str',
        'ibmmq_channel': 'str',
        'ibmmq_cipher_suite': 'str',
        'hdfs_path': 'str',
        'principal_name': 'str',
        'config_file_name': 'str',
        'config_file_content': 'str',
        'connection_instance_id': 'str',
        'connector_params': 'object'
    }

    attribute_map = {
        'gauss100_version': 'gauss100_version',
        'host': 'host',
        'port': 'port',
        'database_name': 'database_name',
        'redis_database': 'redis_database',
        'user_name': 'user_name',
        'password': 'password',
        'mode': 'mode',
        'cdc_mode': 'cdc_mode',
        'multi_oracle_address': 'multi_oracle_address',
        'oracle_service_name': 'oracle_service_name',
        'ftp_connect_mode': 'ftp_connect_mode',
        'ftp_protocol': 'ftp_protocol',
        'address': 'address',
        'ak': 'ak',
        'sk': 'sk',
        'bucket_name': 'bucket_name',
        'https': 'https',
        'url': 'url',
        'api_method': 'api_method',
        'auth_method': 'auth_method',
        'api_auth_detail': 'api_auth_detail',
        'broker': 'broker',
        'ssl': 'ssl',
        'ssl_enable': 'ssl_enable',
        'ssl_username': 'ssl_username',
        'ssl_password': 'ssl_password',
        'mongodb_auth_source': 'mongodb_auth_source',
        'mongodb_cluster_enable': 'mongodb_cluster_enable',
        'mongodb_replica_set': 'mongodb_replica_set',
        'encoding': 'encoding',
        'mysql_timeout': 'mysql_timeout',
        'trust_store_password': 'trust_store_password',
        'trust_store': 'trust_store',
        'trust_store_file_type': 'trust_store_file_type',
        'ssl_auth_method': 'ssl_auth_method',
        'key_store': 'key_store',
        'key_store_file_type': 'key_store_file_type',
        'key_store_password': 'key_store_password',
        'key_store_key_password': 'key_store_key_password',
        'dis_tunnel_name': 'dis_tunnel_name',
        'dis_data_type': 'dis_data_type',
        'dis_setting_type': 'dis_setting_type',
        'dis_endpoint': 'dis_endpoint',
        'dis_region': 'dis_region',
        'dis_source_project_id': 'dis_source_project_id',
        'hl7_position': 'hl7_position',
        'hl7_whitelist_enable': 'hl7_whitelist_enable',
        'hl7_whitelist': 'hl7_whitelist',
        'ldap_security_auth_type': 'ldap_security_auth_type',
        'rabbitmq_virtual_host': 'rabbitmq_virtual_host',
        'rabbitmq_ssl_protocol': 'rabbitmq_ssl_protocol',
        'sap_client': 'sap_client',
        'sap_sysnr': 'sap_sysnr',
        'snmp_network_protocol': 'snmp_network_protocol',
        'snmp_version': 'snmp_version',
        'snmp_community': 'snmp_community',
        'ibmmq_ccs_id': 'ibmmq_ccs_id',
        'ibmmq_queue_manager': 'ibmmq_queue_manager',
        'ibmmq_channel': 'ibmmq_channel',
        'ibmmq_cipher_suite': 'ibmmq_cipher_suite',
        'hdfs_path': 'hdfs_path',
        'principal_name': 'principal_name',
        'config_file_name': 'config_file_name',
        'config_file_content': 'config_file_content',
        'connection_instance_id': 'connection_instance_id',
        'connector_params': 'connector_params'
    }

    def __init__(self, gauss100_version=None, host=None, port=None, database_name=None, redis_database=None, user_name=None, password=None, mode=None, cdc_mode=None, multi_oracle_address=None, oracle_service_name=None, ftp_connect_mode=None, ftp_protocol=None, address=None, ak=None, sk=None, bucket_name=None, https=None, url=None, api_method=None, auth_method=None, api_auth_detail=None, broker=None, ssl=None, ssl_enable=None, ssl_username=None, ssl_password=None, mongodb_auth_source=None, mongodb_cluster_enable=None, mongodb_replica_set=None, encoding=None, mysql_timeout=None, trust_store_password=None, trust_store=None, trust_store_file_type=None, ssl_auth_method=None, key_store=None, key_store_file_type=None, key_store_password=None, key_store_key_password=None, dis_tunnel_name=None, dis_data_type=None, dis_setting_type=None, dis_endpoint=None, dis_region=None, dis_source_project_id=None, hl7_position=None, hl7_whitelist_enable=None, hl7_whitelist=None, ldap_security_auth_type=None, rabbitmq_virtual_host=None, rabbitmq_ssl_protocol=None, sap_client=None, sap_sysnr=None, snmp_network_protocol=None, snmp_version=None, snmp_community=None, ibmmq_ccs_id=None, ibmmq_queue_manager=None, ibmmq_channel=None, ibmmq_cipher_suite=None, hdfs_path=None, principal_name=None, config_file_name=None, config_file_content=None, connection_instance_id=None, connector_params=None):
        """Content

        The model defined in huaweicloud sdk

        :param gauss100_version: gauss100的版本号 - V100R003C20 - V300R001C00
        :type gauss100_version: str
        :param host: 主机IP地址 - 数据源为DWS、HANA、RABBITMQ、SAP、SNMP、IBMMQ类型时需要配置。 - 数据源为MYSQL、ORACLE、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ARTEMISMQ、POSTGRESQL、HIVE类型且mode为default时需要配置。 - 数据源为HL7类型且作为目标端（position为target）时需要配置。 - 初始值为空，配置任务启动后生成host
        :type host: str
        :param port: 端口，端口号为0到65535 - 数据源为DWS、HANA、RABBITMQ、SAP、SNMP、IBMMQ，obs类型时需要配置， - 数据源为MYSQL、ORACLE、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ARTEMISMQ、POSTGRESQL、HIVE类型且mode为default时需要配置， - 数据源为HL7类型且作为目标端（position为target）时需要配置
        :type port: str
        :param database_name: 数据库名称 - 数据源为DWS、HANA、RABBITMQ、SAP、SNMP、IBMMQ，obs类型时需要配置， - 数据源为MYSQL、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ARTEMISMQ、POSTGRESQL、HIVE类型且mode为default时需要配置， - 数据源为ORACLE类型且mode为（default、multiAddress）时需要配置
        :type database_name: str
        :param redis_database: REDIS数据源类型配置，数据库编号, 纯数字编码
        :type redis_database: str
        :param user_name: 访问服务的用户名 - 数据源为MYSQL、DWS、FTP、ORACLE、MONGODB、HANA、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ACTIVEMQ、ARTEMISMQ、POSTGRESQL、RABBITMQ、SAP、IBMMQ、HIVE类型时需要配置 - 数据源为WEBSOCKET类型，认证方式（basicauth）时需要配置 - 数据源为LDAP，安全认证类型（security_auth_type）为simple时需要配置
        :type user_name: str
        :param password: 访问服务的密码 - 数据源为MYSQL、DWS、FTP、ORACLE、MONGODB、HANA、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ACTIVEMQ、ARTEMISMQ、POSTGRESQL、RABBITMQ、SAP、IBMMQ、HIVE类型时需要配置 - 数据源为WEBSOCKET，且认证方式（basicauth）时需要配置 - 数据源为LDAP，且安全认证类型（security_auth_type）为simple时需要配置
        :type password: str
        :param mode: 数据源连接模式 - 数据源为DWS、MONGODB、REDIS、HANA时配置默认， - 数据源为MYSQL、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、POSTGRESQL、HIVE时配置（default,professional）， - 数据源为ORACLE时配置专有的模式multiAddress - default (默认模式) - professional (专业模式) - multiAddress (多地址)
        :type mode: str
        :param cdc_mode: cdc模式，只有组合任务使用
        :type cdc_mode: str
        :param multi_oracle_address: ORACLE集群地址，当mode为multiAddress时需要配置
        :type multi_oracle_address: list[:class:`huaweicloudsdkroma.v2.MultiOracleAddress`]
        :param oracle_service_name: ORACLE集群服务名
        :type oracle_service_name: str
        :param ftp_connect_mode: 访问FTP服务的连接模式 - active (主动模式) - passive (被动模式)
        :type ftp_connect_mode: str
        :param ftp_protocol: 访问FTP服务协议类型 - sftp - ftp
        :type ftp_protocol: str
        :param address: 地址 - OBS (obs远端地址，obs数据源使用) - MONGODB (MONGODB数据源类型主机IP地址，多个IP:PORT, 使用\&quot;,\&quot;隔开) - REDIS (redis服务地址，多个IP:PORT, 使用\&quot;,\&quot;隔开)
        :type address: str
        :param ak: Access Key ID - 数据源为OBS，DIS类型时需要配置
        :type ak: str
        :param sk: Secret Access Key - 数据源为OBS，DIS类型时需要配置
        :type sk: str
        :param bucket_name: 桶名称，数据源为OBS时需要配置
        :type bucket_name: str
        :param https: 是否使用https, 数据源为OBS时需要配置，一般默认使用
        :type https: bool
        :param url: 连接字符串，访问url - 数据源为API、LDAP、WEBSOCKE类型时需要配置， - 数据源为MYSQL、ORACLE、DB2、GAUSS200、GAUSS100、TAURUS、POSTGRESQL，且mode配置为professional专业时需要配置
        :type url: str
        :param api_method: 访问API请求方式 - POST - PUT - DELETE - PATCH - GET
        :type api_method: str
        :param auth_method: 访问WEBSOCKET服务的认证方式 - none - basicauth
        :type auth_method: str
        :param api_auth_detail: 
        :type api_auth_detail: :class:`huaweicloudsdkroma.v2.ApiAuthDetail`
        :param broker: KAFKA、ACTIVEMQ的服务器地址，多个IP:PORT, 使用\&quot;,\&quot;分隔
        :type broker: str
        :param ssl: 是否开启SSL认证 - 连接MQS内网地址时，若MQS开启了SSL，请选择“是”
        :type ssl: bool
        :param ssl_enable: 是否开启SSL认证 - 数据源为KAFKA时需要配置，连接MQS内网地址时，若MQS同时开启了SSL与VPC内网明文访问，请选择“否” - 数据源为ARTEMISMQ、ACTIVEMQ、RABBITMQ、IBMMQ时需要配置， - 数据源为HL7时且作为源端时需要配置
        :type ssl_enable: bool
        :param ssl_username: SSL用户名/应用Key - 数据源为KAFKA且开启SSL认证时需要配置
        :type ssl_username: str
        :param ssl_password: SSL密码/应用Secret - 数据源为KAFKA且开启SSL认证时需要配置
        :type ssl_password: str
        :param mongodb_auth_source: MONGODB认证源
        :type mongodb_auth_source: str
        :param mongodb_cluster_enable: MONGODB集群模式 - true (集群模式) - false （非集群模式）
        :type mongodb_cluster_enable: bool
        :param mongodb_replica_set: MONGODB副本集 当MONGODB为非集群模式时配置
        :type mongodb_replica_set: str
        :param encoding: 编码格式 - 数据源为GAUSS200、GAUSS100、POSTGRESQL类型时配置\&quot;big5\&quot;， - 数据源为MYSQL、TAURUS类型且mode为default时配置
        :type encoding: str
        :param mysql_timeout: MYSQL连接超时时间（秒）
        :type mysql_timeout: int
        :param trust_store_password: 公钥库密码 - 数据源类型为ACTIVEMQ、ARTEMISMQ、RABBITMQ、IBMMQ且开启SSL认证时需要配置 - 数据源类为HL7且HL7为目标端（position为target）时，并且开启SSL认证时需要配置
        :type trust_store_password: str
        :param trust_store: - 数据源类型为ACTIVEMQ、ARTEMISMQ、RABBITMQ、IBMMQ且开启SSL认证时需要配置，公钥库密码 - 数据源类型为HL7且为目标端（position为target），并且开启SSL认证时需要配置，公钥库密码
        :type trust_store: str
        :param trust_store_file_type: - 数据源类型为ACTIVEMQ、ARTEMISMQ、RABBITMQ、IBMMQ且开启SSL认证时需要配置，公钥库密码 - 数据源类型为HL7且为目标端（position为target），并且开启SSL认证时需要配置，公钥库密码
        :type trust_store_file_type: str
        :param ssl_auth_method: 数据源类型为ACTIVEMQ、ARTEMISMQ且开启SSL认证时需要配置 - one-way (单向认证) - two-way (双向认证)
        :type ssl_auth_method: str
        :param key_store: 私钥库文件内容， - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置 - 数据源类型HL7且为源端（position为source），并且开启SSL认证时需要配置
        :type key_store: str
        :param key_store_file_type: 私钥库文件类型 - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置
        :type key_store_file_type: str
        :param key_store_password: 私钥库密码 - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置 - 数据源为HL7类型，为源端（position为source）并且开启SSL认证时需要配置
        :type key_store_password: str
        :param key_store_key_password: 私钥库私钥密码 - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置 - 数据源为HL7类型，为源端（position为source）并且开启SSL认证时需要配置
        :type key_store_key_password: str
        :param dis_tunnel_name: DIS通道名称
        :type dis_tunnel_name: str
        :param dis_data_type: DIS数据类别 - JSON
        :type dis_data_type: str
        :param dis_setting_type: DIS配置类别 - senior (高级) - basic (基础)
        :type dis_setting_type: str
        :param dis_endpoint: DIS Endpoint，当setting_type为senior时填写
        :type dis_endpoint: str
        :param dis_region: DIS Region，当setting_type为senior时填写
        :type dis_region: str
        :param dis_source_project_id: DIS源端项目id，当setting_type为senior时填写
        :type dis_source_project_id: str
        :param hl7_position: HL7数据源方向 - source (源端) - target (目标端)
        :type hl7_position: str
        :param hl7_whitelist_enable: HL7是否开启白名单设置
        :type hl7_whitelist_enable: bool
        :param hl7_whitelist: HL7白名单 - 允许同步数据到源端HL7的服务器地址，当HL7为源端（position为source）并且开启白名单设置(open_whitelist为true)时填写
        :type hl7_whitelist: str
        :param ldap_security_auth_type: LDAP安全认证类型
        :type ldap_security_auth_type: str
        :param rabbitmq_virtual_host: RABBITMQ虚拟主机
        :type rabbitmq_virtual_host: str
        :param rabbitmq_ssl_protocol: RABBITMQ SSL认证协议 - TLS
        :type rabbitmq_ssl_protocol: str
        :param sap_client: SAP客户端号
        :type sap_client: str
        :param sap_sysnr: SAP实例编号
        :type sap_sysnr: str
        :param snmp_network_protocol: SNMP网络协议 - udp - tcp
        :type snmp_network_protocol: str
        :param snmp_version: SNMP版本号
        :type snmp_version: int
        :param snmp_community: SNMP团体名，用于访问SNMP管理代理的身份认证，相当于访问密码
        :type snmp_community: str
        :param ibmmq_ccs_id: IBMMQ字符集标识
        :type ibmmq_ccs_id: str
        :param ibmmq_queue_manager: IBMMQ队列管理器
        :type ibmmq_queue_manager: str
        :param ibmmq_channel: IBMMQ通道名称
        :type ibmmq_channel: str
        :param ibmmq_cipher_suite: IBMMQ密钥算法套件
        :type ibmmq_cipher_suite: str
        :param hdfs_path: HDFS URL - 数据源为MRSHIVE、MRSHDFS、FIHDFS、FIHIVE类型时配置 - fihadfs (/fdi/autotest)
        :type hdfs_path: str
        :param principal_name: 机机交互用户名 - 数据源为MRSHIVE、MRSHDFS、MRSHBASE、MRSKAFKA、FIHDFS、FIHIVE、FIKAFKA类型时配置
        :type principal_name: str
        :param config_file_name: - 用户认证文件，文件获取方式参考《ROMA Connect API参考》的“附录&gt;获取数据源配置文件”章节 - 将获取到的文件打包成zip文件，文件名配置在config_file_name中，内容以BASE64编码形式放到config_file_content。 - 数据源为MRSHIVE、MRSHDFS、MRSHBASE、MRSKAFKA、FIHDFS、FIHIVE、FIKAFKA类型时配置
        :type config_file_name: str
        :param config_file_content: - 用户认证文件内容，config_file_name对应的文件内容BASE64编码 - 数据源为MRSHIVE、MRSHDFS、MRSHBASE、MRSKAFKA、FIHDFS、FIHIVE、FIKAFKA类型时配置
        :type config_file_content: str
        :param connection_instance_id: 连接器实例ID，连接器发布后对应的实例ID
        :type connection_instance_id: str
        :param connector_params: 连接器对应的数据源参数，值按实际填写
        :type connector_params: object
        """
        
        

        self._gauss100_version = None
        self._host = None
        self._port = None
        self._database_name = None
        self._redis_database = None
        self._user_name = None
        self._password = None
        self._mode = None
        self._cdc_mode = None
        self._multi_oracle_address = None
        self._oracle_service_name = None
        self._ftp_connect_mode = None
        self._ftp_protocol = None
        self._address = None
        self._ak = None
        self._sk = None
        self._bucket_name = None
        self._https = None
        self._url = None
        self._api_method = None
        self._auth_method = None
        self._api_auth_detail = None
        self._broker = None
        self._ssl = None
        self._ssl_enable = None
        self._ssl_username = None
        self._ssl_password = None
        self._mongodb_auth_source = None
        self._mongodb_cluster_enable = None
        self._mongodb_replica_set = None
        self._encoding = None
        self._mysql_timeout = None
        self._trust_store_password = None
        self._trust_store = None
        self._trust_store_file_type = None
        self._ssl_auth_method = None
        self._key_store = None
        self._key_store_file_type = None
        self._key_store_password = None
        self._key_store_key_password = None
        self._dis_tunnel_name = None
        self._dis_data_type = None
        self._dis_setting_type = None
        self._dis_endpoint = None
        self._dis_region = None
        self._dis_source_project_id = None
        self._hl7_position = None
        self._hl7_whitelist_enable = None
        self._hl7_whitelist = None
        self._ldap_security_auth_type = None
        self._rabbitmq_virtual_host = None
        self._rabbitmq_ssl_protocol = None
        self._sap_client = None
        self._sap_sysnr = None
        self._snmp_network_protocol = None
        self._snmp_version = None
        self._snmp_community = None
        self._ibmmq_ccs_id = None
        self._ibmmq_queue_manager = None
        self._ibmmq_channel = None
        self._ibmmq_cipher_suite = None
        self._hdfs_path = None
        self._principal_name = None
        self._config_file_name = None
        self._config_file_content = None
        self._connection_instance_id = None
        self._connector_params = None
        self.discriminator = None

        if gauss100_version is not None:
            self.gauss100_version = gauss100_version
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if database_name is not None:
            self.database_name = database_name
        if redis_database is not None:
            self.redis_database = redis_database
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
        if mode is not None:
            self.mode = mode
        if cdc_mode is not None:
            self.cdc_mode = cdc_mode
        if multi_oracle_address is not None:
            self.multi_oracle_address = multi_oracle_address
        if oracle_service_name is not None:
            self.oracle_service_name = oracle_service_name
        if ftp_connect_mode is not None:
            self.ftp_connect_mode = ftp_connect_mode
        if ftp_protocol is not None:
            self.ftp_protocol = ftp_protocol
        if address is not None:
            self.address = address
        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if https is not None:
            self.https = https
        if url is not None:
            self.url = url
        if api_method is not None:
            self.api_method = api_method
        if auth_method is not None:
            self.auth_method = auth_method
        if api_auth_detail is not None:
            self.api_auth_detail = api_auth_detail
        if broker is not None:
            self.broker = broker
        if ssl is not None:
            self.ssl = ssl
        if ssl_enable is not None:
            self.ssl_enable = ssl_enable
        if ssl_username is not None:
            self.ssl_username = ssl_username
        if ssl_password is not None:
            self.ssl_password = ssl_password
        if mongodb_auth_source is not None:
            self.mongodb_auth_source = mongodb_auth_source
        if mongodb_cluster_enable is not None:
            self.mongodb_cluster_enable = mongodb_cluster_enable
        if mongodb_replica_set is not None:
            self.mongodb_replica_set = mongodb_replica_set
        if encoding is not None:
            self.encoding = encoding
        if mysql_timeout is not None:
            self.mysql_timeout = mysql_timeout
        if trust_store_password is not None:
            self.trust_store_password = trust_store_password
        if trust_store is not None:
            self.trust_store = trust_store
        if trust_store_file_type is not None:
            self.trust_store_file_type = trust_store_file_type
        if ssl_auth_method is not None:
            self.ssl_auth_method = ssl_auth_method
        if key_store is not None:
            self.key_store = key_store
        if key_store_file_type is not None:
            self.key_store_file_type = key_store_file_type
        if key_store_password is not None:
            self.key_store_password = key_store_password
        if key_store_key_password is not None:
            self.key_store_key_password = key_store_key_password
        if dis_tunnel_name is not None:
            self.dis_tunnel_name = dis_tunnel_name
        if dis_data_type is not None:
            self.dis_data_type = dis_data_type
        if dis_setting_type is not None:
            self.dis_setting_type = dis_setting_type
        if dis_endpoint is not None:
            self.dis_endpoint = dis_endpoint
        if dis_region is not None:
            self.dis_region = dis_region
        if dis_source_project_id is not None:
            self.dis_source_project_id = dis_source_project_id
        if hl7_position is not None:
            self.hl7_position = hl7_position
        if hl7_whitelist_enable is not None:
            self.hl7_whitelist_enable = hl7_whitelist_enable
        if hl7_whitelist is not None:
            self.hl7_whitelist = hl7_whitelist
        if ldap_security_auth_type is not None:
            self.ldap_security_auth_type = ldap_security_auth_type
        if rabbitmq_virtual_host is not None:
            self.rabbitmq_virtual_host = rabbitmq_virtual_host
        if rabbitmq_ssl_protocol is not None:
            self.rabbitmq_ssl_protocol = rabbitmq_ssl_protocol
        if sap_client is not None:
            self.sap_client = sap_client
        if sap_sysnr is not None:
            self.sap_sysnr = sap_sysnr
        if snmp_network_protocol is not None:
            self.snmp_network_protocol = snmp_network_protocol
        if snmp_version is not None:
            self.snmp_version = snmp_version
        if snmp_community is not None:
            self.snmp_community = snmp_community
        if ibmmq_ccs_id is not None:
            self.ibmmq_ccs_id = ibmmq_ccs_id
        if ibmmq_queue_manager is not None:
            self.ibmmq_queue_manager = ibmmq_queue_manager
        if ibmmq_channel is not None:
            self.ibmmq_channel = ibmmq_channel
        if ibmmq_cipher_suite is not None:
            self.ibmmq_cipher_suite = ibmmq_cipher_suite
        if hdfs_path is not None:
            self.hdfs_path = hdfs_path
        if principal_name is not None:
            self.principal_name = principal_name
        if config_file_name is not None:
            self.config_file_name = config_file_name
        if config_file_content is not None:
            self.config_file_content = config_file_content
        if connection_instance_id is not None:
            self.connection_instance_id = connection_instance_id
        if connector_params is not None:
            self.connector_params = connector_params

    @property
    def gauss100_version(self):
        """Gets the gauss100_version of this Content.

        gauss100的版本号 - V100R003C20 - V300R001C00

        :return: The gauss100_version of this Content.
        :rtype: str
        """
        return self._gauss100_version

    @gauss100_version.setter
    def gauss100_version(self, gauss100_version):
        """Sets the gauss100_version of this Content.

        gauss100的版本号 - V100R003C20 - V300R001C00

        :param gauss100_version: The gauss100_version of this Content.
        :type gauss100_version: str
        """
        self._gauss100_version = gauss100_version

    @property
    def host(self):
        """Gets the host of this Content.

        主机IP地址 - 数据源为DWS、HANA、RABBITMQ、SAP、SNMP、IBMMQ类型时需要配置。 - 数据源为MYSQL、ORACLE、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ARTEMISMQ、POSTGRESQL、HIVE类型且mode为default时需要配置。 - 数据源为HL7类型且作为目标端（position为target）时需要配置。 - 初始值为空，配置任务启动后生成host

        :return: The host of this Content.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Content.

        主机IP地址 - 数据源为DWS、HANA、RABBITMQ、SAP、SNMP、IBMMQ类型时需要配置。 - 数据源为MYSQL、ORACLE、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ARTEMISMQ、POSTGRESQL、HIVE类型且mode为default时需要配置。 - 数据源为HL7类型且作为目标端（position为target）时需要配置。 - 初始值为空，配置任务启动后生成host

        :param host: The host of this Content.
        :type host: str
        """
        self._host = host

    @property
    def port(self):
        """Gets the port of this Content.

        端口，端口号为0到65535 - 数据源为DWS、HANA、RABBITMQ、SAP、SNMP、IBMMQ，obs类型时需要配置， - 数据源为MYSQL、ORACLE、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ARTEMISMQ、POSTGRESQL、HIVE类型且mode为default时需要配置， - 数据源为HL7类型且作为目标端（position为target）时需要配置

        :return: The port of this Content.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Content.

        端口，端口号为0到65535 - 数据源为DWS、HANA、RABBITMQ、SAP、SNMP、IBMMQ，obs类型时需要配置， - 数据源为MYSQL、ORACLE、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ARTEMISMQ、POSTGRESQL、HIVE类型且mode为default时需要配置， - 数据源为HL7类型且作为目标端（position为target）时需要配置

        :param port: The port of this Content.
        :type port: str
        """
        self._port = port

    @property
    def database_name(self):
        """Gets the database_name of this Content.

        数据库名称 - 数据源为DWS、HANA、RABBITMQ、SAP、SNMP、IBMMQ，obs类型时需要配置， - 数据源为MYSQL、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ARTEMISMQ、POSTGRESQL、HIVE类型且mode为default时需要配置， - 数据源为ORACLE类型且mode为（default、multiAddress）时需要配置

        :return: The database_name of this Content.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this Content.

        数据库名称 - 数据源为DWS、HANA、RABBITMQ、SAP、SNMP、IBMMQ，obs类型时需要配置， - 数据源为MYSQL、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ARTEMISMQ、POSTGRESQL、HIVE类型且mode为default时需要配置， - 数据源为ORACLE类型且mode为（default、multiAddress）时需要配置

        :param database_name: The database_name of this Content.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def redis_database(self):
        """Gets the redis_database of this Content.

        REDIS数据源类型配置，数据库编号, 纯数字编码

        :return: The redis_database of this Content.
        :rtype: str
        """
        return self._redis_database

    @redis_database.setter
    def redis_database(self, redis_database):
        """Sets the redis_database of this Content.

        REDIS数据源类型配置，数据库编号, 纯数字编码

        :param redis_database: The redis_database of this Content.
        :type redis_database: str
        """
        self._redis_database = redis_database

    @property
    def user_name(self):
        """Gets the user_name of this Content.

        访问服务的用户名 - 数据源为MYSQL、DWS、FTP、ORACLE、MONGODB、HANA、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ACTIVEMQ、ARTEMISMQ、POSTGRESQL、RABBITMQ、SAP、IBMMQ、HIVE类型时需要配置 - 数据源为WEBSOCKET类型，认证方式（basicauth）时需要配置 - 数据源为LDAP，安全认证类型（security_auth_type）为simple时需要配置

        :return: The user_name of this Content.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this Content.

        访问服务的用户名 - 数据源为MYSQL、DWS、FTP、ORACLE、MONGODB、HANA、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ACTIVEMQ、ARTEMISMQ、POSTGRESQL、RABBITMQ、SAP、IBMMQ、HIVE类型时需要配置 - 数据源为WEBSOCKET类型，认证方式（basicauth）时需要配置 - 数据源为LDAP，安全认证类型（security_auth_type）为simple时需要配置

        :param user_name: The user_name of this Content.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this Content.

        访问服务的密码 - 数据源为MYSQL、DWS、FTP、ORACLE、MONGODB、HANA、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ACTIVEMQ、ARTEMISMQ、POSTGRESQL、RABBITMQ、SAP、IBMMQ、HIVE类型时需要配置 - 数据源为WEBSOCKET，且认证方式（basicauth）时需要配置 - 数据源为LDAP，且安全认证类型（security_auth_type）为simple时需要配置

        :return: The password of this Content.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Content.

        访问服务的密码 - 数据源为MYSQL、DWS、FTP、ORACLE、MONGODB、HANA、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、ACTIVEMQ、ARTEMISMQ、POSTGRESQL、RABBITMQ、SAP、IBMMQ、HIVE类型时需要配置 - 数据源为WEBSOCKET，且认证方式（basicauth）时需要配置 - 数据源为LDAP，且安全认证类型（security_auth_type）为simple时需要配置

        :param password: The password of this Content.
        :type password: str
        """
        self._password = password

    @property
    def mode(self):
        """Gets the mode of this Content.

        数据源连接模式 - 数据源为DWS、MONGODB、REDIS、HANA时配置默认， - 数据源为MYSQL、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、POSTGRESQL、HIVE时配置（default,professional）， - 数据源为ORACLE时配置专有的模式multiAddress - default (默认模式) - professional (专业模式) - multiAddress (多地址)

        :return: The mode of this Content.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Content.

        数据源连接模式 - 数据源为DWS、MONGODB、REDIS、HANA时配置默认， - 数据源为MYSQL、SQLSERVER、DB2、GAUSS200、GAUSS100、TAURUS、POSTGRESQL、HIVE时配置（default,professional）， - 数据源为ORACLE时配置专有的模式multiAddress - default (默认模式) - professional (专业模式) - multiAddress (多地址)

        :param mode: The mode of this Content.
        :type mode: str
        """
        self._mode = mode

    @property
    def cdc_mode(self):
        """Gets the cdc_mode of this Content.

        cdc模式，只有组合任务使用

        :return: The cdc_mode of this Content.
        :rtype: str
        """
        return self._cdc_mode

    @cdc_mode.setter
    def cdc_mode(self, cdc_mode):
        """Sets the cdc_mode of this Content.

        cdc模式，只有组合任务使用

        :param cdc_mode: The cdc_mode of this Content.
        :type cdc_mode: str
        """
        self._cdc_mode = cdc_mode

    @property
    def multi_oracle_address(self):
        """Gets the multi_oracle_address of this Content.

        ORACLE集群地址，当mode为multiAddress时需要配置

        :return: The multi_oracle_address of this Content.
        :rtype: list[:class:`huaweicloudsdkroma.v2.MultiOracleAddress`]
        """
        return self._multi_oracle_address

    @multi_oracle_address.setter
    def multi_oracle_address(self, multi_oracle_address):
        """Sets the multi_oracle_address of this Content.

        ORACLE集群地址，当mode为multiAddress时需要配置

        :param multi_oracle_address: The multi_oracle_address of this Content.
        :type multi_oracle_address: list[:class:`huaweicloudsdkroma.v2.MultiOracleAddress`]
        """
        self._multi_oracle_address = multi_oracle_address

    @property
    def oracle_service_name(self):
        """Gets the oracle_service_name of this Content.

        ORACLE集群服务名

        :return: The oracle_service_name of this Content.
        :rtype: str
        """
        return self._oracle_service_name

    @oracle_service_name.setter
    def oracle_service_name(self, oracle_service_name):
        """Sets the oracle_service_name of this Content.

        ORACLE集群服务名

        :param oracle_service_name: The oracle_service_name of this Content.
        :type oracle_service_name: str
        """
        self._oracle_service_name = oracle_service_name

    @property
    def ftp_connect_mode(self):
        """Gets the ftp_connect_mode of this Content.

        访问FTP服务的连接模式 - active (主动模式) - passive (被动模式)

        :return: The ftp_connect_mode of this Content.
        :rtype: str
        """
        return self._ftp_connect_mode

    @ftp_connect_mode.setter
    def ftp_connect_mode(self, ftp_connect_mode):
        """Sets the ftp_connect_mode of this Content.

        访问FTP服务的连接模式 - active (主动模式) - passive (被动模式)

        :param ftp_connect_mode: The ftp_connect_mode of this Content.
        :type ftp_connect_mode: str
        """
        self._ftp_connect_mode = ftp_connect_mode

    @property
    def ftp_protocol(self):
        """Gets the ftp_protocol of this Content.

        访问FTP服务协议类型 - sftp - ftp

        :return: The ftp_protocol of this Content.
        :rtype: str
        """
        return self._ftp_protocol

    @ftp_protocol.setter
    def ftp_protocol(self, ftp_protocol):
        """Sets the ftp_protocol of this Content.

        访问FTP服务协议类型 - sftp - ftp

        :param ftp_protocol: The ftp_protocol of this Content.
        :type ftp_protocol: str
        """
        self._ftp_protocol = ftp_protocol

    @property
    def address(self):
        """Gets the address of this Content.

        地址 - OBS (obs远端地址，obs数据源使用) - MONGODB (MONGODB数据源类型主机IP地址，多个IP:PORT, 使用\",\"隔开) - REDIS (redis服务地址，多个IP:PORT, 使用\",\"隔开)

        :return: The address of this Content.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Content.

        地址 - OBS (obs远端地址，obs数据源使用) - MONGODB (MONGODB数据源类型主机IP地址，多个IP:PORT, 使用\",\"隔开) - REDIS (redis服务地址，多个IP:PORT, 使用\",\"隔开)

        :param address: The address of this Content.
        :type address: str
        """
        self._address = address

    @property
    def ak(self):
        """Gets the ak of this Content.

        Access Key ID - 数据源为OBS，DIS类型时需要配置

        :return: The ak of this Content.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this Content.

        Access Key ID - 数据源为OBS，DIS类型时需要配置

        :param ak: The ak of this Content.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this Content.

        Secret Access Key - 数据源为OBS，DIS类型时需要配置

        :return: The sk of this Content.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this Content.

        Secret Access Key - 数据源为OBS，DIS类型时需要配置

        :param sk: The sk of this Content.
        :type sk: str
        """
        self._sk = sk

    @property
    def bucket_name(self):
        """Gets the bucket_name of this Content.

        桶名称，数据源为OBS时需要配置

        :return: The bucket_name of this Content.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this Content.

        桶名称，数据源为OBS时需要配置

        :param bucket_name: The bucket_name of this Content.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def https(self):
        """Gets the https of this Content.

        是否使用https, 数据源为OBS时需要配置，一般默认使用

        :return: The https of this Content.
        :rtype: bool
        """
        return self._https

    @https.setter
    def https(self, https):
        """Sets the https of this Content.

        是否使用https, 数据源为OBS时需要配置，一般默认使用

        :param https: The https of this Content.
        :type https: bool
        """
        self._https = https

    @property
    def url(self):
        """Gets the url of this Content.

        连接字符串，访问url - 数据源为API、LDAP、WEBSOCKE类型时需要配置， - 数据源为MYSQL、ORACLE、DB2、GAUSS200、GAUSS100、TAURUS、POSTGRESQL，且mode配置为professional专业时需要配置

        :return: The url of this Content.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Content.

        连接字符串，访问url - 数据源为API、LDAP、WEBSOCKE类型时需要配置， - 数据源为MYSQL、ORACLE、DB2、GAUSS200、GAUSS100、TAURUS、POSTGRESQL，且mode配置为professional专业时需要配置

        :param url: The url of this Content.
        :type url: str
        """
        self._url = url

    @property
    def api_method(self):
        """Gets the api_method of this Content.

        访问API请求方式 - POST - PUT - DELETE - PATCH - GET

        :return: The api_method of this Content.
        :rtype: str
        """
        return self._api_method

    @api_method.setter
    def api_method(self, api_method):
        """Sets the api_method of this Content.

        访问API请求方式 - POST - PUT - DELETE - PATCH - GET

        :param api_method: The api_method of this Content.
        :type api_method: str
        """
        self._api_method = api_method

    @property
    def auth_method(self):
        """Gets the auth_method of this Content.

        访问WEBSOCKET服务的认证方式 - none - basicauth

        :return: The auth_method of this Content.
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this Content.

        访问WEBSOCKET服务的认证方式 - none - basicauth

        :param auth_method: The auth_method of this Content.
        :type auth_method: str
        """
        self._auth_method = auth_method

    @property
    def api_auth_detail(self):
        """Gets the api_auth_detail of this Content.

        :return: The api_auth_detail of this Content.
        :rtype: :class:`huaweicloudsdkroma.v2.ApiAuthDetail`
        """
        return self._api_auth_detail

    @api_auth_detail.setter
    def api_auth_detail(self, api_auth_detail):
        """Sets the api_auth_detail of this Content.

        :param api_auth_detail: The api_auth_detail of this Content.
        :type api_auth_detail: :class:`huaweicloudsdkroma.v2.ApiAuthDetail`
        """
        self._api_auth_detail = api_auth_detail

    @property
    def broker(self):
        """Gets the broker of this Content.

        KAFKA、ACTIVEMQ的服务器地址，多个IP:PORT, 使用\",\"分隔

        :return: The broker of this Content.
        :rtype: str
        """
        return self._broker

    @broker.setter
    def broker(self, broker):
        """Sets the broker of this Content.

        KAFKA、ACTIVEMQ的服务器地址，多个IP:PORT, 使用\",\"分隔

        :param broker: The broker of this Content.
        :type broker: str
        """
        self._broker = broker

    @property
    def ssl(self):
        """Gets the ssl of this Content.

        是否开启SSL认证 - 连接MQS内网地址时，若MQS开启了SSL，请选择“是”

        :return: The ssl of this Content.
        :rtype: bool
        """
        return self._ssl

    @ssl.setter
    def ssl(self, ssl):
        """Sets the ssl of this Content.

        是否开启SSL认证 - 连接MQS内网地址时，若MQS开启了SSL，请选择“是”

        :param ssl: The ssl of this Content.
        :type ssl: bool
        """
        self._ssl = ssl

    @property
    def ssl_enable(self):
        """Gets the ssl_enable of this Content.

        是否开启SSL认证 - 数据源为KAFKA时需要配置，连接MQS内网地址时，若MQS同时开启了SSL与VPC内网明文访问，请选择“否” - 数据源为ARTEMISMQ、ACTIVEMQ、RABBITMQ、IBMMQ时需要配置， - 数据源为HL7时且作为源端时需要配置

        :return: The ssl_enable of this Content.
        :rtype: bool
        """
        return self._ssl_enable

    @ssl_enable.setter
    def ssl_enable(self, ssl_enable):
        """Sets the ssl_enable of this Content.

        是否开启SSL认证 - 数据源为KAFKA时需要配置，连接MQS内网地址时，若MQS同时开启了SSL与VPC内网明文访问，请选择“否” - 数据源为ARTEMISMQ、ACTIVEMQ、RABBITMQ、IBMMQ时需要配置， - 数据源为HL7时且作为源端时需要配置

        :param ssl_enable: The ssl_enable of this Content.
        :type ssl_enable: bool
        """
        self._ssl_enable = ssl_enable

    @property
    def ssl_username(self):
        """Gets the ssl_username of this Content.

        SSL用户名/应用Key - 数据源为KAFKA且开启SSL认证时需要配置

        :return: The ssl_username of this Content.
        :rtype: str
        """
        return self._ssl_username

    @ssl_username.setter
    def ssl_username(self, ssl_username):
        """Sets the ssl_username of this Content.

        SSL用户名/应用Key - 数据源为KAFKA且开启SSL认证时需要配置

        :param ssl_username: The ssl_username of this Content.
        :type ssl_username: str
        """
        self._ssl_username = ssl_username

    @property
    def ssl_password(self):
        """Gets the ssl_password of this Content.

        SSL密码/应用Secret - 数据源为KAFKA且开启SSL认证时需要配置

        :return: The ssl_password of this Content.
        :rtype: str
        """
        return self._ssl_password

    @ssl_password.setter
    def ssl_password(self, ssl_password):
        """Sets the ssl_password of this Content.

        SSL密码/应用Secret - 数据源为KAFKA且开启SSL认证时需要配置

        :param ssl_password: The ssl_password of this Content.
        :type ssl_password: str
        """
        self._ssl_password = ssl_password

    @property
    def mongodb_auth_source(self):
        """Gets the mongodb_auth_source of this Content.

        MONGODB认证源

        :return: The mongodb_auth_source of this Content.
        :rtype: str
        """
        return self._mongodb_auth_source

    @mongodb_auth_source.setter
    def mongodb_auth_source(self, mongodb_auth_source):
        """Sets the mongodb_auth_source of this Content.

        MONGODB认证源

        :param mongodb_auth_source: The mongodb_auth_source of this Content.
        :type mongodb_auth_source: str
        """
        self._mongodb_auth_source = mongodb_auth_source

    @property
    def mongodb_cluster_enable(self):
        """Gets the mongodb_cluster_enable of this Content.

        MONGODB集群模式 - true (集群模式) - false （非集群模式）

        :return: The mongodb_cluster_enable of this Content.
        :rtype: bool
        """
        return self._mongodb_cluster_enable

    @mongodb_cluster_enable.setter
    def mongodb_cluster_enable(self, mongodb_cluster_enable):
        """Sets the mongodb_cluster_enable of this Content.

        MONGODB集群模式 - true (集群模式) - false （非集群模式）

        :param mongodb_cluster_enable: The mongodb_cluster_enable of this Content.
        :type mongodb_cluster_enable: bool
        """
        self._mongodb_cluster_enable = mongodb_cluster_enable

    @property
    def mongodb_replica_set(self):
        """Gets the mongodb_replica_set of this Content.

        MONGODB副本集 当MONGODB为非集群模式时配置

        :return: The mongodb_replica_set of this Content.
        :rtype: str
        """
        return self._mongodb_replica_set

    @mongodb_replica_set.setter
    def mongodb_replica_set(self, mongodb_replica_set):
        """Sets the mongodb_replica_set of this Content.

        MONGODB副本集 当MONGODB为非集群模式时配置

        :param mongodb_replica_set: The mongodb_replica_set of this Content.
        :type mongodb_replica_set: str
        """
        self._mongodb_replica_set = mongodb_replica_set

    @property
    def encoding(self):
        """Gets the encoding of this Content.

        编码格式 - 数据源为GAUSS200、GAUSS100、POSTGRESQL类型时配置\"big5\"， - 数据源为MYSQL、TAURUS类型且mode为default时配置

        :return: The encoding of this Content.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this Content.

        编码格式 - 数据源为GAUSS200、GAUSS100、POSTGRESQL类型时配置\"big5\"， - 数据源为MYSQL、TAURUS类型且mode为default时配置

        :param encoding: The encoding of this Content.
        :type encoding: str
        """
        self._encoding = encoding

    @property
    def mysql_timeout(self):
        """Gets the mysql_timeout of this Content.

        MYSQL连接超时时间（秒）

        :return: The mysql_timeout of this Content.
        :rtype: int
        """
        return self._mysql_timeout

    @mysql_timeout.setter
    def mysql_timeout(self, mysql_timeout):
        """Sets the mysql_timeout of this Content.

        MYSQL连接超时时间（秒）

        :param mysql_timeout: The mysql_timeout of this Content.
        :type mysql_timeout: int
        """
        self._mysql_timeout = mysql_timeout

    @property
    def trust_store_password(self):
        """Gets the trust_store_password of this Content.

        公钥库密码 - 数据源类型为ACTIVEMQ、ARTEMISMQ、RABBITMQ、IBMMQ且开启SSL认证时需要配置 - 数据源类为HL7且HL7为目标端（position为target）时，并且开启SSL认证时需要配置

        :return: The trust_store_password of this Content.
        :rtype: str
        """
        return self._trust_store_password

    @trust_store_password.setter
    def trust_store_password(self, trust_store_password):
        """Sets the trust_store_password of this Content.

        公钥库密码 - 数据源类型为ACTIVEMQ、ARTEMISMQ、RABBITMQ、IBMMQ且开启SSL认证时需要配置 - 数据源类为HL7且HL7为目标端（position为target）时，并且开启SSL认证时需要配置

        :param trust_store_password: The trust_store_password of this Content.
        :type trust_store_password: str
        """
        self._trust_store_password = trust_store_password

    @property
    def trust_store(self):
        """Gets the trust_store of this Content.

        - 数据源类型为ACTIVEMQ、ARTEMISMQ、RABBITMQ、IBMMQ且开启SSL认证时需要配置，公钥库密码 - 数据源类型为HL7且为目标端（position为target），并且开启SSL认证时需要配置，公钥库密码

        :return: The trust_store of this Content.
        :rtype: str
        """
        return self._trust_store

    @trust_store.setter
    def trust_store(self, trust_store):
        """Sets the trust_store of this Content.

        - 数据源类型为ACTIVEMQ、ARTEMISMQ、RABBITMQ、IBMMQ且开启SSL认证时需要配置，公钥库密码 - 数据源类型为HL7且为目标端（position为target），并且开启SSL认证时需要配置，公钥库密码

        :param trust_store: The trust_store of this Content.
        :type trust_store: str
        """
        self._trust_store = trust_store

    @property
    def trust_store_file_type(self):
        """Gets the trust_store_file_type of this Content.

        - 数据源类型为ACTIVEMQ、ARTEMISMQ、RABBITMQ、IBMMQ且开启SSL认证时需要配置，公钥库密码 - 数据源类型为HL7且为目标端（position为target），并且开启SSL认证时需要配置，公钥库密码

        :return: The trust_store_file_type of this Content.
        :rtype: str
        """
        return self._trust_store_file_type

    @trust_store_file_type.setter
    def trust_store_file_type(self, trust_store_file_type):
        """Sets the trust_store_file_type of this Content.

        - 数据源类型为ACTIVEMQ、ARTEMISMQ、RABBITMQ、IBMMQ且开启SSL认证时需要配置，公钥库密码 - 数据源类型为HL7且为目标端（position为target），并且开启SSL认证时需要配置，公钥库密码

        :param trust_store_file_type: The trust_store_file_type of this Content.
        :type trust_store_file_type: str
        """
        self._trust_store_file_type = trust_store_file_type

    @property
    def ssl_auth_method(self):
        """Gets the ssl_auth_method of this Content.

        数据源类型为ACTIVEMQ、ARTEMISMQ且开启SSL认证时需要配置 - one-way (单向认证) - two-way (双向认证)

        :return: The ssl_auth_method of this Content.
        :rtype: str
        """
        return self._ssl_auth_method

    @ssl_auth_method.setter
    def ssl_auth_method(self, ssl_auth_method):
        """Sets the ssl_auth_method of this Content.

        数据源类型为ACTIVEMQ、ARTEMISMQ且开启SSL认证时需要配置 - one-way (单向认证) - two-way (双向认证)

        :param ssl_auth_method: The ssl_auth_method of this Content.
        :type ssl_auth_method: str
        """
        self._ssl_auth_method = ssl_auth_method

    @property
    def key_store(self):
        """Gets the key_store of this Content.

        私钥库文件内容， - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置 - 数据源类型HL7且为源端（position为source），并且开启SSL认证时需要配置

        :return: The key_store of this Content.
        :rtype: str
        """
        return self._key_store

    @key_store.setter
    def key_store(self, key_store):
        """Sets the key_store of this Content.

        私钥库文件内容， - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置 - 数据源类型HL7且为源端（position为source），并且开启SSL认证时需要配置

        :param key_store: The key_store of this Content.
        :type key_store: str
        """
        self._key_store = key_store

    @property
    def key_store_file_type(self):
        """Gets the key_store_file_type of this Content.

        私钥库文件类型 - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置

        :return: The key_store_file_type of this Content.
        :rtype: str
        """
        return self._key_store_file_type

    @key_store_file_type.setter
    def key_store_file_type(self, key_store_file_type):
        """Sets the key_store_file_type of this Content.

        私钥库文件类型 - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置

        :param key_store_file_type: The key_store_file_type of this Content.
        :type key_store_file_type: str
        """
        self._key_store_file_type = key_store_file_type

    @property
    def key_store_password(self):
        """Gets the key_store_password of this Content.

        私钥库密码 - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置 - 数据源为HL7类型，为源端（position为source）并且开启SSL认证时需要配置

        :return: The key_store_password of this Content.
        :rtype: str
        """
        return self._key_store_password

    @key_store_password.setter
    def key_store_password(self, key_store_password):
        """Sets the key_store_password of this Content.

        私钥库密码 - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置 - 数据源为HL7类型，为源端（position为source）并且开启SSL认证时需要配置

        :param key_store_password: The key_store_password of this Content.
        :type key_store_password: str
        """
        self._key_store_password = key_store_password

    @property
    def key_store_key_password(self):
        """Gets the key_store_key_password of this Content.

        私钥库私钥密码 - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置 - 数据源为HL7类型，为源端（position为source）并且开启SSL认证时需要配置

        :return: The key_store_key_password of this Content.
        :rtype: str
        """
        return self._key_store_key_password

    @key_store_key_password.setter
    def key_store_key_password(self, key_store_key_password):
        """Sets the key_store_key_password of this Content.

        私钥库私钥密码 - 数据源类型为ACTIVEMQ、ARTEMISMQ，开启SSL认证并且认证方式是two-way时需要配置 - 数据源为HL7类型，为源端（position为source）并且开启SSL认证时需要配置

        :param key_store_key_password: The key_store_key_password of this Content.
        :type key_store_key_password: str
        """
        self._key_store_key_password = key_store_key_password

    @property
    def dis_tunnel_name(self):
        """Gets the dis_tunnel_name of this Content.

        DIS通道名称

        :return: The dis_tunnel_name of this Content.
        :rtype: str
        """
        return self._dis_tunnel_name

    @dis_tunnel_name.setter
    def dis_tunnel_name(self, dis_tunnel_name):
        """Sets the dis_tunnel_name of this Content.

        DIS通道名称

        :param dis_tunnel_name: The dis_tunnel_name of this Content.
        :type dis_tunnel_name: str
        """
        self._dis_tunnel_name = dis_tunnel_name

    @property
    def dis_data_type(self):
        """Gets the dis_data_type of this Content.

        DIS数据类别 - JSON

        :return: The dis_data_type of this Content.
        :rtype: str
        """
        return self._dis_data_type

    @dis_data_type.setter
    def dis_data_type(self, dis_data_type):
        """Sets the dis_data_type of this Content.

        DIS数据类别 - JSON

        :param dis_data_type: The dis_data_type of this Content.
        :type dis_data_type: str
        """
        self._dis_data_type = dis_data_type

    @property
    def dis_setting_type(self):
        """Gets the dis_setting_type of this Content.

        DIS配置类别 - senior (高级) - basic (基础)

        :return: The dis_setting_type of this Content.
        :rtype: str
        """
        return self._dis_setting_type

    @dis_setting_type.setter
    def dis_setting_type(self, dis_setting_type):
        """Sets the dis_setting_type of this Content.

        DIS配置类别 - senior (高级) - basic (基础)

        :param dis_setting_type: The dis_setting_type of this Content.
        :type dis_setting_type: str
        """
        self._dis_setting_type = dis_setting_type

    @property
    def dis_endpoint(self):
        """Gets the dis_endpoint of this Content.

        DIS Endpoint，当setting_type为senior时填写

        :return: The dis_endpoint of this Content.
        :rtype: str
        """
        return self._dis_endpoint

    @dis_endpoint.setter
    def dis_endpoint(self, dis_endpoint):
        """Sets the dis_endpoint of this Content.

        DIS Endpoint，当setting_type为senior时填写

        :param dis_endpoint: The dis_endpoint of this Content.
        :type dis_endpoint: str
        """
        self._dis_endpoint = dis_endpoint

    @property
    def dis_region(self):
        """Gets the dis_region of this Content.

        DIS Region，当setting_type为senior时填写

        :return: The dis_region of this Content.
        :rtype: str
        """
        return self._dis_region

    @dis_region.setter
    def dis_region(self, dis_region):
        """Sets the dis_region of this Content.

        DIS Region，当setting_type为senior时填写

        :param dis_region: The dis_region of this Content.
        :type dis_region: str
        """
        self._dis_region = dis_region

    @property
    def dis_source_project_id(self):
        """Gets the dis_source_project_id of this Content.

        DIS源端项目id，当setting_type为senior时填写

        :return: The dis_source_project_id of this Content.
        :rtype: str
        """
        return self._dis_source_project_id

    @dis_source_project_id.setter
    def dis_source_project_id(self, dis_source_project_id):
        """Sets the dis_source_project_id of this Content.

        DIS源端项目id，当setting_type为senior时填写

        :param dis_source_project_id: The dis_source_project_id of this Content.
        :type dis_source_project_id: str
        """
        self._dis_source_project_id = dis_source_project_id

    @property
    def hl7_position(self):
        """Gets the hl7_position of this Content.

        HL7数据源方向 - source (源端) - target (目标端)

        :return: The hl7_position of this Content.
        :rtype: str
        """
        return self._hl7_position

    @hl7_position.setter
    def hl7_position(self, hl7_position):
        """Sets the hl7_position of this Content.

        HL7数据源方向 - source (源端) - target (目标端)

        :param hl7_position: The hl7_position of this Content.
        :type hl7_position: str
        """
        self._hl7_position = hl7_position

    @property
    def hl7_whitelist_enable(self):
        """Gets the hl7_whitelist_enable of this Content.

        HL7是否开启白名单设置

        :return: The hl7_whitelist_enable of this Content.
        :rtype: bool
        """
        return self._hl7_whitelist_enable

    @hl7_whitelist_enable.setter
    def hl7_whitelist_enable(self, hl7_whitelist_enable):
        """Sets the hl7_whitelist_enable of this Content.

        HL7是否开启白名单设置

        :param hl7_whitelist_enable: The hl7_whitelist_enable of this Content.
        :type hl7_whitelist_enable: bool
        """
        self._hl7_whitelist_enable = hl7_whitelist_enable

    @property
    def hl7_whitelist(self):
        """Gets the hl7_whitelist of this Content.

        HL7白名单 - 允许同步数据到源端HL7的服务器地址，当HL7为源端（position为source）并且开启白名单设置(open_whitelist为true)时填写

        :return: The hl7_whitelist of this Content.
        :rtype: str
        """
        return self._hl7_whitelist

    @hl7_whitelist.setter
    def hl7_whitelist(self, hl7_whitelist):
        """Sets the hl7_whitelist of this Content.

        HL7白名单 - 允许同步数据到源端HL7的服务器地址，当HL7为源端（position为source）并且开启白名单设置(open_whitelist为true)时填写

        :param hl7_whitelist: The hl7_whitelist of this Content.
        :type hl7_whitelist: str
        """
        self._hl7_whitelist = hl7_whitelist

    @property
    def ldap_security_auth_type(self):
        """Gets the ldap_security_auth_type of this Content.

        LDAP安全认证类型

        :return: The ldap_security_auth_type of this Content.
        :rtype: str
        """
        return self._ldap_security_auth_type

    @ldap_security_auth_type.setter
    def ldap_security_auth_type(self, ldap_security_auth_type):
        """Sets the ldap_security_auth_type of this Content.

        LDAP安全认证类型

        :param ldap_security_auth_type: The ldap_security_auth_type of this Content.
        :type ldap_security_auth_type: str
        """
        self._ldap_security_auth_type = ldap_security_auth_type

    @property
    def rabbitmq_virtual_host(self):
        """Gets the rabbitmq_virtual_host of this Content.

        RABBITMQ虚拟主机

        :return: The rabbitmq_virtual_host of this Content.
        :rtype: str
        """
        return self._rabbitmq_virtual_host

    @rabbitmq_virtual_host.setter
    def rabbitmq_virtual_host(self, rabbitmq_virtual_host):
        """Sets the rabbitmq_virtual_host of this Content.

        RABBITMQ虚拟主机

        :param rabbitmq_virtual_host: The rabbitmq_virtual_host of this Content.
        :type rabbitmq_virtual_host: str
        """
        self._rabbitmq_virtual_host = rabbitmq_virtual_host

    @property
    def rabbitmq_ssl_protocol(self):
        """Gets the rabbitmq_ssl_protocol of this Content.

        RABBITMQ SSL认证协议 - TLS

        :return: The rabbitmq_ssl_protocol of this Content.
        :rtype: str
        """
        return self._rabbitmq_ssl_protocol

    @rabbitmq_ssl_protocol.setter
    def rabbitmq_ssl_protocol(self, rabbitmq_ssl_protocol):
        """Sets the rabbitmq_ssl_protocol of this Content.

        RABBITMQ SSL认证协议 - TLS

        :param rabbitmq_ssl_protocol: The rabbitmq_ssl_protocol of this Content.
        :type rabbitmq_ssl_protocol: str
        """
        self._rabbitmq_ssl_protocol = rabbitmq_ssl_protocol

    @property
    def sap_client(self):
        """Gets the sap_client of this Content.

        SAP客户端号

        :return: The sap_client of this Content.
        :rtype: str
        """
        return self._sap_client

    @sap_client.setter
    def sap_client(self, sap_client):
        """Sets the sap_client of this Content.

        SAP客户端号

        :param sap_client: The sap_client of this Content.
        :type sap_client: str
        """
        self._sap_client = sap_client

    @property
    def sap_sysnr(self):
        """Gets the sap_sysnr of this Content.

        SAP实例编号

        :return: The sap_sysnr of this Content.
        :rtype: str
        """
        return self._sap_sysnr

    @sap_sysnr.setter
    def sap_sysnr(self, sap_sysnr):
        """Sets the sap_sysnr of this Content.

        SAP实例编号

        :param sap_sysnr: The sap_sysnr of this Content.
        :type sap_sysnr: str
        """
        self._sap_sysnr = sap_sysnr

    @property
    def snmp_network_protocol(self):
        """Gets the snmp_network_protocol of this Content.

        SNMP网络协议 - udp - tcp

        :return: The snmp_network_protocol of this Content.
        :rtype: str
        """
        return self._snmp_network_protocol

    @snmp_network_protocol.setter
    def snmp_network_protocol(self, snmp_network_protocol):
        """Sets the snmp_network_protocol of this Content.

        SNMP网络协议 - udp - tcp

        :param snmp_network_protocol: The snmp_network_protocol of this Content.
        :type snmp_network_protocol: str
        """
        self._snmp_network_protocol = snmp_network_protocol

    @property
    def snmp_version(self):
        """Gets the snmp_version of this Content.

        SNMP版本号

        :return: The snmp_version of this Content.
        :rtype: int
        """
        return self._snmp_version

    @snmp_version.setter
    def snmp_version(self, snmp_version):
        """Sets the snmp_version of this Content.

        SNMP版本号

        :param snmp_version: The snmp_version of this Content.
        :type snmp_version: int
        """
        self._snmp_version = snmp_version

    @property
    def snmp_community(self):
        """Gets the snmp_community of this Content.

        SNMP团体名，用于访问SNMP管理代理的身份认证，相当于访问密码

        :return: The snmp_community of this Content.
        :rtype: str
        """
        return self._snmp_community

    @snmp_community.setter
    def snmp_community(self, snmp_community):
        """Sets the snmp_community of this Content.

        SNMP团体名，用于访问SNMP管理代理的身份认证，相当于访问密码

        :param snmp_community: The snmp_community of this Content.
        :type snmp_community: str
        """
        self._snmp_community = snmp_community

    @property
    def ibmmq_ccs_id(self):
        """Gets the ibmmq_ccs_id of this Content.

        IBMMQ字符集标识

        :return: The ibmmq_ccs_id of this Content.
        :rtype: str
        """
        return self._ibmmq_ccs_id

    @ibmmq_ccs_id.setter
    def ibmmq_ccs_id(self, ibmmq_ccs_id):
        """Sets the ibmmq_ccs_id of this Content.

        IBMMQ字符集标识

        :param ibmmq_ccs_id: The ibmmq_ccs_id of this Content.
        :type ibmmq_ccs_id: str
        """
        self._ibmmq_ccs_id = ibmmq_ccs_id

    @property
    def ibmmq_queue_manager(self):
        """Gets the ibmmq_queue_manager of this Content.

        IBMMQ队列管理器

        :return: The ibmmq_queue_manager of this Content.
        :rtype: str
        """
        return self._ibmmq_queue_manager

    @ibmmq_queue_manager.setter
    def ibmmq_queue_manager(self, ibmmq_queue_manager):
        """Sets the ibmmq_queue_manager of this Content.

        IBMMQ队列管理器

        :param ibmmq_queue_manager: The ibmmq_queue_manager of this Content.
        :type ibmmq_queue_manager: str
        """
        self._ibmmq_queue_manager = ibmmq_queue_manager

    @property
    def ibmmq_channel(self):
        """Gets the ibmmq_channel of this Content.

        IBMMQ通道名称

        :return: The ibmmq_channel of this Content.
        :rtype: str
        """
        return self._ibmmq_channel

    @ibmmq_channel.setter
    def ibmmq_channel(self, ibmmq_channel):
        """Sets the ibmmq_channel of this Content.

        IBMMQ通道名称

        :param ibmmq_channel: The ibmmq_channel of this Content.
        :type ibmmq_channel: str
        """
        self._ibmmq_channel = ibmmq_channel

    @property
    def ibmmq_cipher_suite(self):
        """Gets the ibmmq_cipher_suite of this Content.

        IBMMQ密钥算法套件

        :return: The ibmmq_cipher_suite of this Content.
        :rtype: str
        """
        return self._ibmmq_cipher_suite

    @ibmmq_cipher_suite.setter
    def ibmmq_cipher_suite(self, ibmmq_cipher_suite):
        """Sets the ibmmq_cipher_suite of this Content.

        IBMMQ密钥算法套件

        :param ibmmq_cipher_suite: The ibmmq_cipher_suite of this Content.
        :type ibmmq_cipher_suite: str
        """
        self._ibmmq_cipher_suite = ibmmq_cipher_suite

    @property
    def hdfs_path(self):
        """Gets the hdfs_path of this Content.

        HDFS URL - 数据源为MRSHIVE、MRSHDFS、FIHDFS、FIHIVE类型时配置 - fihadfs (/fdi/autotest)

        :return: The hdfs_path of this Content.
        :rtype: str
        """
        return self._hdfs_path

    @hdfs_path.setter
    def hdfs_path(self, hdfs_path):
        """Sets the hdfs_path of this Content.

        HDFS URL - 数据源为MRSHIVE、MRSHDFS、FIHDFS、FIHIVE类型时配置 - fihadfs (/fdi/autotest)

        :param hdfs_path: The hdfs_path of this Content.
        :type hdfs_path: str
        """
        self._hdfs_path = hdfs_path

    @property
    def principal_name(self):
        """Gets the principal_name of this Content.

        机机交互用户名 - 数据源为MRSHIVE、MRSHDFS、MRSHBASE、MRSKAFKA、FIHDFS、FIHIVE、FIKAFKA类型时配置

        :return: The principal_name of this Content.
        :rtype: str
        """
        return self._principal_name

    @principal_name.setter
    def principal_name(self, principal_name):
        """Sets the principal_name of this Content.

        机机交互用户名 - 数据源为MRSHIVE、MRSHDFS、MRSHBASE、MRSKAFKA、FIHDFS、FIHIVE、FIKAFKA类型时配置

        :param principal_name: The principal_name of this Content.
        :type principal_name: str
        """
        self._principal_name = principal_name

    @property
    def config_file_name(self):
        """Gets the config_file_name of this Content.

        - 用户认证文件，文件获取方式参考《ROMA Connect API参考》的“附录>获取数据源配置文件”章节 - 将获取到的文件打包成zip文件，文件名配置在config_file_name中，内容以BASE64编码形式放到config_file_content。 - 数据源为MRSHIVE、MRSHDFS、MRSHBASE、MRSKAFKA、FIHDFS、FIHIVE、FIKAFKA类型时配置

        :return: The config_file_name of this Content.
        :rtype: str
        """
        return self._config_file_name

    @config_file_name.setter
    def config_file_name(self, config_file_name):
        """Sets the config_file_name of this Content.

        - 用户认证文件，文件获取方式参考《ROMA Connect API参考》的“附录>获取数据源配置文件”章节 - 将获取到的文件打包成zip文件，文件名配置在config_file_name中，内容以BASE64编码形式放到config_file_content。 - 数据源为MRSHIVE、MRSHDFS、MRSHBASE、MRSKAFKA、FIHDFS、FIHIVE、FIKAFKA类型时配置

        :param config_file_name: The config_file_name of this Content.
        :type config_file_name: str
        """
        self._config_file_name = config_file_name

    @property
    def config_file_content(self):
        """Gets the config_file_content of this Content.

        - 用户认证文件内容，config_file_name对应的文件内容BASE64编码 - 数据源为MRSHIVE、MRSHDFS、MRSHBASE、MRSKAFKA、FIHDFS、FIHIVE、FIKAFKA类型时配置

        :return: The config_file_content of this Content.
        :rtype: str
        """
        return self._config_file_content

    @config_file_content.setter
    def config_file_content(self, config_file_content):
        """Sets the config_file_content of this Content.

        - 用户认证文件内容，config_file_name对应的文件内容BASE64编码 - 数据源为MRSHIVE、MRSHDFS、MRSHBASE、MRSKAFKA、FIHDFS、FIHIVE、FIKAFKA类型时配置

        :param config_file_content: The config_file_content of this Content.
        :type config_file_content: str
        """
        self._config_file_content = config_file_content

    @property
    def connection_instance_id(self):
        """Gets the connection_instance_id of this Content.

        连接器实例ID，连接器发布后对应的实例ID

        :return: The connection_instance_id of this Content.
        :rtype: str
        """
        return self._connection_instance_id

    @connection_instance_id.setter
    def connection_instance_id(self, connection_instance_id):
        """Sets the connection_instance_id of this Content.

        连接器实例ID，连接器发布后对应的实例ID

        :param connection_instance_id: The connection_instance_id of this Content.
        :type connection_instance_id: str
        """
        self._connection_instance_id = connection_instance_id

    @property
    def connector_params(self):
        """Gets the connector_params of this Content.

        连接器对应的数据源参数，值按实际填写

        :return: The connector_params of this Content.
        :rtype: object
        """
        return self._connector_params

    @connector_params.setter
    def connector_params(self, connector_params):
        """Sets the connector_params of this Content.

        连接器对应的数据源参数，值按实际填写

        :param connector_params: The connector_params of this Content.
        :type connector_params: object
        """
        self._connector_params = connector_params

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
        if not isinstance(other, Content):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
