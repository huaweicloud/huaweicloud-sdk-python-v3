# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageExerciseJudgeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notify_url': 'str',
        'timeout': 'int',
        'output_type': 'str',
        'code_answer': 'str'
    }

    attribute_map = {
        'notify_url': 'notify_url',
        'timeout': 'timeout',
        'output_type': 'output_type',
        'code_answer': 'code_answer'
    }

    def __init__(self, notify_url=None, timeout=None, output_type=None, code_answer=None):
        r"""PackageExerciseJudgeRequestBody

        The model defined in huaweicloud sdk

        :param notify_url: 判题结束后的回调url
        :type notify_url: str
        :param timeout: 代码超时时间
        :type timeout: int
        :param output_type: 结果返回类型
        :type output_type: str
        :param code_answer: 习题作答（需Base64编码）
        :type code_answer: str
        """
        
        

        self._notify_url = None
        self._timeout = None
        self._output_type = None
        self._code_answer = None
        self.discriminator = None

        self.notify_url = notify_url
        if timeout is not None:
            self.timeout = timeout
        self.output_type = output_type
        self.code_answer = code_answer

    @property
    def notify_url(self):
        r"""Gets the notify_url of this PackageExerciseJudgeRequestBody.

        判题结束后的回调url

        :return: The notify_url of this PackageExerciseJudgeRequestBody.
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        r"""Sets the notify_url of this PackageExerciseJudgeRequestBody.

        判题结束后的回调url

        :param notify_url: The notify_url of this PackageExerciseJudgeRequestBody.
        :type notify_url: str
        """
        self._notify_url = notify_url

    @property
    def timeout(self):
        r"""Gets the timeout of this PackageExerciseJudgeRequestBody.

        代码超时时间

        :return: The timeout of this PackageExerciseJudgeRequestBody.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this PackageExerciseJudgeRequestBody.

        代码超时时间

        :param timeout: The timeout of this PackageExerciseJudgeRequestBody.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def output_type(self):
        r"""Gets the output_type of this PackageExerciseJudgeRequestBody.

        结果返回类型

        :return: The output_type of this PackageExerciseJudgeRequestBody.
        :rtype: str
        """
        return self._output_type

    @output_type.setter
    def output_type(self, output_type):
        r"""Sets the output_type of this PackageExerciseJudgeRequestBody.

        结果返回类型

        :param output_type: The output_type of this PackageExerciseJudgeRequestBody.
        :type output_type: str
        """
        self._output_type = output_type

    @property
    def code_answer(self):
        r"""Gets the code_answer of this PackageExerciseJudgeRequestBody.

        习题作答（需Base64编码）

        :return: The code_answer of this PackageExerciseJudgeRequestBody.
        :rtype: str
        """
        return self._code_answer

    @code_answer.setter
    def code_answer(self, code_answer):
        r"""Sets the code_answer of this PackageExerciseJudgeRequestBody.

        习题作答（需Base64编码）

        :param code_answer: The code_answer of this PackageExerciseJudgeRequestBody.
        :type code_answer: str
        """
        self._code_answer = code_answer

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
        if not isinstance(other, PackageExerciseJudgeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
