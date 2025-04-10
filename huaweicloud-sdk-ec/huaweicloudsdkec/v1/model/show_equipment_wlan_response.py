# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEquipmentWlanResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('password')

    openapi_types = {
        'support_wlan': 'bool',
        'wlan_enabled': 'bool',
        'name': 'str',
        'security_enabled': 'bool',
        'password': 'str',
        'authentication_method': 'str',
        'encrption_method': 'str',
        'name_hided': 'bool'
    }

    attribute_map = {
        'support_wlan': 'support_wlan',
        'wlan_enabled': 'wlan_enabled',
        'name': 'name',
        'security_enabled': 'security_enabled',
        'password': 'password',
        'authentication_method': 'authentication_method',
        'encrption_method': 'encrption_method',
        'name_hided': 'name_hided'
    }

    def __init__(self, support_wlan=None, wlan_enabled=None, name=None, security_enabled=None, password=None, authentication_method=None, encrption_method=None, name_hided=None):
        r"""ShowEquipmentWlanResponse

        The model defined in huaweicloud sdk

        :param support_wlan: 是否支持wlan，提供给UI识别是否显示Wi-Fi配置页面
        :type support_wlan: bool
        :param wlan_enabled: 是否使能wlan，取值为true时，必须填写name、security_enabled、name_hided
        :type wlan_enabled: bool
        :param name: Wi-Fi名称，长度1-32个字符，不支持中文字符，特殊字符只支持!~@_.?
        :type name: str
        :param security_enabled: 是否开启无线安全，取值为true时，必须填写authentication_method、encrption_method
        :type security_enabled: bool
        :param password: Wi-Fi密码，长度8-63个字符，包含大写字母、小写字母、数字、特殊字符中至少两种，不能和Wi-Fi名称及名称逆序相同，特殊字符只支持!~@_.?
        :type password: str
        :param authentication_method: 认证类型
        :type authentication_method: str
        :param encrption_method: 加密方式，认证类型为WPA或者WPA2时，可选TKIP、AES
        :type encrption_method: str
        :param name_hided: 是否隐藏Wi-Fi名称
        :type name_hided: bool
        """
        
        super(ShowEquipmentWlanResponse, self).__init__()

        self._support_wlan = None
        self._wlan_enabled = None
        self._name = None
        self._security_enabled = None
        self._password = None
        self._authentication_method = None
        self._encrption_method = None
        self._name_hided = None
        self.discriminator = None

        if support_wlan is not None:
            self.support_wlan = support_wlan
        if wlan_enabled is not None:
            self.wlan_enabled = wlan_enabled
        if name is not None:
            self.name = name
        if security_enabled is not None:
            self.security_enabled = security_enabled
        if password is not None:
            self.password = password
        if authentication_method is not None:
            self.authentication_method = authentication_method
        if encrption_method is not None:
            self.encrption_method = encrption_method
        if name_hided is not None:
            self.name_hided = name_hided

    @property
    def support_wlan(self):
        r"""Gets the support_wlan of this ShowEquipmentWlanResponse.

        是否支持wlan，提供给UI识别是否显示Wi-Fi配置页面

        :return: The support_wlan of this ShowEquipmentWlanResponse.
        :rtype: bool
        """
        return self._support_wlan

    @support_wlan.setter
    def support_wlan(self, support_wlan):
        r"""Sets the support_wlan of this ShowEquipmentWlanResponse.

        是否支持wlan，提供给UI识别是否显示Wi-Fi配置页面

        :param support_wlan: The support_wlan of this ShowEquipmentWlanResponse.
        :type support_wlan: bool
        """
        self._support_wlan = support_wlan

    @property
    def wlan_enabled(self):
        r"""Gets the wlan_enabled of this ShowEquipmentWlanResponse.

        是否使能wlan，取值为true时，必须填写name、security_enabled、name_hided

        :return: The wlan_enabled of this ShowEquipmentWlanResponse.
        :rtype: bool
        """
        return self._wlan_enabled

    @wlan_enabled.setter
    def wlan_enabled(self, wlan_enabled):
        r"""Sets the wlan_enabled of this ShowEquipmentWlanResponse.

        是否使能wlan，取值为true时，必须填写name、security_enabled、name_hided

        :param wlan_enabled: The wlan_enabled of this ShowEquipmentWlanResponse.
        :type wlan_enabled: bool
        """
        self._wlan_enabled = wlan_enabled

    @property
    def name(self):
        r"""Gets the name of this ShowEquipmentWlanResponse.

        Wi-Fi名称，长度1-32个字符，不支持中文字符，特殊字符只支持!~@_.?

        :return: The name of this ShowEquipmentWlanResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowEquipmentWlanResponse.

        Wi-Fi名称，长度1-32个字符，不支持中文字符，特殊字符只支持!~@_.?

        :param name: The name of this ShowEquipmentWlanResponse.
        :type name: str
        """
        self._name = name

    @property
    def security_enabled(self):
        r"""Gets the security_enabled of this ShowEquipmentWlanResponse.

        是否开启无线安全，取值为true时，必须填写authentication_method、encrption_method

        :return: The security_enabled of this ShowEquipmentWlanResponse.
        :rtype: bool
        """
        return self._security_enabled

    @security_enabled.setter
    def security_enabled(self, security_enabled):
        r"""Sets the security_enabled of this ShowEquipmentWlanResponse.

        是否开启无线安全，取值为true时，必须填写authentication_method、encrption_method

        :param security_enabled: The security_enabled of this ShowEquipmentWlanResponse.
        :type security_enabled: bool
        """
        self._security_enabled = security_enabled

    @property
    def password(self):
        r"""Gets the password of this ShowEquipmentWlanResponse.

        Wi-Fi密码，长度8-63个字符，包含大写字母、小写字母、数字、特殊字符中至少两种，不能和Wi-Fi名称及名称逆序相同，特殊字符只支持!~@_.?

        :return: The password of this ShowEquipmentWlanResponse.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this ShowEquipmentWlanResponse.

        Wi-Fi密码，长度8-63个字符，包含大写字母、小写字母、数字、特殊字符中至少两种，不能和Wi-Fi名称及名称逆序相同，特殊字符只支持!~@_.?

        :param password: The password of this ShowEquipmentWlanResponse.
        :type password: str
        """
        self._password = password

    @property
    def authentication_method(self):
        r"""Gets the authentication_method of this ShowEquipmentWlanResponse.

        认证类型

        :return: The authentication_method of this ShowEquipmentWlanResponse.
        :rtype: str
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        r"""Sets the authentication_method of this ShowEquipmentWlanResponse.

        认证类型

        :param authentication_method: The authentication_method of this ShowEquipmentWlanResponse.
        :type authentication_method: str
        """
        self._authentication_method = authentication_method

    @property
    def encrption_method(self):
        r"""Gets the encrption_method of this ShowEquipmentWlanResponse.

        加密方式，认证类型为WPA或者WPA2时，可选TKIP、AES

        :return: The encrption_method of this ShowEquipmentWlanResponse.
        :rtype: str
        """
        return self._encrption_method

    @encrption_method.setter
    def encrption_method(self, encrption_method):
        r"""Sets the encrption_method of this ShowEquipmentWlanResponse.

        加密方式，认证类型为WPA或者WPA2时，可选TKIP、AES

        :param encrption_method: The encrption_method of this ShowEquipmentWlanResponse.
        :type encrption_method: str
        """
        self._encrption_method = encrption_method

    @property
    def name_hided(self):
        r"""Gets the name_hided of this ShowEquipmentWlanResponse.

        是否隐藏Wi-Fi名称

        :return: The name_hided of this ShowEquipmentWlanResponse.
        :rtype: bool
        """
        return self._name_hided

    @name_hided.setter
    def name_hided(self, name_hided):
        r"""Sets the name_hided of this ShowEquipmentWlanResponse.

        是否隐藏Wi-Fi名称

        :param name_hided: The name_hided of this ShowEquipmentWlanResponse.
        :type name_hided: bool
        """
        self._name_hided = name_hided

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
        if not isinstance(other, ShowEquipmentWlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
