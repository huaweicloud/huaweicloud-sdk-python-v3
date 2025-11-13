# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelVendor:

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
        'name_en': 'str',
        'type': 'str',
        'status': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'description': 'str',
        'auth_type': 'str',
        'auth_info': 'VendorAuthInfo',
        'auth_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'name_en': 'name_en',
        'type': 'type',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'description': 'description',
        'auth_type': 'auth_type',
        'auth_info': 'auth_info',
        'auth_url': 'auth_url'
    }

    def __init__(self, id=None, name=None, name_en=None, type=None, status=None, create_time=None, update_time=None, description=None, auth_type=None, auth_info=None, auth_url=None):
        r"""ModelVendor

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type id: str
        :param name: **参数解释**： 模型供应商名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type name: str
        :param name_en: **参数解释**： 模型供应商英文名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type name_en: str
        :param type: **参数解释**： 模型供应商类型。 **约束限制**： 不涉及 **取值范围**： * SYSTEM：预置供应商 * CUSTOM：自定义供应商 **默认取值**： 不涉及 
        :type type: str
        :param status: **参数解释**： 模型服务状态。 **约束限制**： 不涉及 **取值范围**： * AVAILABLE：已接入 * UNAVAILABLE：未接入 **默认取值**： 不涉及 
        :type status: str
        :param create_time: **参数解释**： 模型供应商创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type create_time: str
        :param update_time: **参数解释**： 模型供应商修改时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type update_time: str
        :param description: **参数解释**： 模型供应商描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type description: str
        :param auth_type: **参数解释**： 鉴权类型。 **约束限制**： 不涉及 **取值范围**： * API_KEY：API Key **默认取值**： 不涉及 
        :type auth_type: str
        :param auth_info: 
        :type auth_info: :class:`huaweicloudsdkeihealth.v2.VendorAuthInfo`
        :param auth_url: **参数解释**： 内置供应商获取鉴权信息地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type auth_url: str
        """
        
        

        self._id = None
        self._name = None
        self._name_en = None
        self._type = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._description = None
        self._auth_type = None
        self._auth_info = None
        self._auth_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if name_en is not None:
            self.name_en = name_en
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description
        if auth_type is not None:
            self.auth_type = auth_type
        if auth_info is not None:
            self.auth_info = auth_info
        if auth_url is not None:
            self.auth_url = auth_url

    @property
    def id(self):
        r"""Gets the id of this ModelVendor.

        **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The id of this ModelVendor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelVendor.

        **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param id: The id of this ModelVendor.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ModelVendor.

        **参数解释**： 模型供应商名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The name of this ModelVendor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModelVendor.

        **参数解释**： 模型供应商名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param name: The name of this ModelVendor.
        :type name: str
        """
        self._name = name

    @property
    def name_en(self):
        r"""Gets the name_en of this ModelVendor.

        **参数解释**： 模型供应商英文名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The name_en of this ModelVendor.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this ModelVendor.

        **参数解释**： 模型供应商英文名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param name_en: The name_en of this ModelVendor.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def type(self):
        r"""Gets the type of this ModelVendor.

        **参数解释**： 模型供应商类型。 **约束限制**： 不涉及 **取值范围**： * SYSTEM：预置供应商 * CUSTOM：自定义供应商 **默认取值**： 不涉及 

        :return: The type of this ModelVendor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ModelVendor.

        **参数解释**： 模型供应商类型。 **约束限制**： 不涉及 **取值范围**： * SYSTEM：预置供应商 * CUSTOM：自定义供应商 **默认取值**： 不涉及 

        :param type: The type of this ModelVendor.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ModelVendor.

        **参数解释**： 模型服务状态。 **约束限制**： 不涉及 **取值范围**： * AVAILABLE：已接入 * UNAVAILABLE：未接入 **默认取值**： 不涉及 

        :return: The status of this ModelVendor.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ModelVendor.

        **参数解释**： 模型服务状态。 **约束限制**： 不涉及 **取值范围**： * AVAILABLE：已接入 * UNAVAILABLE：未接入 **默认取值**： 不涉及 

        :param status: The status of this ModelVendor.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ModelVendor.

        **参数解释**： 模型供应商创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The create_time of this ModelVendor.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ModelVendor.

        **参数解释**： 模型供应商创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param create_time: The create_time of this ModelVendor.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ModelVendor.

        **参数解释**： 模型供应商修改时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The update_time of this ModelVendor.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ModelVendor.

        **参数解释**： 模型供应商修改时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param update_time: The update_time of this ModelVendor.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def description(self):
        r"""Gets the description of this ModelVendor.

        **参数解释**： 模型供应商描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The description of this ModelVendor.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModelVendor.

        **参数解释**： 模型供应商描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param description: The description of this ModelVendor.
        :type description: str
        """
        self._description = description

    @property
    def auth_type(self):
        r"""Gets the auth_type of this ModelVendor.

        **参数解释**： 鉴权类型。 **约束限制**： 不涉及 **取值范围**： * API_KEY：API Key **默认取值**： 不涉及 

        :return: The auth_type of this ModelVendor.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this ModelVendor.

        **参数解释**： 鉴权类型。 **约束限制**： 不涉及 **取值范围**： * API_KEY：API Key **默认取值**： 不涉及 

        :param auth_type: The auth_type of this ModelVendor.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def auth_info(self):
        r"""Gets the auth_info of this ModelVendor.

        :return: The auth_info of this ModelVendor.
        :rtype: :class:`huaweicloudsdkeihealth.v2.VendorAuthInfo`
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        r"""Sets the auth_info of this ModelVendor.

        :param auth_info: The auth_info of this ModelVendor.
        :type auth_info: :class:`huaweicloudsdkeihealth.v2.VendorAuthInfo`
        """
        self._auth_info = auth_info

    @property
    def auth_url(self):
        r"""Gets the auth_url of this ModelVendor.

        **参数解释**： 内置供应商获取鉴权信息地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The auth_url of this ModelVendor.
        :rtype: str
        """
        return self._auth_url

    @auth_url.setter
    def auth_url(self, auth_url):
        r"""Sets the auth_url of this ModelVendor.

        **参数解释**： 内置供应商获取鉴权信息地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param auth_url: The auth_url of this ModelVendor.
        :type auth_url: str
        """
        self._auth_url = auth_url

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
        if not isinstance(other, ModelVendor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
