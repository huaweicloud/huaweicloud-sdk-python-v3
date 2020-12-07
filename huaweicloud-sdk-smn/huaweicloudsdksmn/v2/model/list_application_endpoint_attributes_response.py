# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListApplicationEndpointAttributesResponse(SdkResponse):


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
        'attributes': 'ListApplicationEndpointAttributesResponseBodyAttributes'
    }

    attribute_map = {
        'request_id': 'request_id',
        'attributes': 'attributes'
    }

    def __init__(self, request_id=None, attributes=None):
        """ListApplicationEndpointAttributesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._request_id = None
        self._attributes = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if attributes is not None:
            self.attributes = attributes

    @property
    def request_id(self):
        """Gets the request_id of this ListApplicationEndpointAttributesResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListApplicationEndpointAttributesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListApplicationEndpointAttributesResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListApplicationEndpointAttributesResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def attributes(self):
        """Gets the attributes of this ListApplicationEndpointAttributesResponse.


        :return: The attributes of this ListApplicationEndpointAttributesResponse.
        :rtype: ListApplicationEndpointAttributesResponseBodyAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ListApplicationEndpointAttributesResponse.


        :param attributes: The attributes of this ListApplicationEndpointAttributesResponse.
        :type: ListApplicationEndpointAttributesResponseBodyAttributes
        """
        self._attributes = attributes

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
        if not isinstance(other, ListApplicationEndpointAttributesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
