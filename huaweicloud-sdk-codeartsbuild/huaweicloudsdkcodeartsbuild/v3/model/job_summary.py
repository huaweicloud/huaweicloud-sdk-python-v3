# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'avg_success_ratio': 'int',
        'build_no': 'int',
        'job_total': 'int',
        'version_total': 'str'
    }

    attribute_map = {
        'avg_success_ratio': 'avg_success_ratio',
        'build_no': 'build_no',
        'job_total': 'job_total',
        'version_total': 'version_total'
    }

    def __init__(self, avg_success_ratio=None, build_no=None, job_total=None, version_total=None):
        r"""JobSummary

        The model defined in huaweicloud sdk

        :param avg_success_ratio: 构建成功率
        :type avg_success_ratio: int
        :param build_no: 构建总时长
        :type build_no: int
        :param job_total: 任务总数
        :type job_total: int
        :param version_total: 版本
        :type version_total: str
        """
        
        

        self._avg_success_ratio = None
        self._build_no = None
        self._job_total = None
        self._version_total = None
        self.discriminator = None

        if avg_success_ratio is not None:
            self.avg_success_ratio = avg_success_ratio
        if build_no is not None:
            self.build_no = build_no
        if job_total is not None:
            self.job_total = job_total
        if version_total is not None:
            self.version_total = version_total

    @property
    def avg_success_ratio(self):
        r"""Gets the avg_success_ratio of this JobSummary.

        构建成功率

        :return: The avg_success_ratio of this JobSummary.
        :rtype: int
        """
        return self._avg_success_ratio

    @avg_success_ratio.setter
    def avg_success_ratio(self, avg_success_ratio):
        r"""Sets the avg_success_ratio of this JobSummary.

        构建成功率

        :param avg_success_ratio: The avg_success_ratio of this JobSummary.
        :type avg_success_ratio: int
        """
        self._avg_success_ratio = avg_success_ratio

    @property
    def build_no(self):
        r"""Gets the build_no of this JobSummary.

        构建总时长

        :return: The build_no of this JobSummary.
        :rtype: int
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        r"""Sets the build_no of this JobSummary.

        构建总时长

        :param build_no: The build_no of this JobSummary.
        :type build_no: int
        """
        self._build_no = build_no

    @property
    def job_total(self):
        r"""Gets the job_total of this JobSummary.

        任务总数

        :return: The job_total of this JobSummary.
        :rtype: int
        """
        return self._job_total

    @job_total.setter
    def job_total(self, job_total):
        r"""Sets the job_total of this JobSummary.

        任务总数

        :param job_total: The job_total of this JobSummary.
        :type job_total: int
        """
        self._job_total = job_total

    @property
    def version_total(self):
        r"""Gets the version_total of this JobSummary.

        版本

        :return: The version_total of this JobSummary.
        :rtype: str
        """
        return self._version_total

    @version_total.setter
    def version_total(self, version_total):
        r"""Sets the version_total of this JobSummary.

        版本

        :param version_total: The version_total of this JobSummary.
        :type version_total: str
        """
        self._version_total = version_total

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
        if not isinstance(other, JobSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
