# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNextflowWorkflowResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'workflow_file': 'str',
        'workflow_file_url': 'str',
        'main_file': 'str',
        'params_file': 'str',
        'params': 'list[NextflowParamsDto]',
        'create_time': 'str',
        'update_time': 'str',
        'source_project_name': 'str',
        'source_resource_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'labels': 'labels',
        'workflow_file': 'workflow_file',
        'workflow_file_url': 'workflow_file_url',
        'main_file': 'main_file',
        'params_file': 'params_file',
        'params': 'params',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'source_project_name': 'source_project_name',
        'source_resource_id': 'source_resource_id'
    }

    def __init__(self, id=None, name=None, description=None, labels=None, workflow_file=None, workflow_file_url=None, main_file=None, params_file=None, params=None, create_time=None, update_time=None, source_project_name=None, source_resource_id=None):
        r"""ShowNextflowWorkflowResponse

        The model defined in huaweicloud sdk

        :param id: 流程id
        :type id: str
        :param name: 流程名称
        :type name: str
        :param description: 流程描述
        :type description: str
        :param labels: 流程标签
        :type labels: list[str]
        :param workflow_file: 流程的文件名
        :type workflow_file: str
        :param workflow_file_url: 流程的文件名下载地址
        :type workflow_file_url: str
        :param main_file: 主文件名
        :type main_file: str
        :param params_file: 用户上传时使用的参数文件名
        :type params_file: str
        :param params: 流程参数列表
        :type params: list[:class:`huaweicloudsdkeihealth.v1.NextflowParamsDto`]
        :param create_time: 流程的创建时间
        :type create_time: str
        :param update_time: 流程的更新时间
        :type update_time: str
        :param source_project_name: 源项目名称
        :type source_project_name: str
        :param source_resource_id: 源资源id
        :type source_resource_id: str
        """
        
        super(ShowNextflowWorkflowResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._labels = None
        self._workflow_file = None
        self._workflow_file_url = None
        self._main_file = None
        self._params_file = None
        self._params = None
        self._create_time = None
        self._update_time = None
        self._source_project_name = None
        self._source_resource_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if workflow_file is not None:
            self.workflow_file = workflow_file
        if workflow_file_url is not None:
            self.workflow_file_url = workflow_file_url
        if main_file is not None:
            self.main_file = main_file
        if params_file is not None:
            self.params_file = params_file
        if params is not None:
            self.params = params
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if source_project_name is not None:
            self.source_project_name = source_project_name
        if source_resource_id is not None:
            self.source_resource_id = source_resource_id

    @property
    def id(self):
        r"""Gets the id of this ShowNextflowWorkflowResponse.

        流程id

        :return: The id of this ShowNextflowWorkflowResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowNextflowWorkflowResponse.

        流程id

        :param id: The id of this ShowNextflowWorkflowResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowNextflowWorkflowResponse.

        流程名称

        :return: The name of this ShowNextflowWorkflowResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowNextflowWorkflowResponse.

        流程名称

        :param name: The name of this ShowNextflowWorkflowResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowNextflowWorkflowResponse.

        流程描述

        :return: The description of this ShowNextflowWorkflowResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowNextflowWorkflowResponse.

        流程描述

        :param description: The description of this ShowNextflowWorkflowResponse.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        r"""Gets the labels of this ShowNextflowWorkflowResponse.

        流程标签

        :return: The labels of this ShowNextflowWorkflowResponse.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ShowNextflowWorkflowResponse.

        流程标签

        :param labels: The labels of this ShowNextflowWorkflowResponse.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def workflow_file(self):
        r"""Gets the workflow_file of this ShowNextflowWorkflowResponse.

        流程的文件名

        :return: The workflow_file of this ShowNextflowWorkflowResponse.
        :rtype: str
        """
        return self._workflow_file

    @workflow_file.setter
    def workflow_file(self, workflow_file):
        r"""Sets the workflow_file of this ShowNextflowWorkflowResponse.

        流程的文件名

        :param workflow_file: The workflow_file of this ShowNextflowWorkflowResponse.
        :type workflow_file: str
        """
        self._workflow_file = workflow_file

    @property
    def workflow_file_url(self):
        r"""Gets the workflow_file_url of this ShowNextflowWorkflowResponse.

        流程的文件名下载地址

        :return: The workflow_file_url of this ShowNextflowWorkflowResponse.
        :rtype: str
        """
        return self._workflow_file_url

    @workflow_file_url.setter
    def workflow_file_url(self, workflow_file_url):
        r"""Sets the workflow_file_url of this ShowNextflowWorkflowResponse.

        流程的文件名下载地址

        :param workflow_file_url: The workflow_file_url of this ShowNextflowWorkflowResponse.
        :type workflow_file_url: str
        """
        self._workflow_file_url = workflow_file_url

    @property
    def main_file(self):
        r"""Gets the main_file of this ShowNextflowWorkflowResponse.

        主文件名

        :return: The main_file of this ShowNextflowWorkflowResponse.
        :rtype: str
        """
        return self._main_file

    @main_file.setter
    def main_file(self, main_file):
        r"""Sets the main_file of this ShowNextflowWorkflowResponse.

        主文件名

        :param main_file: The main_file of this ShowNextflowWorkflowResponse.
        :type main_file: str
        """
        self._main_file = main_file

    @property
    def params_file(self):
        r"""Gets the params_file of this ShowNextflowWorkflowResponse.

        用户上传时使用的参数文件名

        :return: The params_file of this ShowNextflowWorkflowResponse.
        :rtype: str
        """
        return self._params_file

    @params_file.setter
    def params_file(self, params_file):
        r"""Sets the params_file of this ShowNextflowWorkflowResponse.

        用户上传时使用的参数文件名

        :param params_file: The params_file of this ShowNextflowWorkflowResponse.
        :type params_file: str
        """
        self._params_file = params_file

    @property
    def params(self):
        r"""Gets the params of this ShowNextflowWorkflowResponse.

        流程参数列表

        :return: The params of this ShowNextflowWorkflowResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.NextflowParamsDto`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this ShowNextflowWorkflowResponse.

        流程参数列表

        :param params: The params of this ShowNextflowWorkflowResponse.
        :type params: list[:class:`huaweicloudsdkeihealth.v1.NextflowParamsDto`]
        """
        self._params = params

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowNextflowWorkflowResponse.

        流程的创建时间

        :return: The create_time of this ShowNextflowWorkflowResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowNextflowWorkflowResponse.

        流程的创建时间

        :param create_time: The create_time of this ShowNextflowWorkflowResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowNextflowWorkflowResponse.

        流程的更新时间

        :return: The update_time of this ShowNextflowWorkflowResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowNextflowWorkflowResponse.

        流程的更新时间

        :param update_time: The update_time of this ShowNextflowWorkflowResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def source_project_name(self):
        r"""Gets the source_project_name of this ShowNextflowWorkflowResponse.

        源项目名称

        :return: The source_project_name of this ShowNextflowWorkflowResponse.
        :rtype: str
        """
        return self._source_project_name

    @source_project_name.setter
    def source_project_name(self, source_project_name):
        r"""Sets the source_project_name of this ShowNextflowWorkflowResponse.

        源项目名称

        :param source_project_name: The source_project_name of this ShowNextflowWorkflowResponse.
        :type source_project_name: str
        """
        self._source_project_name = source_project_name

    @property
    def source_resource_id(self):
        r"""Gets the source_resource_id of this ShowNextflowWorkflowResponse.

        源资源id

        :return: The source_resource_id of this ShowNextflowWorkflowResponse.
        :rtype: str
        """
        return self._source_resource_id

    @source_resource_id.setter
    def source_resource_id(self, source_resource_id):
        r"""Sets the source_resource_id of this ShowNextflowWorkflowResponse.

        源资源id

        :param source_resource_id: The source_resource_id of this ShowNextflowWorkflowResponse.
        :type source_resource_id: str
        """
        self._source_resource_id = source_resource_id

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
        if not isinstance(other, ShowNextflowWorkflowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
