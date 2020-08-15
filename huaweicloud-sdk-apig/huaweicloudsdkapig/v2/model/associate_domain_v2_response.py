# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class AssociateDomainV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'url_domain': 'str',
        'id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'url_domain': 'url_domain',
        'id': 'id',
        'status': 'status'
    }

    def __init__(self, url_domain=None, id=None, status=None):
        """AssociateDomainV2Response - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._url_domain = None
        self._id = None
        self._status = None
        self.discriminator = None

        if url_domain is not None:
            self.url_domain = url_domain
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status

    @property
    def url_domain(self):
        """Gets the url_domain of this AssociateDomainV2Response.

        自定义域名

        :return: The url_domain of this AssociateDomainV2Response.
        :rtype: str
        """
        return self._url_domain

    @url_domain.setter
    def url_domain(self, url_domain):
        """Sets the url_domain of this AssociateDomainV2Response.

        自定义域名

        :param url_domain: The url_domain of this AssociateDomainV2Response.
        :type: str
        """
        self._url_domain = url_domain

    @property
    def id(self):
        """Gets the id of this AssociateDomainV2Response.

        域名的编号

        :return: The id of this AssociateDomainV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssociateDomainV2Response.

        域名的编号

        :param id: The id of this AssociateDomainV2Response.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this AssociateDomainV2Response.

        CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败

        :return: The status of this AssociateDomainV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AssociateDomainV2Response.

        CNAME解析状态 - 1: 未解析 - 2: 解析中 - 3: 解析成功 - 4: 解析失败

        :param status: The status of this AssociateDomainV2Response.
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
        if not isinstance(other, AssociateDomainV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
