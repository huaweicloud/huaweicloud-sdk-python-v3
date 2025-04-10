# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'creator_id': 'str',
        'git_url': 'str',
        'git_branch': 'str',
        'last_check_time': 'str',
        'code_line_total': 'int',
        'code_line': 'int',
        'code_quality': 'float',
        'issue_count': 'int',
        'risk_coefficient': 'float',
        'duplication_ratio': 'str',
        'complexity_count': 'int',
        'duplicated_lines': 'int',
        'comment_lines': 'int',
        'comment_ratio': 'str',
        'duplicated_blocks': 'int',
        'last_exec_time': 'str',
        'check_type': 'str',
        'created_at': 'str',
        'cyclomatic_complexity_per_method': 'str',
        'cyclomatic_complexity_per_file': 'str',
        'critical_count': 'str',
        'major_count': 'str',
        'minor_count': 'str',
        'suggestion_count': 'str',
        'is_access': 'str',
        'trigger_type': 'str',
        'file_duplication_ratio': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'creator_id': 'creator_id',
        'git_url': 'git_url',
        'git_branch': 'git_branch',
        'last_check_time': 'last_check_time',
        'code_line_total': 'code_line_total',
        'code_line': 'code_line',
        'code_quality': 'code_quality',
        'issue_count': 'issue_count',
        'risk_coefficient': 'risk_coefficient',
        'duplication_ratio': 'duplication_ratio',
        'complexity_count': 'complexity_count',
        'duplicated_lines': 'duplicated_lines',
        'comment_lines': 'comment_lines',
        'comment_ratio': 'comment_ratio',
        'duplicated_blocks': 'duplicated_blocks',
        'last_exec_time': 'last_exec_time',
        'check_type': 'check_type',
        'created_at': 'created_at',
        'cyclomatic_complexity_per_method': 'cyclomatic_complexity_per_method',
        'cyclomatic_complexity_per_file': 'cyclomatic_complexity_per_file',
        'critical_count': 'critical_count',
        'major_count': 'major_count',
        'minor_count': 'minor_count',
        'suggestion_count': 'suggestion_count',
        'is_access': 'is_access',
        'trigger_type': 'trigger_type',
        'file_duplication_ratio': 'file_duplication_ratio'
    }

    def __init__(self, task_id=None, task_name=None, creator_id=None, git_url=None, git_branch=None, last_check_time=None, code_line_total=None, code_line=None, code_quality=None, issue_count=None, risk_coefficient=None, duplication_ratio=None, complexity_count=None, duplicated_lines=None, comment_lines=None, comment_ratio=None, duplicated_blocks=None, last_exec_time=None, check_type=None, created_at=None, cyclomatic_complexity_per_method=None, cyclomatic_complexity_per_file=None, critical_count=None, major_count=None, minor_count=None, suggestion_count=None, is_access=None, trigger_type=None, file_duplication_ratio=None):
        r"""ShowTaskDetailResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务id
        :type task_id: str
        :param task_name: 任务名字
        :type task_name: str
        :param creator_id: 创建者id
        :type creator_id: str
        :param git_url: 代码仓地址
        :type git_url: str
        :param git_branch: 代码仓分支,如果是MR模式，为源分支
        :type git_branch: str
        :param last_check_time: 上一次检查时间
        :type last_check_time: str
        :param code_line_total: 代码总行数
        :type code_line_total: int
        :param code_line: 代码有效行数
        :type code_line: int
        :param code_quality: 代码质量
        :type code_quality: float
        :param issue_count: 问题数
        :type issue_count: int
        :param risk_coefficient: 危险系数
        :type risk_coefficient: float
        :param duplication_ratio: 重复比例
        :type duplication_ratio: str
        :param complexity_count: 复杂度
        :type complexity_count: int
        :param duplicated_lines: 重复行数
        :type duplicated_lines: int
        :param comment_lines: 注释行数
        :type comment_lines: int
        :param comment_ratio: 注释比例
        :type comment_ratio: str
        :param duplicated_blocks: 重复块
        :type duplicated_blocks: int
        :param last_exec_time: 上次执行时间
        :type last_exec_time: str
        :param check_type: 检查类型
        :type check_type: str
        :param created_at: 创建时间
        :type created_at: str
        :param cyclomatic_complexity_per_method: 代码平均复杂度
        :type cyclomatic_complexity_per_method: str
        :param cyclomatic_complexity_per_file: 代码平均复杂度(文件)
        :type cyclomatic_complexity_per_file: str
        :param critical_count: 致命问题数
        :type critical_count: str
        :param major_count: 严重问题数
        :type major_count: str
        :param minor_count: 一般问题数
        :type minor_count: str
        :param suggestion_count: 提示问题数
        :type suggestion_count: str
        :param is_access: 门禁质量是否通过
        :type is_access: str
        :param trigger_type: 任务触发方式
        :type trigger_type: str
        :param file_duplication_ratio: 文件重复率
        :type file_duplication_ratio: str
        """
        
        super(ShowTaskDetailResponse, self).__init__()

        self._task_id = None
        self._task_name = None
        self._creator_id = None
        self._git_url = None
        self._git_branch = None
        self._last_check_time = None
        self._code_line_total = None
        self._code_line = None
        self._code_quality = None
        self._issue_count = None
        self._risk_coefficient = None
        self._duplication_ratio = None
        self._complexity_count = None
        self._duplicated_lines = None
        self._comment_lines = None
        self._comment_ratio = None
        self._duplicated_blocks = None
        self._last_exec_time = None
        self._check_type = None
        self._created_at = None
        self._cyclomatic_complexity_per_method = None
        self._cyclomatic_complexity_per_file = None
        self._critical_count = None
        self._major_count = None
        self._minor_count = None
        self._suggestion_count = None
        self._is_access = None
        self._trigger_type = None
        self._file_duplication_ratio = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if creator_id is not None:
            self.creator_id = creator_id
        if git_url is not None:
            self.git_url = git_url
        if git_branch is not None:
            self.git_branch = git_branch
        if last_check_time is not None:
            self.last_check_time = last_check_time
        if code_line_total is not None:
            self.code_line_total = code_line_total
        if code_line is not None:
            self.code_line = code_line
        if code_quality is not None:
            self.code_quality = code_quality
        if issue_count is not None:
            self.issue_count = issue_count
        if risk_coefficient is not None:
            self.risk_coefficient = risk_coefficient
        if duplication_ratio is not None:
            self.duplication_ratio = duplication_ratio
        if complexity_count is not None:
            self.complexity_count = complexity_count
        if duplicated_lines is not None:
            self.duplicated_lines = duplicated_lines
        if comment_lines is not None:
            self.comment_lines = comment_lines
        if comment_ratio is not None:
            self.comment_ratio = comment_ratio
        if duplicated_blocks is not None:
            self.duplicated_blocks = duplicated_blocks
        if last_exec_time is not None:
            self.last_exec_time = last_exec_time
        if check_type is not None:
            self.check_type = check_type
        if created_at is not None:
            self.created_at = created_at
        if cyclomatic_complexity_per_method is not None:
            self.cyclomatic_complexity_per_method = cyclomatic_complexity_per_method
        if cyclomatic_complexity_per_file is not None:
            self.cyclomatic_complexity_per_file = cyclomatic_complexity_per_file
        if critical_count is not None:
            self.critical_count = critical_count
        if major_count is not None:
            self.major_count = major_count
        if minor_count is not None:
            self.minor_count = minor_count
        if suggestion_count is not None:
            self.suggestion_count = suggestion_count
        if is_access is not None:
            self.is_access = is_access
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if file_duplication_ratio is not None:
            self.file_duplication_ratio = file_duplication_ratio

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowTaskDetailResponse.

        任务id

        :return: The task_id of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowTaskDetailResponse.

        任务id

        :param task_id: The task_id of this ShowTaskDetailResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ShowTaskDetailResponse.

        任务名字

        :return: The task_name of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ShowTaskDetailResponse.

        任务名字

        :param task_name: The task_name of this ShowTaskDetailResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ShowTaskDetailResponse.

        创建者id

        :return: The creator_id of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ShowTaskDetailResponse.

        创建者id

        :param creator_id: The creator_id of this ShowTaskDetailResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def git_url(self):
        r"""Gets the git_url of this ShowTaskDetailResponse.

        代码仓地址

        :return: The git_url of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this ShowTaskDetailResponse.

        代码仓地址

        :param git_url: The git_url of this ShowTaskDetailResponse.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def git_branch(self):
        r"""Gets the git_branch of this ShowTaskDetailResponse.

        代码仓分支,如果是MR模式，为源分支

        :return: The git_branch of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch):
        r"""Sets the git_branch of this ShowTaskDetailResponse.

        代码仓分支,如果是MR模式，为源分支

        :param git_branch: The git_branch of this ShowTaskDetailResponse.
        :type git_branch: str
        """
        self._git_branch = git_branch

    @property
    def last_check_time(self):
        r"""Gets the last_check_time of this ShowTaskDetailResponse.

        上一次检查时间

        :return: The last_check_time of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._last_check_time

    @last_check_time.setter
    def last_check_time(self, last_check_time):
        r"""Sets the last_check_time of this ShowTaskDetailResponse.

        上一次检查时间

        :param last_check_time: The last_check_time of this ShowTaskDetailResponse.
        :type last_check_time: str
        """
        self._last_check_time = last_check_time

    @property
    def code_line_total(self):
        r"""Gets the code_line_total of this ShowTaskDetailResponse.

        代码总行数

        :return: The code_line_total of this ShowTaskDetailResponse.
        :rtype: int
        """
        return self._code_line_total

    @code_line_total.setter
    def code_line_total(self, code_line_total):
        r"""Sets the code_line_total of this ShowTaskDetailResponse.

        代码总行数

        :param code_line_total: The code_line_total of this ShowTaskDetailResponse.
        :type code_line_total: int
        """
        self._code_line_total = code_line_total

    @property
    def code_line(self):
        r"""Gets the code_line of this ShowTaskDetailResponse.

        代码有效行数

        :return: The code_line of this ShowTaskDetailResponse.
        :rtype: int
        """
        return self._code_line

    @code_line.setter
    def code_line(self, code_line):
        r"""Sets the code_line of this ShowTaskDetailResponse.

        代码有效行数

        :param code_line: The code_line of this ShowTaskDetailResponse.
        :type code_line: int
        """
        self._code_line = code_line

    @property
    def code_quality(self):
        r"""Gets the code_quality of this ShowTaskDetailResponse.

        代码质量

        :return: The code_quality of this ShowTaskDetailResponse.
        :rtype: float
        """
        return self._code_quality

    @code_quality.setter
    def code_quality(self, code_quality):
        r"""Sets the code_quality of this ShowTaskDetailResponse.

        代码质量

        :param code_quality: The code_quality of this ShowTaskDetailResponse.
        :type code_quality: float
        """
        self._code_quality = code_quality

    @property
    def issue_count(self):
        r"""Gets the issue_count of this ShowTaskDetailResponse.

        问题数

        :return: The issue_count of this ShowTaskDetailResponse.
        :rtype: int
        """
        return self._issue_count

    @issue_count.setter
    def issue_count(self, issue_count):
        r"""Sets the issue_count of this ShowTaskDetailResponse.

        问题数

        :param issue_count: The issue_count of this ShowTaskDetailResponse.
        :type issue_count: int
        """
        self._issue_count = issue_count

    @property
    def risk_coefficient(self):
        r"""Gets the risk_coefficient of this ShowTaskDetailResponse.

        危险系数

        :return: The risk_coefficient of this ShowTaskDetailResponse.
        :rtype: float
        """
        return self._risk_coefficient

    @risk_coefficient.setter
    def risk_coefficient(self, risk_coefficient):
        r"""Sets the risk_coefficient of this ShowTaskDetailResponse.

        危险系数

        :param risk_coefficient: The risk_coefficient of this ShowTaskDetailResponse.
        :type risk_coefficient: float
        """
        self._risk_coefficient = risk_coefficient

    @property
    def duplication_ratio(self):
        r"""Gets the duplication_ratio of this ShowTaskDetailResponse.

        重复比例

        :return: The duplication_ratio of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._duplication_ratio

    @duplication_ratio.setter
    def duplication_ratio(self, duplication_ratio):
        r"""Sets the duplication_ratio of this ShowTaskDetailResponse.

        重复比例

        :param duplication_ratio: The duplication_ratio of this ShowTaskDetailResponse.
        :type duplication_ratio: str
        """
        self._duplication_ratio = duplication_ratio

    @property
    def complexity_count(self):
        r"""Gets the complexity_count of this ShowTaskDetailResponse.

        复杂度

        :return: The complexity_count of this ShowTaskDetailResponse.
        :rtype: int
        """
        return self._complexity_count

    @complexity_count.setter
    def complexity_count(self, complexity_count):
        r"""Sets the complexity_count of this ShowTaskDetailResponse.

        复杂度

        :param complexity_count: The complexity_count of this ShowTaskDetailResponse.
        :type complexity_count: int
        """
        self._complexity_count = complexity_count

    @property
    def duplicated_lines(self):
        r"""Gets the duplicated_lines of this ShowTaskDetailResponse.

        重复行数

        :return: The duplicated_lines of this ShowTaskDetailResponse.
        :rtype: int
        """
        return self._duplicated_lines

    @duplicated_lines.setter
    def duplicated_lines(self, duplicated_lines):
        r"""Sets the duplicated_lines of this ShowTaskDetailResponse.

        重复行数

        :param duplicated_lines: The duplicated_lines of this ShowTaskDetailResponse.
        :type duplicated_lines: int
        """
        self._duplicated_lines = duplicated_lines

    @property
    def comment_lines(self):
        r"""Gets the comment_lines of this ShowTaskDetailResponse.

        注释行数

        :return: The comment_lines of this ShowTaskDetailResponse.
        :rtype: int
        """
        return self._comment_lines

    @comment_lines.setter
    def comment_lines(self, comment_lines):
        r"""Sets the comment_lines of this ShowTaskDetailResponse.

        注释行数

        :param comment_lines: The comment_lines of this ShowTaskDetailResponse.
        :type comment_lines: int
        """
        self._comment_lines = comment_lines

    @property
    def comment_ratio(self):
        r"""Gets the comment_ratio of this ShowTaskDetailResponse.

        注释比例

        :return: The comment_ratio of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._comment_ratio

    @comment_ratio.setter
    def comment_ratio(self, comment_ratio):
        r"""Sets the comment_ratio of this ShowTaskDetailResponse.

        注释比例

        :param comment_ratio: The comment_ratio of this ShowTaskDetailResponse.
        :type comment_ratio: str
        """
        self._comment_ratio = comment_ratio

    @property
    def duplicated_blocks(self):
        r"""Gets the duplicated_blocks of this ShowTaskDetailResponse.

        重复块

        :return: The duplicated_blocks of this ShowTaskDetailResponse.
        :rtype: int
        """
        return self._duplicated_blocks

    @duplicated_blocks.setter
    def duplicated_blocks(self, duplicated_blocks):
        r"""Sets the duplicated_blocks of this ShowTaskDetailResponse.

        重复块

        :param duplicated_blocks: The duplicated_blocks of this ShowTaskDetailResponse.
        :type duplicated_blocks: int
        """
        self._duplicated_blocks = duplicated_blocks

    @property
    def last_exec_time(self):
        r"""Gets the last_exec_time of this ShowTaskDetailResponse.

        上次执行时间

        :return: The last_exec_time of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._last_exec_time

    @last_exec_time.setter
    def last_exec_time(self, last_exec_time):
        r"""Sets the last_exec_time of this ShowTaskDetailResponse.

        上次执行时间

        :param last_exec_time: The last_exec_time of this ShowTaskDetailResponse.
        :type last_exec_time: str
        """
        self._last_exec_time = last_exec_time

    @property
    def check_type(self):
        r"""Gets the check_type of this ShowTaskDetailResponse.

        检查类型

        :return: The check_type of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this ShowTaskDetailResponse.

        检查类型

        :param check_type: The check_type of this ShowTaskDetailResponse.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowTaskDetailResponse.

        创建时间

        :return: The created_at of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowTaskDetailResponse.

        创建时间

        :param created_at: The created_at of this ShowTaskDetailResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def cyclomatic_complexity_per_method(self):
        r"""Gets the cyclomatic_complexity_per_method of this ShowTaskDetailResponse.

        代码平均复杂度

        :return: The cyclomatic_complexity_per_method of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._cyclomatic_complexity_per_method

    @cyclomatic_complexity_per_method.setter
    def cyclomatic_complexity_per_method(self, cyclomatic_complexity_per_method):
        r"""Sets the cyclomatic_complexity_per_method of this ShowTaskDetailResponse.

        代码平均复杂度

        :param cyclomatic_complexity_per_method: The cyclomatic_complexity_per_method of this ShowTaskDetailResponse.
        :type cyclomatic_complexity_per_method: str
        """
        self._cyclomatic_complexity_per_method = cyclomatic_complexity_per_method

    @property
    def cyclomatic_complexity_per_file(self):
        r"""Gets the cyclomatic_complexity_per_file of this ShowTaskDetailResponse.

        代码平均复杂度(文件)

        :return: The cyclomatic_complexity_per_file of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._cyclomatic_complexity_per_file

    @cyclomatic_complexity_per_file.setter
    def cyclomatic_complexity_per_file(self, cyclomatic_complexity_per_file):
        r"""Sets the cyclomatic_complexity_per_file of this ShowTaskDetailResponse.

        代码平均复杂度(文件)

        :param cyclomatic_complexity_per_file: The cyclomatic_complexity_per_file of this ShowTaskDetailResponse.
        :type cyclomatic_complexity_per_file: str
        """
        self._cyclomatic_complexity_per_file = cyclomatic_complexity_per_file

    @property
    def critical_count(self):
        r"""Gets the critical_count of this ShowTaskDetailResponse.

        致命问题数

        :return: The critical_count of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._critical_count

    @critical_count.setter
    def critical_count(self, critical_count):
        r"""Sets the critical_count of this ShowTaskDetailResponse.

        致命问题数

        :param critical_count: The critical_count of this ShowTaskDetailResponse.
        :type critical_count: str
        """
        self._critical_count = critical_count

    @property
    def major_count(self):
        r"""Gets the major_count of this ShowTaskDetailResponse.

        严重问题数

        :return: The major_count of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._major_count

    @major_count.setter
    def major_count(self, major_count):
        r"""Sets the major_count of this ShowTaskDetailResponse.

        严重问题数

        :param major_count: The major_count of this ShowTaskDetailResponse.
        :type major_count: str
        """
        self._major_count = major_count

    @property
    def minor_count(self):
        r"""Gets the minor_count of this ShowTaskDetailResponse.

        一般问题数

        :return: The minor_count of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._minor_count

    @minor_count.setter
    def minor_count(self, minor_count):
        r"""Sets the minor_count of this ShowTaskDetailResponse.

        一般问题数

        :param minor_count: The minor_count of this ShowTaskDetailResponse.
        :type minor_count: str
        """
        self._minor_count = minor_count

    @property
    def suggestion_count(self):
        r"""Gets the suggestion_count of this ShowTaskDetailResponse.

        提示问题数

        :return: The suggestion_count of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._suggestion_count

    @suggestion_count.setter
    def suggestion_count(self, suggestion_count):
        r"""Sets the suggestion_count of this ShowTaskDetailResponse.

        提示问题数

        :param suggestion_count: The suggestion_count of this ShowTaskDetailResponse.
        :type suggestion_count: str
        """
        self._suggestion_count = suggestion_count

    @property
    def is_access(self):
        r"""Gets the is_access of this ShowTaskDetailResponse.

        门禁质量是否通过

        :return: The is_access of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._is_access

    @is_access.setter
    def is_access(self, is_access):
        r"""Sets the is_access of this ShowTaskDetailResponse.

        门禁质量是否通过

        :param is_access: The is_access of this ShowTaskDetailResponse.
        :type is_access: str
        """
        self._is_access = is_access

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this ShowTaskDetailResponse.

        任务触发方式

        :return: The trigger_type of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this ShowTaskDetailResponse.

        任务触发方式

        :param trigger_type: The trigger_type of this ShowTaskDetailResponse.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def file_duplication_ratio(self):
        r"""Gets the file_duplication_ratio of this ShowTaskDetailResponse.

        文件重复率

        :return: The file_duplication_ratio of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._file_duplication_ratio

    @file_duplication_ratio.setter
    def file_duplication_ratio(self, file_duplication_ratio):
        r"""Sets the file_duplication_ratio of this ShowTaskDetailResponse.

        文件重复率

        :param file_duplication_ratio: The file_duplication_ratio of this ShowTaskDetailResponse.
        :type file_duplication_ratio: str
        """
        self._file_duplication_ratio = file_duplication_ratio

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
        if not isinstance(other, ShowTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
