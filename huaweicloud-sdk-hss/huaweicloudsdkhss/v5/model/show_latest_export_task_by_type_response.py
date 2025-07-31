# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLatestExportTaskByTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'task_status': 'str',
        'file_id': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_status': 'task_status',
        'file_id': 'file_id',
        'file_name': 'file_name'
    }

    def __init__(self, task_id=None, task_name=None, task_status=None, file_id=None, file_name=None):
        r"""ShowLatestExportTaskByTypeResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        :param task_status: 导出任务状态，success:成功，failure:失败，running:运行中
        :type task_status: str
        :param file_id: 文件ID
        :type file_id: str
        :param file_name: 文件名
        :type file_name: str
        """
        
        super(ShowLatestExportTaskByTypeResponse, self).__init__()

        self._task_id = None
        self._task_name = None
        self._task_status = None
        self._file_id = None
        self._file_name = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_status is not None:
            self.task_status = task_status
        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowLatestExportTaskByTypeResponse.

        任务ID

        :return: The task_id of this ShowLatestExportTaskByTypeResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowLatestExportTaskByTypeResponse.

        任务ID

        :param task_id: The task_id of this ShowLatestExportTaskByTypeResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ShowLatestExportTaskByTypeResponse.

        任务名称

        :return: The task_name of this ShowLatestExportTaskByTypeResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ShowLatestExportTaskByTypeResponse.

        任务名称

        :param task_name: The task_name of this ShowLatestExportTaskByTypeResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_status(self):
        r"""Gets the task_status of this ShowLatestExportTaskByTypeResponse.

        导出任务状态，success:成功，failure:失败，running:运行中

        :return: The task_status of this ShowLatestExportTaskByTypeResponse.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ShowLatestExportTaskByTypeResponse.

        导出任务状态，success:成功，failure:失败，running:运行中

        :param task_status: The task_status of this ShowLatestExportTaskByTypeResponse.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def file_id(self):
        r"""Gets the file_id of this ShowLatestExportTaskByTypeResponse.

        文件ID

        :return: The file_id of this ShowLatestExportTaskByTypeResponse.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this ShowLatestExportTaskByTypeResponse.

        文件ID

        :param file_id: The file_id of this ShowLatestExportTaskByTypeResponse.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def file_name(self):
        r"""Gets the file_name of this ShowLatestExportTaskByTypeResponse.

        文件名

        :return: The file_name of this ShowLatestExportTaskByTypeResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ShowLatestExportTaskByTypeResponse.

        文件名

        :param file_name: The file_name of this ShowLatestExportTaskByTypeResponse.
        :type file_name: str
        """
        self._file_name = file_name

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
        if not isinstance(other, ShowLatestExportTaskByTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
