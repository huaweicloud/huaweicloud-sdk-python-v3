# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobsResponse(SdkResponse):

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
        'jobs': 'list[Job]',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'total': 'total',
        'jobs': 'jobs',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, total=None, jobs=None, page_no=None, page_size=None):
        r"""ShowJobsResponse

        The model defined in huaweicloud sdk

        :param total: 作业数,查询单个作业时为0
        :type total: int
        :param jobs: 作业列表，请参见jobs参数说明
        :type jobs: list[:class:`huaweicloudsdkcdm.v1.Job`]
        :param page_no: 返回指定页号的作业
        :type page_no: int
        :param page_size: 每页作业数
        :type page_size: int
        """
        
        super(ShowJobsResponse, self).__init__()

        self._total = None
        self._jobs = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if jobs is not None:
            self.jobs = jobs
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def total(self):
        r"""Gets the total of this ShowJobsResponse.

        作业数,查询单个作业时为0

        :return: The total of this ShowJobsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowJobsResponse.

        作业数,查询单个作业时为0

        :param total: The total of this ShowJobsResponse.
        :type total: int
        """
        self._total = total

    @property
    def jobs(self):
        r"""Gets the jobs of this ShowJobsResponse.

        作业列表，请参见jobs参数说明

        :return: The jobs of this ShowJobsResponse.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.Job`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this ShowJobsResponse.

        作业列表，请参见jobs参数说明

        :param jobs: The jobs of this ShowJobsResponse.
        :type jobs: list[:class:`huaweicloudsdkcdm.v1.Job`]
        """
        self._jobs = jobs

    @property
    def page_no(self):
        r"""Gets the page_no of this ShowJobsResponse.

        返回指定页号的作业

        :return: The page_no of this ShowJobsResponse.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ShowJobsResponse.

        返回指定页号的作业

        :param page_no: The page_no of this ShowJobsResponse.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowJobsResponse.

        每页作业数

        :return: The page_size of this ShowJobsResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowJobsResponse.

        每页作业数

        :param page_size: The page_size of this ShowJobsResponse.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ShowJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
