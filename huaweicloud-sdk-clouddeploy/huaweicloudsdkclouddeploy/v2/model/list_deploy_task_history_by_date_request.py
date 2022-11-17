# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeployTaskHistoryByDateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'id': 'str',
        'page': 'int',
        'size': 'int',
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'id': 'id',
        'page': 'page',
        'size': 'size',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, project_id=None, id=None, page=None, size=None, start_date=None, end_date=None):
        """ListDeployTaskHistoryByDateRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param id: 任务ID
        :type id: str
        :param page: 分页页码， 表示从此页开始查询， page大于等于1
        :type page: int
        :param size: 每页显示的条目数量，size小于等于100
        :type size: int
        :param start_date: 区间开始时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天
        :type start_date: str
        :param end_date: 区间结束时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天
        :type end_date: str
        """
        
        

        self._project_id = None
        self._id = None
        self._page = None
        self._size = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        self.project_id = project_id
        self.id = id
        self.page = page
        self.size = size
        self.start_date = start_date
        self.end_date = end_date

    @property
    def project_id(self):
        """Gets the project_id of this ListDeployTaskHistoryByDateRequest.

        项目ID

        :return: The project_id of this ListDeployTaskHistoryByDateRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListDeployTaskHistoryByDateRequest.

        项目ID

        :param project_id: The project_id of this ListDeployTaskHistoryByDateRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def id(self):
        """Gets the id of this ListDeployTaskHistoryByDateRequest.

        任务ID

        :return: The id of this ListDeployTaskHistoryByDateRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListDeployTaskHistoryByDateRequest.

        任务ID

        :param id: The id of this ListDeployTaskHistoryByDateRequest.
        :type id: str
        """
        self._id = id

    @property
    def page(self):
        """Gets the page of this ListDeployTaskHistoryByDateRequest.

        分页页码， 表示从此页开始查询， page大于等于1

        :return: The page of this ListDeployTaskHistoryByDateRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListDeployTaskHistoryByDateRequest.

        分页页码， 表示从此页开始查询， page大于等于1

        :param page: The page of this ListDeployTaskHistoryByDateRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListDeployTaskHistoryByDateRequest.

        每页显示的条目数量，size小于等于100

        :return: The size of this ListDeployTaskHistoryByDateRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListDeployTaskHistoryByDateRequest.

        每页显示的条目数量，size小于等于100

        :param size: The size of this ListDeployTaskHistoryByDateRequest.
        :type size: int
        """
        self._size = size

    @property
    def start_date(self):
        """Gets the start_date of this ListDeployTaskHistoryByDateRequest.

        区间开始时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天

        :return: The start_date of this ListDeployTaskHistoryByDateRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ListDeployTaskHistoryByDateRequest.

        区间开始时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天

        :param start_date: The start_date of this ListDeployTaskHistoryByDateRequest.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ListDeployTaskHistoryByDateRequest.

        区间结束时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天

        :return: The end_date of this ListDeployTaskHistoryByDateRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ListDeployTaskHistoryByDateRequest.

        区间结束时间，格式yyyy-MM-dd。 开始时间和结束时间间隔不能超过30天

        :param end_date: The end_date of this ListDeployTaskHistoryByDateRequest.
        :type end_date: str
        """
        self._end_date = end_date

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
        if not isinstance(other, ListDeployTaskHistoryByDateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
