# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateChInstanceRequestBody:

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
        'engine': 'ClickHouseEngineInfo',
        'ha': 'CreateChInstanceRequestBodyHa',
        'flavor_id': 'str',
        'db_root_pwd': 'str',
        'az_mode': 'str',
        'volume': 'CreateChInstanceRequestBodyVolume',
        'az_code': 'str',
        'time_zone': 'str',
        'tags_info': 'CreateChInstanceRequestBodyTagsInfo',
        'pay_info': 'CreateChInstanceRequestBodyPayInfo'
    }

    attribute_map = {
        'name': 'name',
        'engine': 'engine',
        'ha': 'ha',
        'flavor_id': 'flavor_id',
        'db_root_pwd': 'db_root_pwd',
        'az_mode': 'az_mode',
        'volume': 'volume',
        'az_code': 'az_code',
        'time_zone': 'time_zone',
        'tags_info': 'tags_info',
        'pay_info': 'pay_info'
    }

    def __init__(self, name=None, engine=None, ha=None, flavor_id=None, db_root_pwd=None, az_mode=None, volume=None, az_code=None, time_zone=None, tags_info=None, pay_info=None):
        r"""CreateChInstanceRequestBody

        The model defined in huaweicloud sdk

        :param name: ClickHouse实例名称。 - 4位到64位之间 - 必须以字母开头，可以包含字母、数字、中划线或下划线 - 不能包含其他特殊字符
        :type name: str
        :param engine: 
        :type engine: :class:`huaweicloudsdkgaussdb.v3.ClickHouseEngineInfo`
        :param ha: 
        :type ha: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyHa`
        :param flavor_id: 节点规格ID，可通过“HTAP查询规格信息”获取。
        :type flavor_id: str
        :param db_root_pwd: root账户密码。 - 8~32个字符 - 包含大写字母、小写字母、数字或特殊字符(~ ! @ # % ^ * - _ &#x3D; + ? ,)中的三种
        :type db_root_pwd: str
        :param az_mode: 可用区类型。 取值范围： - single：单可用区 - double：多可用区
        :type az_mode: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyVolume`
        :param az_code: 可用区码。  当ha中mode为Ha时，需要填写多个可用区，用\&quot;,\&quot; 分隔。例如：cn-southwest-244b,cn-southwest-244a
        :type az_code: str
        :param time_zone: 时区。默认为所属TaurusDB实例时区。
        :type time_zone: str
        :param tags_info: 
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyTagsInfo`
        :param pay_info: 
        :type pay_info: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyPayInfo`
        """
        
        

        self._name = None
        self._engine = None
        self._ha = None
        self._flavor_id = None
        self._db_root_pwd = None
        self._az_mode = None
        self._volume = None
        self._az_code = None
        self._time_zone = None
        self._tags_info = None
        self._pay_info = None
        self.discriminator = None

        self.name = name
        self.engine = engine
        self.ha = ha
        self.flavor_id = flavor_id
        self.db_root_pwd = db_root_pwd
        self.az_mode = az_mode
        self.volume = volume
        self.az_code = az_code
        if time_zone is not None:
            self.time_zone = time_zone
        self.tags_info = tags_info
        if pay_info is not None:
            self.pay_info = pay_info

    @property
    def name(self):
        r"""Gets the name of this CreateChInstanceRequestBody.

        ClickHouse实例名称。 - 4位到64位之间 - 必须以字母开头，可以包含字母、数字、中划线或下划线 - 不能包含其他特殊字符

        :return: The name of this CreateChInstanceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateChInstanceRequestBody.

        ClickHouse实例名称。 - 4位到64位之间 - 必须以字母开头，可以包含字母、数字、中划线或下划线 - 不能包含其他特殊字符

        :param name: The name of this CreateChInstanceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def engine(self):
        r"""Gets the engine of this CreateChInstanceRequestBody.

        :return: The engine of this CreateChInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ClickHouseEngineInfo`
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this CreateChInstanceRequestBody.

        :param engine: The engine of this CreateChInstanceRequestBody.
        :type engine: :class:`huaweicloudsdkgaussdb.v3.ClickHouseEngineInfo`
        """
        self._engine = engine

    @property
    def ha(self):
        r"""Gets the ha of this CreateChInstanceRequestBody.

        :return: The ha of this CreateChInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyHa`
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        r"""Sets the ha of this CreateChInstanceRequestBody.

        :param ha: The ha of this CreateChInstanceRequestBody.
        :type ha: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyHa`
        """
        self._ha = ha

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this CreateChInstanceRequestBody.

        节点规格ID，可通过“HTAP查询规格信息”获取。

        :return: The flavor_id of this CreateChInstanceRequestBody.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this CreateChInstanceRequestBody.

        节点规格ID，可通过“HTAP查询规格信息”获取。

        :param flavor_id: The flavor_id of this CreateChInstanceRequestBody.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def db_root_pwd(self):
        r"""Gets the db_root_pwd of this CreateChInstanceRequestBody.

        root账户密码。 - 8~32个字符 - 包含大写字母、小写字母、数字或特殊字符(~ ! @ # % ^ * - _ = + ? ,)中的三种

        :return: The db_root_pwd of this CreateChInstanceRequestBody.
        :rtype: str
        """
        return self._db_root_pwd

    @db_root_pwd.setter
    def db_root_pwd(self, db_root_pwd):
        r"""Sets the db_root_pwd of this CreateChInstanceRequestBody.

        root账户密码。 - 8~32个字符 - 包含大写字母、小写字母、数字或特殊字符(~ ! @ # % ^ * - _ = + ? ,)中的三种

        :param db_root_pwd: The db_root_pwd of this CreateChInstanceRequestBody.
        :type db_root_pwd: str
        """
        self._db_root_pwd = db_root_pwd

    @property
    def az_mode(self):
        r"""Gets the az_mode of this CreateChInstanceRequestBody.

        可用区类型。 取值范围： - single：单可用区 - double：多可用区

        :return: The az_mode of this CreateChInstanceRequestBody.
        :rtype: str
        """
        return self._az_mode

    @az_mode.setter
    def az_mode(self, az_mode):
        r"""Sets the az_mode of this CreateChInstanceRequestBody.

        可用区类型。 取值范围： - single：单可用区 - double：多可用区

        :param az_mode: The az_mode of this CreateChInstanceRequestBody.
        :type az_mode: str
        """
        self._az_mode = az_mode

    @property
    def volume(self):
        r"""Gets the volume of this CreateChInstanceRequestBody.

        :return: The volume of this CreateChInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyVolume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this CreateChInstanceRequestBody.

        :param volume: The volume of this CreateChInstanceRequestBody.
        :type volume: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyVolume`
        """
        self._volume = volume

    @property
    def az_code(self):
        r"""Gets the az_code of this CreateChInstanceRequestBody.

        可用区码。  当ha中mode为Ha时，需要填写多个可用区，用\",\" 分隔。例如：cn-southwest-244b,cn-southwest-244a

        :return: The az_code of this CreateChInstanceRequestBody.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this CreateChInstanceRequestBody.

        可用区码。  当ha中mode为Ha时，需要填写多个可用区，用\",\" 分隔。例如：cn-southwest-244b,cn-southwest-244a

        :param az_code: The az_code of this CreateChInstanceRequestBody.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def time_zone(self):
        r"""Gets the time_zone of this CreateChInstanceRequestBody.

        时区。默认为所属TaurusDB实例时区。

        :return: The time_zone of this CreateChInstanceRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this CreateChInstanceRequestBody.

        时区。默认为所属TaurusDB实例时区。

        :param time_zone: The time_zone of this CreateChInstanceRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def tags_info(self):
        r"""Gets the tags_info of this CreateChInstanceRequestBody.

        :return: The tags_info of this CreateChInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyTagsInfo`
        """
        return self._tags_info

    @tags_info.setter
    def tags_info(self, tags_info):
        r"""Sets the tags_info of this CreateChInstanceRequestBody.

        :param tags_info: The tags_info of this CreateChInstanceRequestBody.
        :type tags_info: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyTagsInfo`
        """
        self._tags_info = tags_info

    @property
    def pay_info(self):
        r"""Gets the pay_info of this CreateChInstanceRequestBody.

        :return: The pay_info of this CreateChInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyPayInfo`
        """
        return self._pay_info

    @pay_info.setter
    def pay_info(self, pay_info):
        r"""Sets the pay_info of this CreateChInstanceRequestBody.

        :param pay_info: The pay_info of this CreateChInstanceRequestBody.
        :type pay_info: :class:`huaweicloudsdkgaussdb.v3.CreateChInstanceRequestBodyPayInfo`
        """
        self._pay_info = pay_info

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
        if not isinstance(other, CreateChInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
