# coding: utf-8

import pprint
import re

import six





class DeleteCloudPersistentVolumeClaimsRequest:


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
        'namespace': 'str',
        'content_type': 'str',
        'x_cluster_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'content_type': 'Content-Type',
        'x_cluster_id': 'X-Cluster-ID'
    }

    def __init__(self, name=None, namespace=None, content_type='application/json', x_cluster_id=None):
        """DeleteCloudPersistentVolumeClaimsRequest - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._namespace = None
        self._content_type = None
        self._x_cluster_id = None
        self.discriminator = None

        self.name = name
        self.namespace = namespace
        self.content_type = content_type
        if x_cluster_id is not None:
            self.x_cluster_id = x_cluster_id

    @property
    def name(self):
        """Gets the name of this DeleteCloudPersistentVolumeClaimsRequest.


        :return: The name of this DeleteCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeleteCloudPersistentVolumeClaimsRequest.


        :param name: The name of this DeleteCloudPersistentVolumeClaimsRequest.
        :type: str
        """
        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this DeleteCloudPersistentVolumeClaimsRequest.


        :return: The namespace of this DeleteCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this DeleteCloudPersistentVolumeClaimsRequest.


        :param namespace: The namespace of this DeleteCloudPersistentVolumeClaimsRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def content_type(self):
        """Gets the content_type of this DeleteCloudPersistentVolumeClaimsRequest.


        :return: The content_type of this DeleteCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this DeleteCloudPersistentVolumeClaimsRequest.


        :param content_type: The content_type of this DeleteCloudPersistentVolumeClaimsRequest.
        :type: str
        """
        self._content_type = content_type

    @property
    def x_cluster_id(self):
        """Gets the x_cluster_id of this DeleteCloudPersistentVolumeClaimsRequest.


        :return: The x_cluster_id of this DeleteCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._x_cluster_id

    @x_cluster_id.setter
    def x_cluster_id(self, x_cluster_id):
        """Sets the x_cluster_id of this DeleteCloudPersistentVolumeClaimsRequest.


        :param x_cluster_id: The x_cluster_id of this DeleteCloudPersistentVolumeClaimsRequest.
        :type: str
        """
        self._x_cluster_id = x_cluster_id

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
        if not isinstance(other, DeleteCloudPersistentVolumeClaimsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
