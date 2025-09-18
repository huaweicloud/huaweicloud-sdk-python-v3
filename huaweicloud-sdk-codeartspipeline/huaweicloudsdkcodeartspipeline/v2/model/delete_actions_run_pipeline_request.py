# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteActionsRunPipelineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'pipeline_id': 'str',
        'pipeline_run_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'pipeline_id': 'pipeline_id',
        'pipeline_run_id': 'pipeline_run_id'
    }

    def __init__(self, domain_id=None, pipeline_id=None, pipeline_run_id=None):
        r"""DeleteActionsRunPipelineRequest

        The model defined in huaweicloud sdk

        :param domain_id: **参数解释**： 租户id。 **约束限制**： 不涉及。 **取值范围**： 32位字符，由数字和字母组成。 **默认取值**： 不涉及。 
        :type domain_id: str
        :param pipeline_id: **参数解释**： 流水线ID，可以通过[查询流水线列表](ListPipelines.xml)接口，其中pipelines.pipelineId即为流水线ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 
        :type pipeline_id: str
        :param pipeline_run_id: **参数解释**： 流水线运行实例ID，[运行流水线](RunPipeline.xml)接口的返回值即为流水线运行实例ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 
        :type pipeline_run_id: str
        """
        
        

        self._domain_id = None
        self._pipeline_id = None
        self._pipeline_run_id = None
        self.discriminator = None

        self.domain_id = domain_id
        self.pipeline_id = pipeline_id
        self.pipeline_run_id = pipeline_run_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DeleteActionsRunPipelineRequest.

        **参数解释**： 租户id。 **约束限制**： 不涉及。 **取值范围**： 32位字符，由数字和字母组成。 **默认取值**： 不涉及。 

        :return: The domain_id of this DeleteActionsRunPipelineRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DeleteActionsRunPipelineRequest.

        **参数解释**： 租户id。 **约束限制**： 不涉及。 **取值范围**： 32位字符，由数字和字母组成。 **默认取值**： 不涉及。 

        :param domain_id: The domain_id of this DeleteActionsRunPipelineRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def pipeline_id(self):
        r"""Gets the pipeline_id of this DeleteActionsRunPipelineRequest.

        **参数解释**： 流水线ID，可以通过[查询流水线列表](ListPipelines.xml)接口，其中pipelines.pipelineId即为流水线ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :return: The pipeline_id of this DeleteActionsRunPipelineRequest.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        r"""Sets the pipeline_id of this DeleteActionsRunPipelineRequest.

        **参数解释**： 流水线ID，可以通过[查询流水线列表](ListPipelines.xml)接口，其中pipelines.pipelineId即为流水线ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :param pipeline_id: The pipeline_id of this DeleteActionsRunPipelineRequest.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def pipeline_run_id(self):
        r"""Gets the pipeline_run_id of this DeleteActionsRunPipelineRequest.

        **参数解释**： 流水线运行实例ID，[运行流水线](RunPipeline.xml)接口的返回值即为流水线运行实例ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :return: The pipeline_run_id of this DeleteActionsRunPipelineRequest.
        :rtype: str
        """
        return self._pipeline_run_id

    @pipeline_run_id.setter
    def pipeline_run_id(self, pipeline_run_id):
        r"""Sets the pipeline_run_id of this DeleteActionsRunPipelineRequest.

        **参数解释**： 流水线运行实例ID，[运行流水线](RunPipeline.xml)接口的返回值即为流水线运行实例ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :param pipeline_run_id: The pipeline_run_id of this DeleteActionsRunPipelineRequest.
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
        if not isinstance(other, DeleteActionsRunPipelineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
