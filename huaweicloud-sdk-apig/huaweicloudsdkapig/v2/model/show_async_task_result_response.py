# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAsyncTaskResultResponse(SdkResponse):

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
        'task_status': 'str',
        'task_type': 'str',
        'task_result': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_status': 'task_status',
        'task_type': 'task_type',
        'task_result': 'task_result'
    }

    def __init__(self, task_id=None, task_status=None, task_type=None, task_result=None):
        """ShowAsyncTaskResultResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务id
        :type task_id: str
        :param task_status: 任务状态。waiting等待处理，processing处理中，succeed成功，failed失败。
        :type task_status: str
        :param task_type: 任务类型。 import_api为异步导入api，export_api为异步导出api。
        :type task_type: str
        :param task_result: 任务结果。string可转成json object。 当task_type为import_api时，字段包括API分组编号group_id、success数组、failure数组、swagger结构体、ignore数组。其中success数组元素中包括4个字段，导入成功的API编号id、API请求方法method、API请求路径path、导入行为action（枚举值，update表示更新API，create表示新建API）。failure数组元素中包括4个字段，API请求方法method、API请求路径path、导入失败的错误码error_code、导入失败的错误信息error_msg。swagger结构体包括2个字段，swagger文档编号id、导入结果说明result。ignore数组元素包括API请求方法method、API请求路径path。 当task_type为export_api时，字段包括导出文件类型file_type、导出文件内容content。
        :type task_result: str
        """
        
        super(ShowAsyncTaskResultResponse, self).__init__()

        self._task_id = None
        self._task_status = None
        self._task_type = None
        self._task_result = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_status is not None:
            self.task_status = task_status
        if task_type is not None:
            self.task_type = task_type
        if task_result is not None:
            self.task_result = task_result

    @property
    def task_id(self):
        """Gets the task_id of this ShowAsyncTaskResultResponse.

        任务id

        :return: The task_id of this ShowAsyncTaskResultResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowAsyncTaskResultResponse.

        任务id

        :param task_id: The task_id of this ShowAsyncTaskResultResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_status(self):
        """Gets the task_status of this ShowAsyncTaskResultResponse.

        任务状态。waiting等待处理，processing处理中，succeed成功，failed失败。

        :return: The task_status of this ShowAsyncTaskResultResponse.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ShowAsyncTaskResultResponse.

        任务状态。waiting等待处理，processing处理中，succeed成功，failed失败。

        :param task_status: The task_status of this ShowAsyncTaskResultResponse.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def task_type(self):
        """Gets the task_type of this ShowAsyncTaskResultResponse.

        任务类型。 import_api为异步导入api，export_api为异步导出api。

        :return: The task_type of this ShowAsyncTaskResultResponse.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ShowAsyncTaskResultResponse.

        任务类型。 import_api为异步导入api，export_api为异步导出api。

        :param task_type: The task_type of this ShowAsyncTaskResultResponse.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def task_result(self):
        """Gets the task_result of this ShowAsyncTaskResultResponse.

        任务结果。string可转成json object。 当task_type为import_api时，字段包括API分组编号group_id、success数组、failure数组、swagger结构体、ignore数组。其中success数组元素中包括4个字段，导入成功的API编号id、API请求方法method、API请求路径path、导入行为action（枚举值，update表示更新API，create表示新建API）。failure数组元素中包括4个字段，API请求方法method、API请求路径path、导入失败的错误码error_code、导入失败的错误信息error_msg。swagger结构体包括2个字段，swagger文档编号id、导入结果说明result。ignore数组元素包括API请求方法method、API请求路径path。 当task_type为export_api时，字段包括导出文件类型file_type、导出文件内容content。

        :return: The task_result of this ShowAsyncTaskResultResponse.
        :rtype: str
        """
        return self._task_result

    @task_result.setter
    def task_result(self, task_result):
        """Sets the task_result of this ShowAsyncTaskResultResponse.

        任务结果。string可转成json object。 当task_type为import_api时，字段包括API分组编号group_id、success数组、failure数组、swagger结构体、ignore数组。其中success数组元素中包括4个字段，导入成功的API编号id、API请求方法method、API请求路径path、导入行为action（枚举值，update表示更新API，create表示新建API）。failure数组元素中包括4个字段，API请求方法method、API请求路径path、导入失败的错误码error_code、导入失败的错误信息error_msg。swagger结构体包括2个字段，swagger文档编号id、导入结果说明result。ignore数组元素包括API请求方法method、API请求路径path。 当task_type为export_api时，字段包括导出文件类型file_type、导出文件内容content。

        :param task_result: The task_result of this ShowAsyncTaskResultResponse.
        :type task_result: str
        """
        self._task_result = task_result

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
        if not isinstance(other, ShowAsyncTaskResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
