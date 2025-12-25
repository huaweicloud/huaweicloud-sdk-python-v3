# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EsMonitorBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'dataspace_id': 'str',
        'pipe_id': 'str',
        'storage_bytes': 'int',
        'storage_count': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'dataspace_id': 'dataspace_id',
        'pipe_id': 'pipe_id',
        'storage_bytes': 'storage_bytes',
        'storage_count': 'storage_count'
    }

    def __init__(self, domain_id=None, project_id=None, workspace_id=None, dataspace_id=None, pipe_id=None, storage_bytes=None, storage_count=None):
        r"""EsMonitorBody

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param pipe_id: 管道ID
        :type pipe_id: str
        :param storage_bytes: 存储字节数
        :type storage_bytes: int
        :param storage_count: 存储条数
        :type storage_count: int
        """
        
        

        self._domain_id = None
        self._project_id = None
        self._workspace_id = None
        self._dataspace_id = None
        self._pipe_id = None
        self._storage_bytes = None
        self._storage_count = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if dataspace_id is not None:
            self.dataspace_id = dataspace_id
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if storage_bytes is not None:
            self.storage_bytes = storage_bytes
        if storage_count is not None:
            self.storage_count = storage_count

    @property
    def domain_id(self):
        r"""Gets the domain_id of this EsMonitorBody.

        租户ID

        :return: The domain_id of this EsMonitorBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this EsMonitorBody.

        租户ID

        :param domain_id: The domain_id of this EsMonitorBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this EsMonitorBody.

        项目ID

        :return: The project_id of this EsMonitorBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this EsMonitorBody.

        项目ID

        :param project_id: The project_id of this EsMonitorBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this EsMonitorBody.

        工作空间ID

        :return: The workspace_id of this EsMonitorBody.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this EsMonitorBody.

        工作空间ID

        :param workspace_id: The workspace_id of this EsMonitorBody.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this EsMonitorBody.

        数据空间ID

        :return: The dataspace_id of this EsMonitorBody.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this EsMonitorBody.

        数据空间ID

        :param dataspace_id: The dataspace_id of this EsMonitorBody.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this EsMonitorBody.

        管道ID

        :return: The pipe_id of this EsMonitorBody.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this EsMonitorBody.

        管道ID

        :param pipe_id: The pipe_id of this EsMonitorBody.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def storage_bytes(self):
        r"""Gets the storage_bytes of this EsMonitorBody.

        存储字节数

        :return: The storage_bytes of this EsMonitorBody.
        :rtype: int
        """
        return self._storage_bytes

    @storage_bytes.setter
    def storage_bytes(self, storage_bytes):
        r"""Sets the storage_bytes of this EsMonitorBody.

        存储字节数

        :param storage_bytes: The storage_bytes of this EsMonitorBody.
        :type storage_bytes: int
        """
        self._storage_bytes = storage_bytes

    @property
    def storage_count(self):
        r"""Gets the storage_count of this EsMonitorBody.

        存储条数

        :return: The storage_count of this EsMonitorBody.
        :rtype: int
        """
        return self._storage_count

    @storage_count.setter
    def storage_count(self, storage_count):
        r"""Sets the storage_count of this EsMonitorBody.

        存储条数

        :param storage_count: The storage_count of this EsMonitorBody.
        :type storage_count: int
        """
        self._storage_count = storage_count

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
        if not isinstance(other, EsMonitorBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
