# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionsPipelineRunsPollingQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_run_ids': 'list[str]'
    }

    attribute_map = {
        'pipeline_run_ids': 'pipeline_run_ids'
    }

    def __init__(self, pipeline_run_ids=None):
        r"""ActionsPipelineRunsPollingQueryDTO

        The model defined in huaweicloud sdk

        :param pipeline_run_ids: **参数解释**： 流水线运行实例ID列表。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 
        :type pipeline_run_ids: list[str]
        """
        
        

        self._pipeline_run_ids = None
        self.discriminator = None

        if pipeline_run_ids is not None:
            self.pipeline_run_ids = pipeline_run_ids

    @property
    def pipeline_run_ids(self):
        r"""Gets the pipeline_run_ids of this ActionsPipelineRunsPollingQueryDTO.

        **参数解释**： 流水线运行实例ID列表。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :return: The pipeline_run_ids of this ActionsPipelineRunsPollingQueryDTO.
        :rtype: list[str]
        """
        return self._pipeline_run_ids

    @pipeline_run_ids.setter
    def pipeline_run_ids(self, pipeline_run_ids):
        r"""Sets the pipeline_run_ids of this ActionsPipelineRunsPollingQueryDTO.

        **参数解释**： 流水线运行实例ID列表。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :param pipeline_run_ids: The pipeline_run_ids of this ActionsPipelineRunsPollingQueryDTO.
        :type pipeline_run_ids: list[str]
        """
        self._pipeline_run_ids = pipeline_run_ids

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
        if not isinstance(other, ActionsPipelineRunsPollingQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
