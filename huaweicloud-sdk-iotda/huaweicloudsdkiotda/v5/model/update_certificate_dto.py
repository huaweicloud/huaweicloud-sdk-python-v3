# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCertificateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provision_enable': 'bool',
        'template_id': 'str',
        'ocsp_enable': 'bool',
        'ocsp_ssl_enable': 'bool',
        'ocsp_server_ca_id': 'str'
    }

    attribute_map = {
        'provision_enable': 'provision_enable',
        'template_id': 'template_id',
        'ocsp_enable': 'ocsp_enable',
        'ocsp_ssl_enable': 'ocsp_ssl_enable',
        'ocsp_server_ca_id': 'ocsp_server_ca_id'
    }

    def __init__(self, provision_enable=None, template_id=None, ocsp_enable=None, ocsp_ssl_enable=None, ocsp_server_ca_id=None):
        r"""UpdateCertificateDTO

        The model defined in huaweicloud sdk

        :param provision_enable: 是否开启自注册能力，当为true时该功能必须配合预调配功能使用，true：是，false：否。
        :type provision_enable: bool
        :param template_id: 预调配模板ID，该CA证书绑定的预调配模板id，当该字段传null时表示解除绑定关系。
        :type template_id: str
        :param ocsp_enable: 是否开启该CA证书下的设备证书OCSP校验，当为true且设备证书信息中包含OCSP url时则平台会校验证书的状态，当证书状态为revoked时平台会拒绝设备连接，true：开启，false：关闭。
        :type ocsp_enable: bool
        :param ocsp_ssl_enable: 访问ocsp服务器是否开启SSL，开启后必须配置服务器CA证书校验。
        :type ocsp_ssl_enable: bool
        :param ocsp_server_ca_id: ocsp服务器端CA证书id，当ocsp服务器为https协议时需要配置，否则认证失败。
        :type ocsp_server_ca_id: str
        """
        
        

        self._provision_enable = None
        self._template_id = None
        self._ocsp_enable = None
        self._ocsp_ssl_enable = None
        self._ocsp_server_ca_id = None
        self.discriminator = None

        if provision_enable is not None:
            self.provision_enable = provision_enable
        if template_id is not None:
            self.template_id = template_id
        if ocsp_enable is not None:
            self.ocsp_enable = ocsp_enable
        if ocsp_ssl_enable is not None:
            self.ocsp_ssl_enable = ocsp_ssl_enable
        if ocsp_server_ca_id is not None:
            self.ocsp_server_ca_id = ocsp_server_ca_id

    @property
    def provision_enable(self):
        r"""Gets the provision_enable of this UpdateCertificateDTO.

        是否开启自注册能力，当为true时该功能必须配合预调配功能使用，true：是，false：否。

        :return: The provision_enable of this UpdateCertificateDTO.
        :rtype: bool
        """
        return self._provision_enable

    @provision_enable.setter
    def provision_enable(self, provision_enable):
        r"""Sets the provision_enable of this UpdateCertificateDTO.

        是否开启自注册能力，当为true时该功能必须配合预调配功能使用，true：是，false：否。

        :param provision_enable: The provision_enable of this UpdateCertificateDTO.
        :type provision_enable: bool
        """
        self._provision_enable = provision_enable

    @property
    def template_id(self):
        r"""Gets the template_id of this UpdateCertificateDTO.

        预调配模板ID，该CA证书绑定的预调配模板id，当该字段传null时表示解除绑定关系。

        :return: The template_id of this UpdateCertificateDTO.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this UpdateCertificateDTO.

        预调配模板ID，该CA证书绑定的预调配模板id，当该字段传null时表示解除绑定关系。

        :param template_id: The template_id of this UpdateCertificateDTO.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def ocsp_enable(self):
        r"""Gets the ocsp_enable of this UpdateCertificateDTO.

        是否开启该CA证书下的设备证书OCSP校验，当为true且设备证书信息中包含OCSP url时则平台会校验证书的状态，当证书状态为revoked时平台会拒绝设备连接，true：开启，false：关闭。

        :return: The ocsp_enable of this UpdateCertificateDTO.
        :rtype: bool
        """
        return self._ocsp_enable

    @ocsp_enable.setter
    def ocsp_enable(self, ocsp_enable):
        r"""Sets the ocsp_enable of this UpdateCertificateDTO.

        是否开启该CA证书下的设备证书OCSP校验，当为true且设备证书信息中包含OCSP url时则平台会校验证书的状态，当证书状态为revoked时平台会拒绝设备连接，true：开启，false：关闭。

        :param ocsp_enable: The ocsp_enable of this UpdateCertificateDTO.
        :type ocsp_enable: bool
        """
        self._ocsp_enable = ocsp_enable

    @property
    def ocsp_ssl_enable(self):
        r"""Gets the ocsp_ssl_enable of this UpdateCertificateDTO.

        访问ocsp服务器是否开启SSL，开启后必须配置服务器CA证书校验。

        :return: The ocsp_ssl_enable of this UpdateCertificateDTO.
        :rtype: bool
        """
        return self._ocsp_ssl_enable

    @ocsp_ssl_enable.setter
    def ocsp_ssl_enable(self, ocsp_ssl_enable):
        r"""Sets the ocsp_ssl_enable of this UpdateCertificateDTO.

        访问ocsp服务器是否开启SSL，开启后必须配置服务器CA证书校验。

        :param ocsp_ssl_enable: The ocsp_ssl_enable of this UpdateCertificateDTO.
        :type ocsp_ssl_enable: bool
        """
        self._ocsp_ssl_enable = ocsp_ssl_enable

    @property
    def ocsp_server_ca_id(self):
        r"""Gets the ocsp_server_ca_id of this UpdateCertificateDTO.

        ocsp服务器端CA证书id，当ocsp服务器为https协议时需要配置，否则认证失败。

        :return: The ocsp_server_ca_id of this UpdateCertificateDTO.
        :rtype: str
        """
        return self._ocsp_server_ca_id

    @ocsp_server_ca_id.setter
    def ocsp_server_ca_id(self, ocsp_server_ca_id):
        r"""Sets the ocsp_server_ca_id of this UpdateCertificateDTO.

        ocsp服务器端CA证书id，当ocsp服务器为https协议时需要配置，否则认证失败。

        :param ocsp_server_ca_id: The ocsp_server_ca_id of this UpdateCertificateDTO.
        :type ocsp_server_ca_id: str
        """
        self._ocsp_server_ca_id = ocsp_server_ca_id

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
        if not isinstance(other, UpdateCertificateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
