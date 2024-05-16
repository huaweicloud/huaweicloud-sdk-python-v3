# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StarRocksCreateRequest:

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
        'engine': 'StarRocksCreateRequestEngine',
        'ha': 'StarRocksCreateRequestHa',
        'fe_flavor_id': 'str',
        'be_flavor_id': 'str',
        'db_root_pwd': 'str',
        'fe_count': 'int',
        'be_count': 'int',
        'az_mode': 'str',
        'fe_volume': 'StarRocksCreateRequestFeVolume',
        'be_volume': 'StarRocksCreateRequestBeVolume',
        'az_code': 'str',
        'time_zone': 'str',
        'tags_info': 'StarRocksCreateRequestTagsInfo'
    }

    attribute_map = {
        'name': 'name',
        'engine': 'engine',
        'ha': 'ha',
        'fe_flavor_id': 'fe_flavor_id',
        'be_flavor_id': 'be_flavor_id',
        'db_root_pwd': 'db_root_pwd',
        'fe_count': 'fe_count',
        'be_count': 'be_count',
        'az_mode': 'az_mode',
        'fe_volume': 'fe_volume',
        'be_volume': 'be_volume',
        'az_code': 'az_code',
        'time_zone': 'time_zone',
        'tags_info': 'tags_info'
    }

    def __init__(self, name=None, engine=None, ha=None, fe_flavor_id=None, be_flavor_id=None, db_root_pwd=None, fe_count=None, be_count=None, az_mode=None, fe_volume=None, be_volume=None, az_code=None, time_zone=None, tags_info=None):
        """StarRocksCreateRequest

        The model defined in huaweicloud sdk

        :param name: 实例名称。同一租户下，同类型的实例名可重名。  取值范围：最小为4个字符，最大为64个字符且不超过64个字节，必须以字母开头，区分大小写，可以包含字母、数字、中划线、下划线，不能包含其他特殊字符。不支持中文名。
        :type name: str
        :param engine: 
        :type engine: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestEngine`
        :param ha: 
        :type ha: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestHa`
        :param fe_flavor_id: FE节点规格ID。使用可通过查询HTAP规格响应消息中的“id”。
        :type fe_flavor_id: str
        :param be_flavor_id: BE节点规格ID。使用可通过查询HTAP规格响应消息中的“id”。
        :type be_flavor_id: str
        :param db_root_pwd: 数据库密码。  取值范围：至少包含以下字符的三种：大小写字母、数字和特殊符号~!@#$%^*-_&#x3D;+?,()&amp;|.，长度8~32个字符。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。如果您输入弱密码，系统会自动判定密码非法。
        :type db_root_pwd: str
        :param fe_count: FE节点数。 - 单机时固定为1 - 集群时取值[3, 10]
        :type fe_count: int
        :param be_count: BE节点数。 - 单机时固定为1 - 集群时取值[3, 10]
        :type be_count: int
        :param az_mode: 可用区类型。 当前仅支持single。
        :type az_mode: str
        :param fe_volume: 
        :type fe_volume: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestFeVolume`
        :param be_volume: 
        :type be_volume: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestBeVolume`
        :param az_code: 可用区代码。
        :type az_code: str
        :param time_zone: 时区。默认时区为UTC+08:00。
        :type time_zone: str
        :param tags_info: 
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestTagsInfo`
        """
        
        

        self._name = None
        self._engine = None
        self._ha = None
        self._fe_flavor_id = None
        self._be_flavor_id = None
        self._db_root_pwd = None
        self._fe_count = None
        self._be_count = None
        self._az_mode = None
        self._fe_volume = None
        self._be_volume = None
        self._az_code = None
        self._time_zone = None
        self._tags_info = None
        self.discriminator = None

        self.name = name
        self.engine = engine
        self.ha = ha
        self.fe_flavor_id = fe_flavor_id
        self.be_flavor_id = be_flavor_id
        self.db_root_pwd = db_root_pwd
        self.fe_count = fe_count
        self.be_count = be_count
        self.az_mode = az_mode
        self.fe_volume = fe_volume
        self.be_volume = be_volume
        self.az_code = az_code
        if time_zone is not None:
            self.time_zone = time_zone
        self.tags_info = tags_info

    @property
    def name(self):
        """Gets the name of this StarRocksCreateRequest.

        实例名称。同一租户下，同类型的实例名可重名。  取值范围：最小为4个字符，最大为64个字符且不超过64个字节，必须以字母开头，区分大小写，可以包含字母、数字、中划线、下划线，不能包含其他特殊字符。不支持中文名。

        :return: The name of this StarRocksCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StarRocksCreateRequest.

        实例名称。同一租户下，同类型的实例名可重名。  取值范围：最小为4个字符，最大为64个字符且不超过64个字节，必须以字母开头，区分大小写，可以包含字母、数字、中划线、下划线，不能包含其他特殊字符。不支持中文名。

        :param name: The name of this StarRocksCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def engine(self):
        """Gets the engine of this StarRocksCreateRequest.

        :return: The engine of this StarRocksCreateRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestEngine`
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this StarRocksCreateRequest.

        :param engine: The engine of this StarRocksCreateRequest.
        :type engine: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestEngine`
        """
        self._engine = engine

    @property
    def ha(self):
        """Gets the ha of this StarRocksCreateRequest.

        :return: The ha of this StarRocksCreateRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestHa`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this StarRocksCreateRequest.

        :param ha: The ha of this StarRocksCreateRequest.
        :type ha: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestHa`
        """
        self._ha = ha

    @property
    def fe_flavor_id(self):
        """Gets the fe_flavor_id of this StarRocksCreateRequest.

        FE节点规格ID。使用可通过查询HTAP规格响应消息中的“id”。

        :return: The fe_flavor_id of this StarRocksCreateRequest.
        :rtype: str
        """
        return self._fe_flavor_id

    @fe_flavor_id.setter
    def fe_flavor_id(self, fe_flavor_id):
        """Sets the fe_flavor_id of this StarRocksCreateRequest.

        FE节点规格ID。使用可通过查询HTAP规格响应消息中的“id”。

        :param fe_flavor_id: The fe_flavor_id of this StarRocksCreateRequest.
        :type fe_flavor_id: str
        """
        self._fe_flavor_id = fe_flavor_id

    @property
    def be_flavor_id(self):
        """Gets the be_flavor_id of this StarRocksCreateRequest.

        BE节点规格ID。使用可通过查询HTAP规格响应消息中的“id”。

        :return: The be_flavor_id of this StarRocksCreateRequest.
        :rtype: str
        """
        return self._be_flavor_id

    @be_flavor_id.setter
    def be_flavor_id(self, be_flavor_id):
        """Sets the be_flavor_id of this StarRocksCreateRequest.

        BE节点规格ID。使用可通过查询HTAP规格响应消息中的“id”。

        :param be_flavor_id: The be_flavor_id of this StarRocksCreateRequest.
        :type be_flavor_id: str
        """
        self._be_flavor_id = be_flavor_id

    @property
    def db_root_pwd(self):
        """Gets the db_root_pwd of this StarRocksCreateRequest.

        数据库密码。  取值范围：至少包含以下字符的三种：大小写字母、数字和特殊符号~!@#$%^*-_=+?,()&|.，长度8~32个字符。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。如果您输入弱密码，系统会自动判定密码非法。

        :return: The db_root_pwd of this StarRocksCreateRequest.
        :rtype: str
        """
        return self._db_root_pwd

    @db_root_pwd.setter
    def db_root_pwd(self, db_root_pwd):
        """Sets the db_root_pwd of this StarRocksCreateRequest.

        数据库密码。  取值范围：至少包含以下字符的三种：大小写字母、数字和特殊符号~!@#$%^*-_=+?,()&|.，长度8~32个字符。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。如果您输入弱密码，系统会自动判定密码非法。

        :param db_root_pwd: The db_root_pwd of this StarRocksCreateRequest.
        :type db_root_pwd: str
        """
        self._db_root_pwd = db_root_pwd

    @property
    def fe_count(self):
        """Gets the fe_count of this StarRocksCreateRequest.

        FE节点数。 - 单机时固定为1 - 集群时取值[3, 10]

        :return: The fe_count of this StarRocksCreateRequest.
        :rtype: int
        """
        return self._fe_count

    @fe_count.setter
    def fe_count(self, fe_count):
        """Sets the fe_count of this StarRocksCreateRequest.

        FE节点数。 - 单机时固定为1 - 集群时取值[3, 10]

        :param fe_count: The fe_count of this StarRocksCreateRequest.
        :type fe_count: int
        """
        self._fe_count = fe_count

    @property
    def be_count(self):
        """Gets the be_count of this StarRocksCreateRequest.

        BE节点数。 - 单机时固定为1 - 集群时取值[3, 10]

        :return: The be_count of this StarRocksCreateRequest.
        :rtype: int
        """
        return self._be_count

    @be_count.setter
    def be_count(self, be_count):
        """Sets the be_count of this StarRocksCreateRequest.

        BE节点数。 - 单机时固定为1 - 集群时取值[3, 10]

        :param be_count: The be_count of this StarRocksCreateRequest.
        :type be_count: int
        """
        self._be_count = be_count

    @property
    def az_mode(self):
        """Gets the az_mode of this StarRocksCreateRequest.

        可用区类型。 当前仅支持single。

        :return: The az_mode of this StarRocksCreateRequest.
        :rtype: str
        """
        return self._az_mode

    @az_mode.setter
    def az_mode(self, az_mode):
        """Sets the az_mode of this StarRocksCreateRequest.

        可用区类型。 当前仅支持single。

        :param az_mode: The az_mode of this StarRocksCreateRequest.
        :type az_mode: str
        """
        self._az_mode = az_mode

    @property
    def fe_volume(self):
        """Gets the fe_volume of this StarRocksCreateRequest.

        :return: The fe_volume of this StarRocksCreateRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestFeVolume`
        """
        return self._fe_volume

    @fe_volume.setter
    def fe_volume(self, fe_volume):
        """Sets the fe_volume of this StarRocksCreateRequest.

        :param fe_volume: The fe_volume of this StarRocksCreateRequest.
        :type fe_volume: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestFeVolume`
        """
        self._fe_volume = fe_volume

    @property
    def be_volume(self):
        """Gets the be_volume of this StarRocksCreateRequest.

        :return: The be_volume of this StarRocksCreateRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestBeVolume`
        """
        return self._be_volume

    @be_volume.setter
    def be_volume(self, be_volume):
        """Sets the be_volume of this StarRocksCreateRequest.

        :param be_volume: The be_volume of this StarRocksCreateRequest.
        :type be_volume: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestBeVolume`
        """
        self._be_volume = be_volume

    @property
    def az_code(self):
        """Gets the az_code of this StarRocksCreateRequest.

        可用区代码。

        :return: The az_code of this StarRocksCreateRequest.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this StarRocksCreateRequest.

        可用区代码。

        :param az_code: The az_code of this StarRocksCreateRequest.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def time_zone(self):
        """Gets the time_zone of this StarRocksCreateRequest.

        时区。默认时区为UTC+08:00。

        :return: The time_zone of this StarRocksCreateRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this StarRocksCreateRequest.

        时区。默认时区为UTC+08:00。

        :param time_zone: The time_zone of this StarRocksCreateRequest.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def tags_info(self):
        """Gets the tags_info of this StarRocksCreateRequest.

        :return: The tags_info of this StarRocksCreateRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestTagsInfo`
        """
        return self._tags_info

    @tags_info.setter
    def tags_info(self, tags_info):
        """Sets the tags_info of this StarRocksCreateRequest.

        :param tags_info: The tags_info of this StarRocksCreateRequest.
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.StarRocksCreateRequestTagsInfo`
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
        if not isinstance(other, StarRocksCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
