# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateChInstanceInfo:

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
        'az_code': 'str',
        'az_mode': 'str',
        'name': 'str',
        'engine': 'ClickHouseEngineInfo',
        'vpc_id': 'str',
        'security_group_id': 'str',
        'subnet_id': 'str',
        'db_user': 'str',
        'port': 'int',
        'ha_mode': 'str',
        'pay_info': 'CreateChInstanceInfoPayInfo',
        'ssl_option': 'bool',
        'status': 'str',
        'region': 'str',
        'tags_info': 'CreateChInstanceInfoTagsInfo'
    }

    attribute_map = {
        'id': 'id',
        'az_code': 'az_code',
        'az_mode': 'az_mode',
        'name': 'name',
        'engine': 'engine',
        'vpc_id': 'vpc_id',
        'security_group_id': 'security_group_id',
        'subnet_id': 'subnet_id',
        'db_user': 'db_user',
        'port': 'port',
        'ha_mode': 'ha_mode',
        'pay_info': 'pay_info',
        'ssl_option': 'ssl_option',
        'status': 'status',
        'region': 'region',
        'tags_info': 'tags_info'
    }

    def __init__(self, id=None, az_code=None, az_mode=None, name=None, engine=None, vpc_id=None, security_group_id=None, subnet_id=None, db_user=None, port=None, ha_mode=None, pay_info=None, ssl_option=None, status=None, region=None, tags_info=None):
        r"""CreateChInstanceInfo

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param az_code: 可用区。
        :type az_code: str
        :param az_mode: 可用区模式。 取值范围： - single：单可用区 - double：多可用区
        :type az_mode: str
        :param name: 实例名。
        :type name: str
        :param engine: 
        :type engine: :class:`huaweicloudsdkgaussdb.v3.ClickHouseEngineInfo`
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param db_user: 数据库用户。
        :type db_user: str
        :param port: 数据库端口。取值范围：0~65535。
        :type port: int
        :param ha_mode: 部署模式。 取值范围： - Single：单机 - Ha：主备
        :type ha_mode: str
        :param pay_info: 
        :type pay_info: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceInfoPayInfo`
        :param ssl_option: SSL开关。
        :type ssl_option: bool
        :param status: 实例状态。 取值范围： - creating：创建 - normal：正常 - abnormal：异常 - createfailed：创建失败 - deleted：已删除
        :type status: str
        :param region: 实例所在区。
        :type region: str
        :param tags_info: 
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceInfoTagsInfo`
        """
        
        

        self._id = None
        self._az_code = None
        self._az_mode = None
        self._name = None
        self._engine = None
        self._vpc_id = None
        self._security_group_id = None
        self._subnet_id = None
        self._db_user = None
        self._port = None
        self._ha_mode = None
        self._pay_info = None
        self._ssl_option = None
        self._status = None
        self._region = None
        self._tags_info = None
        self.discriminator = None

        self.id = id
        self.az_code = az_code
        self.az_mode = az_mode
        self.name = name
        self.engine = engine
        self.vpc_id = vpc_id
        self.security_group_id = security_group_id
        self.subnet_id = subnet_id
        self.db_user = db_user
        self.port = port
        self.ha_mode = ha_mode
        self.pay_info = pay_info
        self.ssl_option = ssl_option
        self.status = status
        self.region = region
        self.tags_info = tags_info

    @property
    def id(self):
        r"""Gets the id of this CreateChInstanceInfo.

        实例ID。

        :return: The id of this CreateChInstanceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateChInstanceInfo.

        实例ID。

        :param id: The id of this CreateChInstanceInfo.
        :type id: str
        """
        self._id = id

    @property
    def az_code(self):
        r"""Gets the az_code of this CreateChInstanceInfo.

        可用区。

        :return: The az_code of this CreateChInstanceInfo.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this CreateChInstanceInfo.

        可用区。

        :param az_code: The az_code of this CreateChInstanceInfo.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def az_mode(self):
        r"""Gets the az_mode of this CreateChInstanceInfo.

        可用区模式。 取值范围： - single：单可用区 - double：多可用区

        :return: The az_mode of this CreateChInstanceInfo.
        :rtype: str
        """
        return self._az_mode

    @az_mode.setter
    def az_mode(self, az_mode):
        r"""Sets the az_mode of this CreateChInstanceInfo.

        可用区模式。 取值范围： - single：单可用区 - double：多可用区

        :param az_mode: The az_mode of this CreateChInstanceInfo.
        :type az_mode: str
        """
        self._az_mode = az_mode

    @property
    def name(self):
        r"""Gets the name of this CreateChInstanceInfo.

        实例名。

        :return: The name of this CreateChInstanceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateChInstanceInfo.

        实例名。

        :param name: The name of this CreateChInstanceInfo.
        :type name: str
        """
        self._name = name

    @property
    def engine(self):
        r"""Gets the engine of this CreateChInstanceInfo.

        :return: The engine of this CreateChInstanceInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ClickHouseEngineInfo`
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this CreateChInstanceInfo.

        :param engine: The engine of this CreateChInstanceInfo.
        :type engine: :class:`huaweicloudsdkgaussdb.v3.ClickHouseEngineInfo`
        """
        self._engine = engine

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateChInstanceInfo.

        虚拟私有云ID。

        :return: The vpc_id of this CreateChInstanceInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateChInstanceInfo.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this CreateChInstanceInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this CreateChInstanceInfo.

        安全组ID。

        :return: The security_group_id of this CreateChInstanceInfo.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this CreateChInstanceInfo.

        安全组ID。

        :param security_group_id: The security_group_id of this CreateChInstanceInfo.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateChInstanceInfo.

        子网ID。

        :return: The subnet_id of this CreateChInstanceInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateChInstanceInfo.

        子网ID。

        :param subnet_id: The subnet_id of this CreateChInstanceInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def db_user(self):
        r"""Gets the db_user of this CreateChInstanceInfo.

        数据库用户。

        :return: The db_user of this CreateChInstanceInfo.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        r"""Sets the db_user of this CreateChInstanceInfo.

        数据库用户。

        :param db_user: The db_user of this CreateChInstanceInfo.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def port(self):
        r"""Gets the port of this CreateChInstanceInfo.

        数据库端口。取值范围：0~65535。

        :return: The port of this CreateChInstanceInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this CreateChInstanceInfo.

        数据库端口。取值范围：0~65535。

        :param port: The port of this CreateChInstanceInfo.
        :type port: int
        """
        self._port = port

    @property
    def ha_mode(self):
        r"""Gets the ha_mode of this CreateChInstanceInfo.

        部署模式。 取值范围： - Single：单机 - Ha：主备

        :return: The ha_mode of this CreateChInstanceInfo.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        r"""Sets the ha_mode of this CreateChInstanceInfo.

        部署模式。 取值范围： - Single：单机 - Ha：主备

        :param ha_mode: The ha_mode of this CreateChInstanceInfo.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def pay_info(self):
        r"""Gets the pay_info of this CreateChInstanceInfo.

        :return: The pay_info of this CreateChInstanceInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceInfoPayInfo`
        """
        return self._pay_info

    @pay_info.setter
    def pay_info(self, pay_info):
        r"""Sets the pay_info of this CreateChInstanceInfo.

        :param pay_info: The pay_info of this CreateChInstanceInfo.
        :type pay_info: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceInfoPayInfo`
        """
        self._pay_info = pay_info

    @property
    def ssl_option(self):
        r"""Gets the ssl_option of this CreateChInstanceInfo.

        SSL开关。

        :return: The ssl_option of this CreateChInstanceInfo.
        :rtype: bool
        """
        return self._ssl_option

    @ssl_option.setter
    def ssl_option(self, ssl_option):
        r"""Sets the ssl_option of this CreateChInstanceInfo.

        SSL开关。

        :param ssl_option: The ssl_option of this CreateChInstanceInfo.
        :type ssl_option: bool
        """
        self._ssl_option = ssl_option

    @property
    def status(self):
        r"""Gets the status of this CreateChInstanceInfo.

        实例状态。 取值范围： - creating：创建 - normal：正常 - abnormal：异常 - createfailed：创建失败 - deleted：已删除

        :return: The status of this CreateChInstanceInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateChInstanceInfo.

        实例状态。 取值范围： - creating：创建 - normal：正常 - abnormal：异常 - createfailed：创建失败 - deleted：已删除

        :param status: The status of this CreateChInstanceInfo.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        r"""Gets the region of this CreateChInstanceInfo.

        实例所在区。

        :return: The region of this CreateChInstanceInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateChInstanceInfo.

        实例所在区。

        :param region: The region of this CreateChInstanceInfo.
        :type region: str
        """
        self._region = region

    @property
    def tags_info(self):
        r"""Gets the tags_info of this CreateChInstanceInfo.

        :return: The tags_info of this CreateChInstanceInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceInfoTagsInfo`
        """
        return self._tags_info

    @tags_info.setter
    def tags_info(self, tags_info):
        r"""Sets the tags_info of this CreateChInstanceInfo.

        :param tags_info: The tags_info of this CreateChInstanceInfo.
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceInfoTagsInfo`
        """
        self._tags_info = tags_info

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
        if not isinstance(other, CreateChInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
