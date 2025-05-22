# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'build_no': 'int',
        'stage_name': 'str',
        'root_id': 'str',
        'total': 'int',
        'success': 'int',
        'failures': 'int',
        'errors': 'int',
        'others': 'int',
        'execution_time': 'int',
        'genrate_time': 'str',
        'region': 'str',
        'is_success': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'build_no': 'build_no',
        'stage_name': 'stage_name',
        'root_id': 'root_id',
        'total': 'total',
        'success': 'success',
        'failures': 'failures',
        'errors': 'errors',
        'others': 'others',
        'execution_time': 'execution_time',
        'genrate_time': 'genrate_time',
        'region': 'region',
        'is_success': 'is_success'
    }

    def __init__(self, job_id=None, build_no=None, stage_name=None, root_id=None, total=None, success=None, failures=None, errors=None, others=None, execution_time=None, genrate_time=None, region=None, is_success=None):
        r"""ShowReportSummary

        The model defined in huaweicloud sdk

        :param job_id: 任务编号
        :type job_id: str
        :param build_no: 构建编号
        :type build_no: int
        :param stage_name: 步骤名称，对应构建步骤，例如stage2
        :type stage_name: str
        :param root_id: 报告编号
        :type root_id: str
        :param total: 总数
        :type total: int
        :param success: 成功数量
        :type success: int
        :param failures: 失败数量
        :type failures: int
        :param errors: 错误数量
        :type errors: int
        :param others: 其他
        :type others: int
        :param execution_time: 执行耗时
        :type execution_time: int
        :param genrate_time: 生成时间
        :type genrate_time: str
        :param region: 局点
        :type region: str
        :param is_success: 是否通过
        :type is_success: bool
        """
        
        

        self._job_id = None
        self._build_no = None
        self._stage_name = None
        self._root_id = None
        self._total = None
        self._success = None
        self._failures = None
        self._errors = None
        self._others = None
        self._execution_time = None
        self._genrate_time = None
        self._region = None
        self._is_success = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if build_no is not None:
            self.build_no = build_no
        if stage_name is not None:
            self.stage_name = stage_name
        if root_id is not None:
            self.root_id = root_id
        if total is not None:
            self.total = total
        if success is not None:
            self.success = success
        if failures is not None:
            self.failures = failures
        if errors is not None:
            self.errors = errors
        if others is not None:
            self.others = others
        if execution_time is not None:
            self.execution_time = execution_time
        if genrate_time is not None:
            self.genrate_time = genrate_time
        if region is not None:
            self.region = region
        if is_success is not None:
            self.is_success = is_success

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowReportSummary.

        任务编号

        :return: The job_id of this ShowReportSummary.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowReportSummary.

        任务编号

        :param job_id: The job_id of this ShowReportSummary.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def build_no(self):
        r"""Gets the build_no of this ShowReportSummary.

        构建编号

        :return: The build_no of this ShowReportSummary.
        :rtype: int
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        r"""Sets the build_no of this ShowReportSummary.

        构建编号

        :param build_no: The build_no of this ShowReportSummary.
        :type build_no: int
        """
        self._build_no = build_no

    @property
    def stage_name(self):
        r"""Gets the stage_name of this ShowReportSummary.

        步骤名称，对应构建步骤，例如stage2

        :return: The stage_name of this ShowReportSummary.
        :rtype: str
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name):
        r"""Sets the stage_name of this ShowReportSummary.

        步骤名称，对应构建步骤，例如stage2

        :param stage_name: The stage_name of this ShowReportSummary.
        :type stage_name: str
        """
        self._stage_name = stage_name

    @property
    def root_id(self):
        r"""Gets the root_id of this ShowReportSummary.

        报告编号

        :return: The root_id of this ShowReportSummary.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this ShowReportSummary.

        报告编号

        :param root_id: The root_id of this ShowReportSummary.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def total(self):
        r"""Gets the total of this ShowReportSummary.

        总数

        :return: The total of this ShowReportSummary.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowReportSummary.

        总数

        :param total: The total of this ShowReportSummary.
        :type total: int
        """
        self._total = total

    @property
    def success(self):
        r"""Gets the success of this ShowReportSummary.

        成功数量

        :return: The success of this ShowReportSummary.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ShowReportSummary.

        成功数量

        :param success: The success of this ShowReportSummary.
        :type success: int
        """
        self._success = success

    @property
    def failures(self):
        r"""Gets the failures of this ShowReportSummary.

        失败数量

        :return: The failures of this ShowReportSummary.
        :rtype: int
        """
        return self._failures

    @failures.setter
    def failures(self, failures):
        r"""Sets the failures of this ShowReportSummary.

        失败数量

        :param failures: The failures of this ShowReportSummary.
        :type failures: int
        """
        self._failures = failures

    @property
    def errors(self):
        r"""Gets the errors of this ShowReportSummary.

        错误数量

        :return: The errors of this ShowReportSummary.
        :rtype: int
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        r"""Sets the errors of this ShowReportSummary.

        错误数量

        :param errors: The errors of this ShowReportSummary.
        :type errors: int
        """
        self._errors = errors

    @property
    def others(self):
        r"""Gets the others of this ShowReportSummary.

        其他

        :return: The others of this ShowReportSummary.
        :rtype: int
        """
        return self._others

    @others.setter
    def others(self, others):
        r"""Sets the others of this ShowReportSummary.

        其他

        :param others: The others of this ShowReportSummary.
        :type others: int
        """
        self._others = others

    @property
    def execution_time(self):
        r"""Gets the execution_time of this ShowReportSummary.

        执行耗时

        :return: The execution_time of this ShowReportSummary.
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        r"""Sets the execution_time of this ShowReportSummary.

        执行耗时

        :param execution_time: The execution_time of this ShowReportSummary.
        :type execution_time: int
        """
        self._execution_time = execution_time

    @property
    def genrate_time(self):
        r"""Gets the genrate_time of this ShowReportSummary.

        生成时间

        :return: The genrate_time of this ShowReportSummary.
        :rtype: str
        """
        return self._genrate_time

    @genrate_time.setter
    def genrate_time(self, genrate_time):
        r"""Sets the genrate_time of this ShowReportSummary.

        生成时间

        :param genrate_time: The genrate_time of this ShowReportSummary.
        :type genrate_time: str
        """
        self._genrate_time = genrate_time

    @property
    def region(self):
        r"""Gets the region of this ShowReportSummary.

        局点

        :return: The region of this ShowReportSummary.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowReportSummary.

        局点

        :param region: The region of this ShowReportSummary.
        :type region: str
        """
        self._region = region

    @property
    def is_success(self):
        r"""Gets the is_success of this ShowReportSummary.

        是否通过

        :return: The is_success of this ShowReportSummary.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ShowReportSummary.

        是否通过

        :param is_success: The is_success of this ShowReportSummary.
        :type is_success: bool
        """
        self._is_success = is_success

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
        if not isinstance(other, ShowReportSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
