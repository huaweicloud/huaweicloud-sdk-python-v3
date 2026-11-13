# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupabaseInstanceCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore': 'SupabaseDatastore',
        'charge_info': 'ChargeInfo',
        'flavor_ref': 'str',
        'volume': 'SupabaseVolumeConfig',
        'availability_zone': 'str',
        'configuration_id': 'str',
        'port': 'int',
        'security_group_id': 'str',
        'password': 'str',
        'data_vip': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[TagWithKeyValue]'
    }

    attribute_map = {
        'datastore': 'datastore',
        'charge_info': 'charge_info',
        'flavor_ref': 'flavor_ref',
        'volume': 'volume',
        'availability_zone': 'availability_zone',
        'configuration_id': 'configuration_id',
        'port': 'port',
        'security_group_id': 'security_group_id',
        'password': 'password',
        'data_vip': 'data_vip',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, datastore=None, charge_info=None, flavor_ref=None, volume=None, availability_zone=None, configuration_id=None, port=None, security_group_id=None, password=None, data_vip=None, enterprise_project_id=None, tags=None):
        r"""SupabaseInstanceCreateRequest

        The model defined in huaweicloud sdk

        :param datastore: 
        :type datastore: :class:`huaweicloudsdkrds.v3.SupabaseDatastore`
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkrds.v3.ChargeInfo`
        :param flavor_ref: PG实例规格码。
        :type flavor_ref: str
        :param volume: 
        :type volume: :class:`huaweicloudsdkrds.v3.SupabaseVolumeConfig`
        :param availability_zone: 可用区，Single模式下为1个，需与顶层主AZ一致。
        :type availability_zone: str
        :param configuration_id: 参数模板ID（可选）。
        :type configuration_id: str
        :param port: 数据库端口，2100~9500，默认5432。
        :type port: int
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param password: 数据库密码。
        :type password: str
        :param data_vip: 内网IP（可选）。
        :type data_vip: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param tags: 标签列表，最多20个。
        :type tags: list[:class:`huaweicloudsdkrds.v3.TagWithKeyValue`]
        """
        
        

        self._datastore = None
        self._charge_info = None
        self._flavor_ref = None
        self._volume = None
        self._availability_zone = None
        self._configuration_id = None
        self._port = None
        self._security_group_id = None
        self._password = None
        self._data_vip = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        self.datastore = datastore
        self.charge_info = charge_info
        self.flavor_ref = flavor_ref
        self.volume = volume
        self.availability_zone = availability_zone
        if configuration_id is not None:
            self.configuration_id = configuration_id
        if port is not None:
            self.port = port
        self.security_group_id = security_group_id
        self.password = password
        if data_vip is not None:
            self.data_vip = data_vip
        self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def datastore(self):
        r"""Gets the datastore of this SupabaseInstanceCreateRequest.

        :return: The datastore of this SupabaseInstanceCreateRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this SupabaseInstanceCreateRequest.

        :param datastore: The datastore of this SupabaseInstanceCreateRequest.
        :type datastore: :class:`huaweicloudsdkrds.v3.SupabaseDatastore`
        """
        self._datastore = datastore

    @property
    def charge_info(self):
        r"""Gets the charge_info of this SupabaseInstanceCreateRequest.

        :return: The charge_info of this SupabaseInstanceCreateRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this SupabaseInstanceCreateRequest.

        :param charge_info: The charge_info of this SupabaseInstanceCreateRequest.
        :type charge_info: :class:`huaweicloudsdkrds.v3.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this SupabaseInstanceCreateRequest.

        PG实例规格码。

        :return: The flavor_ref of this SupabaseInstanceCreateRequest.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this SupabaseInstanceCreateRequest.

        PG实例规格码。

        :param flavor_ref: The flavor_ref of this SupabaseInstanceCreateRequest.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def volume(self):
        r"""Gets the volume of this SupabaseInstanceCreateRequest.

        :return: The volume of this SupabaseInstanceCreateRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseVolumeConfig`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this SupabaseInstanceCreateRequest.

        :param volume: The volume of this SupabaseInstanceCreateRequest.
        :type volume: :class:`huaweicloudsdkrds.v3.SupabaseVolumeConfig`
        """
        self._volume = volume

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this SupabaseInstanceCreateRequest.

        可用区，Single模式下为1个，需与顶层主AZ一致。

        :return: The availability_zone of this SupabaseInstanceCreateRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this SupabaseInstanceCreateRequest.

        可用区，Single模式下为1个，需与顶层主AZ一致。

        :param availability_zone: The availability_zone of this SupabaseInstanceCreateRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def configuration_id(self):
        r"""Gets the configuration_id of this SupabaseInstanceCreateRequest.

        参数模板ID（可选）。

        :return: The configuration_id of this SupabaseInstanceCreateRequest.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        r"""Sets the configuration_id of this SupabaseInstanceCreateRequest.

        参数模板ID（可选）。

        :param configuration_id: The configuration_id of this SupabaseInstanceCreateRequest.
        :type configuration_id: str
        """
        self._configuration_id = configuration_id

    @property
    def port(self):
        r"""Gets the port of this SupabaseInstanceCreateRequest.

        数据库端口，2100~9500，默认5432。

        :return: The port of this SupabaseInstanceCreateRequest.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this SupabaseInstanceCreateRequest.

        数据库端口，2100~9500，默认5432。

        :param port: The port of this SupabaseInstanceCreateRequest.
        :type port: int
        """
        self._port = port

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this SupabaseInstanceCreateRequest.

        安全组ID。

        :return: The security_group_id of this SupabaseInstanceCreateRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this SupabaseInstanceCreateRequest.

        安全组ID。

        :param security_group_id: The security_group_id of this SupabaseInstanceCreateRequest.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def password(self):
        r"""Gets the password of this SupabaseInstanceCreateRequest.

        数据库密码。

        :return: The password of this SupabaseInstanceCreateRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this SupabaseInstanceCreateRequest.

        数据库密码。

        :param password: The password of this SupabaseInstanceCreateRequest.
        :type password: str
        """
        self._password = password

    @property
    def data_vip(self):
        r"""Gets the data_vip of this SupabaseInstanceCreateRequest.

        内网IP（可选）。

        :return: The data_vip of this SupabaseInstanceCreateRequest.
        :rtype: str
        """
        return self._data_vip

    @data_vip.setter
    def data_vip(self, data_vip):
        r"""Sets the data_vip of this SupabaseInstanceCreateRequest.

        内网IP（可选）。

        :param data_vip: The data_vip of this SupabaseInstanceCreateRequest.
        :type data_vip: str
        """
        self._data_vip = data_vip

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SupabaseInstanceCreateRequest.

        企业项目ID。

        :return: The enterprise_project_id of this SupabaseInstanceCreateRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SupabaseInstanceCreateRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this SupabaseInstanceCreateRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this SupabaseInstanceCreateRequest.

        标签列表，最多20个。

        :return: The tags of this SupabaseInstanceCreateRequest.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TagWithKeyValue`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SupabaseInstanceCreateRequest.

        标签列表，最多20个。

        :param tags: The tags of this SupabaseInstanceCreateRequest.
        :type tags: list[:class:`huaweicloudsdkrds.v3.TagWithKeyValue`]
        """
        self._tags = tags

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
        if not isinstance(other, SupabaseInstanceCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
