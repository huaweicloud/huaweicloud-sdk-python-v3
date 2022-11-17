# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExecuteJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_size': 'str',
        'current_page': 'str',
        'job_name': 'str',
        'cluster_id': 'str',
        'state': 'str',
        'id': 'str'
    }

    attribute_map = {
        'page_size': 'page_size',
        'current_page': 'current_page',
        'job_name': 'job_name',
        'cluster_id': 'cluster_id',
        'state': 'state',
        'id': 'id'
    }

    def __init__(self, page_size=None, current_page=None, job_name=None, cluster_id=None, state=None, id=None):
        """ListExecuteJobRequest

        The model defined in huaweicloud sdk

        :param page_size: 分页查询每页返回的最大作业数量。  取值范围：[1～100]
        :type page_size: str
        :param current_page: 当前查询页码。
        :type current_page: str
        :param job_name: 作业名称。
        :type job_name: str
        :param cluster_id: 集群编号。
        :type cluster_id: str
        :param state: 作业状态编码：  - 1：Terminated表示已终止的作业状态 - 2：Running表示运行中的作业状态 - 3：Completed表示已完成的作业状态 - 4：Abnormal表示异常的作业状态
        :type state: str
        :param id: 作业执行对象的编号。
        :type id: str
        """
        
        

        self._page_size = None
        self._current_page = None
        self._job_name = None
        self._cluster_id = None
        self._state = None
        self._id = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if current_page is not None:
            self.current_page = current_page
        if job_name is not None:
            self.job_name = job_name
        self.cluster_id = cluster_id
        if state is not None:
            self.state = state
        if id is not None:
            self.id = id

    @property
    def page_size(self):
        """Gets the page_size of this ListExecuteJobRequest.

        分页查询每页返回的最大作业数量。  取值范围：[1～100]

        :return: The page_size of this ListExecuteJobRequest.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListExecuteJobRequest.

        分页查询每页返回的最大作业数量。  取值范围：[1～100]

        :param page_size: The page_size of this ListExecuteJobRequest.
        :type page_size: str
        """
        self._page_size = page_size

    @property
    def current_page(self):
        """Gets the current_page of this ListExecuteJobRequest.

        当前查询页码。

        :return: The current_page of this ListExecuteJobRequest.
        :rtype: str
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this ListExecuteJobRequest.

        当前查询页码。

        :param current_page: The current_page of this ListExecuteJobRequest.
        :type current_page: str
        """
        self._current_page = current_page

    @property
    def job_name(self):
        """Gets the job_name of this ListExecuteJobRequest.

        作业名称。

        :return: The job_name of this ListExecuteJobRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ListExecuteJobRequest.

        作业名称。

        :param job_name: The job_name of this ListExecuteJobRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListExecuteJobRequest.

        集群编号。

        :return: The cluster_id of this ListExecuteJobRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListExecuteJobRequest.

        集群编号。

        :param cluster_id: The cluster_id of this ListExecuteJobRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def state(self):
        """Gets the state of this ListExecuteJobRequest.

        作业状态编码：  - 1：Terminated表示已终止的作业状态 - 2：Running表示运行中的作业状态 - 3：Completed表示已完成的作业状态 - 4：Abnormal表示异常的作业状态

        :return: The state of this ListExecuteJobRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListExecuteJobRequest.

        作业状态编码：  - 1：Terminated表示已终止的作业状态 - 2：Running表示运行中的作业状态 - 3：Completed表示已完成的作业状态 - 4：Abnormal表示异常的作业状态

        :param state: The state of this ListExecuteJobRequest.
        :type state: str
        """
        self._state = state

    @property
    def id(self):
        """Gets the id of this ListExecuteJobRequest.

        作业执行对象的编号。

        :return: The id of this ListExecuteJobRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListExecuteJobRequest.

        作业执行对象的编号。

        :param id: The id of this ListExecuteJobRequest.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ListExecuteJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
