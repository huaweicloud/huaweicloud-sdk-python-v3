# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobBuildSuccessRatioResult:

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
        'branch': 'str',
        'total_success_count': 'int',
        'total_count': 'int',
        'total_success_ratio_fraction': 'str',
        'every_day_report': 'list[ShowJobBuildSuccessRatioResultEveryDayReport]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'branch': 'branch',
        'total_success_count': 'total_success_count',
        'total_count': 'total_count',
        'total_success_ratio_fraction': 'total_success_ratio_fraction',
        'every_day_report': 'every_day_report'
    }

    def __init__(self, job_id=None, branch=None, total_success_count=None, total_count=None, total_success_ratio_fraction=None, every_day_report=None):
        r"""ShowJobBuildSuccessRatioResult

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param branch: 分支
        :type branch: str
        :param total_success_count: 构建成功总数
        :type total_success_count: int
        :param total_count: 构建总数
        :type total_count: int
        :param total_success_ratio_fraction: 总成功比率分数
        :type total_success_ratio_fraction: str
        :param every_day_report: 每日构建成功率
        :type every_day_report: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildSuccessRatioResultEveryDayReport`]
        """
        
        

        self._job_id = None
        self._branch = None
        self._total_success_count = None
        self._total_count = None
        self._total_success_ratio_fraction = None
        self._every_day_report = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if branch is not None:
            self.branch = branch
        if total_success_count is not None:
            self.total_success_count = total_success_count
        if total_count is not None:
            self.total_count = total_count
        if total_success_ratio_fraction is not None:
            self.total_success_ratio_fraction = total_success_ratio_fraction
        if every_day_report is not None:
            self.every_day_report = every_day_report

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowJobBuildSuccessRatioResult.

        任务ID

        :return: The job_id of this ShowJobBuildSuccessRatioResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowJobBuildSuccessRatioResult.

        任务ID

        :param job_id: The job_id of this ShowJobBuildSuccessRatioResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def branch(self):
        r"""Gets the branch of this ShowJobBuildSuccessRatioResult.

        分支

        :return: The branch of this ShowJobBuildSuccessRatioResult.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this ShowJobBuildSuccessRatioResult.

        分支

        :param branch: The branch of this ShowJobBuildSuccessRatioResult.
        :type branch: str
        """
        self._branch = branch

    @property
    def total_success_count(self):
        r"""Gets the total_success_count of this ShowJobBuildSuccessRatioResult.

        构建成功总数

        :return: The total_success_count of this ShowJobBuildSuccessRatioResult.
        :rtype: int
        """
        return self._total_success_count

    @total_success_count.setter
    def total_success_count(self, total_success_count):
        r"""Sets the total_success_count of this ShowJobBuildSuccessRatioResult.

        构建成功总数

        :param total_success_count: The total_success_count of this ShowJobBuildSuccessRatioResult.
        :type total_success_count: int
        """
        self._total_success_count = total_success_count

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowJobBuildSuccessRatioResult.

        构建总数

        :return: The total_count of this ShowJobBuildSuccessRatioResult.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowJobBuildSuccessRatioResult.

        构建总数

        :param total_count: The total_count of this ShowJobBuildSuccessRatioResult.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def total_success_ratio_fraction(self):
        r"""Gets the total_success_ratio_fraction of this ShowJobBuildSuccessRatioResult.

        总成功比率分数

        :return: The total_success_ratio_fraction of this ShowJobBuildSuccessRatioResult.
        :rtype: str
        """
        return self._total_success_ratio_fraction

    @total_success_ratio_fraction.setter
    def total_success_ratio_fraction(self, total_success_ratio_fraction):
        r"""Sets the total_success_ratio_fraction of this ShowJobBuildSuccessRatioResult.

        总成功比率分数

        :param total_success_ratio_fraction: The total_success_ratio_fraction of this ShowJobBuildSuccessRatioResult.
        :type total_success_ratio_fraction: str
        """
        self._total_success_ratio_fraction = total_success_ratio_fraction

    @property
    def every_day_report(self):
        r"""Gets the every_day_report of this ShowJobBuildSuccessRatioResult.

        每日构建成功率

        :return: The every_day_report of this ShowJobBuildSuccessRatioResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildSuccessRatioResultEveryDayReport`]
        """
        return self._every_day_report

    @every_day_report.setter
    def every_day_report(self, every_day_report):
        r"""Sets the every_day_report of this ShowJobBuildSuccessRatioResult.

        每日构建成功率

        :param every_day_report: The every_day_report of this ShowJobBuildSuccessRatioResult.
        :type every_day_report: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildSuccessRatioResultEveryDayReport`]
        """
        self._every_day_report = every_day_report

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
        if not isinstance(other, ShowJobBuildSuccessRatioResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
