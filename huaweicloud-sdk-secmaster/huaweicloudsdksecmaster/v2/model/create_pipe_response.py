# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePipeResponse(SdkResponse):

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
        'dataspace_id': 'str',
        'dataspace_name': 'str',
        'pipe_id': 'str',
        'pipe_name': 'str',
        'pipe_type': 'str',
        'description': 'str',
        'storage_period': 'int',
        'shards': 'int',
        'create_by': 'str',
        'create_time': 'int',
        'update_by': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'dataspace_id': 'dataspace_id',
        'dataspace_name': 'dataspace_name',
        'pipe_id': 'pipe_id',
        'pipe_name': 'pipe_name',
        'pipe_type': 'pipe_type',
        'description': 'description',
        'storage_period': 'storage_period',
        'shards': 'shards',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'update_by': 'update_by',
        'update_time': 'update_time'
    }

    def __init__(self, domain_id=None, project_id=None, dataspace_id=None, dataspace_name=None, pipe_id=None, pipe_name=None, pipe_type=None, description=None, storage_period=None, shards=None, create_by=None, create_time=None, update_by=None, update_time=None):
        """CreatePipeResponse

        The model defined in huaweicloud sdk

        :param domain_id: 用户domainId
        :type domain_id: str
        :param project_id: 项目id
        :type project_id: str
        :param dataspace_id: 数据空间id
        :type dataspace_id: str
        :param dataspace_name: 数据空间名称
        :type dataspace_name: str
        :param pipe_id: 管道id
        :type pipe_id: str
        :param pipe_name: 管道名称
        :type pipe_name: str
        :param pipe_type: 管道类型（system-defined，系统预定义)、1（user-defined，用户自定义)
        :type pipe_type: str
        :param description: 描述信息
        :type description: str
        :param storage_period: 索引存储天数
        :type storage_period: int
        :param shards: 索引分片数量
        :type shards: int
        :param create_by: 创建者
        :type create_by: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_by: 更新者
        :type update_by: str
        :param update_time: 更新时间
        :type update_time: int
        """
        
        super(CreatePipeResponse, self).__init__()

        self._domain_id = None
        self._project_id = None
        self._dataspace_id = None
        self._dataspace_name = None
        self._pipe_id = None
        self._pipe_name = None
        self._pipe_type = None
        self._description = None
        self._storage_period = None
        self._shards = None
        self._create_by = None
        self._create_time = None
        self._update_by = None
        self._update_time = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if dataspace_id is not None:
            self.dataspace_id = dataspace_id
        if dataspace_name is not None:
            self.dataspace_name = dataspace_name
        if pipe_id is not None:
            self.pipe_id = pipe_id
        if pipe_name is not None:
            self.pipe_name = pipe_name
        if pipe_type is not None:
            self.pipe_type = pipe_type
        if description is not None:
            self.description = description
        if storage_period is not None:
            self.storage_period = storage_period
        if shards is not None:
            self.shards = shards
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time

    @property
    def domain_id(self):
        """Gets the domain_id of this CreatePipeResponse.

        用户domainId

        :return: The domain_id of this CreatePipeResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreatePipeResponse.

        用户domainId

        :param domain_id: The domain_id of this CreatePipeResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this CreatePipeResponse.

        项目id

        :return: The project_id of this CreatePipeResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreatePipeResponse.

        项目id

        :param project_id: The project_id of this CreatePipeResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def dataspace_id(self):
        """Gets the dataspace_id of this CreatePipeResponse.

        数据空间id

        :return: The dataspace_id of this CreatePipeResponse.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        """Sets the dataspace_id of this CreatePipeResponse.

        数据空间id

        :param dataspace_id: The dataspace_id of this CreatePipeResponse.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def dataspace_name(self):
        """Gets the dataspace_name of this CreatePipeResponse.

        数据空间名称

        :return: The dataspace_name of this CreatePipeResponse.
        :rtype: str
        """
        return self._dataspace_name

    @dataspace_name.setter
    def dataspace_name(self, dataspace_name):
        """Sets the dataspace_name of this CreatePipeResponse.

        数据空间名称

        :param dataspace_name: The dataspace_name of this CreatePipeResponse.
        :type dataspace_name: str
        """
        self._dataspace_name = dataspace_name

    @property
    def pipe_id(self):
        """Gets the pipe_id of this CreatePipeResponse.

        管道id

        :return: The pipe_id of this CreatePipeResponse.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        """Sets the pipe_id of this CreatePipeResponse.

        管道id

        :param pipe_id: The pipe_id of this CreatePipeResponse.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def pipe_name(self):
        """Gets the pipe_name of this CreatePipeResponse.

        管道名称

        :return: The pipe_name of this CreatePipeResponse.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        """Sets the pipe_name of this CreatePipeResponse.

        管道名称

        :param pipe_name: The pipe_name of this CreatePipeResponse.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def pipe_type(self):
        """Gets the pipe_type of this CreatePipeResponse.

        管道类型（system-defined，系统预定义)、1（user-defined，用户自定义)

        :return: The pipe_type of this CreatePipeResponse.
        :rtype: str
        """
        return self._pipe_type

    @pipe_type.setter
    def pipe_type(self, pipe_type):
        """Sets the pipe_type of this CreatePipeResponse.

        管道类型（system-defined，系统预定义)、1（user-defined，用户自定义)

        :param pipe_type: The pipe_type of this CreatePipeResponse.
        :type pipe_type: str
        """
        self._pipe_type = pipe_type

    @property
    def description(self):
        """Gets the description of this CreatePipeResponse.

        描述信息

        :return: The description of this CreatePipeResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePipeResponse.

        描述信息

        :param description: The description of this CreatePipeResponse.
        :type description: str
        """
        self._description = description

    @property
    def storage_period(self):
        """Gets the storage_period of this CreatePipeResponse.

        索引存储天数

        :return: The storage_period of this CreatePipeResponse.
        :rtype: int
        """
        return self._storage_period

    @storage_period.setter
    def storage_period(self, storage_period):
        """Sets the storage_period of this CreatePipeResponse.

        索引存储天数

        :param storage_period: The storage_period of this CreatePipeResponse.
        :type storage_period: int
        """
        self._storage_period = storage_period

    @property
    def shards(self):
        """Gets the shards of this CreatePipeResponse.

        索引分片数量

        :return: The shards of this CreatePipeResponse.
        :rtype: int
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        """Sets the shards of this CreatePipeResponse.

        索引分片数量

        :param shards: The shards of this CreatePipeResponse.
        :type shards: int
        """
        self._shards = shards

    @property
    def create_by(self):
        """Gets the create_by of this CreatePipeResponse.

        创建者

        :return: The create_by of this CreatePipeResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this CreatePipeResponse.

        创建者

        :param create_by: The create_by of this CreatePipeResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        """Gets the create_time of this CreatePipeResponse.

        创建时间

        :return: The create_time of this CreatePipeResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreatePipeResponse.

        创建时间

        :param create_time: The create_time of this CreatePipeResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_by(self):
        """Gets the update_by of this CreatePipeResponse.

        更新者

        :return: The update_by of this CreatePipeResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this CreatePipeResponse.

        更新者

        :param update_by: The update_by of this CreatePipeResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        """Gets the update_time of this CreatePipeResponse.

        更新时间

        :return: The update_time of this CreatePipeResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreatePipeResponse.

        更新时间

        :param update_time: The update_time of this CreatePipeResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, CreatePipeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
