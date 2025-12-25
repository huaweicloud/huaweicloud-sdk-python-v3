# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Website:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'str',
        'main_domain': 'str',
        'protected_status': 'str',
        'is_public': 'bool',
        'remark': 'str',
        'name_server': 'list[str]',
        'extend_properties': 'WebsiteExtendProperties'
    }

    attribute_map = {
        'value': 'value',
        'main_domain': 'main_domain',
        'protected_status': 'protected_status',
        'is_public': 'is_public',
        'remark': 'remark',
        'name_server': 'name_server',
        'extend_properties': 'extend_properties'
    }

    def __init__(self, value=None, main_domain=None, protected_status=None, is_public=None, remark=None, name_server=None, extend_properties=None):
        r"""Website

        The model defined in huaweicloud sdk

        :param value: 网站url
        :type value: str
        :param main_domain: 主域名
        :type main_domain: str
        :param protected_status: WAF开启状态：OPEN | CLOSE
        :type protected_status: str
        :param is_public: 外网或内网 true：外网 false: 内网
        :type is_public: bool
        :param remark: 网站备注
        :type remark: str
        :param name_server: 网站服务器列表
        :type name_server: list[str]
        :param extend_properties: 
        :type extend_properties: :class:`huaweicloudsdksecmaster.v1.WebsiteExtendProperties`
        """
        
        

        self._value = None
        self._main_domain = None
        self._protected_status = None
        self._is_public = None
        self._remark = None
        self._name_server = None
        self._extend_properties = None
        self.discriminator = None

        self.value = value
        self.main_domain = main_domain
        self.protected_status = protected_status
        self.is_public = is_public
        if remark is not None:
            self.remark = remark
        self.name_server = name_server
        if extend_properties is not None:
            self.extend_properties = extend_properties

    @property
    def value(self):
        r"""Gets the value of this Website.

        网站url

        :return: The value of this Website.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Website.

        网站url

        :param value: The value of this Website.
        :type value: str
        """
        self._value = value

    @property
    def main_domain(self):
        r"""Gets the main_domain of this Website.

        主域名

        :return: The main_domain of this Website.
        :rtype: str
        """
        return self._main_domain

    @main_domain.setter
    def main_domain(self, main_domain):
        r"""Sets the main_domain of this Website.

        主域名

        :param main_domain: The main_domain of this Website.
        :type main_domain: str
        """
        self._main_domain = main_domain

    @property
    def protected_status(self):
        r"""Gets the protected_status of this Website.

        WAF开启状态：OPEN | CLOSE

        :return: The protected_status of this Website.
        :rtype: str
        """
        return self._protected_status

    @protected_status.setter
    def protected_status(self, protected_status):
        r"""Sets the protected_status of this Website.

        WAF开启状态：OPEN | CLOSE

        :param protected_status: The protected_status of this Website.
        :type protected_status: str
        """
        self._protected_status = protected_status

    @property
    def is_public(self):
        r"""Gets the is_public of this Website.

        外网或内网 true：外网 false: 内网

        :return: The is_public of this Website.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        r"""Sets the is_public of this Website.

        外网或内网 true：外网 false: 内网

        :param is_public: The is_public of this Website.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def remark(self):
        r"""Gets the remark of this Website.

        网站备注

        :return: The remark of this Website.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this Website.

        网站备注

        :param remark: The remark of this Website.
        :type remark: str
        """
        self._remark = remark

    @property
    def name_server(self):
        r"""Gets the name_server of this Website.

        网站服务器列表

        :return: The name_server of this Website.
        :rtype: list[str]
        """
        return self._name_server

    @name_server.setter
    def name_server(self, name_server):
        r"""Sets the name_server of this Website.

        网站服务器列表

        :param name_server: The name_server of this Website.
        :type name_server: list[str]
        """
        self._name_server = name_server

    @property
    def extend_properties(self):
        r"""Gets the extend_properties of this Website.

        :return: The extend_properties of this Website.
        :rtype: :class:`huaweicloudsdksecmaster.v1.WebsiteExtendProperties`
        """
        return self._extend_properties

    @extend_properties.setter
    def extend_properties(self, extend_properties):
        r"""Sets the extend_properties of this Website.

        :param extend_properties: The extend_properties of this Website.
        :type extend_properties: :class:`huaweicloudsdksecmaster.v1.WebsiteExtendProperties`
        """
        self._extend_properties = extend_properties

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
        if not isinstance(other, Website):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
