# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateModelVendorReq:

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
        'name_en': 'str',
        'description': 'str',
        'auth_type': 'str',
        'auth_info': 'VendorAuthInfo'
    }

    attribute_map = {
        'name': 'name',
        'name_en': 'name_en',
        'description': 'description',
        'auth_type': 'auth_type',
        'auth_info': 'auth_info'
    }

    def __init__(self, name=None, name_en=None, description=None, auth_type=None, auth_info=None):
        r"""CreateModelVendorReq

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 模型供应商名称。 **约束限制**： 不涉及 **取值范围**： 支持中英文、数字、下划线、中划线、空格，长度2-64。 **默认取值**： 不涉及 
        :type name: str
        :param name_en: **参数解释**： 模型供应商英文名称。 **约束限制**： 不涉及 **取值范围**： 支持英文、数字、下划线、中划线、空格，长度2-64。 **默认取值**： 不涉及 
        :type name_en: str
        :param description: **参数解释**： 模型供应商描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type description: str
        :param auth_type: **参数解释**： 鉴权类型。 **约束限制**： 不涉及 **取值范围**： * api_key：API Key **默认取值**： 不涉及 
        :type auth_type: str
        :param auth_info: 
        :type auth_info: :class:`huaweicloudsdkeihealth.v2.VendorAuthInfo`
        """
        
        

        self._name = None
        self._name_en = None
        self._description = None
        self._auth_type = None
        self._auth_info = None
        self.discriminator = None

        self.name = name
        self.name_en = name_en
        if description is not None:
            self.description = description
        self.auth_type = auth_type
        self.auth_info = auth_info

    @property
    def name(self):
        r"""Gets the name of this CreateModelVendorReq.

        **参数解释**： 模型供应商名称。 **约束限制**： 不涉及 **取值范围**： 支持中英文、数字、下划线、中划线、空格，长度2-64。 **默认取值**： 不涉及 

        :return: The name of this CreateModelVendorReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateModelVendorReq.

        **参数解释**： 模型供应商名称。 **约束限制**： 不涉及 **取值范围**： 支持中英文、数字、下划线、中划线、空格，长度2-64。 **默认取值**： 不涉及 

        :param name: The name of this CreateModelVendorReq.
        :type name: str
        """
        self._name = name

    @property
    def name_en(self):
        r"""Gets the name_en of this CreateModelVendorReq.

        **参数解释**： 模型供应商英文名称。 **约束限制**： 不涉及 **取值范围**： 支持英文、数字、下划线、中划线、空格，长度2-64。 **默认取值**： 不涉及 

        :return: The name_en of this CreateModelVendorReq.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this CreateModelVendorReq.

        **参数解释**： 模型供应商英文名称。 **约束限制**： 不涉及 **取值范围**： 支持英文、数字、下划线、中划线、空格，长度2-64。 **默认取值**： 不涉及 

        :param name_en: The name_en of this CreateModelVendorReq.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def description(self):
        r"""Gets the description of this CreateModelVendorReq.

        **参数解释**： 模型供应商描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The description of this CreateModelVendorReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateModelVendorReq.

        **参数解释**： 模型供应商描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param description: The description of this CreateModelVendorReq.
        :type description: str
        """
        self._description = description

    @property
    def auth_type(self):
        r"""Gets the auth_type of this CreateModelVendorReq.

        **参数解释**： 鉴权类型。 **约束限制**： 不涉及 **取值范围**： * api_key：API Key **默认取值**： 不涉及 

        :return: The auth_type of this CreateModelVendorReq.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this CreateModelVendorReq.

        **参数解释**： 鉴权类型。 **约束限制**： 不涉及 **取值范围**： * api_key：API Key **默认取值**： 不涉及 

        :param auth_type: The auth_type of this CreateModelVendorReq.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def auth_info(self):
        r"""Gets the auth_info of this CreateModelVendorReq.

        :return: The auth_info of this CreateModelVendorReq.
        :rtype: :class:`huaweicloudsdkeihealth.v2.VendorAuthInfo`
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        r"""Sets the auth_info of this CreateModelVendorReq.

        :param auth_info: The auth_info of this CreateModelVendorReq.
        :type auth_info: :class:`huaweicloudsdkeihealth.v2.VendorAuthInfo`
        """
        self._auth_info = auth_info

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
        if not isinstance(other, CreateModelVendorReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
