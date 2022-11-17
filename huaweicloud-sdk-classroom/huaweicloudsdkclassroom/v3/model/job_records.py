# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'auto_score': 'int',
        'case_pass_count': 'int',
        'exe_case_count': 'int',
        'code_line': 'int',
        'commit_time': 'str',
        'complexity_file_avg': 'str',
        'auto_score_using_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'auto_score': 'auto_score',
        'case_pass_count': 'case_pass_count',
        'exe_case_count': 'exe_case_count',
        'code_line': 'code_line',
        'commit_time': 'commit_time',
        'complexity_file_avg': 'complexity_file_avg',
        'auto_score_using_time': 'auto_score_using_time'
    }

    def __init__(self, name=None, auto_score=None, case_pass_count=None, exe_case_count=None, code_line=None, commit_time=None, complexity_file_avg=None, auto_score_using_time=None):
        """JobRecords

        The model defined in huaweicloud sdk

        :param name: 第XX次提交
        :type name: str
        :param auto_score: 习题判题得分
        :type auto_score: int
        :param case_pass_count: 习题用例通过数
        :type case_pass_count: int
        :param exe_case_count: 习题用例总数
        :type exe_case_count: int
        :param code_line: 代码行数
        :type code_line: int
        :param commit_time: 习题提交时间, 日期格式：yyyy-MM-dd HH:mm:ss
        :type commit_time: str
        :param complexity_file_avg: 习题圈复杂度
        :type complexity_file_avg: str
        :param auto_score_using_time: 习题判题耗时(毫秒)
        :type auto_score_using_time: int
        """
        
        

        self._name = None
        self._auto_score = None
        self._case_pass_count = None
        self._exe_case_count = None
        self._code_line = None
        self._commit_time = None
        self._complexity_file_avg = None
        self._auto_score_using_time = None
        self.discriminator = None

        self.name = name
        self.auto_score = auto_score
        self.case_pass_count = case_pass_count
        self.exe_case_count = exe_case_count
        self.code_line = code_line
        self.commit_time = commit_time
        self.complexity_file_avg = complexity_file_avg
        self.auto_score_using_time = auto_score_using_time

    @property
    def name(self):
        """Gets the name of this JobRecords.

        第XX次提交

        :return: The name of this JobRecords.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobRecords.

        第XX次提交

        :param name: The name of this JobRecords.
        :type name: str
        """
        self._name = name

    @property
    def auto_score(self):
        """Gets the auto_score of this JobRecords.

        习题判题得分

        :return: The auto_score of this JobRecords.
        :rtype: int
        """
        return self._auto_score

    @auto_score.setter
    def auto_score(self, auto_score):
        """Sets the auto_score of this JobRecords.

        习题判题得分

        :param auto_score: The auto_score of this JobRecords.
        :type auto_score: int
        """
        self._auto_score = auto_score

    @property
    def case_pass_count(self):
        """Gets the case_pass_count of this JobRecords.

        习题用例通过数

        :return: The case_pass_count of this JobRecords.
        :rtype: int
        """
        return self._case_pass_count

    @case_pass_count.setter
    def case_pass_count(self, case_pass_count):
        """Sets the case_pass_count of this JobRecords.

        习题用例通过数

        :param case_pass_count: The case_pass_count of this JobRecords.
        :type case_pass_count: int
        """
        self._case_pass_count = case_pass_count

    @property
    def exe_case_count(self):
        """Gets the exe_case_count of this JobRecords.

        习题用例总数

        :return: The exe_case_count of this JobRecords.
        :rtype: int
        """
        return self._exe_case_count

    @exe_case_count.setter
    def exe_case_count(self, exe_case_count):
        """Sets the exe_case_count of this JobRecords.

        习题用例总数

        :param exe_case_count: The exe_case_count of this JobRecords.
        :type exe_case_count: int
        """
        self._exe_case_count = exe_case_count

    @property
    def code_line(self):
        """Gets the code_line of this JobRecords.

        代码行数

        :return: The code_line of this JobRecords.
        :rtype: int
        """
        return self._code_line

    @code_line.setter
    def code_line(self, code_line):
        """Sets the code_line of this JobRecords.

        代码行数

        :param code_line: The code_line of this JobRecords.
        :type code_line: int
        """
        self._code_line = code_line

    @property
    def commit_time(self):
        """Gets the commit_time of this JobRecords.

        习题提交时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :return: The commit_time of this JobRecords.
        :rtype: str
        """
        return self._commit_time

    @commit_time.setter
    def commit_time(self, commit_time):
        """Sets the commit_time of this JobRecords.

        习题提交时间, 日期格式：yyyy-MM-dd HH:mm:ss

        :param commit_time: The commit_time of this JobRecords.
        :type commit_time: str
        """
        self._commit_time = commit_time

    @property
    def complexity_file_avg(self):
        """Gets the complexity_file_avg of this JobRecords.

        习题圈复杂度

        :return: The complexity_file_avg of this JobRecords.
        :rtype: str
        """
        return self._complexity_file_avg

    @complexity_file_avg.setter
    def complexity_file_avg(self, complexity_file_avg):
        """Sets the complexity_file_avg of this JobRecords.

        习题圈复杂度

        :param complexity_file_avg: The complexity_file_avg of this JobRecords.
        :type complexity_file_avg: str
        """
        self._complexity_file_avg = complexity_file_avg

    @property
    def auto_score_using_time(self):
        """Gets the auto_score_using_time of this JobRecords.

        习题判题耗时(毫秒)

        :return: The auto_score_using_time of this JobRecords.
        :rtype: int
        """
        return self._auto_score_using_time

    @auto_score_using_time.setter
    def auto_score_using_time(self, auto_score_using_time):
        """Sets the auto_score_using_time of this JobRecords.

        习题判题耗时(毫秒)

        :param auto_score_using_time: The auto_score_using_time of this JobRecords.
        :type auto_score_using_time: int
        """
        self._auto_score_using_time = auto_score_using_time

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
        if not isinstance(other, JobRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
