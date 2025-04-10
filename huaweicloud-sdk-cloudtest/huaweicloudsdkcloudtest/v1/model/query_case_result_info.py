# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCaseResultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'task_uri': 'str',
        'task_id': 'str',
        'release_dev': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'sort_field': 'str',
        'sort_type': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'task_uri': 'task_uri',
        'task_id': 'task_id',
        'release_dev': 'release_dev',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type'
    }

    def __init__(self, uri=None, task_uri=None, task_id=None, release_dev=None, page_no=None, page_size=None, sort_field=None, sort_type=None):
        r"""QueryCaseResultInfo

        The model defined in huaweicloud sdk

        :param uri: 结果URI
        :type uri: str
        :param task_uri: 测试任务URI
        :type task_uri: str
        :param task_id: 执行id
        :type task_id: str
        :param release_dev: 版本号
        :type release_dev: str
        :param page_no: 当前页数
        :type page_no: int
        :param page_size: 每页条数
        :type page_size: int
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_type: 排序类型
        :type sort_type: str
        """
        
        

        self._uri = None
        self._task_uri = None
        self._task_id = None
        self._release_dev = None
        self._page_no = None
        self._page_size = None
        self._sort_field = None
        self._sort_type = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if task_uri is not None:
            self.task_uri = task_uri
        if task_id is not None:
            self.task_id = task_id
        if release_dev is not None:
            self.release_dev = release_dev
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type

    @property
    def uri(self):
        r"""Gets the uri of this QueryCaseResultInfo.

        结果URI

        :return: The uri of this QueryCaseResultInfo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this QueryCaseResultInfo.

        结果URI

        :param uri: The uri of this QueryCaseResultInfo.
        :type uri: str
        """
        self._uri = uri

    @property
    def task_uri(self):
        r"""Gets the task_uri of this QueryCaseResultInfo.

        测试任务URI

        :return: The task_uri of this QueryCaseResultInfo.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this QueryCaseResultInfo.

        测试任务URI

        :param task_uri: The task_uri of this QueryCaseResultInfo.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def task_id(self):
        r"""Gets the task_id of this QueryCaseResultInfo.

        执行id

        :return: The task_id of this QueryCaseResultInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this QueryCaseResultInfo.

        执行id

        :param task_id: The task_id of this QueryCaseResultInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def release_dev(self):
        r"""Gets the release_dev of this QueryCaseResultInfo.

        版本号

        :return: The release_dev of this QueryCaseResultInfo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this QueryCaseResultInfo.

        版本号

        :param release_dev: The release_dev of this QueryCaseResultInfo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def page_no(self):
        r"""Gets the page_no of this QueryCaseResultInfo.

        当前页数

        :return: The page_no of this QueryCaseResultInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this QueryCaseResultInfo.

        当前页数

        :param page_no: The page_no of this QueryCaseResultInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this QueryCaseResultInfo.

        每页条数

        :return: The page_size of this QueryCaseResultInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this QueryCaseResultInfo.

        每页条数

        :param page_size: The page_size of this QueryCaseResultInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def sort_field(self):
        r"""Gets the sort_field of this QueryCaseResultInfo.

        排序字段

        :return: The sort_field of this QueryCaseResultInfo.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this QueryCaseResultInfo.

        排序字段

        :param sort_field: The sort_field of this QueryCaseResultInfo.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this QueryCaseResultInfo.

        排序类型

        :return: The sort_type of this QueryCaseResultInfo.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this QueryCaseResultInfo.

        排序类型

        :param sort_type: The sort_type of this QueryCaseResultInfo.
        :type sort_type: str
        """
        self._sort_type = sort_type

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
        if not isinstance(other, QueryCaseResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
