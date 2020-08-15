# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class AssociateCertificateV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ssl_name': 'str',
        'url_domain': 'str',
        'ssl_id': 'str',
        'id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'ssl_name': 'ssl_name',
        'url_domain': 'url_domain',
        'ssl_id': 'ssl_id',
        'id': 'id',
        'status': 'status'
    }

    def __init__(self, ssl_name=None, url_domain=None, ssl_id=None, id=None, status=None):
        """AssociateCertificateV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._ssl_name = None
        self._url_domain = None
        self._ssl_id = None
        self._id = None
        self._status = None
        self.discriminator = None

        if ssl_name is not None:
            self.ssl_name = ssl_name
        if url_domain is not None:
            self.url_domain = url_domain
        if ssl_id is not None:
            self.ssl_id = ssl_id
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status

    @property
    def ssl_name(self):
        """Gets the ssl_name of this AssociateCertificateV2Response.

        证书的名称

        :return: The ssl_name of this AssociateCertificateV2Response.
        :rtype: str
        """
        return self._ssl_name

    @ssl_name.setter
    def ssl_name(self, ssl_name):
        """Sets the ssl_name of this AssociateCertificateV2Response.

        证书的名称

        :param ssl_name: The ssl_name of this AssociateCertificateV2Response.
        :type: str
        """
        self._ssl_name = ssl_name

    @property
    def url_domain(self):
        """Gets the url_domain of this AssociateCertificateV2Response.

        自定义域名

        :return: The url_domain of this AssociateCertificateV2Response.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        """Sets the url_domain of this AssociateCertificateV2Response.

        自定义域名

        :param url_domain: The url_domain of this AssociateCertificateV2Response.
        :type: str
        """
        self._url_domain = url_domain

    @property
    def ssl_id(self):
        """Gets the ssl_id of this AssociateCertificateV2Response.

        证书的编号

        :return: The ssl_id of this AssociateCertificateV2Response.
        :rtype: str
        """
        return self._ssl_id

    @ssl_id.setter
    def ssl_id(self, ssl_id):
        """Sets the ssl_id of this AssociateCertificateV2Response.

        证书的编号

        :param ssl_id: The ssl_id of this AssociateCertificateV2Response.
        :type: str
        """
        self._ssl_id = ssl_id

    @property
    def id(self):
        """Gets the id of this AssociateCertificateV2Response.

        自定义域名的编号

        :return: The id of this AssociateCertificateV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssociateCertificateV2Response.

        自定义域名的编号

        :param id: The id of this AssociateCertificateV2Response.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this AssociateCertificateV2Response.

        解析状态值

        :return: The status of this AssociateCertificateV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AssociateCertificateV2Response.

        解析状态值

        :param status: The status of this AssociateCertificateV2Response.
        :type: int
        """
        self._status = status

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssociateCertificateV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
