# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelatedTempRunningData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_run_info_id': 'int',
        'related_temp_running_id': 'int',
        'temp_id': 'int',
        'temp_name': 'str',
        'content_method_url': 'list[str]',
        'related_temp_running_data': 'list[TempRunningData]'
    }

    attribute_map = {
        'task_run_info_id': 'task_run_info_id',
        'related_temp_running_id': 'related_temp_running_id',
        'temp_id': 'temp_id',
        'temp_name': 'temp_name',
        'content_method_url': 'content_method_url',
        'related_temp_running_data': 'related_temp_running_data'
    }

    def __init__(self, task_run_info_id=None, related_temp_running_id=None, temp_id=None, temp_name=None, content_method_url=None, related_temp_running_data=None):
        r"""RelatedTempRunningData

        The model defined in huaweicloud sdk

        :param task_run_info_id: 运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。
        :type task_run_info_id: int
        :param related_temp_running_id: 运行用例id。对应其他（如报告）接口的运行用例id（case_run_id）。
        :type related_temp_running_id: int
        :param temp_id: 用例id
        :type temp_id: int
        :param temp_name: 用例名称
        :type temp_name: str
        :param content_method_url: 请求信息，包括请求名称，方法，url信息
        :type content_method_url: list[str]
        :param related_temp_running_data: 最近一次运行的报告简略信息
        :type related_temp_running_data: list[:class:`huaweicloudsdkcpts.v1.TempRunningData`]
        """
        
        

        self._task_run_info_id = None
        self._related_temp_running_id = None
        self._temp_id = None
        self._temp_name = None
        self._content_method_url = None
        self._related_temp_running_data = None
        self.discriminator = None

        if task_run_info_id is not None:
            self.task_run_info_id = task_run_info_id
        if related_temp_running_id is not None:
            self.related_temp_running_id = related_temp_running_id
        if temp_id is not None:
            self.temp_id = temp_id
        if temp_name is not None:
            self.temp_name = temp_name
        if content_method_url is not None:
            self.content_method_url = content_method_url
        if related_temp_running_data is not None:
            self.related_temp_running_data = related_temp_running_data

    @property
    def task_run_info_id(self):
        r"""Gets the task_run_info_id of this RelatedTempRunningData.

        运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。

        :return: The task_run_info_id of this RelatedTempRunningData.
        :rtype: int
        """
        return self._task_run_info_id

    @task_run_info_id.setter
    def task_run_info_id(self, task_run_info_id):
        r"""Sets the task_run_info_id of this RelatedTempRunningData.

        运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。

        :param task_run_info_id: The task_run_info_id of this RelatedTempRunningData.
        :type task_run_info_id: int
        """
        self._task_run_info_id = task_run_info_id

    @property
    def related_temp_running_id(self):
        r"""Gets the related_temp_running_id of this RelatedTempRunningData.

        运行用例id。对应其他（如报告）接口的运行用例id（case_run_id）。

        :return: The related_temp_running_id of this RelatedTempRunningData.
        :rtype: int
        """
        return self._related_temp_running_id

    @related_temp_running_id.setter
    def related_temp_running_id(self, related_temp_running_id):
        r"""Sets the related_temp_running_id of this RelatedTempRunningData.

        运行用例id。对应其他（如报告）接口的运行用例id（case_run_id）。

        :param related_temp_running_id: The related_temp_running_id of this RelatedTempRunningData.
        :type related_temp_running_id: int
        """
        self._related_temp_running_id = related_temp_running_id

    @property
    def temp_id(self):
        r"""Gets the temp_id of this RelatedTempRunningData.

        用例id

        :return: The temp_id of this RelatedTempRunningData.
        :rtype: int
        """
        return self._temp_id

    @temp_id.setter
    def temp_id(self, temp_id):
        r"""Sets the temp_id of this RelatedTempRunningData.

        用例id

        :param temp_id: The temp_id of this RelatedTempRunningData.
        :type temp_id: int
        """
        self._temp_id = temp_id

    @property
    def temp_name(self):
        r"""Gets the temp_name of this RelatedTempRunningData.

        用例名称

        :return: The temp_name of this RelatedTempRunningData.
        :rtype: str
        """
        return self._temp_name

    @temp_name.setter
    def temp_name(self, temp_name):
        r"""Sets the temp_name of this RelatedTempRunningData.

        用例名称

        :param temp_name: The temp_name of this RelatedTempRunningData.
        :type temp_name: str
        """
        self._temp_name = temp_name

    @property
    def content_method_url(self):
        r"""Gets the content_method_url of this RelatedTempRunningData.

        请求信息，包括请求名称，方法，url信息

        :return: The content_method_url of this RelatedTempRunningData.
        :rtype: list[str]
        """
        return self._content_method_url

    @content_method_url.setter
    def content_method_url(self, content_method_url):
        r"""Sets the content_method_url of this RelatedTempRunningData.

        请求信息，包括请求名称，方法，url信息

        :param content_method_url: The content_method_url of this RelatedTempRunningData.
        :type content_method_url: list[str]
        """
        self._content_method_url = content_method_url

    @property
    def related_temp_running_data(self):
        r"""Gets the related_temp_running_data of this RelatedTempRunningData.

        最近一次运行的报告简略信息

        :return: The related_temp_running_data of this RelatedTempRunningData.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.TempRunningData`]
        """
        return self._related_temp_running_data

    @related_temp_running_data.setter
    def related_temp_running_data(self, related_temp_running_data):
        r"""Sets the related_temp_running_data of this RelatedTempRunningData.

        最近一次运行的报告简略信息

        :param related_temp_running_data: The related_temp_running_data of this RelatedTempRunningData.
        :type related_temp_running_data: list[:class:`huaweicloudsdkcpts.v1.TempRunningData`]
        """
        self._related_temp_running_data = related_temp_running_data

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
        if not isinstance(other, RelatedTempRunningData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
