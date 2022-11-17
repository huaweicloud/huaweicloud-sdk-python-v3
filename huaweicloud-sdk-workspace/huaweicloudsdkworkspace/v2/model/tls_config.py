# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TlsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cert_pem': 'str',
        'cert_start_time': 'str',
        'cert_end_time': 'str'
    }

    attribute_map = {
        'cert_pem': 'cert_pem',
        'cert_start_time': 'cert_start_time',
        'cert_end_time': 'cert_end_time'
    }

    def __init__(self, cert_pem=None, cert_start_time=None, cert_end_time=None):
        """TlsConfig

        The model defined in huaweicloud sdk

        :param cert_pem: pem内容, 有则更新，无则上传。查询不返回。
        :type cert_pem: str
        :param cert_start_time: 证书生效开始时间，时间参考样例 2022-01-25T09:24:27。
        :type cert_start_time: str
        :param cert_end_time: 证书生效截止时间，时间参考样例 2022-01-25T09:24:27。
        :type cert_end_time: str
        """
        
        

        self._cert_pem = None
        self._cert_start_time = None
        self._cert_end_time = None
        self.discriminator = None

        if cert_pem is not None:
            self.cert_pem = cert_pem
        if cert_start_time is not None:
            self.cert_start_time = cert_start_time
        if cert_end_time is not None:
            self.cert_end_time = cert_end_time

    @property
    def cert_pem(self):
        """Gets the cert_pem of this TlsConfig.

        pem内容, 有则更新，无则上传。查询不返回。

        :return: The cert_pem of this TlsConfig.
        :rtype: str
        """
        return self._cert_pem

    @cert_pem.setter
    def cert_pem(self, cert_pem):
        """Sets the cert_pem of this TlsConfig.

        pem内容, 有则更新，无则上传。查询不返回。

        :param cert_pem: The cert_pem of this TlsConfig.
        :type cert_pem: str
        """
        self._cert_pem = cert_pem

    @property
    def cert_start_time(self):
        """Gets the cert_start_time of this TlsConfig.

        证书生效开始时间，时间参考样例 2022-01-25T09:24:27。

        :return: The cert_start_time of this TlsConfig.
        :rtype: str
        """
        return self._cert_start_time

    @cert_start_time.setter
    def cert_start_time(self, cert_start_time):
        """Sets the cert_start_time of this TlsConfig.

        证书生效开始时间，时间参考样例 2022-01-25T09:24:27。

        :param cert_start_time: The cert_start_time of this TlsConfig.
        :type cert_start_time: str
        """
        self._cert_start_time = cert_start_time

    @property
    def cert_end_time(self):
        """Gets the cert_end_time of this TlsConfig.

        证书生效截止时间，时间参考样例 2022-01-25T09:24:27。

        :return: The cert_end_time of this TlsConfig.
        :rtype: str
        """
        return self._cert_end_time

    @cert_end_time.setter
    def cert_end_time(self, cert_end_time):
        """Sets the cert_end_time of this TlsConfig.

        证书生效截止时间，时间参考样例 2022-01-25T09:24:27。

        :param cert_end_time: The cert_end_time of this TlsConfig.
        :type cert_end_time: str
        """
        self._cert_end_time = cert_end_time

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
        if not isinstance(other, TlsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
