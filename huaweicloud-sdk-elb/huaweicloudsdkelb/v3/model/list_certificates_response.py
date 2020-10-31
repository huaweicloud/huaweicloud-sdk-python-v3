# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCertificatesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'page_info': 'PageInfo',
        'certificates': 'list[CertificateInfo]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'certificates': 'certificates'
    }

    def __init__(self, request_id=None, page_info=None, certificates=None):
        """ListCertificatesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._request_id = None
        self._page_info = None
        self._certificates = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        if certificates is not None:
            self.certificates = certificates

    @property
    def request_id(self):
        """Gets the request_id of this ListCertificatesResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this ListCertificatesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListCertificatesResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this ListCertificatesResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListCertificatesResponse.


        :return: The page_info of this ListCertificatesResponse.
        :rtype: PageInfo
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListCertificatesResponse.


        :param page_info: The page_info of this ListCertificatesResponse.
        :type: PageInfo
        """
        self._page_info = page_info

    @property
    def certificates(self):
        """Gets the certificates of this ListCertificatesResponse.

        证书对象列表。

        :return: The certificates of this ListCertificatesResponse.
        :rtype: list[CertificateInfo]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """Sets the certificates of this ListCertificatesResponse.

        证书对象列表。

        :param certificates: The certificates of this ListCertificatesResponse.
        :type: list[CertificateInfo]
        """
        self._certificates = certificates

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
        if not isinstance(other, ListCertificatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
