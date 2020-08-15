# coding: utf-8

import pprint
import re

import six





class ListKmsByTagsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_instances': 'str',
        'version_id': 'str',
        'body': 'ListKmsByTagsRequestBody'
    }

    attribute_map = {
        'resource_instances': 'resource_instances',
        'version_id': 'version_id',
        'body': 'body'
    }

    def __init__(self, resource_instances='resource_instances', version_id='v1.0', body=None):
        """ListKmsByTagsRequest - a model defined in huaweicloud sdk"""
        
        

        self._resource_instances = None
        self._version_id = None
        self._body = None
        self.discriminator = None

        self.resource_instances = resource_instances
        self.version_id = version_id
        if body is not None:
            self.body = body

    @property
    def resource_instances(self):
        """Gets the resource_instances of this ListKmsByTagsRequest.


        :return: The resource_instances of this ListKmsByTagsRequest.
        :rtype: str
        """
        return self._resource_instances

    @resource_instances.setter
    def resource_instances(self, resource_instances):
        """Sets the resource_instances of this ListKmsByTagsRequest.


        :param resource_instances: The resource_instances of this ListKmsByTagsRequest.
        :type: str
        """
        self._resource_instances = resource_instances

    @property
    def version_id(self):
        """Gets the version_id of this ListKmsByTagsRequest.


        :return: The version_id of this ListKmsByTagsRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ListKmsByTagsRequest.


        :param version_id: The version_id of this ListKmsByTagsRequest.
        :type: str
        """
        self._version_id = version_id

    @property
    def body(self):
        """Gets the body of this ListKmsByTagsRequest.


        :return: The body of this ListKmsByTagsRequest.
        :rtype: ListKmsByTagsRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListKmsByTagsRequest.


        :param body: The body of this ListKmsByTagsRequest.
        :type: ListKmsByTagsRequestBody
        """
        self._body = body

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
        if not isinstance(other, ListKmsByTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
