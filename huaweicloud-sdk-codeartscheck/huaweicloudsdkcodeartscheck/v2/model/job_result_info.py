# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobResultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'critical': 'int',
        'delaystatus_count': 'int',
        'fatal': 'int',
        'general': 'int',
        'info': 'int',
        'prompt': 'int',
        'code_line': 'int',
        'defect_count': 'int',
        'dismissed': 'int',
        'file_total': 'int',
        'fixed': 'int',
        'id': 'str',
        'job_id': 'str',
        'new_unsolved_defect_count': 'int',
        'non_security_defect_count': 'int',
        'review_result': 'str',
        'security_defect_count': 'int',
        'solved_defect_count': 'int',
        'unsolved_defect_count': 'int'
    }

    attribute_map = {
        'critical': 'CRITICAL',
        'delaystatus_count': 'DELAYSTATUS_COUNT',
        'fatal': 'FATAL',
        'general': 'GENERAL',
        'info': 'INFO',
        'prompt': 'PROMPT',
        'code_line': 'codeLine',
        'defect_count': 'defectCount',
        'dismissed': 'dismissed',
        'file_total': 'fileTotal',
        'fixed': 'fixed',
        'id': 'id',
        'job_id': 'jobId',
        'new_unsolved_defect_count': 'newUnsolvedDefectCount',
        'non_security_defect_count': 'nonSecurityDefectCount',
        'review_result': 'reviewResult',
        'security_defect_count': 'securityDefectCount',
        'solved_defect_count': 'solvedDefectCount',
        'unsolved_defect_count': 'unsolvedDefectCount'
    }

    def __init__(self, critical=None, delaystatus_count=None, fatal=None, general=None, info=None, prompt=None, code_line=None, defect_count=None, dismissed=None, file_total=None, fixed=None, id=None, job_id=None, new_unsolved_defect_count=None, non_security_defect_count=None, review_result=None, security_defect_count=None, solved_defect_count=None, unsolved_defect_count=None):
        r"""JobResultInfo

        The model defined in huaweicloud sdk

        :param critical: **参数解释：** 严重问题数。 **取值范围：** ≥0
        :type critical: int
        :param delaystatus_count: **参数解释：** 延迟上线问题数。 **取值范围：** ≥0
        :type delaystatus_count: int
        :param fatal: **参数解释：** 致命问题数。 **取值范围：** ≥0
        :type fatal: int
        :param general: **参数解释：** 一般问题数。 **取值范围：** ≥0
        :type general: int
        :param info: **参数解释：** 信息问题数。 **取值范围：** ≥0
        :type info: int
        :param prompt: **参数解释：** 提示问题数。 **取值范围：** ≥0
        :type prompt: int
        :param code_line: **参数解释：** 扫描代码行数，不包括空行和注释行。 **取值范围：** ≥0
        :type code_line: int
        :param defect_count: **参数解释：** 缺陷总数。 **取值范围：** ≥0
        :type defect_count: int
        :param dismissed: **参数解释：** 已忽略问题数。 **取值范围：** ≥0
        :type dismissed: int
        :param file_total: **参数解释：** 文件总数。 **取值范围：** ≥0
        :type file_total: int
        :param fixed: **参数解释：** 已修复问题数。 **取值范围：** ≥0
        :type fixed: int
        :param id: **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 不涉及。
        :type id: str
        :param job_id: **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 不涉及。
        :type job_id: str
        :param new_unsolved_defect_count: **参数解释：** 未解决且新增的问题数。 **取值范围：** ≥0
        :type new_unsolved_defect_count: int
        :param non_security_defect_count: **参数解释：** 非安全问题数。 **取值范围：** ≥0
        :type non_security_defect_count: int
        :param review_result: **参数解释：** 门禁结果。 **取值范围：** - success：门禁通过。 - error：门禁未通过。
        :type review_result: str
        :param security_defect_count: **参数解释：** 安全问题数。 **取值范围：** ≥0
        :type security_defect_count: int
        :param solved_defect_count: **参数解释：** 已解决的问题数。 **取值范围：** 不涉及。
        :type solved_defect_count: int
        :param unsolved_defect_count: **参数解释：** 未解决的问题数。 **取值范围：** 不涉及。
        :type unsolved_defect_count: int
        """
        
        

        self._critical = None
        self._delaystatus_count = None
        self._fatal = None
        self._general = None
        self._info = None
        self._prompt = None
        self._code_line = None
        self._defect_count = None
        self._dismissed = None
        self._file_total = None
        self._fixed = None
        self._id = None
        self._job_id = None
        self._new_unsolved_defect_count = None
        self._non_security_defect_count = None
        self._review_result = None
        self._security_defect_count = None
        self._solved_defect_count = None
        self._unsolved_defect_count = None
        self.discriminator = None

        if critical is not None:
            self.critical = critical
        if delaystatus_count is not None:
            self.delaystatus_count = delaystatus_count
        if fatal is not None:
            self.fatal = fatal
        if general is not None:
            self.general = general
        if info is not None:
            self.info = info
        if prompt is not None:
            self.prompt = prompt
        if code_line is not None:
            self.code_line = code_line
        if defect_count is not None:
            self.defect_count = defect_count
        if dismissed is not None:
            self.dismissed = dismissed
        if file_total is not None:
            self.file_total = file_total
        if fixed is not None:
            self.fixed = fixed
        if id is not None:
            self.id = id
        if job_id is not None:
            self.job_id = job_id
        if new_unsolved_defect_count is not None:
            self.new_unsolved_defect_count = new_unsolved_defect_count
        if non_security_defect_count is not None:
            self.non_security_defect_count = non_security_defect_count
        if review_result is not None:
            self.review_result = review_result
        if security_defect_count is not None:
            self.security_defect_count = security_defect_count
        if solved_defect_count is not None:
            self.solved_defect_count = solved_defect_count
        if unsolved_defect_count is not None:
            self.unsolved_defect_count = unsolved_defect_count

    @property
    def critical(self):
        r"""Gets the critical of this JobResultInfo.

        **参数解释：** 严重问题数。 **取值范围：** ≥0

        :return: The critical of this JobResultInfo.
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        r"""Sets the critical of this JobResultInfo.

        **参数解释：** 严重问题数。 **取值范围：** ≥0

        :param critical: The critical of this JobResultInfo.
        :type critical: int
        """
        self._critical = critical

    @property
    def delaystatus_count(self):
        r"""Gets the delaystatus_count of this JobResultInfo.

        **参数解释：** 延迟上线问题数。 **取值范围：** ≥0

        :return: The delaystatus_count of this JobResultInfo.
        :rtype: int
        """
        return self._delaystatus_count

    @delaystatus_count.setter
    def delaystatus_count(self, delaystatus_count):
        r"""Sets the delaystatus_count of this JobResultInfo.

        **参数解释：** 延迟上线问题数。 **取值范围：** ≥0

        :param delaystatus_count: The delaystatus_count of this JobResultInfo.
        :type delaystatus_count: int
        """
        self._delaystatus_count = delaystatus_count

    @property
    def fatal(self):
        r"""Gets the fatal of this JobResultInfo.

        **参数解释：** 致命问题数。 **取值范围：** ≥0

        :return: The fatal of this JobResultInfo.
        :rtype: int
        """
        return self._fatal

    @fatal.setter
    def fatal(self, fatal):
        r"""Sets the fatal of this JobResultInfo.

        **参数解释：** 致命问题数。 **取值范围：** ≥0

        :param fatal: The fatal of this JobResultInfo.
        :type fatal: int
        """
        self._fatal = fatal

    @property
    def general(self):
        r"""Gets the general of this JobResultInfo.

        **参数解释：** 一般问题数。 **取值范围：** ≥0

        :return: The general of this JobResultInfo.
        :rtype: int
        """
        return self._general

    @general.setter
    def general(self, general):
        r"""Sets the general of this JobResultInfo.

        **参数解释：** 一般问题数。 **取值范围：** ≥0

        :param general: The general of this JobResultInfo.
        :type general: int
        """
        self._general = general

    @property
    def info(self):
        r"""Gets the info of this JobResultInfo.

        **参数解释：** 信息问题数。 **取值范围：** ≥0

        :return: The info of this JobResultInfo.
        :rtype: int
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this JobResultInfo.

        **参数解释：** 信息问题数。 **取值范围：** ≥0

        :param info: The info of this JobResultInfo.
        :type info: int
        """
        self._info = info

    @property
    def prompt(self):
        r"""Gets the prompt of this JobResultInfo.

        **参数解释：** 提示问题数。 **取值范围：** ≥0

        :return: The prompt of this JobResultInfo.
        :rtype: int
        """
        return self._prompt

    @prompt.setter
    def prompt(self, prompt):
        r"""Sets the prompt of this JobResultInfo.

        **参数解释：** 提示问题数。 **取值范围：** ≥0

        :param prompt: The prompt of this JobResultInfo.
        :type prompt: int
        """
        self._prompt = prompt

    @property
    def code_line(self):
        r"""Gets the code_line of this JobResultInfo.

        **参数解释：** 扫描代码行数，不包括空行和注释行。 **取值范围：** ≥0

        :return: The code_line of this JobResultInfo.
        :rtype: int
        """
        return self._code_line

    @code_line.setter
    def code_line(self, code_line):
        r"""Sets the code_line of this JobResultInfo.

        **参数解释：** 扫描代码行数，不包括空行和注释行。 **取值范围：** ≥0

        :param code_line: The code_line of this JobResultInfo.
        :type code_line: int
        """
        self._code_line = code_line

    @property
    def defect_count(self):
        r"""Gets the defect_count of this JobResultInfo.

        **参数解释：** 缺陷总数。 **取值范围：** ≥0

        :return: The defect_count of this JobResultInfo.
        :rtype: int
        """
        return self._defect_count

    @defect_count.setter
    def defect_count(self, defect_count):
        r"""Sets the defect_count of this JobResultInfo.

        **参数解释：** 缺陷总数。 **取值范围：** ≥0

        :param defect_count: The defect_count of this JobResultInfo.
        :type defect_count: int
        """
        self._defect_count = defect_count

    @property
    def dismissed(self):
        r"""Gets the dismissed of this JobResultInfo.

        **参数解释：** 已忽略问题数。 **取值范围：** ≥0

        :return: The dismissed of this JobResultInfo.
        :rtype: int
        """
        return self._dismissed

    @dismissed.setter
    def dismissed(self, dismissed):
        r"""Sets the dismissed of this JobResultInfo.

        **参数解释：** 已忽略问题数。 **取值范围：** ≥0

        :param dismissed: The dismissed of this JobResultInfo.
        :type dismissed: int
        """
        self._dismissed = dismissed

    @property
    def file_total(self):
        r"""Gets the file_total of this JobResultInfo.

        **参数解释：** 文件总数。 **取值范围：** ≥0

        :return: The file_total of this JobResultInfo.
        :rtype: int
        """
        return self._file_total

    @file_total.setter
    def file_total(self, file_total):
        r"""Sets the file_total of this JobResultInfo.

        **参数解释：** 文件总数。 **取值范围：** ≥0

        :param file_total: The file_total of this JobResultInfo.
        :type file_total: int
        """
        self._file_total = file_total

    @property
    def fixed(self):
        r"""Gets the fixed of this JobResultInfo.

        **参数解释：** 已修复问题数。 **取值范围：** ≥0

        :return: The fixed of this JobResultInfo.
        :rtype: int
        """
        return self._fixed

    @fixed.setter
    def fixed(self, fixed):
        r"""Sets the fixed of this JobResultInfo.

        **参数解释：** 已修复问题数。 **取值范围：** ≥0

        :param fixed: The fixed of this JobResultInfo.
        :type fixed: int
        """
        self._fixed = fixed

    @property
    def id(self):
        r"""Gets the id of this JobResultInfo.

        **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 不涉及。

        :return: The id of this JobResultInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobResultInfo.

        **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 不涉及。

        :param id: The id of this JobResultInfo.
        :type id: str
        """
        self._id = id

    @property
    def job_id(self):
        r"""Gets the job_id of this JobResultInfo.

        **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 不涉及。

        :return: The job_id of this JobResultInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this JobResultInfo.

        **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 不涉及。

        :param job_id: The job_id of this JobResultInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def new_unsolved_defect_count(self):
        r"""Gets the new_unsolved_defect_count of this JobResultInfo.

        **参数解释：** 未解决且新增的问题数。 **取值范围：** ≥0

        :return: The new_unsolved_defect_count of this JobResultInfo.
        :rtype: int
        """
        return self._new_unsolved_defect_count

    @new_unsolved_defect_count.setter
    def new_unsolved_defect_count(self, new_unsolved_defect_count):
        r"""Sets the new_unsolved_defect_count of this JobResultInfo.

        **参数解释：** 未解决且新增的问题数。 **取值范围：** ≥0

        :param new_unsolved_defect_count: The new_unsolved_defect_count of this JobResultInfo.
        :type new_unsolved_defect_count: int
        """
        self._new_unsolved_defect_count = new_unsolved_defect_count

    @property
    def non_security_defect_count(self):
        r"""Gets the non_security_defect_count of this JobResultInfo.

        **参数解释：** 非安全问题数。 **取值范围：** ≥0

        :return: The non_security_defect_count of this JobResultInfo.
        :rtype: int
        """
        return self._non_security_defect_count

    @non_security_defect_count.setter
    def non_security_defect_count(self, non_security_defect_count):
        r"""Sets the non_security_defect_count of this JobResultInfo.

        **参数解释：** 非安全问题数。 **取值范围：** ≥0

        :param non_security_defect_count: The non_security_defect_count of this JobResultInfo.
        :type non_security_defect_count: int
        """
        self._non_security_defect_count = non_security_defect_count

    @property
    def review_result(self):
        r"""Gets the review_result of this JobResultInfo.

        **参数解释：** 门禁结果。 **取值范围：** - success：门禁通过。 - error：门禁未通过。

        :return: The review_result of this JobResultInfo.
        :rtype: str
        """
        return self._review_result

    @review_result.setter
    def review_result(self, review_result):
        r"""Sets the review_result of this JobResultInfo.

        **参数解释：** 门禁结果。 **取值范围：** - success：门禁通过。 - error：门禁未通过。

        :param review_result: The review_result of this JobResultInfo.
        :type review_result: str
        """
        self._review_result = review_result

    @property
    def security_defect_count(self):
        r"""Gets the security_defect_count of this JobResultInfo.

        **参数解释：** 安全问题数。 **取值范围：** ≥0

        :return: The security_defect_count of this JobResultInfo.
        :rtype: int
        """
        return self._security_defect_count

    @security_defect_count.setter
    def security_defect_count(self, security_defect_count):
        r"""Sets the security_defect_count of this JobResultInfo.

        **参数解释：** 安全问题数。 **取值范围：** ≥0

        :param security_defect_count: The security_defect_count of this JobResultInfo.
        :type security_defect_count: int
        """
        self._security_defect_count = security_defect_count

    @property
    def solved_defect_count(self):
        r"""Gets the solved_defect_count of this JobResultInfo.

        **参数解释：** 已解决的问题数。 **取值范围：** 不涉及。

        :return: The solved_defect_count of this JobResultInfo.
        :rtype: int
        """
        return self._solved_defect_count

    @solved_defect_count.setter
    def solved_defect_count(self, solved_defect_count):
        r"""Sets the solved_defect_count of this JobResultInfo.

        **参数解释：** 已解决的问题数。 **取值范围：** 不涉及。

        :param solved_defect_count: The solved_defect_count of this JobResultInfo.
        :type solved_defect_count: int
        """
        self._solved_defect_count = solved_defect_count

    @property
    def unsolved_defect_count(self):
        r"""Gets the unsolved_defect_count of this JobResultInfo.

        **参数解释：** 未解决的问题数。 **取值范围：** 不涉及。

        :return: The unsolved_defect_count of this JobResultInfo.
        :rtype: int
        """
        return self._unsolved_defect_count

    @unsolved_defect_count.setter
    def unsolved_defect_count(self, unsolved_defect_count):
        r"""Sets the unsolved_defect_count of this JobResultInfo.

        **参数解释：** 未解决的问题数。 **取值范围：** 不涉及。

        :param unsolved_defect_count: The unsolved_defect_count of this JobResultInfo.
        :type unsolved_defect_count: int
        """
        self._unsolved_defect_count = unsolved_defect_count

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
