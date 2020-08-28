# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class StartNewPipelineResponse(SdkResponse):


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
        'build_id': 'str'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'build_id': 'build_id'
    }

    def __init__(self, pipeline_id=None, build_id=None):
        """StartNewPipelineResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._pipeline_id = None
        self._build_id = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if build_id is not None:
            self.build_id = build_id

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this StartNewPipelineResponse.

        流水线ID

        :return: The pipeline_id of this StartNewPipelineResponse.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this StartNewPipelineResponse.

        流水线ID

        :param pipeline_id: The pipeline_id of this StartNewPipelineResponse.
        :type: str
        """
        self._pipeline_id = pipeline_id

    @property
    def build_id(self):
        """Gets the build_id of this StartNewPipelineResponse.

        流水线构建ID

        :return: The build_id of this StartNewPipelineResponse.
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this StartNewPipelineResponse.

        流水线构建ID

        :param build_id: The build_id of this StartNewPipelineResponse.
        :type: str
        """
        self._build_id = build_id

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
        if not isinstance(other, StartNewPipelineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
