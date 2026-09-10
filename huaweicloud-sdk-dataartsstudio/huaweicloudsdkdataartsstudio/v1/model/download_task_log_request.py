# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadTaskLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'x_project_id': 'str',
        'task_id': 'str',
        'path': 'str',
        'range': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'task_id': 'task_id',
        'path': 'path',
        'range': 'range'
    }

    def __init__(self, workspace=None, x_project_id=None, task_id=None, path=None, range=None):
        r"""DownloadTaskLogRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param task_id: 作业任务ID。
        :type task_id: str
        :param path: 需要下载内容的文件路径。
        :type path: str
        :param range: 下载文件内容范围，如0-100，表示下载0-100字节范围的内容。
        :type range: str
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._task_id = None
        self._path = None
        self._range = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.task_id = task_id
        self.path = path
        if range is not None:
            self.range = range

    @property
    def workspace(self):
        r"""Gets the workspace of this DownloadTaskLogRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this DownloadTaskLogRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this DownloadTaskLogRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this DownloadTaskLogRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this DownloadTaskLogRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this DownloadTaskLogRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this DownloadTaskLogRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this DownloadTaskLogRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def task_id(self):
        r"""Gets the task_id of this DownloadTaskLogRequest.

        作业任务ID。

        :return: The task_id of this DownloadTaskLogRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this DownloadTaskLogRequest.

        作业任务ID。

        :param task_id: The task_id of this DownloadTaskLogRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def path(self):
        r"""Gets the path of this DownloadTaskLogRequest.

        需要下载内容的文件路径。

        :return: The path of this DownloadTaskLogRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this DownloadTaskLogRequest.

        需要下载内容的文件路径。

        :param path: The path of this DownloadTaskLogRequest.
        :type path: str
        """
        self._path = path

    @property
    def range(self):
        r"""Gets the range of this DownloadTaskLogRequest.

        下载文件内容范围，如0-100，表示下载0-100字节范围的内容。

        :return: The range of this DownloadTaskLogRequest.
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        r"""Sets the range of this DownloadTaskLogRequest.

        下载文件内容范围，如0-100，表示下载0-100字节范围的内容。

        :param range: The range of this DownloadTaskLogRequest.
        :type range: str
        """
        self._range = range

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DownloadTaskLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
