# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpdateJobHistoryRequest:

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
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, job_id=None, page_no=None, page_size=None):
        r"""ListUpdateJobHistoryRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param page_no: 分页页码， 表示从此页开始查询， page_no大于等于1
        :type page_no: int
        :param page_size: 每页显示的条目数量，page_size小于等于100
        :type page_size: int
        """
        
        

        self._job_id = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        self.job_id = job_id
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def job_id(self):
        r"""Gets the job_id of this ListUpdateJobHistoryRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this ListUpdateJobHistoryRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListUpdateJobHistoryRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this ListUpdateJobHistoryRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def page_no(self):
        r"""Gets the page_no of this ListUpdateJobHistoryRequest.

        分页页码， 表示从此页开始查询， page_no大于等于1

        :return: The page_no of this ListUpdateJobHistoryRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListUpdateJobHistoryRequest.

        分页页码， 表示从此页开始查询， page_no大于等于1

        :param page_no: The page_no of this ListUpdateJobHistoryRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListUpdateJobHistoryRequest.

        每页显示的条目数量，page_size小于等于100

        :return: The page_size of this ListUpdateJobHistoryRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListUpdateJobHistoryRequest.

        每页显示的条目数量，page_size小于等于100

        :param page_size: The page_size of this ListUpdateJobHistoryRequest.
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
        if not isinstance(other, ListUpdateJobHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
