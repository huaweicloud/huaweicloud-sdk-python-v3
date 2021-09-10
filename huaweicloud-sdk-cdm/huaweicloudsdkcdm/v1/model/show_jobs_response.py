# coding: utf-8

import re
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
        'simple': 'bool',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'total': 'total',
        'jobs': 'jobs',
        'simple': 'simple',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, total=None, jobs=None, simple=None, page_no=None, page_size=None):
        """ShowJobsResponse - a model defined in huaweicloud sdk"""
        
        super(ShowJobsResponse, self).__init__()

        self._total = None
        self._jobs = None
        self._simple = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if jobs is not None:
            self.jobs = jobs
        if simple is not None:
            self.simple = simple
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def total(self):
        """Gets the total of this ShowJobsResponse.

        作业数

        :return: The total of this ShowJobsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowJobsResponse.

        作业数

        :param total: The total of this ShowJobsResponse.
        :type: int
        """
        self._total = total

    @property
    def jobs(self):
        """Gets the jobs of this ShowJobsResponse.

        作业列表，请参见jobs参数说明

        :return: The jobs of this ShowJobsResponse.
        :rtype: list[Job]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ShowJobsResponse.

        作业列表，请参见jobs参数说明

        :param jobs: The jobs of this ShowJobsResponse.
        :type: list[Job]
        """
        self._jobs = jobs

    @property
    def simple(self):
        """Gets the simple of this ShowJobsResponse.

        当为“true”时返回精简消息，即作业参数只返回参数名和值，不返回参数的“size”、“type”、“id”等属性

        :return: The simple of this ShowJobsResponse.
        :rtype: bool
        """
        return self._simple

    @simple.setter
    def simple(self, simple):
        """Sets the simple of this ShowJobsResponse.

        当为“true”时返回精简消息，即作业参数只返回参数名和值，不返回参数的“size”、“type”、“id”等属性

        :param simple: The simple of this ShowJobsResponse.
        :type: bool
        """
        self._simple = simple

    @property
    def page_no(self):
        """Gets the page_no of this ShowJobsResponse.

        返回指定页号的作业

        :return: The page_no of this ShowJobsResponse.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this ShowJobsResponse.

        返回指定页号的作业

        :param page_no: The page_no of this ShowJobsResponse.
        :type: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this ShowJobsResponse.

        每页作业数

        :return: The page_size of this ShowJobsResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowJobsResponse.

        每页作业数

        :param page_size: The page_size of this ShowJobsResponse.
        :type: int
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
