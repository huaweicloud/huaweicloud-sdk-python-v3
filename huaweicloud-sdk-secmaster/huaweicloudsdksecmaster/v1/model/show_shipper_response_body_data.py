# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShipperResponseBodyData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'consumption_type': 'int',
        'create_time': 'int',
        'dataspace_id': 'str',
        'dataspace_name': 'str',
        'domain_id': 'str',
        'id': 'int',
        'pipe_id': 'str',
        'pipe_name': 'str',
        'project_id': 'str',
        'shipper_destination': 'ShowShipperResponseBodyDataShipperDestination',
        'shipper_id': 'str',
        'shipper_name': 'str',
        'shipper_source': 'ShowShipperResponseBodyDataShipperSource',
        'status': 'int',
        'update_time': 'int',
        'version': 'str',
        'workspace_id': 'str',
        'workspace_name': 'str'
    }

    attribute_map = {
        'consumption_type': 'consumption_type',
        'create_time': 'create_time',
        'dataspace_id': 'dataspace_id',
        'dataspace_name': 'dataspace_name',
        'domain_id': 'domain_id',
        'id': 'id',
        'pipe_id': 'pipe_id',
        'pipe_name': 'pipe_name',
        'project_id': 'project_id',
        'shipper_destination': 'shipper_destination',
        'shipper_id': 'shipper_id',
        'shipper_name': 'shipper_name',
        'shipper_source': 'shipper_source',
        'status': 'status',
        'update_time': 'update_time',
        'version': 'version',
        'workspace_id': 'workspace_id',
        'workspace_name': 'workspace_name'
    }

    def __init__(self, consumption_type=None, create_time=None, dataspace_id=None, dataspace_name=None, domain_id=None, id=None, pipe_id=None, pipe_name=None, project_id=None, shipper_destination=None, shipper_id=None, shipper_name=None, shipper_source=None, status=None, update_time=None, version=None, workspace_id=None, workspace_name=None):
        r"""ShowShipperResponseBodyData

        The model defined in huaweicloud sdk

        :param consumption_type: 消费类型
        :type consumption_type: int
        :param create_time: 创建时间（时间戳）
        :type create_time: int
        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param dataspace_name: 数据空间名称
        :type dataspace_name: str
        :param domain_id: 域ID
        :type domain_id: str
        :param id: 管道ID
        :type id: int
        :param pipe_id: 管道ID
        :type pipe_id: str
        :param pipe_name: 管道名称
        :type pipe_name: str
        :param project_id: 项目ID
        :type project_id: str
        :param shipper_destination: 
        :type shipper_destination: :class:`huaweicloudsdksecmaster.v1.ShowShipperResponseBodyDataShipperDestination`
        :param shipper_id: 投递ID
        :type shipper_id: str
        :param shipper_name: 投递名称
        :type shipper_name: str
        :param shipper_source: 
        :type shipper_source: :class:`huaweicloudsdksecmaster.v1.ShowShipperResponseBodyDataShipperSource`
        :param status: 状态
        :type status: int
        :param update_time: 更新时间（时间戳）
        :type update_time: int
        :param version: 版本
        :type version: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param workspace_name: 工作空间名称
        :type workspace_name: str
        """
        
        

        self._consumption_type = None
        self._create_time = None
        self._dataspace_id = None
        self._dataspace_name = None
        self._domain_id = None
        self._id = None
        self._pipe_id = None
        self._pipe_name = None
        self._project_id = None
        self._shipper_destination = None
        self._shipper_id = None
        self._shipper_name = None
        self._shipper_source = None
        self._status = None
        self._update_time = None
        self._version = None
        self._workspace_id = None
        self._workspace_name = None
        self.discriminator = None

        if consumption_type is not None:
            self.consumption_type = consumption_type
        if create_time is not None:
            self.create_time = create_time
        if dataspace_id is not None:
            self.dataspace_id = dataspace_id
        if dataspace_name is not None:
            self.dataspace_name = dataspace_name
        if domain_id is not None:
            self.domain_id = domain_id
        if id is not None:
            self.id = id
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if pipe_name is not None:
            self.pipe_name = pipe_name
        if project_id is not None:
            self.project_id = project_id
        if shipper_destination is not None:
            self.shipper_destination = shipper_destination
        if shipper_id is not None:
            self.shipper_id = shipper_id
        if shipper_name is not None:
            self.shipper_name = shipper_name
        if shipper_source is not None:
            self.shipper_source = shipper_source
        if status is not None:
            self.status = status
        if update_time is not None:
            self.update_time = update_time
        if version is not None:
            self.version = version
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if workspace_name is not None:
            self.workspace_name = workspace_name

    @property
    def consumption_type(self):
        r"""Gets the consumption_type of this ShowShipperResponseBodyData.

        消费类型

        :return: The consumption_type of this ShowShipperResponseBodyData.
        :rtype: int
        """
        return self._consumption_type

    @consumption_type.setter
    def consumption_type(self, consumption_type):
        r"""Sets the consumption_type of this ShowShipperResponseBodyData.

        消费类型

        :param consumption_type: The consumption_type of this ShowShipperResponseBodyData.
        :type consumption_type: int
        """
        self._consumption_type = consumption_type

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowShipperResponseBodyData.

        创建时间（时间戳）

        :return: The create_time of this ShowShipperResponseBodyData.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowShipperResponseBodyData.

        创建时间（时间戳）

        :param create_time: The create_time of this ShowShipperResponseBodyData.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this ShowShipperResponseBodyData.

        数据空间ID

        :return: The dataspace_id of this ShowShipperResponseBodyData.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this ShowShipperResponseBodyData.

        数据空间ID

        :param dataspace_id: The dataspace_id of this ShowShipperResponseBodyData.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def dataspace_name(self):
        r"""Gets the dataspace_name of this ShowShipperResponseBodyData.

        数据空间名称

        :return: The dataspace_name of this ShowShipperResponseBodyData.
        :rtype: str
        """
        return self._dataspace_name

    @dataspace_name.setter
    def dataspace_name(self, dataspace_name):
        r"""Sets the dataspace_name of this ShowShipperResponseBodyData.

        数据空间名称

        :param dataspace_name: The dataspace_name of this ShowShipperResponseBodyData.
        :type dataspace_name: str
        """
        self._dataspace_name = dataspace_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowShipperResponseBodyData.

        域ID

        :return: The domain_id of this ShowShipperResponseBodyData.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowShipperResponseBodyData.

        域ID

        :param domain_id: The domain_id of this ShowShipperResponseBodyData.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def id(self):
        r"""Gets the id of this ShowShipperResponseBodyData.

        管道ID

        :return: The id of this ShowShipperResponseBodyData.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowShipperResponseBodyData.

        管道ID

        :param id: The id of this ShowShipperResponseBodyData.
        :type id: int
        """
        self._id = id

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this ShowShipperResponseBodyData.

        管道ID

        :return: The pipe_id of this ShowShipperResponseBodyData.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this ShowShipperResponseBodyData.

        管道ID

        :param pipe_id: The pipe_id of this ShowShipperResponseBodyData.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this ShowShipperResponseBodyData.

        管道名称

        :return: The pipe_name of this ShowShipperResponseBodyData.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this ShowShipperResponseBodyData.

        管道名称

        :param pipe_name: The pipe_name of this ShowShipperResponseBodyData.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowShipperResponseBodyData.

        项目ID

        :return: The project_id of this ShowShipperResponseBodyData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowShipperResponseBodyData.

        项目ID

        :param project_id: The project_id of this ShowShipperResponseBodyData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def shipper_destination(self):
        r"""Gets the shipper_destination of this ShowShipperResponseBodyData.

        :return: The shipper_destination of this ShowShipperResponseBodyData.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowShipperResponseBodyDataShipperDestination`
        """
        return self._shipper_destination

    @shipper_destination.setter
    def shipper_destination(self, shipper_destination):
        r"""Sets the shipper_destination of this ShowShipperResponseBodyData.

        :param shipper_destination: The shipper_destination of this ShowShipperResponseBodyData.
        :type shipper_destination: :class:`huaweicloudsdksecmaster.v1.ShowShipperResponseBodyDataShipperDestination`
        """
        self._shipper_destination = shipper_destination

    @property
    def shipper_id(self):
        r"""Gets the shipper_id of this ShowShipperResponseBodyData.

        投递ID

        :return: The shipper_id of this ShowShipperResponseBodyData.
        :rtype: str
        """
        return self._shipper_id

    @shipper_id.setter
    def shipper_id(self, shipper_id):
        r"""Sets the shipper_id of this ShowShipperResponseBodyData.

        投递ID

        :param shipper_id: The shipper_id of this ShowShipperResponseBodyData.
        :type shipper_id: str
        """
        self._shipper_id = shipper_id

    @property
    def shipper_name(self):
        r"""Gets the shipper_name of this ShowShipperResponseBodyData.

        投递名称

        :return: The shipper_name of this ShowShipperResponseBodyData.
        :rtype: str
        """
        return self._shipper_name

    @shipper_name.setter
    def shipper_name(self, shipper_name):
        r"""Sets the shipper_name of this ShowShipperResponseBodyData.

        投递名称

        :param shipper_name: The shipper_name of this ShowShipperResponseBodyData.
        :type shipper_name: str
        """
        self._shipper_name = shipper_name

    @property
    def shipper_source(self):
        r"""Gets the shipper_source of this ShowShipperResponseBodyData.

        :return: The shipper_source of this ShowShipperResponseBodyData.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ShowShipperResponseBodyDataShipperSource`
        """
        return self._shipper_source

    @shipper_source.setter
    def shipper_source(self, shipper_source):
        r"""Sets the shipper_source of this ShowShipperResponseBodyData.

        :param shipper_source: The shipper_source of this ShowShipperResponseBodyData.
        :type shipper_source: :class:`huaweicloudsdksecmaster.v1.ShowShipperResponseBodyDataShipperSource`
        """
        self._shipper_source = shipper_source

    @property
    def status(self):
        r"""Gets the status of this ShowShipperResponseBodyData.

        状态

        :return: The status of this ShowShipperResponseBodyData.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowShipperResponseBodyData.

        状态

        :param status: The status of this ShowShipperResponseBodyData.
        :type status: int
        """
        self._status = status

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowShipperResponseBodyData.

        更新时间（时间戳）

        :return: The update_time of this ShowShipperResponseBodyData.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowShipperResponseBodyData.

        更新时间（时间戳）

        :param update_time: The update_time of this ShowShipperResponseBodyData.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def version(self):
        r"""Gets the version of this ShowShipperResponseBodyData.

        版本

        :return: The version of this ShowShipperResponseBodyData.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowShipperResponseBodyData.

        版本

        :param version: The version of this ShowShipperResponseBodyData.
        :type version: str
        """
        self._version = version

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowShipperResponseBodyData.

        工作空间ID

        :return: The workspace_id of this ShowShipperResponseBodyData.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowShipperResponseBodyData.

        工作空间ID

        :param workspace_id: The workspace_id of this ShowShipperResponseBodyData.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def workspace_name(self):
        r"""Gets the workspace_name of this ShowShipperResponseBodyData.

        工作空间名称

        :return: The workspace_name of this ShowShipperResponseBodyData.
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        r"""Sets the workspace_name of this ShowShipperResponseBodyData.

        工作空间名称

        :param workspace_name: The workspace_name of this ShowShipperResponseBodyData.
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
        if not isinstance(other, ShowShipperResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
