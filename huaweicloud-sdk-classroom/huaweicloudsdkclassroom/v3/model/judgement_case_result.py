# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JudgementCaseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'output': 'str',
        'case_status': 'str'
    }

    attribute_map = {
        'output': 'output',
        'case_status': 'case_status'
    }

    def __init__(self, output=None, case_status=None):
        r"""JudgementCaseResult

        The model defined in huaweicloud sdk

        :param output: 用例实际运行结果输出
        :type output: str
        :param case_status: 用例运行结果状态： judgeout判题类型对应：pass（用例比对成功）、failed（用例比对失败）； caseout判题类型对应：success（用例运行成功）、error（用例运行失败）；run_timeout（用例运行超时）
        :type case_status: str
        """
        
        

        self._output = None
        self._case_status = None
        self.discriminator = None

        self.output = output
        self.case_status = case_status

    @property
    def output(self):
        r"""Gets the output of this JudgementCaseResult.

        用例实际运行结果输出

        :return: The output of this JudgementCaseResult.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this JudgementCaseResult.

        用例实际运行结果输出

        :param output: The output of this JudgementCaseResult.
        :type output: str
        """
        self._output = output

    @property
    def case_status(self):
        r"""Gets the case_status of this JudgementCaseResult.

        用例运行结果状态： judgeout判题类型对应：pass（用例比对成功）、failed（用例比对失败）； caseout判题类型对应：success（用例运行成功）、error（用例运行失败）；run_timeout（用例运行超时）

        :return: The case_status of this JudgementCaseResult.
        :rtype: str
        """
        return self._case_status

    @case_status.setter
    def case_status(self, case_status):
        r"""Sets the case_status of this JudgementCaseResult.

        用例运行结果状态： judgeout判题类型对应：pass（用例比对成功）、failed（用例比对失败）； caseout判题类型对应：success（用例运行成功）、error（用例运行失败）；run_timeout（用例运行超时）

        :param case_status: The case_status of this JudgementCaseResult.
        :type case_status: str
        """
        self._case_status = case_status

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
        if not isinstance(other, JudgementCaseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
