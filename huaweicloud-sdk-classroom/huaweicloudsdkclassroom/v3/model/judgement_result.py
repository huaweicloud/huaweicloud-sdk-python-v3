# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JudgementResult:

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
        'file_id': 'str',
        'image_id': 'str',
        'case_count': 'int',
        'executed_count': 'int',
        'testcases': 'list[JudgementCaseResult]'
    }

    attribute_map = {
        'output': 'output',
        'file_id': 'file_id',
        'image_id': 'image_id',
        'case_count': 'case_count',
        'executed_count': 'executed_count',
        'testcases': 'testcases'
    }

    def __init__(self, output=None, file_id=None, image_id=None, case_count=None, executed_count=None, testcases=None):
        """JudgementResult

        The model defined in huaweicloud sdk

        :param output: 标准类型输出结果
        :type output: str
        :param file_id: 文件形式输出的文件id，可根据文件id下载详情
        :type file_id: str
        :param image_id: 图片形式输出的图片id，可根据图片id下载详情
        :type image_id: str
        :param case_count: 用例形式输出的用例总个数
        :type case_count: int
        :param executed_count: 用例形式输出的已执行用例的个数
        :type executed_count: int
        :param testcases: 用例形式输出的已执行用例的结果
        :type testcases: list[:class:`huaweicloudsdkclassroom.v3.JudgementCaseResult`]
        """
        
        

        self._output = None
        self._file_id = None
        self._image_id = None
        self._case_count = None
        self._executed_count = None
        self._testcases = None
        self.discriminator = None

        self.output = output
        self.file_id = file_id
        self.image_id = image_id
        self.case_count = case_count
        self.executed_count = executed_count
        self.testcases = testcases

    @property
    def output(self):
        """Gets the output of this JudgementResult.

        标准类型输出结果

        :return: The output of this JudgementResult.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this JudgementResult.

        标准类型输出结果

        :param output: The output of this JudgementResult.
        :type output: str
        """
        self._output = output

    @property
    def file_id(self):
        """Gets the file_id of this JudgementResult.

        文件形式输出的文件id，可根据文件id下载详情

        :return: The file_id of this JudgementResult.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this JudgementResult.

        文件形式输出的文件id，可根据文件id下载详情

        :param file_id: The file_id of this JudgementResult.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def image_id(self):
        """Gets the image_id of this JudgementResult.

        图片形式输出的图片id，可根据图片id下载详情

        :return: The image_id of this JudgementResult.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this JudgementResult.

        图片形式输出的图片id，可根据图片id下载详情

        :param image_id: The image_id of this JudgementResult.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def case_count(self):
        """Gets the case_count of this JudgementResult.

        用例形式输出的用例总个数

        :return: The case_count of this JudgementResult.
        :rtype: int
        """
        return self._case_count

    @case_count.setter
    def case_count(self, case_count):
        """Sets the case_count of this JudgementResult.

        用例形式输出的用例总个数

        :param case_count: The case_count of this JudgementResult.
        :type case_count: int
        """
        self._case_count = case_count

    @property
    def executed_count(self):
        """Gets the executed_count of this JudgementResult.

        用例形式输出的已执行用例的个数

        :return: The executed_count of this JudgementResult.
        :rtype: int
        """
        return self._executed_count

    @executed_count.setter
    def executed_count(self, executed_count):
        """Sets the executed_count of this JudgementResult.

        用例形式输出的已执行用例的个数

        :param executed_count: The executed_count of this JudgementResult.
        :type executed_count: int
        """
        self._executed_count = executed_count

    @property
    def testcases(self):
        """Gets the testcases of this JudgementResult.

        用例形式输出的已执行用例的结果

        :return: The testcases of this JudgementResult.
        :rtype: list[:class:`huaweicloudsdkclassroom.v3.JudgementCaseResult`]
        """
        return self._testcases

    @testcases.setter
    def testcases(self, testcases):
        """Sets the testcases of this JudgementResult.

        用例形式输出的已执行用例的结果

        :param testcases: The testcases of this JudgementResult.
        :type testcases: list[:class:`huaweicloudsdkclassroom.v3.JudgementCaseResult`]
        """
        self._testcases = testcases

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
        if not isinstance(other, JudgementResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
