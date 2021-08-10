# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePremiumHostRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'proxy': 'bool',
        'certificateid': 'str',
        'certificatename': 'str',
        'tls': 'str',
        'cipher': 'str'
    }

    attribute_map = {
        'proxy': 'proxy',
        'certificateid': 'certificateid',
        'certificatename': 'certificatename',
        'tls': 'tls',
        'cipher': 'cipher'
    }

    def __init__(self, proxy=None, certificateid=None, certificatename=None, tls=None, cipher=None):
        """UpdatePremiumHostRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._proxy = None
        self._certificateid = None
        self._certificatename = None
        self._tls = None
        self._cipher = None
        self.discriminator = None

        if proxy is not None:
            self.proxy = proxy
        if certificateid is not None:
            self.certificateid = certificateid
        if certificatename is not None:
            self.certificatename = certificatename
        if tls is not None:
            self.tls = tls
        if cipher is not None:
            self.cipher = cipher

    @property
    def proxy(self):
        """Gets the proxy of this UpdatePremiumHostRequestBody.

        是否使用代理

        :return: The proxy of this UpdatePremiumHostRequestBody.
        :rtype: bool
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this UpdatePremiumHostRequestBody.

        是否使用代理

        :param proxy: The proxy of this UpdatePremiumHostRequestBody.
        :type: bool
        """
        self._proxy = proxy

    @property
    def certificateid(self):
        """Gets the certificateid of this UpdatePremiumHostRequestBody.

        证书ID

        :return: The certificateid of this UpdatePremiumHostRequestBody.
        :rtype: str
        """
        return self._certificateid

    @certificateid.setter
    def certificateid(self, certificateid):
        """Sets the certificateid of this UpdatePremiumHostRequestBody.

        证书ID

        :param certificateid: The certificateid of this UpdatePremiumHostRequestBody.
        :type: str
        """
        self._certificateid = certificateid

    @property
    def certificatename(self):
        """Gets the certificatename of this UpdatePremiumHostRequestBody.

        证书名称

        :return: The certificatename of this UpdatePremiumHostRequestBody.
        :rtype: str
        """
        return self._certificatename

    @certificatename.setter
    def certificatename(self, certificatename):
        """Sets the certificatename of this UpdatePremiumHostRequestBody.

        证书名称

        :param certificatename: The certificatename of this UpdatePremiumHostRequestBody.
        :type: str
        """
        self._certificatename = certificatename

    @property
    def tls(self):
        """Gets the tls of this UpdatePremiumHostRequestBody.

        支持最低的TLS版本

        :return: The tls of this UpdatePremiumHostRequestBody.
        :rtype: str
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this UpdatePremiumHostRequestBody.

        支持最低的TLS版本

        :param tls: The tls of this UpdatePremiumHostRequestBody.
        :type: str
        """
        self._tls = tls

    @property
    def cipher(self):
        """Gets the cipher of this UpdatePremiumHostRequestBody.

        加密套件代码

        :return: The cipher of this UpdatePremiumHostRequestBody.
        :rtype: str
        """
        return self._cipher

    @cipher.setter
    def cipher(self, cipher):
        """Sets the cipher of this UpdatePremiumHostRequestBody.

        加密套件代码

        :param cipher: The cipher of this UpdatePremiumHostRequestBody.
        :type: str
        """
        self._cipher = cipher

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
        if not isinstance(other, UpdatePremiumHostRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
