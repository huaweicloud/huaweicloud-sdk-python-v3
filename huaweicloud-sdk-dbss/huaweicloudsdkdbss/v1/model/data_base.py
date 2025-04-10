# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataBase:

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
        'name': 'str',
        'type': 'str',
        'version': 'str',
        'charset': 'str',
        'ip': 'str',
        'port': 'str',
        'os': 'str',
        'status': 'str',
        'instance_name': 'str',
        'audit_status': 'str',
        'agent_url': 'list[str]',
        'db_classification': 'str',
        'rds_audit_switch_mismatch': 'bool',
        'rds_id': 'str',
        'rds_obj_info': 'str',
        'dws_obj_info': 'str',
        'clouddb_obj_info': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'version': 'version',
        'charset': 'charset',
        'ip': 'ip',
        'port': 'port',
        'os': 'os',
        'status': 'status',
        'instance_name': 'instance_name',
        'audit_status': 'audit_status',
        'agent_url': 'agent_url',
        'db_classification': 'db_classification',
        'rds_audit_switch_mismatch': 'rds_audit_switch_mismatch',
        'rds_id': 'rds_id',
        'rds_obj_info': 'rds_obj_info',
        'dws_obj_info': 'dws_obj_info',
        'clouddb_obj_info': 'clouddb_obj_info'
    }

    def __init__(self, id=None, name=None, type=None, version=None, charset=None, ip=None, port=None, os=None, status=None, instance_name=None, audit_status=None, agent_url=None, db_classification=None, rds_audit_switch_mismatch=None, rds_id=None, rds_obj_info=None, dws_obj_info=None, clouddb_obj_info=None):
        r"""DataBase

        The model defined in huaweicloud sdk

        :param id: 数据库ID
        :type id: str
        :param name: 数据库名称
        :type name: str
        :param type: 添加的数据库类型： - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - GAUSSDBOPENGAUSS - GREENPLUM - HIGHGO - SHENTONG - GBASE8A - GBASE8S - GBASEXDM - MONGODB - DDS
        :type type: str
        :param version: 数据库版本
        :type version: str
        :param charset: 数据库字符集 - GBK - UTF8
        :type charset: str
        :param ip: 数据库IP
        :type ip: str
        :param port: 数据库端口
        :type port: str
        :param os: 数据库操作系统
        :type os: str
        :param status: 实例状态 - ON :开启 - OFF : 关闭
        :type status: str
        :param instance_name: 数据库实例名
        :type instance_name: str
        :param audit_status: 数据库的运行状态 - ACTIVE - SHUTOFF - ERROR
        :type audit_status: str
        :param agent_url: agent的唯一ID
        :type agent_url: list[str]
        :param db_classification: 数据库分类 - RDS: 表示RDS数据库 - ECS:自建数据库
        :type db_classification: str
        :param rds_audit_switch_mismatch: rds实例审计开关状态不匹配。当数据库审计开启且rds侧日志上传开关关闭时该字段为true。
        :type rds_audit_switch_mismatch: bool
        :param rds_id: RDS数据库的ID。
        :type rds_id: str
        :param rds_obj_info: RDS数据库信息。
        :type rds_obj_info: str
        :param dws_obj_info: DWS数据库信息。
        :type dws_obj_info: str
        :param clouddb_obj_info: 云数据库信息，该字段已废弃。
        :type clouddb_obj_info: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._version = None
        self._charset = None
        self._ip = None
        self._port = None
        self._os = None
        self._status = None
        self._instance_name = None
        self._audit_status = None
        self._agent_url = None
        self._db_classification = None
        self._rds_audit_switch_mismatch = None
        self._rds_id = None
        self._rds_obj_info = None
        self._dws_obj_info = None
        self._clouddb_obj_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.type = type
        self.version = version
        self.charset = charset
        self.ip = ip
        self.port = port
        self.os = os
        self.status = status
        self.instance_name = instance_name
        if audit_status is not None:
            self.audit_status = audit_status
        if agent_url is not None:
            self.agent_url = agent_url
        self.db_classification = db_classification
        if rds_audit_switch_mismatch is not None:
            self.rds_audit_switch_mismatch = rds_audit_switch_mismatch
        if rds_id is not None:
            self.rds_id = rds_id
        if rds_obj_info is not None:
            self.rds_obj_info = rds_obj_info
        if dws_obj_info is not None:
            self.dws_obj_info = dws_obj_info
        if clouddb_obj_info is not None:
            self.clouddb_obj_info = clouddb_obj_info

    @property
    def id(self):
        r"""Gets the id of this DataBase.

        数据库ID

        :return: The id of this DataBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DataBase.

        数据库ID

        :param id: The id of this DataBase.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DataBase.

        数据库名称

        :return: The name of this DataBase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DataBase.

        数据库名称

        :param name: The name of this DataBase.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this DataBase.

        添加的数据库类型： - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - GAUSSDBOPENGAUSS - GREENPLUM - HIGHGO - SHENTONG - GBASE8A - GBASE8S - GBASEXDM - MONGODB - DDS

        :return: The type of this DataBase.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DataBase.

        添加的数据库类型： - MYSQL - ORACLE - POSTGRESQL - SQLSERVER - DAMENG - TAURUS - DWS - KINGBASE - GAUSSDBOPENGAUSS - GREENPLUM - HIGHGO - SHENTONG - GBASE8A - GBASE8S - GBASEXDM - MONGODB - DDS

        :param type: The type of this DataBase.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this DataBase.

        数据库版本

        :return: The version of this DataBase.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this DataBase.

        数据库版本

        :param version: The version of this DataBase.
        :type version: str
        """
        self._version = version

    @property
    def charset(self):
        r"""Gets the charset of this DataBase.

        数据库字符集 - GBK - UTF8

        :return: The charset of this DataBase.
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        r"""Sets the charset of this DataBase.

        数据库字符集 - GBK - UTF8

        :param charset: The charset of this DataBase.
        :type charset: str
        """
        self._charset = charset

    @property
    def ip(self):
        r"""Gets the ip of this DataBase.

        数据库IP

        :return: The ip of this DataBase.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this DataBase.

        数据库IP

        :param ip: The ip of this DataBase.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this DataBase.

        数据库端口

        :return: The port of this DataBase.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this DataBase.

        数据库端口

        :param port: The port of this DataBase.
        :type port: str
        """
        self._port = port

    @property
    def os(self):
        r"""Gets the os of this DataBase.

        数据库操作系统

        :return: The os of this DataBase.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this DataBase.

        数据库操作系统

        :param os: The os of this DataBase.
        :type os: str
        """
        self._os = os

    @property
    def status(self):
        r"""Gets the status of this DataBase.

        实例状态 - ON :开启 - OFF : 关闭

        :return: The status of this DataBase.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DataBase.

        实例状态 - ON :开启 - OFF : 关闭

        :param status: The status of this DataBase.
        :type status: str
        """
        self._status = status

    @property
    def instance_name(self):
        r"""Gets the instance_name of this DataBase.

        数据库实例名

        :return: The instance_name of this DataBase.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this DataBase.

        数据库实例名

        :param instance_name: The instance_name of this DataBase.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def audit_status(self):
        r"""Gets the audit_status of this DataBase.

        数据库的运行状态 - ACTIVE - SHUTOFF - ERROR

        :return: The audit_status of this DataBase.
        :rtype: str
        """
        return self._audit_status

    @audit_status.setter
    def audit_status(self, audit_status):
        r"""Sets the audit_status of this DataBase.

        数据库的运行状态 - ACTIVE - SHUTOFF - ERROR

        :param audit_status: The audit_status of this DataBase.
        :type audit_status: str
        """
        self._audit_status = audit_status

    @property
    def agent_url(self):
        r"""Gets the agent_url of this DataBase.

        agent的唯一ID

        :return: The agent_url of this DataBase.
        :rtype: list[str]
        """
        return self._agent_url

    @agent_url.setter
    def agent_url(self, agent_url):
        r"""Sets the agent_url of this DataBase.

        agent的唯一ID

        :param agent_url: The agent_url of this DataBase.
        :type agent_url: list[str]
        """
        self._agent_url = agent_url

    @property
    def db_classification(self):
        r"""Gets the db_classification of this DataBase.

        数据库分类 - RDS: 表示RDS数据库 - ECS:自建数据库

        :return: The db_classification of this DataBase.
        :rtype: str
        """
        return self._db_classification

    @db_classification.setter
    def db_classification(self, db_classification):
        r"""Sets the db_classification of this DataBase.

        数据库分类 - RDS: 表示RDS数据库 - ECS:自建数据库

        :param db_classification: The db_classification of this DataBase.
        :type db_classification: str
        """
        self._db_classification = db_classification

    @property
    def rds_audit_switch_mismatch(self):
        r"""Gets the rds_audit_switch_mismatch of this DataBase.

        rds实例审计开关状态不匹配。当数据库审计开启且rds侧日志上传开关关闭时该字段为true。

        :return: The rds_audit_switch_mismatch of this DataBase.
        :rtype: bool
        """
        return self._rds_audit_switch_mismatch

    @rds_audit_switch_mismatch.setter
    def rds_audit_switch_mismatch(self, rds_audit_switch_mismatch):
        r"""Sets the rds_audit_switch_mismatch of this DataBase.

        rds实例审计开关状态不匹配。当数据库审计开启且rds侧日志上传开关关闭时该字段为true。

        :param rds_audit_switch_mismatch: The rds_audit_switch_mismatch of this DataBase.
        :type rds_audit_switch_mismatch: bool
        """
        self._rds_audit_switch_mismatch = rds_audit_switch_mismatch

    @property
    def rds_id(self):
        r"""Gets the rds_id of this DataBase.

        RDS数据库的ID。

        :return: The rds_id of this DataBase.
        :rtype: str
        """
        return self._rds_id

    @rds_id.setter
    def rds_id(self, rds_id):
        r"""Sets the rds_id of this DataBase.

        RDS数据库的ID。

        :param rds_id: The rds_id of this DataBase.
        :type rds_id: str
        """
        self._rds_id = rds_id

    @property
    def rds_obj_info(self):
        r"""Gets the rds_obj_info of this DataBase.

        RDS数据库信息。

        :return: The rds_obj_info of this DataBase.
        :rtype: str
        """
        return self._rds_obj_info

    @rds_obj_info.setter
    def rds_obj_info(self, rds_obj_info):
        r"""Sets the rds_obj_info of this DataBase.

        RDS数据库信息。

        :param rds_obj_info: The rds_obj_info of this DataBase.
        :type rds_obj_info: str
        """
        self._rds_obj_info = rds_obj_info

    @property
    def dws_obj_info(self):
        r"""Gets the dws_obj_info of this DataBase.

        DWS数据库信息。

        :return: The dws_obj_info of this DataBase.
        :rtype: str
        """
        return self._dws_obj_info

    @dws_obj_info.setter
    def dws_obj_info(self, dws_obj_info):
        r"""Sets the dws_obj_info of this DataBase.

        DWS数据库信息。

        :param dws_obj_info: The dws_obj_info of this DataBase.
        :type dws_obj_info: str
        """
        self._dws_obj_info = dws_obj_info

    @property
    def clouddb_obj_info(self):
        r"""Gets the clouddb_obj_info of this DataBase.

        云数据库信息，该字段已废弃。

        :return: The clouddb_obj_info of this DataBase.
        :rtype: str
        """
        return self._clouddb_obj_info

    @clouddb_obj_info.setter
    def clouddb_obj_info(self, clouddb_obj_info):
        r"""Sets the clouddb_obj_info of this DataBase.

        云数据库信息，该字段已废弃。

        :param clouddb_obj_info: The clouddb_obj_info of this DataBase.
        :type clouddb_obj_info: str
        """
        self._clouddb_obj_info = clouddb_obj_info

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
        if not isinstance(other, DataBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
