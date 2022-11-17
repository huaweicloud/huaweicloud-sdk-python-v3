# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHistoryTaskDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'task_type': 'str',
        'status': 'str',
        'urls': 'list[UrlObject]',
        'create_time': 'int',
        'processing': 'int',
        'succeed': 'int',
        'failed': 'int',
        'total': 'int',
        'file_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_type': 'task_type',
        'status': 'status',
        'urls': 'urls',
        'create_time': 'create_time',
        'processing': 'processing',
        'succeed': 'succeed',
        'failed': 'failed',
        'total': 'total',
        'file_type': 'file_type'
    }

    def __init__(self, id=None, task_type=None, status=None, urls=None, create_time=None, processing=None, succeed=None, failed=None, total=None, file_type=None):
        """ShowHistoryTaskDetailsResponse

        The model defined in huaweicloud sdk

        :param id: 任务id。
        :type id: str
        :param task_type: 任务类型，REFRESH：刷新任务；PREHEATING：预热任务。
        :type task_type: str
        :param status: 任务执行结果,task_done:成功，task_inprocess:处理中。
        :type status: str
        :param urls: 本次提交的url列表。
        :type urls: list[:class:`huaweicloudsdkcdn.v1.UrlObject`]
        :param create_time: 创建时间。
        :type create_time: int
        :param processing: 处理中的url个数。
        :type processing: int
        :param succeed: 成功处理的url个数。
        :type succeed: int
        :param failed: 处理失败的url个数。
        :type failed: int
        :param total: 历史任务的url个数。
        :type total: int
        :param file_type: 文件类型，file：文件；directory：目录，默认是文件file,
        :type file_type: str
        """
        
        super(ShowHistoryTaskDetailsResponse, self).__init__()

        self._id = None
        self._task_type = None
        self._status = None
        self._urls = None
        self._create_time = None
        self._processing = None
        self._succeed = None
        self._failed = None
        self._total = None
        self._file_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_type is not None:
            self.task_type = task_type
        if status is not None:
            self.status = status
        if urls is not None:
            self.urls = urls
        if create_time is not None:
            self.create_time = create_time
        if processing is not None:
            self.processing = processing
        if succeed is not None:
            self.succeed = succeed
        if failed is not None:
            self.failed = failed
        if total is not None:
            self.total = total
        if file_type is not None:
            self.file_type = file_type

    @property
    def id(self):
        """Gets the id of this ShowHistoryTaskDetailsResponse.

        任务id。

        :return: The id of this ShowHistoryTaskDetailsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowHistoryTaskDetailsResponse.

        任务id。

        :param id: The id of this ShowHistoryTaskDetailsResponse.
        :type id: str
        """
        self._id = id

    @property
    def task_type(self):
        """Gets the task_type of this ShowHistoryTaskDetailsResponse.

        任务类型，REFRESH：刷新任务；PREHEATING：预热任务。

        :return: The task_type of this ShowHistoryTaskDetailsResponse.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ShowHistoryTaskDetailsResponse.

        任务类型，REFRESH：刷新任务；PREHEATING：预热任务。

        :param task_type: The task_type of this ShowHistoryTaskDetailsResponse.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def status(self):
        """Gets the status of this ShowHistoryTaskDetailsResponse.

        任务执行结果,task_done:成功，task_inprocess:处理中。

        :return: The status of this ShowHistoryTaskDetailsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowHistoryTaskDetailsResponse.

        任务执行结果,task_done:成功，task_inprocess:处理中。

        :param status: The status of this ShowHistoryTaskDetailsResponse.
        :type status: str
        """
        self._status = status

    @property
    def urls(self):
        """Gets the urls of this ShowHistoryTaskDetailsResponse.

        本次提交的url列表。

        :return: The urls of this ShowHistoryTaskDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.UrlObject`]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this ShowHistoryTaskDetailsResponse.

        本次提交的url列表。

        :param urls: The urls of this ShowHistoryTaskDetailsResponse.
        :type urls: list[:class:`huaweicloudsdkcdn.v1.UrlObject`]
        """
        self._urls = urls

    @property
    def create_time(self):
        """Gets the create_time of this ShowHistoryTaskDetailsResponse.

        创建时间。

        :return: The create_time of this ShowHistoryTaskDetailsResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowHistoryTaskDetailsResponse.

        创建时间。

        :param create_time: The create_time of this ShowHistoryTaskDetailsResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def processing(self):
        """Gets the processing of this ShowHistoryTaskDetailsResponse.

        处理中的url个数。

        :return: The processing of this ShowHistoryTaskDetailsResponse.
        :rtype: int
        """
        return self._processing

    @processing.setter
    def processing(self, processing):
        """Sets the processing of this ShowHistoryTaskDetailsResponse.

        处理中的url个数。

        :param processing: The processing of this ShowHistoryTaskDetailsResponse.
        :type processing: int
        """
        self._processing = processing

    @property
    def succeed(self):
        """Gets the succeed of this ShowHistoryTaskDetailsResponse.

        成功处理的url个数。

        :return: The succeed of this ShowHistoryTaskDetailsResponse.
        :rtype: int
        """
        return self._succeed

    @succeed.setter
    def succeed(self, succeed):
        """Sets the succeed of this ShowHistoryTaskDetailsResponse.

        成功处理的url个数。

        :param succeed: The succeed of this ShowHistoryTaskDetailsResponse.
        :type succeed: int
        """
        self._succeed = succeed

    @property
    def failed(self):
        """Gets the failed of this ShowHistoryTaskDetailsResponse.

        处理失败的url个数。

        :return: The failed of this ShowHistoryTaskDetailsResponse.
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this ShowHistoryTaskDetailsResponse.

        处理失败的url个数。

        :param failed: The failed of this ShowHistoryTaskDetailsResponse.
        :type failed: int
        """
        self._failed = failed

    @property
    def total(self):
        """Gets the total of this ShowHistoryTaskDetailsResponse.

        历史任务的url个数。

        :return: The total of this ShowHistoryTaskDetailsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowHistoryTaskDetailsResponse.

        历史任务的url个数。

        :param total: The total of this ShowHistoryTaskDetailsResponse.
        :type total: int
        """
        self._total = total

    @property
    def file_type(self):
        """Gets the file_type of this ShowHistoryTaskDetailsResponse.

        文件类型，file：文件；directory：目录，默认是文件file,

        :return: The file_type of this ShowHistoryTaskDetailsResponse.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ShowHistoryTaskDetailsResponse.

        文件类型，file：文件；directory：目录，默认是文件file,

        :param file_type: The file_type of this ShowHistoryTaskDetailsResponse.
        :type file_type: str
        """
        self._file_type = file_type

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
        if not isinstance(other, ShowHistoryTaskDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
