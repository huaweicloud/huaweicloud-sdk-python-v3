# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShipperResponseBodyDataShipperSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_type': 'int',
        'dataspace': 'str',
        'dataspace_name': 'str',
        'id': 'int',
        'identity': 'str',
        'pipe': 'str',
        'pipe_name': 'str',
        'region': 'str',
        'type': 'int',
        'workspace': 'str',
        'workspace_name': 'str'
    }

    attribute_map = {
        'data_type': 'data_type',
        'dataspace': 'dataspace',
        'dataspace_name': 'dataspace_name',
        'id': 'id',
        'identity': 'identity',
        'pipe': 'pipe',
        'pipe_name': 'pipe_name',
        'region': 'region',
        'type': 'type',
        'workspace': 'workspace',
        'workspace_name': 'workspace_name'
    }

    def __init__(self, data_type=None, dataspace=None, dataspace_name=None, id=None, identity=None, pipe=None, pipe_name=None, region=None, type=None, workspace=None, workspace_name=None):
        r"""ShowShipperResponseBodyDataShipperSource

        The model defined in huaweicloud sdk

        :param data_type: 数据类型
        :type data_type: int
        :param dataspace: 数据空间
        :type dataspace: str
        :param dataspace_name: 数据空间名称
        :type dataspace_name: str
        :param id: 源ID
        :type id: int
        :param identity: 标识
        :type identity: str
        :param pipe: 管道ID
        :type pipe: str
        :param pipe_name: 管道名称
        :type pipe_name: str
        :param region: 区域
        :type region: str
        :param type: 类型
        :type type: int
        :param workspace: 工作空间ID
        :type workspace: str
        :param workspace_name: 工作空间名称
        :type workspace_name: str
        """
        
        

        self._data_type = None
        self._dataspace = None
        self._dataspace_name = None
        self._id = None
        self._identity = None
        self._pipe = None
        self._pipe_name = None
        self._region = None
        self._type = None
        self._workspace = None
        self._workspace_name = None
        self.discriminator = None

        if data_type is not None:
            self.data_type = data_type
        if dataspace is not None:
            self.dataspace = dataspace
        if dataspace_name is not None:
            self.dataspace_name = dataspace_name
        if id is not None:
            self.id = id
        if identity is not None:
            self.identity = identity
        if pipe is not None:
            self.pipe = pipe
        if pipe_name is not None:
            self.pipe_name = pipe_name
        if region is not None:
            self.region = region
        if type is not None:
            self.type = type
        if workspace is not None:
            self.workspace = workspace
        if workspace_name is not None:
            self.workspace_name = workspace_name

    @property
    def data_type(self):
        r"""Gets the data_type of this ShowShipperResponseBodyDataShipperSource.

        数据类型

        :return: The data_type of this ShowShipperResponseBodyDataShipperSource.
        :rtype: int
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this ShowShipperResponseBodyDataShipperSource.

        数据类型

        :param data_type: The data_type of this ShowShipperResponseBodyDataShipperSource.
        :type data_type: int
        """
        self._data_type = data_type

    @property
    def dataspace(self):
        r"""Gets the dataspace of this ShowShipperResponseBodyDataShipperSource.

        数据空间

        :return: The dataspace of this ShowShipperResponseBodyDataShipperSource.
        :rtype: str
        """
        return self._dataspace

    @dataspace.setter
    def dataspace(self, dataspace):
        r"""Sets the dataspace of this ShowShipperResponseBodyDataShipperSource.

        数据空间

        :param dataspace: The dataspace of this ShowShipperResponseBodyDataShipperSource.
        :type dataspace: str
        """
        self._dataspace = dataspace

    @property
    def dataspace_name(self):
        r"""Gets the dataspace_name of this ShowShipperResponseBodyDataShipperSource.

        数据空间名称

        :return: The dataspace_name of this ShowShipperResponseBodyDataShipperSource.
        :rtype: str
        """
        return self._dataspace_name

    @dataspace_name.setter
    def dataspace_name(self, dataspace_name):
        r"""Sets the dataspace_name of this ShowShipperResponseBodyDataShipperSource.

        数据空间名称

        :param dataspace_name: The dataspace_name of this ShowShipperResponseBodyDataShipperSource.
        :type dataspace_name: str
        """
        self._dataspace_name = dataspace_name

    @property
    def id(self):
        r"""Gets the id of this ShowShipperResponseBodyDataShipperSource.

        源ID

        :return: The id of this ShowShipperResponseBodyDataShipperSource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowShipperResponseBodyDataShipperSource.

        源ID

        :param id: The id of this ShowShipperResponseBodyDataShipperSource.
        :type id: int
        """
        self._id = id

    @property
    def identity(self):
        r"""Gets the identity of this ShowShipperResponseBodyDataShipperSource.

        标识

        :return: The identity of this ShowShipperResponseBodyDataShipperSource.
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        r"""Sets the identity of this ShowShipperResponseBodyDataShipperSource.

        标识

        :param identity: The identity of this ShowShipperResponseBodyDataShipperSource.
        :type identity: str
        """
        self._identity = identity

    @property
    def pipe(self):
        r"""Gets the pipe of this ShowShipperResponseBodyDataShipperSource.

        管道ID

        :return: The pipe of this ShowShipperResponseBodyDataShipperSource.
        :rtype: str
        """
        return self._pipe

    @pipe.setter
    def pipe(self, pipe):
        r"""Sets the pipe of this ShowShipperResponseBodyDataShipperSource.

        管道ID

        :param pipe: The pipe of this ShowShipperResponseBodyDataShipperSource.
        :type pipe: str
        """
        self._pipe = pipe

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this ShowShipperResponseBodyDataShipperSource.

        管道名称

        :return: The pipe_name of this ShowShipperResponseBodyDataShipperSource.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this ShowShipperResponseBodyDataShipperSource.

        管道名称

        :param pipe_name: The pipe_name of this ShowShipperResponseBodyDataShipperSource.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def region(self):
        r"""Gets the region of this ShowShipperResponseBodyDataShipperSource.

        区域

        :return: The region of this ShowShipperResponseBodyDataShipperSource.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowShipperResponseBodyDataShipperSource.

        区域

        :param region: The region of this ShowShipperResponseBodyDataShipperSource.
        :type region: str
        """
        self._region = region

    @property
    def type(self):
        r"""Gets the type of this ShowShipperResponseBodyDataShipperSource.

        类型

        :return: The type of this ShowShipperResponseBodyDataShipperSource.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowShipperResponseBodyDataShipperSource.

        类型

        :param type: The type of this ShowShipperResponseBodyDataShipperSource.
        :type type: int
        """
        self._type = type

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowShipperResponseBodyDataShipperSource.

        工作空间ID

        :return: The workspace of this ShowShipperResponseBodyDataShipperSource.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowShipperResponseBodyDataShipperSource.

        工作空间ID

        :param workspace: The workspace of this ShowShipperResponseBodyDataShipperSource.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def workspace_name(self):
        r"""Gets the workspace_name of this ShowShipperResponseBodyDataShipperSource.

        工作空间名称

        :return: The workspace_name of this ShowShipperResponseBodyDataShipperSource.
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        r"""Sets the workspace_name of this ShowShipperResponseBodyDataShipperSource.

        工作空间名称

        :param workspace_name: The workspace_name of this ShowShipperResponseBodyDataShipperSource.
        :type workspace_name: str
        """
        self._workspace_name = workspace_name

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
        if not isinstance(other, ShowShipperResponseBodyDataShipperSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
