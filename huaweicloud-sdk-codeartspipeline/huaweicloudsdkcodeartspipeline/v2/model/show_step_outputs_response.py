# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStepOutputsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step_outputs': 'list[OutputRespStepOutputs]',
        'current_system_time': 'int'
    }

    attribute_map = {
        'step_outputs': 'step_outputs',
        'current_system_time': 'current_system_time'
    }

    def __init__(self, step_outputs=None, current_system_time=None):
        """ShowStepOutputsResponse

        The model defined in huaweicloud sdk

        :param step_outputs: 
        :type step_outputs: list[:class:`huaweicloudsdkcodeartspipeline.v2.OutputRespStepOutputs`]
        :param current_system_time: 
        :type current_system_time: int
        """
        
        super(ShowStepOutputsResponse, self).__init__()

        self._step_outputs = None
        self._current_system_time = None
        self.discriminator = None

        if step_outputs is not None:
            self.step_outputs = step_outputs
        if current_system_time is not None:
            self.current_system_time = current_system_time

    @property
    def step_outputs(self):
        """Gets the step_outputs of this ShowStepOutputsResponse.

        :return: The step_outputs of this ShowStepOutputsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.OutputRespStepOutputs`]
        """
        return self._step_outputs

    @step_outputs.setter
    def step_outputs(self, step_outputs):
        """Sets the step_outputs of this ShowStepOutputsResponse.

        :param step_outputs: The step_outputs of this ShowStepOutputsResponse.
        :type step_outputs: list[:class:`huaweicloudsdkcodeartspipeline.v2.OutputRespStepOutputs`]
        """
        self._step_outputs = step_outputs

    @property
    def current_system_time(self):
        """Gets the current_system_time of this ShowStepOutputsResponse.

        :return: The current_system_time of this ShowStepOutputsResponse.
        :rtype: int
        """
        return self._current_system_time

    @current_system_time.setter
    def current_system_time(self, current_system_time):
        """Sets the current_system_time of this ShowStepOutputsResponse.

        :param current_system_time: The current_system_time of this ShowStepOutputsResponse.
        :type current_system_time: int
        """
        self._current_system_time = current_system_time

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
        if not isinstance(other, ShowStepOutputsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
