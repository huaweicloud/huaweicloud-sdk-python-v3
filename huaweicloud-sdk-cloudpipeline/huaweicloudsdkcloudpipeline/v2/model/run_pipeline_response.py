# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunPipelineResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_run_id': 'str'
    }

    attribute_map = {
        'pipeline_run_id': 'pipeline_run_id'
    }

    def __init__(self, pipeline_run_id=None):
        """RunPipelineResponse

        The model defined in huaweicloud sdk

        :param pipeline_run_id: 
        :type pipeline_run_id: str
        """
        
        super(RunPipelineResponse, self).__init__()

        self._pipeline_run_id = None
        self.discriminator = None

        if pipeline_run_id is not None:
            self.pipeline_run_id = pipeline_run_id

    @property
    def pipeline_run_id(self):
        """Gets the pipeline_run_id of this RunPipelineResponse.

        :return: The pipeline_run_id of this RunPipelineResponse.
        :rtype: str
        """
        return self._pipeline_run_id

    @pipeline_run_id.setter
    def pipeline_run_id(self, pipeline_run_id):
        """Sets the pipeline_run_id of this RunPipelineResponse.

        :param pipeline_run_id: The pipeline_run_id of this RunPipelineResponse.
        :type pipeline_run_id: str
        """
        self._pipeline_run_id = pipeline_run_id

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RunPipelineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
