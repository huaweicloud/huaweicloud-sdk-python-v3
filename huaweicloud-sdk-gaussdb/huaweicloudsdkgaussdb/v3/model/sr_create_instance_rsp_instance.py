# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SrCreateInstanceRspInstance:

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
        'engine': 'SrCreateInstanceRspInstanceEngine',
        'vpc_id': 'str',
        'security_group_id': 'str',
        'sub_net_id': 'str',
        'db_user': 'str',
        'port': 'int',
        'ha_mode': 'str',
        'pay_info': 'SrCreateInstanceRspInstancePayInfo',
        'enable_ssl': 'bool',
        'status': 'str',
        'region': 'str',
        'tags_info': 'SrCreateInstanceRspInstanceTagsInfo'
    }

    attribute_map = {
        'id': 'id',
        'az_code': 'az_code',
        'az_mode': 'az_mode',
        'name': 'name',
        'engine': 'engine',
        'vpc_id': 'vpc_id',
        'security_group_id': 'security_group_id',
        'sub_net_id': 'sub_net_id',
        'db_user': 'db_user',
        'port': 'port',
        'ha_mode': 'ha_mode',
        'pay_info': 'pay_info',
        'enable_ssl': 'enable_ssl',
        'status': 'status',
        'region': 'region',
        'tags_info': 'tags_info'
    }

    def __init__(self, id=None, az_code=None, az_mode=None, name=None, engine=None, vpc_id=None, security_group_id=None, sub_net_id=None, db_user=None, port=None, ha_mode=None, pay_info=None, enable_ssl=None, status=None, region=None, tags_info=None):
        """SrCreateInstanceRspInstance

        The model defined in huaweicloud sdk

        :param id: StarRocks实例ID，严格匹配UUID规则。
        :type id: str
        :param az_code: 可用区码。
        :type az_code: str
        :param az_mode: 可用区模式。  取值范围：  single：单可用区。  multi：多可用区。
        :type az_mode: str
        :param name: 实例名称。
        :type name: str
        :param engine: 
        :type engine: :class:`huaweicloudsdkgaussdb.v3.SrCreateInstanceRspInstanceEngine`
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param sub_net_id: 子网ID。
        :type sub_net_id: str
        :param db_user: 数据库用户。默认root。
        :type db_user: str
        :param port: 数据库端口号。默认3306。
        :type port: int
        :param ha_mode: 部署模式。
        :type ha_mode: str
        :param pay_info: 
        :type pay_info: :class:`huaweicloudsdkgaussdb.v3.SrCreateInstanceRspInstancePayInfo`
        :param enable_ssl: SSL开关。
        :type enable_ssl: bool
        :param status: 实例状态。
        :type status: str
        :param region: 实例所在区域。
        :type region: str
        :param tags_info: 
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.SrCreateInstanceRspInstanceTagsInfo`
        """
        
        

        self._id = None
        self._az_code = None
        self._az_mode = None
        self._name = None
        self._engine = None
        self._vpc_id = None
        self._security_group_id = None
        self._sub_net_id = None
        self._db_user = None
        self._port = None
        self._ha_mode = None
        self._pay_info = None
        self._enable_ssl = None
        self._status = None
        self._region = None
        self._tags_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if az_code is not None:
            self.az_code = az_code
        if az_mode is not None:
            self.az_mode = az_mode
        if name is not None:
            self.name = name
        if engine is not None:
            self.engine = engine
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if sub_net_id is not None:
            self.sub_net_id = sub_net_id
        if db_user is not None:
            self.db_user = db_user
        if port is not None:
            self.port = port
        if ha_mode is not None:
            self.ha_mode = ha_mode
        if pay_info is not None:
            self.pay_info = pay_info
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region
        if tags_info is not None:
            self.tags_info = tags_info

    @property
    def id(self):
        """Gets the id of this SrCreateInstanceRspInstance.

        StarRocks实例ID，严格匹配UUID规则。

        :return: The id of this SrCreateInstanceRspInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SrCreateInstanceRspInstance.

        StarRocks实例ID，严格匹配UUID规则。

        :param id: The id of this SrCreateInstanceRspInstance.
        :type id: str
        """
        self._id = id

    @property
    def az_code(self):
        """Gets the az_code of this SrCreateInstanceRspInstance.

        可用区码。

        :return: The az_code of this SrCreateInstanceRspInstance.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this SrCreateInstanceRspInstance.

        可用区码。

        :param az_code: The az_code of this SrCreateInstanceRspInstance.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def az_mode(self):
        """Gets the az_mode of this SrCreateInstanceRspInstance.

        可用区模式。  取值范围：  single：单可用区。  multi：多可用区。

        :return: The az_mode of this SrCreateInstanceRspInstance.
        :rtype: str
        """
        return self._az_mode

    @az_mode.setter
    def az_mode(self, az_mode):
        """Sets the az_mode of this SrCreateInstanceRspInstance.

        可用区模式。  取值范围：  single：单可用区。  multi：多可用区。

        :param az_mode: The az_mode of this SrCreateInstanceRspInstance.
        :type az_mode: str
        """
        self._az_mode = az_mode

    @property
    def name(self):
        """Gets the name of this SrCreateInstanceRspInstance.

        实例名称。

        :return: The name of this SrCreateInstanceRspInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SrCreateInstanceRspInstance.

        实例名称。

        :param name: The name of this SrCreateInstanceRspInstance.
        :type name: str
        """
        self._name = name

    @property
    def engine(self):
        """Gets the engine of this SrCreateInstanceRspInstance.

        :return: The engine of this SrCreateInstanceRspInstance.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SrCreateInstanceRspInstanceEngine`
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this SrCreateInstanceRspInstance.

        :param engine: The engine of this SrCreateInstanceRspInstance.
        :type engine: :class:`huaweicloudsdkgaussdb.v3.SrCreateInstanceRspInstanceEngine`
        """
        self._engine = engine

    @property
    def vpc_id(self):
        """Gets the vpc_id of this SrCreateInstanceRspInstance.

        虚拟私有云ID。

        :return: The vpc_id of this SrCreateInstanceRspInstance.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this SrCreateInstanceRspInstance.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this SrCreateInstanceRspInstance.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this SrCreateInstanceRspInstance.

        安全组ID。

        :return: The security_group_id of this SrCreateInstanceRspInstance.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this SrCreateInstanceRspInstance.

        安全组ID。

        :param security_group_id: The security_group_id of this SrCreateInstanceRspInstance.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def sub_net_id(self):
        """Gets the sub_net_id of this SrCreateInstanceRspInstance.

        子网ID。

        :return: The sub_net_id of this SrCreateInstanceRspInstance.
        :rtype: str
        """
        return self._sub_net_id

    @sub_net_id.setter
    def sub_net_id(self, sub_net_id):
        """Sets the sub_net_id of this SrCreateInstanceRspInstance.

        子网ID。

        :param sub_net_id: The sub_net_id of this SrCreateInstanceRspInstance.
        :type sub_net_id: str
        """
        self._sub_net_id = sub_net_id

    @property
    def db_user(self):
        """Gets the db_user of this SrCreateInstanceRspInstance.

        数据库用户。默认root。

        :return: The db_user of this SrCreateInstanceRspInstance.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        """Sets the db_user of this SrCreateInstanceRspInstance.

        数据库用户。默认root。

        :param db_user: The db_user of this SrCreateInstanceRspInstance.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def port(self):
        """Gets the port of this SrCreateInstanceRspInstance.

        数据库端口号。默认3306。

        :return: The port of this SrCreateInstanceRspInstance.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SrCreateInstanceRspInstance.

        数据库端口号。默认3306。

        :param port: The port of this SrCreateInstanceRspInstance.
        :type port: int
        """
        self._port = port

    @property
    def ha_mode(self):
        """Gets the ha_mode of this SrCreateInstanceRspInstance.

        部署模式。

        :return: The ha_mode of this SrCreateInstanceRspInstance.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        """Sets the ha_mode of this SrCreateInstanceRspInstance.

        部署模式。

        :param ha_mode: The ha_mode of this SrCreateInstanceRspInstance.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def pay_info(self):
        """Gets the pay_info of this SrCreateInstanceRspInstance.

        :return: The pay_info of this SrCreateInstanceRspInstance.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SrCreateInstanceRspInstancePayInfo`
        """
        return self._pay_info

    @pay_info.setter
    def pay_info(self, pay_info):
        """Sets the pay_info of this SrCreateInstanceRspInstance.

        :param pay_info: The pay_info of this SrCreateInstanceRspInstance.
        :type pay_info: :class:`huaweicloudsdkgaussdb.v3.SrCreateInstanceRspInstancePayInfo`
        """
        self._pay_info = pay_info

    @property
    def enable_ssl(self):
        """Gets the enable_ssl of this SrCreateInstanceRspInstance.

        SSL开关。

        :return: The enable_ssl of this SrCreateInstanceRspInstance.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """Sets the enable_ssl of this SrCreateInstanceRspInstance.

        SSL开关。

        :param enable_ssl: The enable_ssl of this SrCreateInstanceRspInstance.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def status(self):
        """Gets the status of this SrCreateInstanceRspInstance.

        实例状态。

        :return: The status of this SrCreateInstanceRspInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SrCreateInstanceRspInstance.

        实例状态。

        :param status: The status of this SrCreateInstanceRspInstance.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        """Gets the region of this SrCreateInstanceRspInstance.

        实例所在区域。

        :return: The region of this SrCreateInstanceRspInstance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SrCreateInstanceRspInstance.

        实例所在区域。

        :param region: The region of this SrCreateInstanceRspInstance.
        :type region: str
        """
        self._region = region

    @property
    def tags_info(self):
        """Gets the tags_info of this SrCreateInstanceRspInstance.

        :return: The tags_info of this SrCreateInstanceRspInstance.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SrCreateInstanceRspInstanceTagsInfo`
        """
        return self._tags_info

    @tags_info.setter
    def tags_info(self, tags_info):
        """Sets the tags_info of this SrCreateInstanceRspInstance.

        :param tags_info: The tags_info of this SrCreateInstanceRspInstance.
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.SrCreateInstanceRspInstanceTagsInfo`
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
        if not isinstance(other, SrCreateInstanceRspInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
