# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCertificateRequestBody:

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
        'content': 'str',
        'key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'content': 'content',
        'key': 'key'
    }

    def __init__(self, name=None, content=None, key=None):
        """UpdateCertificateRequestBody

        The model defined in huaweicloud sdk

        :param name: 证书名称，证书名称只能由数字、字母、中划线、下划线和英文句点组成，长度不能超过64位字符
        :type name: str
        :param content: 证书文件，仅支持PEM格式的证书和私钥文件，且文件中的换行符应以\\n替换
        :type content: str
        :param key: 证书私钥，仅支持PEM格式的证书和私钥文件，且文件中的换行符应以\\n替换
        :type key: str
        """
        
        

        self._name = None
        self._content = None
        self._key = None
        self.discriminator = None

        self.name = name
        if content is not None:
            self.content = content
        if key is not None:
            self.key = key

    @property
    def name(self):
        """Gets the name of this UpdateCertificateRequestBody.

        证书名称，证书名称只能由数字、字母、中划线、下划线和英文句点组成，长度不能超过64位字符

        :return: The name of this UpdateCertificateRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCertificateRequestBody.

        证书名称，证书名称只能由数字、字母、中划线、下划线和英文句点组成，长度不能超过64位字符

        :param name: The name of this UpdateCertificateRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def content(self):
        """Gets the content of this UpdateCertificateRequestBody.

        证书文件，仅支持PEM格式的证书和私钥文件，且文件中的换行符应以\\n替换

        :return: The content of this UpdateCertificateRequestBody.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this UpdateCertificateRequestBody.

        证书文件，仅支持PEM格式的证书和私钥文件，且文件中的换行符应以\\n替换

        :param content: The content of this UpdateCertificateRequestBody.
        :type content: str
        """
        self._content = content

    @property
    def key(self):
        """Gets the key of this UpdateCertificateRequestBody.

        证书私钥，仅支持PEM格式的证书和私钥文件，且文件中的换行符应以\\n替换

        :return: The key of this UpdateCertificateRequestBody.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this UpdateCertificateRequestBody.

        证书私钥，仅支持PEM格式的证书和私钥文件，且文件中的换行符应以\\n替换

        :param key: The key of this UpdateCertificateRequestBody.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, UpdateCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
