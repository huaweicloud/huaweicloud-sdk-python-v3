# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskResultsRequest:

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
        'iterator_uri': 'str',
        'page_no': 'str',
        'page_size': 'str',
        'release_dev': 'str'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'task_uri': 'task_uri',
        'iterator_uri': 'iterator_uri',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'release_dev': 'release_dev'
    }

    def __init__(self, project_uuid=None, task_uri=None, iterator_uri=None, page_no=None, page_size=None, release_dev=None):
        r"""ListTaskResultsRequest

        The model defined in huaweicloud sdk

        :param project_uuid: 项目id
        :type project_uuid: str
        :param task_uri: 任务URI
        :type task_uri: str
        :param iterator_uri: 测试计划id
        :type iterator_uri: str
        :param page_no: 当前页数
        :type page_no: str
        :param page_size: 每页多少记录
        :type page_size: str
        :param release_dev: 发布版本
        :type release_dev: str
        """
        
        

        self._project_uuid = None
        self._task_uri = None
        self._iterator_uri = None
        self._page_no = None
        self._page_size = None
        self._release_dev = None
        self.discriminator = None

        self.project_uuid = project_uuid
        self.task_uri = task_uri
        if iterator_uri is not None:
            self.iterator_uri = iterator_uri
        self.page_no = page_no
        self.page_size = page_size
        if release_dev is not None:
            self.release_dev = release_dev

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ListTaskResultsRequest.

        项目id

        :return: The project_uuid of this ListTaskResultsRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ListTaskResultsRequest.

        项目id

        :param project_uuid: The project_uuid of this ListTaskResultsRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def task_uri(self):
        r"""Gets the task_uri of this ListTaskResultsRequest.

        任务URI

        :return: The task_uri of this ListTaskResultsRequest.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this ListTaskResultsRequest.

        任务URI

        :param task_uri: The task_uri of this ListTaskResultsRequest.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def iterator_uri(self):
        r"""Gets the iterator_uri of this ListTaskResultsRequest.

        测试计划id

        :return: The iterator_uri of this ListTaskResultsRequest.
        :rtype: str
        """
        return self._iterator_uri

    @iterator_uri.setter
    def iterator_uri(self, iterator_uri):
        r"""Sets the iterator_uri of this ListTaskResultsRequest.

        测试计划id

        :param iterator_uri: The iterator_uri of this ListTaskResultsRequest.
        :type iterator_uri: str
        """
        self._iterator_uri = iterator_uri

    @property
    def page_no(self):
        r"""Gets the page_no of this ListTaskResultsRequest.

        当前页数

        :return: The page_no of this ListTaskResultsRequest.
        :rtype: str
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListTaskResultsRequest.

        当前页数

        :param page_no: The page_no of this ListTaskResultsRequest.
        :type page_no: str
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListTaskResultsRequest.

        每页多少记录

        :return: The page_size of this ListTaskResultsRequest.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListTaskResultsRequest.

        每页多少记录

        :param page_size: The page_size of this ListTaskResultsRequest.
        :type page_size: str
        """
        self._page_size = page_size

    @property
    def release_dev(self):
        r"""Gets the release_dev of this ListTaskResultsRequest.

        发布版本

        :return: The release_dev of this ListTaskResultsRequest.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this ListTaskResultsRequest.

        发布版本

        :param release_dev: The release_dev of this ListTaskResultsRequest.
        :type release_dev: str
        """
        self._release_dev = release_dev

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
        if not isinstance(other, ListTaskResultsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
