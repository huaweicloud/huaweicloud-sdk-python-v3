# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPlaybookMonitorsRequest:

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
        'workspace_id': 'str',
        'playbook_id': 'str',
        'start_time': 'str',
        'version_query_type': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'playbook_id': 'playbook_id',
        'start_time': 'start_time',
        'version_query_type': 'version_query_type',
        'end_time': 'end_time'
    }

    def __init__(self, project_id=None, workspace_id=None, playbook_id=None, start_time=None, version_query_type=None, end_time=None):
        r"""ShowPlaybookMonitorsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param playbook_id: 剧本ID
        :type playbook_id: str
        :param start_time: 开始时间。格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。例如：2021-01-30T23:00:00Z+0800。时区信息为剧本实例产生的时区，无法解析时区的时间，默认时区填东八区。
        :type start_time: str
        :param version_query_type: 统计剧本版本类型（ALL:全部，VALID:有效的，DELETED:已删除）
        :type version_query_type: str
        :param end_time: 结束时间。格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。例如：2021-01-30T23:00:00Z+0800。时区信息为剧本实例产生的时区，无法解析时区的时间，默认时区填东八区。
        :type end_time: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._playbook_id = None
        self._start_time = None
        self._version_query_type = None
        self._end_time = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.playbook_id = playbook_id
        self.start_time = start_time
        self.version_query_type = version_query_type
        self.end_time = end_time

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowPlaybookMonitorsRequest.

        项目ID

        :return: The project_id of this ShowPlaybookMonitorsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowPlaybookMonitorsRequest.

        项目ID

        :param project_id: The project_id of this ShowPlaybookMonitorsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowPlaybookMonitorsRequest.

        工作空间ID

        :return: The workspace_id of this ShowPlaybookMonitorsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowPlaybookMonitorsRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ShowPlaybookMonitorsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def playbook_id(self):
        r"""Gets the playbook_id of this ShowPlaybookMonitorsRequest.

        剧本ID

        :return: The playbook_id of this ShowPlaybookMonitorsRequest.
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        r"""Sets the playbook_id of this ShowPlaybookMonitorsRequest.

        剧本ID

        :param playbook_id: The playbook_id of this ShowPlaybookMonitorsRequest.
        :type playbook_id: str
        """
        self._playbook_id = playbook_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowPlaybookMonitorsRequest.

        开始时间。格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。例如：2021-01-30T23:00:00Z+0800。时区信息为剧本实例产生的时区，无法解析时区的时间，默认时区填东八区。

        :return: The start_time of this ShowPlaybookMonitorsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowPlaybookMonitorsRequest.

        开始时间。格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。例如：2021-01-30T23:00:00Z+0800。时区信息为剧本实例产生的时区，无法解析时区的时间，默认时区填东八区。

        :param start_time: The start_time of this ShowPlaybookMonitorsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def version_query_type(self):
        r"""Gets the version_query_type of this ShowPlaybookMonitorsRequest.

        统计剧本版本类型（ALL:全部，VALID:有效的，DELETED:已删除）

        :return: The version_query_type of this ShowPlaybookMonitorsRequest.
        :rtype: str
        """
        return self._version_query_type

    @version_query_type.setter
    def version_query_type(self, version_query_type):
        r"""Sets the version_query_type of this ShowPlaybookMonitorsRequest.

        统计剧本版本类型（ALL:全部，VALID:有效的，DELETED:已删除）

        :param version_query_type: The version_query_type of this ShowPlaybookMonitorsRequest.
        :type version_query_type: str
        """
        self._version_query_type = version_query_type

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowPlaybookMonitorsRequest.

        结束时间。格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。例如：2021-01-30T23:00:00Z+0800。时区信息为剧本实例产生的时区，无法解析时区的时间，默认时区填东八区。

        :return: The end_time of this ShowPlaybookMonitorsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowPlaybookMonitorsRequest.

        结束时间。格式ISO8601：YYYY-MM-DDTHH:mm:ss.ms+timezone。例如：2021-01-30T23:00:00Z+0800。时区信息为剧本实例产生的时区，无法解析时区的时间，默认时区填东八区。

        :param end_time: The end_time of this ShowPlaybookMonitorsRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowPlaybookMonitorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
