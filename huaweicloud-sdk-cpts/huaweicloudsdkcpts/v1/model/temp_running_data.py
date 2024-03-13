# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TempRunningData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_method_url': 'list[str]',
        'crawler_status': 'int',
        'related_temp_running_id': 'int',
        'task_run_info_id': 'int',
        'temp_id': 'int',
        'temp_name': 'str',
        'temp_running_status': 'int'
    }

    attribute_map = {
        'content_method_url': 'content_method_url',
        'crawler_status': 'crawler_status',
        'related_temp_running_id': 'related_temp_running_id',
        'task_run_info_id': 'task_run_info_id',
        'temp_id': 'temp_id',
        'temp_name': 'temp_name',
        'temp_running_status': 'temp_running_status'
    }

    def __init__(self, content_method_url=None, crawler_status=None, related_temp_running_id=None, task_run_info_id=None, temp_id=None, temp_name=None, temp_running_status=None):
        """TempRunningData

        The model defined in huaweicloud sdk

        :param content_method_url: 请求信息，包括请求名称，方法，url信息
        :type content_method_url: list[str]
        :param crawler_status: 请求运行状态（0：正常返回；1：解析失败； 2：比对失败； 3：响应超时；）
        :type crawler_status: int
        :param related_temp_running_id: 运行用例id。对应其他（如报告）接口的运行用例id（case_run_id）。
        :type related_temp_running_id: int
        :param task_run_info_id: 运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。
        :type task_run_info_id: int
        :param temp_id: 用例或者事务id
        :type temp_id: int
        :param temp_name: 用例或者事务名称
        :type temp_name: str
        :param temp_running_status: 运行状态（9：表示等待运行；0：表示运行中；2：表示结束；3：异常中止；4：用户主动终止（完成状态）；5：用户主动终止（终止中状态））
        :type temp_running_status: int
        """
        
        

        self._content_method_url = None
        self._crawler_status = None
        self._related_temp_running_id = None
        self._task_run_info_id = None
        self._temp_id = None
        self._temp_name = None
        self._temp_running_status = None
        self.discriminator = None

        if content_method_url is not None:
            self.content_method_url = content_method_url
        if crawler_status is not None:
            self.crawler_status = crawler_status
        if related_temp_running_id is not None:
            self.related_temp_running_id = related_temp_running_id
        if task_run_info_id is not None:
            self.task_run_info_id = task_run_info_id
        if temp_id is not None:
            self.temp_id = temp_id
        if temp_name is not None:
            self.temp_name = temp_name
        if temp_running_status is not None:
            self.temp_running_status = temp_running_status

    @property
    def content_method_url(self):
        """Gets the content_method_url of this TempRunningData.

        请求信息，包括请求名称，方法，url信息

        :return: The content_method_url of this TempRunningData.
        :rtype: list[str]
        """
        return self._content_method_url

    @content_method_url.setter
    def content_method_url(self, content_method_url):
        """Sets the content_method_url of this TempRunningData.

        请求信息，包括请求名称，方法，url信息

        :param content_method_url: The content_method_url of this TempRunningData.
        :type content_method_url: list[str]
        """
        self._content_method_url = content_method_url

    @property
    def crawler_status(self):
        """Gets the crawler_status of this TempRunningData.

        请求运行状态（0：正常返回；1：解析失败； 2：比对失败； 3：响应超时；）

        :return: The crawler_status of this TempRunningData.
        :rtype: int
        """
        return self._crawler_status

    @crawler_status.setter
    def crawler_status(self, crawler_status):
        """Sets the crawler_status of this TempRunningData.

        请求运行状态（0：正常返回；1：解析失败； 2：比对失败； 3：响应超时；）

        :param crawler_status: The crawler_status of this TempRunningData.
        :type crawler_status: int
        """
        self._crawler_status = crawler_status

    @property
    def related_temp_running_id(self):
        """Gets the related_temp_running_id of this TempRunningData.

        运行用例id。对应其他（如报告）接口的运行用例id（case_run_id）。

        :return: The related_temp_running_id of this TempRunningData.
        :rtype: int
        """
        return self._related_temp_running_id

    @related_temp_running_id.setter
    def related_temp_running_id(self, related_temp_running_id):
        """Sets the related_temp_running_id of this TempRunningData.

        运行用例id。对应其他（如报告）接口的运行用例id（case_run_id）。

        :param related_temp_running_id: The related_temp_running_id of this TempRunningData.
        :type related_temp_running_id: int
        """
        self._related_temp_running_id = related_temp_running_id

    @property
    def task_run_info_id(self):
        """Gets the task_run_info_id of this TempRunningData.

        运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。

        :return: The task_run_info_id of this TempRunningData.
        :rtype: int
        """
        return self._task_run_info_id

    @task_run_info_id.setter
    def task_run_info_id(self, task_run_info_id):
        """Sets the task_run_info_id of this TempRunningData.

        运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。

        :param task_run_info_id: The task_run_info_id of this TempRunningData.
        :type task_run_info_id: int
        """
        self._task_run_info_id = task_run_info_id

    @property
    def temp_id(self):
        """Gets the temp_id of this TempRunningData.

        用例或者事务id

        :return: The temp_id of this TempRunningData.
        :rtype: int
        """
        return self._temp_id

    @temp_id.setter
    def temp_id(self, temp_id):
        """Sets the temp_id of this TempRunningData.

        用例或者事务id

        :param temp_id: The temp_id of this TempRunningData.
        :type temp_id: int
        """
        self._temp_id = temp_id

    @property
    def temp_name(self):
        """Gets the temp_name of this TempRunningData.

        用例或者事务名称

        :return: The temp_name of this TempRunningData.
        :rtype: str
        """
        return self._temp_name

    @temp_name.setter
    def temp_name(self, temp_name):
        """Sets the temp_name of this TempRunningData.

        用例或者事务名称

        :param temp_name: The temp_name of this TempRunningData.
        :type temp_name: str
        """
        self._temp_name = temp_name

    @property
    def temp_running_status(self):
        """Gets the temp_running_status of this TempRunningData.

        运行状态（9：表示等待运行；0：表示运行中；2：表示结束；3：异常中止；4：用户主动终止（完成状态）；5：用户主动终止（终止中状态））

        :return: The temp_running_status of this TempRunningData.
        :rtype: int
        """
        return self._temp_running_status

    @temp_running_status.setter
    def temp_running_status(self, temp_running_status):
        """Sets the temp_running_status of this TempRunningData.

        运行状态（9：表示等待运行；0：表示运行中；2：表示结束；3：异常中止；4：用户主动终止（完成状态）；5：用户主动终止（终止中状态））

        :param temp_running_status: The temp_running_status of this TempRunningData.
        :type temp_running_status: int
        """
        self._temp_running_status = temp_running_status

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
        if not isinstance(other, TempRunningData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
