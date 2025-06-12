# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'job_list': 'list[ListJobResultJobList]'
    }

    attribute_map = {
        'total': 'total',
        'job_list': 'job_list'
    }

    def __init__(self, total=None, job_list=None):
        r"""ListJobResult

        The model defined in huaweicloud sdk

        :param total: 任务总数
        :type total: int
        :param job_list: 任务列表
        :type job_list: list[:class:`huaweicloudsdkcodeartsbuild.v3.ListJobResultJobList`]
        """
        
        

        self._total = None
        self._job_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if job_list is not None:
            self.job_list = job_list

    @property
    def total(self):
        r"""Gets the total of this ListJobResult.

        任务总数

        :return: The total of this ListJobResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListJobResult.

        任务总数

        :param total: The total of this ListJobResult.
        :type total: int
        """
        self._total = total

    @property
    def job_list(self):
        r"""Gets the job_list of this ListJobResult.

        任务列表

        :return: The job_list of this ListJobResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.ListJobResultJobList`]
        """
        return self._job_list

    @job_list.setter
    def job_list(self, job_list):
        r"""Sets the job_list of this ListJobResult.

        任务列表

        :param job_list: The job_list of this ListJobResult.
        :type job_list: list[:class:`huaweicloudsdkcodeartsbuild.v3.ListJobResultJobList`]
        """
        self._job_list = job_list

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
        if not isinstance(other, ListJobResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
