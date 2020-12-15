# coding: utf-8

import pprint
import re

import six





class CreateCloudPersistentVolumeClaimsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'content_type': 'str',
        'x_cluster_id': 'str',
        'body': 'PersistentVolumeClaim'
    }

    attribute_map = {
        'namespace': 'namespace',
        'content_type': 'Content-Type',
        'x_cluster_id': 'X-Cluster-ID',
        'body': 'body'
    }

    def __init__(self, namespace=None, content_type='application/json', x_cluster_id=None, body=None):
        """CreateCloudPersistentVolumeClaimsRequest - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._content_type = None
        self._x_cluster_id = None
        self._body = None
        self.discriminator = None

        self.namespace = namespace
        self.content_type = content_type
        if x_cluster_id is not None:
            self.x_cluster_id = x_cluster_id
        if body is not None:
            self.body = body

    @property
    def namespace(self):
        """Gets the namespace of this CreateCloudPersistentVolumeClaimsRequest.


        :return: The namespace of this CreateCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CreateCloudPersistentVolumeClaimsRequest.


        :param namespace: The namespace of this CreateCloudPersistentVolumeClaimsRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def content_type(self):
        """Gets the content_type of this CreateCloudPersistentVolumeClaimsRequest.


        :return: The content_type of this CreateCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this CreateCloudPersistentVolumeClaimsRequest.


        :param content_type: The content_type of this CreateCloudPersistentVolumeClaimsRequest.
        :type: str
        """
        self._content_type = content_type

    @property
    def x_cluster_id(self):
        """Gets the x_cluster_id of this CreateCloudPersistentVolumeClaimsRequest.


        :return: The x_cluster_id of this CreateCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._x_cluster_id

    @x_cluster_id.setter
    def x_cluster_id(self, x_cluster_id):
        """Sets the x_cluster_id of this CreateCloudPersistentVolumeClaimsRequest.


        :param x_cluster_id: The x_cluster_id of this CreateCloudPersistentVolumeClaimsRequest.
        :type: str
        """
        self._x_cluster_id = x_cluster_id

    @property
    def body(self):
        """Gets the body of this CreateCloudPersistentVolumeClaimsRequest.


        :return: The body of this CreateCloudPersistentVolumeClaimsRequest.
        :rtype: PersistentVolumeClaim
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateCloudPersistentVolumeClaimsRequest.


        :param body: The body of this CreateCloudPersistentVolumeClaimsRequest.
        :type: PersistentVolumeClaim
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
        if not isinstance(other, CreateCloudPersistentVolumeClaimsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
