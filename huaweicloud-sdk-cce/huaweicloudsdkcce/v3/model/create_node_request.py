# coding: utf-8

import pprint
import re

import six





class CreateNodeRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'content_type': 'str',
        'nodepool_scale_up': 'str',
        'body': 'V3NodeCreateRequest'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'content_type': 'Content-Type',
        'nodepool_scale_up': 'nodepoolScaleUp',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, content_type='application/json', nodepool_scale_up=None, body=None):
        """CreateNodeRequest - a model defined in huaweicloud sdk"""
        
        

        self._cluster_id = None
        self._content_type = None
        self._nodepool_scale_up = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.content_type = content_type
        if nodepool_scale_up is not None:
            self.nodepool_scale_up = nodepool_scale_up
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateNodeRequest.


        :return: The cluster_id of this CreateNodeRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateNodeRequest.


        :param cluster_id: The cluster_id of this CreateNodeRequest.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def content_type(self):
        """Gets the content_type of this CreateNodeRequest.


        :return: The content_type of this CreateNodeRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this CreateNodeRequest.


        :param content_type: The content_type of this CreateNodeRequest.
        :type: str
        """
        self._content_type = content_type

    @property
    def nodepool_scale_up(self):
        """Gets the nodepool_scale_up of this CreateNodeRequest.


        :return: The nodepool_scale_up of this CreateNodeRequest.
        :rtype: str
        """
        return self._nodepool_scale_up

    @nodepool_scale_up.setter
    def nodepool_scale_up(self, nodepool_scale_up):
        """Sets the nodepool_scale_up of this CreateNodeRequest.


        :param nodepool_scale_up: The nodepool_scale_up of this CreateNodeRequest.
        :type: str
        """
        self._nodepool_scale_up = nodepool_scale_up

    @property
    def body(self):
        """Gets the body of this CreateNodeRequest.


        :return: The body of this CreateNodeRequest.
        :rtype: V3NodeCreateRequest
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateNodeRequest.


        :param body: The body of this CreateNodeRequest.
        :type: V3NodeCreateRequest
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
        if not isinstance(other, CreateNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
