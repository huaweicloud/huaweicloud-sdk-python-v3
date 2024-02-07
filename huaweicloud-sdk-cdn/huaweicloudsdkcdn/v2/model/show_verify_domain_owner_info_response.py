# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVerifyDomainOwnerInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dns_verify_type': 'str',
        'dns_verify_name': 'str',
        'file_verify_url': 'str',
        'domain_name': 'str',
        'verify_domain_name': 'str',
        'file_verify_filename': 'str',
        'verify_content': 'str'
    }

    attribute_map = {
        'dns_verify_type': 'dns_verify_type',
        'dns_verify_name': 'dns_verify_name',
        'file_verify_url': 'file_verify_url',
        'domain_name': 'domain_name',
        'verify_domain_name': 'verify_domain_name',
        'file_verify_filename': 'file_verify_filename',
        'verify_content': 'verify_content'
    }

    def __init__(self, dns_verify_type=None, dns_verify_name=None, file_verify_url=None, domain_name=None, verify_domain_name=None, file_verify_filename=None, verify_content=None):
        """ShowVerifyDomainOwnerInfoResponse

        The model defined in huaweicloud sdk

        :param dns_verify_type: DNS探测类型
        :type dns_verify_type: str
        :param dns_verify_name: DNS记录名称
        :type dns_verify_name: str
        :param file_verify_url: 文件探测地址
        :type file_verify_url: str
        :param domain_name: 域名
        :type domain_name: str
        :param verify_domain_name: 探测域名
        :type verify_domain_name: str
        :param file_verify_filename: 探测文件名
        :type file_verify_filename: str
        :param verify_content: 探测内容，DNS值或者文件内容，时间加uuid
        :type verify_content: str
        """
        
        super(ShowVerifyDomainOwnerInfoResponse, self).__init__()

        self._dns_verify_type = None
        self._dns_verify_name = None
        self._file_verify_url = None
        self._domain_name = None
        self._verify_domain_name = None
        self._file_verify_filename = None
        self._verify_content = None
        self.discriminator = None

        if dns_verify_type is not None:
            self.dns_verify_type = dns_verify_type
        if dns_verify_name is not None:
            self.dns_verify_name = dns_verify_name
        if file_verify_url is not None:
            self.file_verify_url = file_verify_url
        if domain_name is not None:
            self.domain_name = domain_name
        if verify_domain_name is not None:
            self.verify_domain_name = verify_domain_name
        if file_verify_filename is not None:
            self.file_verify_filename = file_verify_filename
        if verify_content is not None:
            self.verify_content = verify_content

    @property
    def dns_verify_type(self):
        """Gets the dns_verify_type of this ShowVerifyDomainOwnerInfoResponse.

        DNS探测类型

        :return: The dns_verify_type of this ShowVerifyDomainOwnerInfoResponse.
        :rtype: str
        """
        return self._dns_verify_type

    @dns_verify_type.setter
    def dns_verify_type(self, dns_verify_type):
        """Sets the dns_verify_type of this ShowVerifyDomainOwnerInfoResponse.

        DNS探测类型

        :param dns_verify_type: The dns_verify_type of this ShowVerifyDomainOwnerInfoResponse.
        :type dns_verify_type: str
        """
        self._dns_verify_type = dns_verify_type

    @property
    def dns_verify_name(self):
        """Gets the dns_verify_name of this ShowVerifyDomainOwnerInfoResponse.

        DNS记录名称

        :return: The dns_verify_name of this ShowVerifyDomainOwnerInfoResponse.
        :rtype: str
        """
        return self._dns_verify_name

    @dns_verify_name.setter
    def dns_verify_name(self, dns_verify_name):
        """Sets the dns_verify_name of this ShowVerifyDomainOwnerInfoResponse.

        DNS记录名称

        :param dns_verify_name: The dns_verify_name of this ShowVerifyDomainOwnerInfoResponse.
        :type dns_verify_name: str
        """
        self._dns_verify_name = dns_verify_name

    @property
    def file_verify_url(self):
        """Gets the file_verify_url of this ShowVerifyDomainOwnerInfoResponse.

        文件探测地址

        :return: The file_verify_url of this ShowVerifyDomainOwnerInfoResponse.
        :rtype: str
        """
        return self._file_verify_url

    @file_verify_url.setter
    def file_verify_url(self, file_verify_url):
        """Sets the file_verify_url of this ShowVerifyDomainOwnerInfoResponse.

        文件探测地址

        :param file_verify_url: The file_verify_url of this ShowVerifyDomainOwnerInfoResponse.
        :type file_verify_url: str
        """
        self._file_verify_url = file_verify_url

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowVerifyDomainOwnerInfoResponse.

        域名

        :return: The domain_name of this ShowVerifyDomainOwnerInfoResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowVerifyDomainOwnerInfoResponse.

        域名

        :param domain_name: The domain_name of this ShowVerifyDomainOwnerInfoResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def verify_domain_name(self):
        """Gets the verify_domain_name of this ShowVerifyDomainOwnerInfoResponse.

        探测域名

        :return: The verify_domain_name of this ShowVerifyDomainOwnerInfoResponse.
        :rtype: str
        """
        return self._verify_domain_name

    @verify_domain_name.setter
    def verify_domain_name(self, verify_domain_name):
        """Sets the verify_domain_name of this ShowVerifyDomainOwnerInfoResponse.

        探测域名

        :param verify_domain_name: The verify_domain_name of this ShowVerifyDomainOwnerInfoResponse.
        :type verify_domain_name: str
        """
        self._verify_domain_name = verify_domain_name

    @property
    def file_verify_filename(self):
        """Gets the file_verify_filename of this ShowVerifyDomainOwnerInfoResponse.

        探测文件名

        :return: The file_verify_filename of this ShowVerifyDomainOwnerInfoResponse.
        :rtype: str
        """
        return self._file_verify_filename

    @file_verify_filename.setter
    def file_verify_filename(self, file_verify_filename):
        """Sets the file_verify_filename of this ShowVerifyDomainOwnerInfoResponse.

        探测文件名

        :param file_verify_filename: The file_verify_filename of this ShowVerifyDomainOwnerInfoResponse.
        :type file_verify_filename: str
        """
        self._file_verify_filename = file_verify_filename

    @property
    def verify_content(self):
        """Gets the verify_content of this ShowVerifyDomainOwnerInfoResponse.

        探测内容，DNS值或者文件内容，时间加uuid

        :return: The verify_content of this ShowVerifyDomainOwnerInfoResponse.
        :rtype: str
        """
        return self._verify_content

    @verify_content.setter
    def verify_content(self, verify_content):
        """Sets the verify_content of this ShowVerifyDomainOwnerInfoResponse.

        探测内容，DNS值或者文件内容，时间加uuid

        :param verify_content: The verify_content of this ShowVerifyDomainOwnerInfoResponse.
        :type verify_content: str
        """
        self._verify_content = verify_content

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
        if not isinstance(other, ShowVerifyDomainOwnerInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
