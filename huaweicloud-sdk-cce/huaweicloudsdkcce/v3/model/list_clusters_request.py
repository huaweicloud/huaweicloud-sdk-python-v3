# coding: utf-8

import pprint
import re

import six





class ListClustersRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'error_status': 'str',
        'detail': 'str',
        'status': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'error_status': 'errorStatus',
        'detail': 'detail',
        'status': 'status',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, content_type='application/json', error_status=None, detail=None, status=None, type=None, version=None):
        """ListClustersRequest - a model defined in huaweicloud sdk"""
        
        

        self._content_type = None
        self._error_status = None
        self._detail = None
        self._status = None
        self._type = None
        self._version = None
        self.discriminator = None

        self.content_type = content_type
        if error_status is not None:
            self.error_status = error_status
        if detail is not None:
            self.detail = detail
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def content_type(self):
        """Gets the content_type of this ListClustersRequest.


        :return: The content_type of this ListClustersRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ListClustersRequest.


        :param content_type: The content_type of this ListClustersRequest.
        :type: str
        """
        self._content_type = content_type

    @property
    def error_status(self):
        """Gets the error_status of this ListClustersRequest.


        :return: The error_status of this ListClustersRequest.
        :rtype: str
        """
        return self._error_status

    @error_status.setter
    def error_status(self, error_status):
        """Sets the error_status of this ListClustersRequest.


        :param error_status: The error_status of this ListClustersRequest.
        :type: str
        """
        self._error_status = error_status

    @property
    def detail(self):
        """Gets the detail of this ListClustersRequest.


        :return: The detail of this ListClustersRequest.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ListClustersRequest.


        :param detail: The detail of this ListClustersRequest.
        :type: str
        """
        self._detail = detail

    @property
    def status(self):
        """Gets the status of this ListClustersRequest.


        :return: The status of this ListClustersRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListClustersRequest.


        :param status: The status of this ListClustersRequest.
        :type: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ListClustersRequest.


        :return: The type of this ListClustersRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListClustersRequest.


        :param type: The type of this ListClustersRequest.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ListClustersRequest.


        :return: The version of this ListClustersRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListClustersRequest.


        :param version: The version of this ListClustersRequest.
        :type: str
        """
        self._version = version

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
        if not isinstance(other, ListClustersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
