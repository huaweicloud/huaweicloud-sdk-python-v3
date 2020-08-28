# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class RemovePipelineResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pipeline_id': 'str',
        'pipeline_name': 'str'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'pipeline_name': 'pipeline_name'
    }

    def __init__(self, pipeline_id=None, pipeline_name=None):
        """RemovePipelineResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._pipeline_id = None
        self._pipeline_name = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this RemovePipelineResponse.

        流水线ID

        :return: The pipeline_id of this RemovePipelineResponse.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this RemovePipelineResponse.

        流水线ID

        :param pipeline_id: The pipeline_id of this RemovePipelineResponse.
        :type: str
        """
        self._pipeline_id = pipeline_id

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this RemovePipelineResponse.

        流水线名字

        :return: The pipeline_name of this RemovePipelineResponse.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this RemovePipelineResponse.

        流水线名字

        :param pipeline_name: The pipeline_name of this RemovePipelineResponse.
        :type: str
        """
        self._pipeline_name = pipeline_name

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
        if not isinstance(other, RemovePipelineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
