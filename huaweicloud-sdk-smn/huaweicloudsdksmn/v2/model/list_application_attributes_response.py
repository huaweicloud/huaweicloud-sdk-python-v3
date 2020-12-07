# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListApplicationAttributesResponse(SdkResponse):


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
        'application_id': 'str',
        'attributes': 'ListApplicationAttributesResponseBodyAttributes'
    }

    attribute_map = {
        'request_id': 'request_id',
        'application_id': 'application_id',
        'attributes': 'attributes'
    }

    def __init__(self, request_id=None, application_id=None, attributes=None):
        """ListApplicationAttributesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._request_id = None
        self._application_id = None
        self._attributes = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if application_id is not None:
            self.application_id = application_id
        if attributes is not None:
            self.attributes = attributes

    @property
    def request_id(self):
        """Gets the request_id of this ListApplicationAttributesResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListApplicationAttributesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListApplicationAttributesResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListApplicationAttributesResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def application_id(self):
        """Gets the application_id of this ListApplicationAttributesResponse.

        Application的唯一标识ID。

        :return: The application_id of this ListApplicationAttributesResponse.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ListApplicationAttributesResponse.

        Application的唯一标识ID。

        :param application_id: The application_id of this ListApplicationAttributesResponse.
        :type: str
        """
        self._application_id = application_id

    @property
    def attributes(self):
        """Gets the attributes of this ListApplicationAttributesResponse.


        :return: The attributes of this ListApplicationAttributesResponse.
        :rtype: ListApplicationAttributesResponseBodyAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ListApplicationAttributesResponse.


        :param attributes: The attributes of this ListApplicationAttributesResponse.
        :type: ListApplicationAttributesResponseBodyAttributes
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
        if not isinstance(other, ListApplicationAttributesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
