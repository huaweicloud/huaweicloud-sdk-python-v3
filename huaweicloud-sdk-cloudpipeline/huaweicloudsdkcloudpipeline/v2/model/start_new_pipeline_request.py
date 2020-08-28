# coding: utf-8

import pprint
import re

import six





class StartNewPipelineRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'pipeline_id': 'str',
        'body': 'StartPipelineParameters'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'pipeline_id': 'pipeline_id',
        'body': 'body'
    }

    def __init__(self, x_language=None, pipeline_id=None, body=None):
        """StartNewPipelineRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._pipeline_id = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.pipeline_id = pipeline_id
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        """Gets the x_language of this StartNewPipelineRequest.


        :return: The x_language of this StartNewPipelineRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this StartNewPipelineRequest.


        :param x_language: The x_language of this StartNewPipelineRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this StartNewPipelineRequest.


        :return: The pipeline_id of this StartNewPipelineRequest.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this StartNewPipelineRequest.


        :param pipeline_id: The pipeline_id of this StartNewPipelineRequest.
        :type: str
        """
        self._pipeline_id = pipeline_id

    @property
    def body(self):
        """Gets the body of this StartNewPipelineRequest.


        :return: The body of this StartNewPipelineRequest.
        :rtype: StartPipelineParameters
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this StartNewPipelineRequest.


        :param body: The body of this StartNewPipelineRequest.
        :type: StartPipelineParameters
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
        if not isinstance(other, StartNewPipelineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
