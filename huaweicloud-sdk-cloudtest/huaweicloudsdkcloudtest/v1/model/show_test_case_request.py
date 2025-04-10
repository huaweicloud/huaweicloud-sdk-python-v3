# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTestCaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'testcase_id': 'str',
        'version_uri': 'str',
        'project_uuid': 'str',
        'task_uri': 'str',
        'refresh': 'bool',
        'is_recycle': 'bool'
    }

    attribute_map = {
        'testcase_id': 'testcase_id',
        'version_uri': 'version_uri',
        'project_uuid': 'project_uuid',
        'task_uri': 'task_uri',
        'refresh': 'refresh',
        'is_recycle': 'is_recycle'
    }

    def __init__(self, testcase_id=None, version_uri=None, project_uuid=None, task_uri=None, refresh=None, is_recycle=None):
        r"""ShowTestCaseRequest

        The model defined in huaweicloud sdk

        :param testcase_id: 用例id
        :type testcase_id: str
        :param version_uri: 分支uri
        :type version_uri: str
        :param project_uuid: 项目id
        :type project_uuid: str
        :param task_uri: 任务
        :type task_uri: str
        :param refresh: 是否刷新缓存
        :type refresh: bool
        :param is_recycle: 是否回收站资源
        :type is_recycle: bool
        """
        
        

        self._testcase_id = None
        self._version_uri = None
        self._project_uuid = None
        self._task_uri = None
        self._refresh = None
        self._is_recycle = None
        self.discriminator = None

        self.testcase_id = testcase_id
        if version_uri is not None:
            self.version_uri = version_uri
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if task_uri is not None:
            self.task_uri = task_uri
        if refresh is not None:
            self.refresh = refresh
        if is_recycle is not None:
            self.is_recycle = is_recycle

    @property
    def testcase_id(self):
        r"""Gets the testcase_id of this ShowTestCaseRequest.

        用例id

        :return: The testcase_id of this ShowTestCaseRequest.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        r"""Sets the testcase_id of this ShowTestCaseRequest.

        用例id

        :param testcase_id: The testcase_id of this ShowTestCaseRequest.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    @property
    def version_uri(self):
        r"""Gets the version_uri of this ShowTestCaseRequest.

        分支uri

        :return: The version_uri of this ShowTestCaseRequest.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this ShowTestCaseRequest.

        分支uri

        :param version_uri: The version_uri of this ShowTestCaseRequest.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ShowTestCaseRequest.

        项目id

        :return: The project_uuid of this ShowTestCaseRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ShowTestCaseRequest.

        项目id

        :param project_uuid: The project_uuid of this ShowTestCaseRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def task_uri(self):
        r"""Gets the task_uri of this ShowTestCaseRequest.

        任务

        :return: The task_uri of this ShowTestCaseRequest.
        :rtype: str
        """
        return self._task_uri

    @task_uri.setter
    def task_uri(self, task_uri):
        r"""Sets the task_uri of this ShowTestCaseRequest.

        任务

        :param task_uri: The task_uri of this ShowTestCaseRequest.
        :type task_uri: str
        """
        self._task_uri = task_uri

    @property
    def refresh(self):
        r"""Gets the refresh of this ShowTestCaseRequest.

        是否刷新缓存

        :return: The refresh of this ShowTestCaseRequest.
        :rtype: bool
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        r"""Sets the refresh of this ShowTestCaseRequest.

        是否刷新缓存

        :param refresh: The refresh of this ShowTestCaseRequest.
        :type refresh: bool
        """
        self._refresh = refresh

    @property
    def is_recycle(self):
        r"""Gets the is_recycle of this ShowTestCaseRequest.

        是否回收站资源

        :return: The is_recycle of this ShowTestCaseRequest.
        :rtype: bool
        """
        return self._is_recycle

    @is_recycle.setter
    def is_recycle(self, is_recycle):
        r"""Sets the is_recycle of this ShowTestCaseRequest.

        是否回收站资源

        :param is_recycle: The is_recycle of this ShowTestCaseRequest.
        :type is_recycle: bool
        """
        self._is_recycle = is_recycle

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
        if not isinstance(other, ShowTestCaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
