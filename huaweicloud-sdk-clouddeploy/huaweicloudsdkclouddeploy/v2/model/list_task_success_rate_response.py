# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskSuccessRateResponse(SdkResponse):

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
        'project_name': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'tasks_success_rate': 'list[TaskSuccessRate]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'project_name': 'project_name',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'tasks_success_rate': 'tasks_success_rate'
    }

    def __init__(self, project_id=None, project_name=None, start_date=None, end_date=None, tasks_success_rate=None):
        """ListTaskSuccessRateResponse

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param start_date: 部署应用开始时间范围的左边界（包含），格式yyyy-MM-dd
        :type start_date: str
        :param end_date: 部署应用开始时间范围的右边界（包含），格式yyyy-MM-dd 。最大时间范围为1年。
        :type end_date: str
        :param tasks_success_rate: 应用的成功率列表
        :type tasks_success_rate: list[:class:`huaweicloudsdkclouddeploy.v2.TaskSuccessRate`]
        """
        
        super(ListTaskSuccessRateResponse, self).__init__()

        self._project_id = None
        self._project_name = None
        self._start_date = None
        self._end_date = None
        self._tasks_success_rate = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if tasks_success_rate is not None:
            self.tasks_success_rate = tasks_success_rate

    @property
    def project_id(self):
        """Gets the project_id of this ListTaskSuccessRateResponse.

        项目id

        :return: The project_id of this ListTaskSuccessRateResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListTaskSuccessRateResponse.

        项目id

        :param project_id: The project_id of this ListTaskSuccessRateResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ListTaskSuccessRateResponse.

        项目名称

        :return: The project_name of this ListTaskSuccessRateResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ListTaskSuccessRateResponse.

        项目名称

        :param project_name: The project_name of this ListTaskSuccessRateResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def start_date(self):
        """Gets the start_date of this ListTaskSuccessRateResponse.

        部署应用开始时间范围的左边界（包含），格式yyyy-MM-dd

        :return: The start_date of this ListTaskSuccessRateResponse.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ListTaskSuccessRateResponse.

        部署应用开始时间范围的左边界（包含），格式yyyy-MM-dd

        :param start_date: The start_date of this ListTaskSuccessRateResponse.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ListTaskSuccessRateResponse.

        部署应用开始时间范围的右边界（包含），格式yyyy-MM-dd 。最大时间范围为1年。

        :return: The end_date of this ListTaskSuccessRateResponse.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ListTaskSuccessRateResponse.

        部署应用开始时间范围的右边界（包含），格式yyyy-MM-dd 。最大时间范围为1年。

        :param end_date: The end_date of this ListTaskSuccessRateResponse.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def tasks_success_rate(self):
        """Gets the tasks_success_rate of this ListTaskSuccessRateResponse.

        应用的成功率列表

        :return: The tasks_success_rate of this ListTaskSuccessRateResponse.
        :rtype: list[:class:`huaweicloudsdkclouddeploy.v2.TaskSuccessRate`]
        """
        return self._tasks_success_rate

    @tasks_success_rate.setter
    def tasks_success_rate(self, tasks_success_rate):
        """Sets the tasks_success_rate of this ListTaskSuccessRateResponse.

        应用的成功率列表

        :param tasks_success_rate: The tasks_success_rate of this ListTaskSuccessRateResponse.
        :type tasks_success_rate: list[:class:`huaweicloudsdkclouddeploy.v2.TaskSuccessRate`]
        """
        self._tasks_success_rate = tasks_success_rate

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
        if not isinstance(other, ListTaskSuccessRateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
