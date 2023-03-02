# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SummarizationAnalysisInference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'output_duration': 'int',
        'outcome_type': 'str'
    }

    attribute_map = {
        'output_duration': 'output_duration',
        'outcome_type': 'outcome_type'
    }

    def __init__(self, output_duration=None, outcome_type=None):
        """SummarizationAnalysisInference

        The model defined in huaweicloud sdk

        :param output_duration: 摘要片段输出总时长
        :type output_duration: int
        :param outcome_type: 输出类型，不填摘要片段和集锦都输出。填summary只输出集锦；填fragment只输出片段。
        :type outcome_type: str
        """
        
        

        self._output_duration = None
        self._outcome_type = None
        self.discriminator = None

        self.output_duration = output_duration
        if outcome_type is not None:
            self.outcome_type = outcome_type

    @property
    def output_duration(self):
        """Gets the output_duration of this SummarizationAnalysisInference.

        摘要片段输出总时长

        :return: The output_duration of this SummarizationAnalysisInference.
        :rtype: int
        """
        return self._output_duration

    @output_duration.setter
    def output_duration(self, output_duration):
        """Sets the output_duration of this SummarizationAnalysisInference.

        摘要片段输出总时长

        :param output_duration: The output_duration of this SummarizationAnalysisInference.
        :type output_duration: int
        """
        self._output_duration = output_duration

    @property
    def outcome_type(self):
        """Gets the outcome_type of this SummarizationAnalysisInference.

        输出类型，不填摘要片段和集锦都输出。填summary只输出集锦；填fragment只输出片段。

        :return: The outcome_type of this SummarizationAnalysisInference.
        :rtype: str
        """
        return self._outcome_type

    @outcome_type.setter
    def outcome_type(self, outcome_type):
        """Sets the outcome_type of this SummarizationAnalysisInference.

        输出类型，不填摘要片段和集锦都输出。填summary只输出集锦；填fragment只输出片段。

        :param outcome_type: The outcome_type of this SummarizationAnalysisInference.
        :type outcome_type: str
        """
        self._outcome_type = outcome_type

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
        if not isinstance(other, SummarizationAnalysisInference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
