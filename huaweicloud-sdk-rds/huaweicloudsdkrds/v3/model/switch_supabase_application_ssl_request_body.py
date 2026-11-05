# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchSupabaseApplicationSslRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_ssl': 'bool',
        'cert_id': 'str'
    }

    attribute_map = {
        'enable_ssl': 'enable_ssl',
        'cert_id': 'cert_id'
    }

    def __init__(self, enable_ssl=None, cert_id=None):
        r"""SwitchSupabaseApplicationSslRequestBody

        The model defined in huaweicloud sdk

        :param enable_ssl: 是否开启SSL。false时cert_id必须为空；true时cert_id必填。
        :type enable_ssl: bool
        :param cert_id: 证书ID。enable_ssl&#x3D;true时必填。
        :type cert_id: str
        """
        
        

        self._enable_ssl = None
        self._cert_id = None
        self.discriminator = None

        self.enable_ssl = enable_ssl
        if cert_id is not None:
            self.cert_id = cert_id

    @property
    def enable_ssl(self):
        r"""Gets the enable_ssl of this SwitchSupabaseApplicationSslRequestBody.

        是否开启SSL。false时cert_id必须为空；true时cert_id必填。

        :return: The enable_ssl of this SwitchSupabaseApplicationSslRequestBody.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        r"""Sets the enable_ssl of this SwitchSupabaseApplicationSslRequestBody.

        是否开启SSL。false时cert_id必须为空；true时cert_id必填。

        :param enable_ssl: The enable_ssl of this SwitchSupabaseApplicationSslRequestBody.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def cert_id(self):
        r"""Gets the cert_id of this SwitchSupabaseApplicationSslRequestBody.

        证书ID。enable_ssl=true时必填。

        :return: The cert_id of this SwitchSupabaseApplicationSslRequestBody.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        r"""Sets the cert_id of this SwitchSupabaseApplicationSslRequestBody.

        证书ID。enable_ssl=true时必填。

        :param cert_id: The cert_id of this SwitchSupabaseApplicationSslRequestBody.
        :type cert_id: str
        """
        self._cert_id = cert_id

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
        if not isinstance(other, SwitchSupabaseApplicationSslRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
