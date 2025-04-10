# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFunctionAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'last_modified_time': 'int',
        'stack_resources': 'StackResource',
        'status': 'str',
        'stack_name': 'str',
        'stack_id': 'str',
        'repo_name': 'str',
        'description': 'str',
        'repo': 'RepoInfo',
        'pipeline_id': 'str',
        'project_id': 'str',
        'apig_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'last_modified_time': 'last_modified_time',
        'stack_resources': 'stack_resources',
        'status': 'status',
        'stack_name': 'stack_name',
        'stack_id': 'stack_id',
        'repo_name': 'repo_name',
        'description': 'description',
        'repo': 'repo',
        'pipeline_id': 'pipeline_id',
        'project_id': 'project_id',
        'apig_url': 'apig_url'
    }

    def __init__(self, name=None, last_modified_time=None, stack_resources=None, status=None, stack_name=None, stack_id=None, repo_name=None, description=None, repo=None, pipeline_id=None, project_id=None, apig_url=None):
        r"""ShowFunctionAppResponse

        The model defined in huaweicloud sdk

        :param name: 应用名称
        :type name: str
        :param last_modified_time: 最后修改时间
        :type last_modified_time: int
        :param stack_resources: 
        :type stack_resources: :class:`huaweicloudsdkfunctiongraph.v2.StackResource`
        :param status: 应用状态
        :type status: str
        :param stack_name: 资源栈名称
        :type stack_name: str
        :param stack_id: 资源栈id
        :type stack_id: str
        :param repo_name: 存储库名称
        :type repo_name: str
        :param description: 应用描述
        :type description: str
        :param repo: 
        :type repo: :class:`huaweicloudsdkfunctiongraph.v2.RepoInfo`
        :param pipeline_id: 管道id
        :type pipeline_id: str
        :param project_id: 项目id
        :type project_id: str
        :param apig_url: 调用URL
        :type apig_url: str
        """
        
        super(ShowFunctionAppResponse, self).__init__()

        self._name = None
        self._last_modified_time = None
        self._stack_resources = None
        self._status = None
        self._stack_name = None
        self._stack_id = None
        self._repo_name = None
        self._description = None
        self._repo = None
        self._pipeline_id = None
        self._project_id = None
        self._apig_url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if stack_resources is not None:
            self.stack_resources = stack_resources
        if status is not None:
            self.status = status
        if stack_name is not None:
            self.stack_name = stack_name
        if stack_id is not None:
            self.stack_id = stack_id
        if repo_name is not None:
            self.repo_name = repo_name
        if description is not None:
            self.description = description
        if repo is not None:
            self.repo = repo
        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if project_id is not None:
            self.project_id = project_id
        if apig_url is not None:
            self.apig_url = apig_url

    @property
    def name(self):
        r"""Gets the name of this ShowFunctionAppResponse.

        应用名称

        :return: The name of this ShowFunctionAppResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowFunctionAppResponse.

        应用名称

        :param name: The name of this ShowFunctionAppResponse.
        :type name: str
        """
        self._name = name

    @property
    def last_modified_time(self):
        r"""Gets the last_modified_time of this ShowFunctionAppResponse.

        最后修改时间

        :return: The last_modified_time of this ShowFunctionAppResponse.
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        r"""Sets the last_modified_time of this ShowFunctionAppResponse.

        最后修改时间

        :param last_modified_time: The last_modified_time of this ShowFunctionAppResponse.
        :type last_modified_time: int
        """
        self._last_modified_time = last_modified_time

    @property
    def stack_resources(self):
        r"""Gets the stack_resources of this ShowFunctionAppResponse.

        :return: The stack_resources of this ShowFunctionAppResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.StackResource`
        """
        return self._stack_resources

    @stack_resources.setter
    def stack_resources(self, stack_resources):
        r"""Sets the stack_resources of this ShowFunctionAppResponse.

        :param stack_resources: The stack_resources of this ShowFunctionAppResponse.
        :type stack_resources: :class:`huaweicloudsdkfunctiongraph.v2.StackResource`
        """
        self._stack_resources = stack_resources

    @property
    def status(self):
        r"""Gets the status of this ShowFunctionAppResponse.

        应用状态

        :return: The status of this ShowFunctionAppResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowFunctionAppResponse.

        应用状态

        :param status: The status of this ShowFunctionAppResponse.
        :type status: str
        """
        self._status = status

    @property
    def stack_name(self):
        r"""Gets the stack_name of this ShowFunctionAppResponse.

        资源栈名称

        :return: The stack_name of this ShowFunctionAppResponse.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        r"""Sets the stack_name of this ShowFunctionAppResponse.

        资源栈名称

        :param stack_name: The stack_name of this ShowFunctionAppResponse.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def stack_id(self):
        r"""Gets the stack_id of this ShowFunctionAppResponse.

        资源栈id

        :return: The stack_id of this ShowFunctionAppResponse.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        r"""Sets the stack_id of this ShowFunctionAppResponse.

        资源栈id

        :param stack_id: The stack_id of this ShowFunctionAppResponse.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def repo_name(self):
        r"""Gets the repo_name of this ShowFunctionAppResponse.

        存储库名称

        :return: The repo_name of this ShowFunctionAppResponse.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this ShowFunctionAppResponse.

        存储库名称

        :param repo_name: The repo_name of this ShowFunctionAppResponse.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def description(self):
        r"""Gets the description of this ShowFunctionAppResponse.

        应用描述

        :return: The description of this ShowFunctionAppResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowFunctionAppResponse.

        应用描述

        :param description: The description of this ShowFunctionAppResponse.
        :type description: str
        """
        self._description = description

    @property
    def repo(self):
        r"""Gets the repo of this ShowFunctionAppResponse.

        :return: The repo of this ShowFunctionAppResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.RepoInfo`
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        r"""Sets the repo of this ShowFunctionAppResponse.

        :param repo: The repo of this ShowFunctionAppResponse.
        :type repo: :class:`huaweicloudsdkfunctiongraph.v2.RepoInfo`
        """
        self._repo = repo

    @property
    def pipeline_id(self):
        r"""Gets the pipeline_id of this ShowFunctionAppResponse.

        管道id

        :return: The pipeline_id of this ShowFunctionAppResponse.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        r"""Sets the pipeline_id of this ShowFunctionAppResponse.

        管道id

        :param pipeline_id: The pipeline_id of this ShowFunctionAppResponse.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowFunctionAppResponse.

        项目id

        :return: The project_id of this ShowFunctionAppResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowFunctionAppResponse.

        项目id

        :param project_id: The project_id of this ShowFunctionAppResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def apig_url(self):
        r"""Gets the apig_url of this ShowFunctionAppResponse.

        调用URL

        :return: The apig_url of this ShowFunctionAppResponse.
        :rtype: str
        """
        return self._apig_url

    @apig_url.setter
    def apig_url(self, apig_url):
        r"""Sets the apig_url of this ShowFunctionAppResponse.

        调用URL

        :param apig_url: The apig_url of this ShowFunctionAppResponse.
        :type apig_url: str
        """
        self._apig_url = apig_url

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
        if not isinstance(other, ShowFunctionAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
