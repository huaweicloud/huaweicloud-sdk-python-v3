# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopPipelineJobRequest:

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
        'trigger_savepoint': 'bool'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'trigger_savepoint': 'trigger_savepoint'
    }

    def __init__(self, pipeline_id=None, trigger_savepoint=None):
        """StopPipelineJobRequest

        The model defined in huaweicloud sdk

        :param pipeline_id: 管道ID
        :type pipeline_id: str
        :param trigger_savepoint: 停止管道作业触发savepoint
        :type trigger_savepoint: bool
        """
        
        

        self._pipeline_id = None
        self._trigger_savepoint = None
        self.discriminator = None

        self.pipeline_id = pipeline_id
        if trigger_savepoint is not None:
            self.trigger_savepoint = trigger_savepoint

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this StopPipelineJobRequest.

        管道ID

        :return: The pipeline_id of this StopPipelineJobRequest.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this StopPipelineJobRequest.

        管道ID

        :param pipeline_id: The pipeline_id of this StopPipelineJobRequest.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def trigger_savepoint(self):
        """Gets the trigger_savepoint of this StopPipelineJobRequest.

        停止管道作业触发savepoint

        :return: The trigger_savepoint of this StopPipelineJobRequest.
        :rtype: bool
        """
        return self._trigger_savepoint

    @trigger_savepoint.setter
    def trigger_savepoint(self, trigger_savepoint):
        """Sets the trigger_savepoint of this StopPipelineJobRequest.

        停止管道作业触发savepoint

        :param trigger_savepoint: The trigger_savepoint of this StopPipelineJobRequest.
        :type trigger_savepoint: bool
        """
        self._trigger_savepoint = trigger_savepoint

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
        if not isinstance(other, StopPipelineJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
