# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobBuildSuccessRatioRequest:

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
        'repository_name': 'str',
        'branch': 'str',
        'interval': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'repository_name': 'repository_name',
        'branch': 'branch',
        'interval': 'interval'
    }

    def __init__(self, job_id=None, repository_name=None, branch=None, interval=None):
        r"""ShowJobBuildSuccessRatioRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param repository_name: 代码仓名称。
        :type repository_name: str
        :param branch: 代码仓分支名。
        :type branch: str
        :param interval: 查询时间，查最近几天的。
        :type interval: int
        """
        
        

        self._job_id = None
        self._repository_name = None
        self._branch = None
        self._interval = None
        self.discriminator = None

        self.job_id = job_id
        self.repository_name = repository_name
        if branch is not None:
            self.branch = branch
        self.interval = interval

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowJobBuildSuccessRatioRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this ShowJobBuildSuccessRatioRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowJobBuildSuccessRatioRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this ShowJobBuildSuccessRatioRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def repository_name(self):
        r"""Gets the repository_name of this ShowJobBuildSuccessRatioRequest.

        代码仓名称。

        :return: The repository_name of this ShowJobBuildSuccessRatioRequest.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this ShowJobBuildSuccessRatioRequest.

        代码仓名称。

        :param repository_name: The repository_name of this ShowJobBuildSuccessRatioRequest.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def branch(self):
        r"""Gets the branch of this ShowJobBuildSuccessRatioRequest.

        代码仓分支名。

        :return: The branch of this ShowJobBuildSuccessRatioRequest.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this ShowJobBuildSuccessRatioRequest.

        代码仓分支名。

        :param branch: The branch of this ShowJobBuildSuccessRatioRequest.
        :type branch: str
        """
        self._branch = branch

    @property
    def interval(self):
        r"""Gets the interval of this ShowJobBuildSuccessRatioRequest.

        查询时间，查最近几天的。

        :return: The interval of this ShowJobBuildSuccessRatioRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ShowJobBuildSuccessRatioRequest.

        查询时间，查最近几天的。

        :param interval: The interval of this ShowJobBuildSuccessRatioRequest.
        :type interval: int
        """
        self._interval = interval

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
        if not isinstance(other, ShowJobBuildSuccessRatioRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
