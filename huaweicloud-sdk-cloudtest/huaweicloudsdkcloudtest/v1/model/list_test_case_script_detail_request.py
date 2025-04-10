# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTestCaseScriptDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'task_id': 'str',
        'tmss_case_uri': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'task_id': 'task_id',
        'tmss_case_uri': 'tmss_case_uri'
    }

    def __init__(self, project_id=None, task_id=None, tmss_case_uri=None):
        r"""ListTestCaseScriptDetailRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param task_id: 执行任务id
        :type task_id: str
        :param tmss_case_uri: TMSS用例uri
        :type tmss_case_uri: str
        """
        
        

        self._project_id = None
        self._task_id = None
        self._tmss_case_uri = None
        self.discriminator = None

        self.project_id = project_id
        if task_id is not None:
            self.task_id = task_id
        self.tmss_case_uri = tmss_case_uri

    @property
    def project_id(self):
        r"""Gets the project_id of this ListTestCaseScriptDetailRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this ListTestCaseScriptDetailRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListTestCaseScriptDetailRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this ListTestCaseScriptDetailRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ListTestCaseScriptDetailRequest.

        执行任务id

        :return: The task_id of this ListTestCaseScriptDetailRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListTestCaseScriptDetailRequest.

        执行任务id

        :param task_id: The task_id of this ListTestCaseScriptDetailRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def tmss_case_uri(self):
        r"""Gets the tmss_case_uri of this ListTestCaseScriptDetailRequest.

        TMSS用例uri

        :return: The tmss_case_uri of this ListTestCaseScriptDetailRequest.
        :rtype: str
        """
        return self._tmss_case_uri

    @tmss_case_uri.setter
    def tmss_case_uri(self, tmss_case_uri):
        r"""Sets the tmss_case_uri of this ListTestCaseScriptDetailRequest.

        TMSS用例uri

        :param tmss_case_uri: The tmss_case_uri of this ListTestCaseScriptDetailRequest.
        :type tmss_case_uri: str
        """
        self._tmss_case_uri = tmss_case_uri

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
        if not isinstance(other, ListTestCaseScriptDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
