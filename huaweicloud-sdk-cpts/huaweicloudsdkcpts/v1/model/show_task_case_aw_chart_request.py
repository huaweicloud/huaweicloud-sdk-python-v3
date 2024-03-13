# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskCaseAwChartRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_run_id': 'int',
        'case_run_id': 'int',
        'detail_id': 'str'
    }

    attribute_map = {
        'task_run_id': 'task_run_id',
        'case_run_id': 'case_run_id',
        'detail_id': 'detail_id'
    }

    def __init__(self, task_run_id=None, case_run_id=None, detail_id=None):
        """ShowTaskCaseAwChartRequest

        The model defined in huaweicloud sdk

        :param task_run_id: 运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。
        :type task_run_id: int
        :param case_run_id: 运行用例id，通过报告管理中的“内外融合当前任务用例列表”接口获取：使用任务运行id（task_run_id）作为路径参数，可以查询到该报告关联的用例运行id集合，即返回结构体中result.case_aw_info_list[index].case_uri_i为索引为index的运行用例id（case_run_id）。
        :type case_run_id: int
        :param detail_id: 运行用例详情id，通过报告管理中的“内外融合当前任务用例列表”接口获取：使用运行任务id（task_run_id）作为路径参数，可以查询到该报告关联的运行用例详情id集合，即返回结构体中result.case_aw_info_list[index].testcaseId为索引为index的运行用例详情id（detail_id）。
        :type detail_id: str
        """
        
        

        self._task_run_id = None
        self._case_run_id = None
        self._detail_id = None
        self.discriminator = None

        self.task_run_id = task_run_id
        self.case_run_id = case_run_id
        self.detail_id = detail_id

    @property
    def task_run_id(self):
        """Gets the task_run_id of this ShowTaskCaseAwChartRequest.

        运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。

        :return: The task_run_id of this ShowTaskCaseAwChartRequest.
        :rtype: int
        """
        return self._task_run_id

    @task_run_id.setter
    def task_run_id(self, task_run_id):
        """Sets the task_run_id of this ShowTaskCaseAwChartRequest.

        运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。

        :param task_run_id: The task_run_id of this ShowTaskCaseAwChartRequest.
        :type task_run_id: int
        """
        self._task_run_id = task_run_id

    @property
    def case_run_id(self):
        """Gets the case_run_id of this ShowTaskCaseAwChartRequest.

        运行用例id，通过报告管理中的“内外融合当前任务用例列表”接口获取：使用任务运行id（task_run_id）作为路径参数，可以查询到该报告关联的用例运行id集合，即返回结构体中result.case_aw_info_list[index].case_uri_i为索引为index的运行用例id（case_run_id）。

        :return: The case_run_id of this ShowTaskCaseAwChartRequest.
        :rtype: int
        """
        return self._case_run_id

    @case_run_id.setter
    def case_run_id(self, case_run_id):
        """Sets the case_run_id of this ShowTaskCaseAwChartRequest.

        运行用例id，通过报告管理中的“内外融合当前任务用例列表”接口获取：使用任务运行id（task_run_id）作为路径参数，可以查询到该报告关联的用例运行id集合，即返回结构体中result.case_aw_info_list[index].case_uri_i为索引为index的运行用例id（case_run_id）。

        :param case_run_id: The case_run_id of this ShowTaskCaseAwChartRequest.
        :type case_run_id: int
        """
        self._case_run_id = case_run_id

    @property
    def detail_id(self):
        """Gets the detail_id of this ShowTaskCaseAwChartRequest.

        运行用例详情id，通过报告管理中的“内外融合当前任务用例列表”接口获取：使用运行任务id（task_run_id）作为路径参数，可以查询到该报告关联的运行用例详情id集合，即返回结构体中result.case_aw_info_list[index].testcaseId为索引为index的运行用例详情id（detail_id）。

        :return: The detail_id of this ShowTaskCaseAwChartRequest.
        :rtype: str
        """
        return self._detail_id

    @detail_id.setter
    def detail_id(self, detail_id):
        """Sets the detail_id of this ShowTaskCaseAwChartRequest.

        运行用例详情id，通过报告管理中的“内外融合当前任务用例列表”接口获取：使用运行任务id（task_run_id）作为路径参数，可以查询到该报告关联的运行用例详情id集合，即返回结构体中result.case_aw_info_list[index].testcaseId为索引为index的运行用例详情id（detail_id）。

        :param detail_id: The detail_id of this ShowTaskCaseAwChartRequest.
        :type detail_id: str
        """
        self._detail_id = detail_id

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
        if not isinstance(other, ShowTaskCaseAwChartRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
