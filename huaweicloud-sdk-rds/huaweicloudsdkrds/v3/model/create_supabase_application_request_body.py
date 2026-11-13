# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSupabaseApplicationRequestBody:

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
        'basic_config': 'SupabaseAppBasicConfig',
        'version': 'str',
        'mode': 'str',
        'flavor_ref': 'str',
        'availability_zone': 'str',
        'data_vip': 'str',
        'security_group_id': 'str',
        'password': 'str',
        'storage_component': 'SupabaseStorageComponentConfig',
        'manage_type': 'str',
        'managed_instance': 'SupabaseInstanceCreateRequest',
        'existing_instance': 'SupabaseExistingInstanceRequest'
    }

    attribute_map = {
        'name': 'name',
        'basic_config': 'basic_config',
        'version': 'version',
        'mode': 'mode',
        'flavor_ref': 'flavor_ref',
        'availability_zone': 'availability_zone',
        'data_vip': 'data_vip',
        'security_group_id': 'security_group_id',
        'password': 'password',
        'storage_component': 'storage_component',
        'manage_type': 'manage_type',
        'managed_instance': 'managed_instance',
        'existing_instance': 'existing_instance'
    }

    def __init__(self, name=None, basic_config=None, version=None, mode=None, flavor_ref=None, availability_zone=None, data_vip=None, security_group_id=None, password=None, storage_component=None, manage_type=None, managed_instance=None, existing_instance=None):
        r"""CreateSupabaseApplicationRequestBody

        The model defined in huaweicloud sdk

        :param name: Supabase应用名称，4~64个字符。
        :type name: str
        :param basic_config: 
        :type basic_config: :class:`huaweicloudsdkrds.v3.SupabaseAppBasicConfig`
        :param version: Supabase版本号，格式 x.y.z。
        :type version: str
        :param mode: 部署模式。当前仅支持Single。
        :type mode: str
        :param flavor_ref: 规格码，格式 rds.supabase.{...}。
        :type flavor_ref: str
        :param availability_zone: 可用区ID。Single模式下为1个可用区。
        :type availability_zone: str
        :param data_vip: 指定实例内网IP（可选）。IPv4格式。
        :type data_vip: str
        :param security_group_id: 指定实例所属安全组（可选）。UUID格式。
        :type security_group_id: str
        :param password: 默认用户supabase的密码。
        :type password: str
        :param storage_component: 
        :type storage_component: :class:`huaweicloudsdkrds.v3.SupabaseStorageComponentConfig`
        :param manage_type: 实例纳管方式。默认newly_instance。
        :type manage_type: str
        :param managed_instance: 
        :type managed_instance: :class:`huaweicloudsdkrds.v3.SupabaseInstanceCreateRequest`
        :param existing_instance: 
        :type existing_instance: :class:`huaweicloudsdkrds.v3.SupabaseExistingInstanceRequest`
        """
        
        

        self._name = None
        self._basic_config = None
        self._version = None
        self._mode = None
        self._flavor_ref = None
        self._availability_zone = None
        self._data_vip = None
        self._security_group_id = None
        self._password = None
        self._storage_component = None
        self._manage_type = None
        self._managed_instance = None
        self._existing_instance = None
        self.discriminator = None

        self.name = name
        self.basic_config = basic_config
        self.version = version
        self.mode = mode
        self.flavor_ref = flavor_ref
        self.availability_zone = availability_zone
        if data_vip is not None:
            self.data_vip = data_vip
        if security_group_id is not None:
            self.security_group_id = security_group_id
        self.password = password
        self.storage_component = storage_component
        if manage_type is not None:
            self.manage_type = manage_type
        if managed_instance is not None:
            self.managed_instance = managed_instance
        if existing_instance is not None:
            self.existing_instance = existing_instance

    @property
    def name(self):
        r"""Gets the name of this CreateSupabaseApplicationRequestBody.

        Supabase应用名称，4~64个字符。

        :return: The name of this CreateSupabaseApplicationRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSupabaseApplicationRequestBody.

        Supabase应用名称，4~64个字符。

        :param name: The name of this CreateSupabaseApplicationRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def basic_config(self):
        r"""Gets the basic_config of this CreateSupabaseApplicationRequestBody.

        :return: The basic_config of this CreateSupabaseApplicationRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseAppBasicConfig`
        """
        return self._basic_config

    @basic_config.setter
    def basic_config(self, basic_config):
        r"""Sets the basic_config of this CreateSupabaseApplicationRequestBody.

        :param basic_config: The basic_config of this CreateSupabaseApplicationRequestBody.
        :type basic_config: :class:`huaweicloudsdkrds.v3.SupabaseAppBasicConfig`
        """
        self._basic_config = basic_config

    @property
    def version(self):
        r"""Gets the version of this CreateSupabaseApplicationRequestBody.

        Supabase版本号，格式 x.y.z。

        :return: The version of this CreateSupabaseApplicationRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateSupabaseApplicationRequestBody.

        Supabase版本号，格式 x.y.z。

        :param version: The version of this CreateSupabaseApplicationRequestBody.
        :type version: str
        """
        self._version = version

    @property
    def mode(self):
        r"""Gets the mode of this CreateSupabaseApplicationRequestBody.

        部署模式。当前仅支持Single。

        :return: The mode of this CreateSupabaseApplicationRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateSupabaseApplicationRequestBody.

        部署模式。当前仅支持Single。

        :param mode: The mode of this CreateSupabaseApplicationRequestBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this CreateSupabaseApplicationRequestBody.

        规格码，格式 rds.supabase.{...}。

        :return: The flavor_ref of this CreateSupabaseApplicationRequestBody.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this CreateSupabaseApplicationRequestBody.

        规格码，格式 rds.supabase.{...}。

        :param flavor_ref: The flavor_ref of this CreateSupabaseApplicationRequestBody.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateSupabaseApplicationRequestBody.

        可用区ID。Single模式下为1个可用区。

        :return: The availability_zone of this CreateSupabaseApplicationRequestBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateSupabaseApplicationRequestBody.

        可用区ID。Single模式下为1个可用区。

        :param availability_zone: The availability_zone of this CreateSupabaseApplicationRequestBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def data_vip(self):
        r"""Gets the data_vip of this CreateSupabaseApplicationRequestBody.

        指定实例内网IP（可选）。IPv4格式。

        :return: The data_vip of this CreateSupabaseApplicationRequestBody.
        :rtype: str
        """
        return self._data_vip

    @data_vip.setter
    def data_vip(self, data_vip):
        r"""Sets the data_vip of this CreateSupabaseApplicationRequestBody.

        指定实例内网IP（可选）。IPv4格式。

        :param data_vip: The data_vip of this CreateSupabaseApplicationRequestBody.
        :type data_vip: str
        """
        self._data_vip = data_vip

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this CreateSupabaseApplicationRequestBody.

        指定实例所属安全组（可选）。UUID格式。

        :return: The security_group_id of this CreateSupabaseApplicationRequestBody.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this CreateSupabaseApplicationRequestBody.

        指定实例所属安全组（可选）。UUID格式。

        :param security_group_id: The security_group_id of this CreateSupabaseApplicationRequestBody.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def password(self):
        r"""Gets the password of this CreateSupabaseApplicationRequestBody.

        默认用户supabase的密码。

        :return: The password of this CreateSupabaseApplicationRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this CreateSupabaseApplicationRequestBody.

        默认用户supabase的密码。

        :param password: The password of this CreateSupabaseApplicationRequestBody.
        :type password: str
        """
        self._password = password

    @property
    def storage_component(self):
        r"""Gets the storage_component of this CreateSupabaseApplicationRequestBody.

        :return: The storage_component of this CreateSupabaseApplicationRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseStorageComponentConfig`
        """
        return self._storage_component

    @storage_component.setter
    def storage_component(self, storage_component):
        r"""Sets the storage_component of this CreateSupabaseApplicationRequestBody.

        :param storage_component: The storage_component of this CreateSupabaseApplicationRequestBody.
        :type storage_component: :class:`huaweicloudsdkrds.v3.SupabaseStorageComponentConfig`
        """
        self._storage_component = storage_component

    @property
    def manage_type(self):
        r"""Gets the manage_type of this CreateSupabaseApplicationRequestBody.

        实例纳管方式。默认newly_instance。

        :return: The manage_type of this CreateSupabaseApplicationRequestBody.
        :rtype: str
        """
        return self._manage_type

    @manage_type.setter
    def manage_type(self, manage_type):
        r"""Sets the manage_type of this CreateSupabaseApplicationRequestBody.

        实例纳管方式。默认newly_instance。

        :param manage_type: The manage_type of this CreateSupabaseApplicationRequestBody.
        :type manage_type: str
        """
        self._manage_type = manage_type

    @property
    def managed_instance(self):
        r"""Gets the managed_instance of this CreateSupabaseApplicationRequestBody.

        :return: The managed_instance of this CreateSupabaseApplicationRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseInstanceCreateRequest`
        """
        return self._managed_instance

    @managed_instance.setter
    def managed_instance(self, managed_instance):
        r"""Sets the managed_instance of this CreateSupabaseApplicationRequestBody.

        :param managed_instance: The managed_instance of this CreateSupabaseApplicationRequestBody.
        :type managed_instance: :class:`huaweicloudsdkrds.v3.SupabaseInstanceCreateRequest`
        """
        self._managed_instance = managed_instance

    @property
    def existing_instance(self):
        r"""Gets the existing_instance of this CreateSupabaseApplicationRequestBody.

        :return: The existing_instance of this CreateSupabaseApplicationRequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.SupabaseExistingInstanceRequest`
        """
        return self._existing_instance

    @existing_instance.setter
    def existing_instance(self, existing_instance):
        r"""Sets the existing_instance of this CreateSupabaseApplicationRequestBody.

        :param existing_instance: The existing_instance of this CreateSupabaseApplicationRequestBody.
        :type existing_instance: :class:`huaweicloudsdkrds.v3.SupabaseExistingInstanceRequest`
        """
        self._existing_instance = existing_instance

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
        if not isinstance(other, CreateSupabaseApplicationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
