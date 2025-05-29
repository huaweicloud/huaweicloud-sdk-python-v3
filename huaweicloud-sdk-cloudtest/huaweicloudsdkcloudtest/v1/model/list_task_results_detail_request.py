# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskResultsDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'task_uri': 'str',
        'result_uri': 'str',
        'page_no': 'str',
        'page_size': 'str',
        'result': 'str'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'task_uri': 'task_uri',
        'result_uri': 'result_uri',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'result': 'result'
    }

    def __init__(self, project_uuid=None, task_uri=None, result_uri=None, page_no=None, page_size=None, result=None):
        r"""ListTaskResultsDetailRequest

        The model defined in huaweicloud sdk

        :param project_uuid: 项目id
        :type project_uuid: str
        :param task_uri: 任务URI
        :type task_uri: str
        :param result_uri: 测试任务结果uri
        :type result_uri: str
        :param page_no: 当前页数
        :type page_no: str
        :param page_size: 每页多少记录
        :type page_size: str
        :param result: 结果过滤条件
        :type result: str
        """
        
        

        self._project_uuid = None
        self._task_uri = None
        self._result_uri = None
        self._page_no = None
        self._page_size = None
        self._result = None
        self.discriminator = None

        self.project_uuid = project_uuid
        self.task_uri = task_uri
        self.result_uri = result_uri
        self.page_no = page_no
        self.page_size = page_size
        if result is not None:
            self.result = result

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ListTaskResultsDetailRequest.

        项目id

        :return: The project_uuid of this ListTaskResultsDetailRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ListTaskResultsDetailRequest.

        项目id

        :param project_uuid: The project_uuid of this ListTaskResultsDetailRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def task_uri(self):
        r"""Gets the task_uri of this ListTaskResultsDetailRequest.

        任务URI

        :return: The task_uri of this ListTaskResultsDetailRequest.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this ListTaskResultsDetailRequest.

        任务URI

        :param task_uri: The task_uri of this ListTaskResultsDetailRequest.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def result_uri(self):
        r"""Gets the result_uri of this ListTaskResultsDetailRequest.

        测试任务结果uri

        :return: The result_uri of this ListTaskResultsDetailRequest.
        :rtype: str
        """
        return self._result_uri

    @result_uri.setter
    def result_uri(self, result_uri):
        r"""Sets the result_uri of this ListTaskResultsDetailRequest.

        测试任务结果uri

        :param result_uri: The result_uri of this ListTaskResultsDetailRequest.
        :type result_uri: str
        """
        self._result_uri = result_uri

    @property
    def page_no(self):
        r"""Gets the page_no of this ListTaskResultsDetailRequest.

        当前页数

        :return: The page_no of this ListTaskResultsDetailRequest.
        :rtype: str
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListTaskResultsDetailRequest.

        当前页数

        :param page_no: The page_no of this ListTaskResultsDetailRequest.
        :type page_no: str
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListTaskResultsDetailRequest.

        每页多少记录

        :return: The page_size of this ListTaskResultsDetailRequest.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListTaskResultsDetailRequest.

        每页多少记录

        :param page_size: The page_size of this ListTaskResultsDetailRequest.
        :type page_size: str
        """
        self._page_size = page_size

    @property
    def result(self):
        r"""Gets the result of this ListTaskResultsDetailRequest.

        结果过滤条件

        :return: The result of this ListTaskResultsDetailRequest.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListTaskResultsDetailRequest.

        结果过滤条件

        :param result: The result of this ListTaskResultsDetailRequest.
        :type result: str
        """
        self._result = result

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
        if not isinstance(other, ListTaskResultsDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
