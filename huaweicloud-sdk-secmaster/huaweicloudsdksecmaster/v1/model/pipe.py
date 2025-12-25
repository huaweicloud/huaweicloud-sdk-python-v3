# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Pipe:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_by': 'str',
        'create_time': 'int',
        'dataspace_id': 'str',
        'dataspace_name': 'str',
        'description': 'str',
        'domain_id': 'str',
        'pipe_id': 'str',
        'pipe_name': 'str',
        'pipe_type': 'str',
        'project_id': 'str',
        'shards': 'int',
        'storage_period': 'int',
        'update_by': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'create_by': 'create_by',
        'create_time': 'create_time',
        'dataspace_id': 'dataspace_id',
        'dataspace_name': 'dataspace_name',
        'description': 'description',
        'domain_id': 'domain_id',
        'pipe_id': 'pipe_id',
        'pipe_name': 'pipe_name',
        'pipe_type': 'pipe_type',
        'project_id': 'project_id',
        'shards': 'shards',
        'storage_period': 'storage_period',
        'update_by': 'update_by',
        'update_time': 'update_time'
    }

    def __init__(self, create_by=None, create_time=None, dataspace_id=None, dataspace_name=None, description=None, domain_id=None, pipe_id=None, pipe_name=None, pipe_type=None, project_id=None, shards=None, storage_period=None, update_by=None, update_time=None):
        r"""Pipe

        The model defined in huaweicloud sdk

        :param create_by: 创建者
        :type create_by: str
        :param create_time: 创建时间
        :type create_time: int
        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param dataspace_name: 数据空间名称
        :type dataspace_name: str
        :param description: 描述
        :type description: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param pipe_id: 数据管道ID
        :type pipe_id: str
        :param pipe_name: 数据管道名称
        :type pipe_name: str
        :param pipe_type: 数据管道类型；可选值：system-defined(系统预定义)、user-defined(用户自定义)
        :type pipe_type: str
        :param project_id: 项目ID
        :type project_id: str
        :param shards: 分区个数；默认创建1个，最大支持创建64个分区
        :type shards: int
        :param storage_period: 数据的保存时间，单位为天；默认30天，取值范围为1~3600
        :type storage_period: int
        :param update_by: 更新者
        :type update_by: str
        :param update_time: 更新时间
        :type update_time: int
        """
        
        

        self._create_by = None
        self._create_time = None
        self._dataspace_id = None
        self._dataspace_name = None
        self._description = None
        self._domain_id = None
        self._pipe_id = None
        self._pipe_name = None
        self._pipe_type = None
        self._project_id = None
        self._shards = None
        self._storage_period = None
        self._update_by = None
        self._update_time = None
        self.discriminator = None

        self.create_by = create_by
        self.create_time = create_time
        self.dataspace_id = dataspace_id
        self.dataspace_name = dataspace_name
        self.description = description
        self.domain_id = domain_id
        self.pipe_id = pipe_id
        self.pipe_name = pipe_name
        if pipe_type is not None:
            self.pipe_type = pipe_type
        self.project_id = project_id
        self.shards = shards
        self.storage_period = storage_period
        self.update_by = update_by
        self.update_time = update_time

    @property
    def create_by(self):
        r"""Gets the create_by of this Pipe.

        创建者

        :return: The create_by of this Pipe.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this Pipe.

        创建者

        :param create_by: The create_by of this Pipe.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this Pipe.

        创建时间

        :return: The create_time of this Pipe.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Pipe.

        创建时间

        :param create_time: The create_time of this Pipe.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this Pipe.

        数据空间ID

        :return: The dataspace_id of this Pipe.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this Pipe.

        数据空间ID

        :param dataspace_id: The dataspace_id of this Pipe.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def dataspace_name(self):
        r"""Gets the dataspace_name of this Pipe.

        数据空间名称

        :return: The dataspace_name of this Pipe.
        :rtype: str
        """
        return self._dataspace_name

    @dataspace_name.setter
    def dataspace_name(self, dataspace_name):
        r"""Sets the dataspace_name of this Pipe.

        数据空间名称

        :param dataspace_name: The dataspace_name of this Pipe.
        :type dataspace_name: str
        """
        self._dataspace_name = dataspace_name

    @property
    def description(self):
        r"""Gets the description of this Pipe.

        描述

        :return: The description of this Pipe.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Pipe.

        描述

        :param description: The description of this Pipe.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        r"""Gets the domain_id of this Pipe.

        账号ID

        :return: The domain_id of this Pipe.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this Pipe.

        账号ID

        :param domain_id: The domain_id of this Pipe.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this Pipe.

        数据管道ID

        :return: The pipe_id of this Pipe.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this Pipe.

        数据管道ID

        :param pipe_id: The pipe_id of this Pipe.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this Pipe.

        数据管道名称

        :return: The pipe_name of this Pipe.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this Pipe.

        数据管道名称

        :param pipe_name: The pipe_name of this Pipe.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def pipe_type(self):
        r"""Gets the pipe_type of this Pipe.

        数据管道类型；可选值：system-defined(系统预定义)、user-defined(用户自定义)

        :return: The pipe_type of this Pipe.
        :rtype: str
        """
        return self._pipe_type

    @pipe_type.setter
    def pipe_type(self, pipe_type):
        r"""Sets the pipe_type of this Pipe.

        数据管道类型；可选值：system-defined(系统预定义)、user-defined(用户自定义)

        :param pipe_type: The pipe_type of this Pipe.
        :type pipe_type: str
        """
        self._pipe_type = pipe_type

    @property
    def project_id(self):
        r"""Gets the project_id of this Pipe.

        项目ID

        :return: The project_id of this Pipe.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Pipe.

        项目ID

        :param project_id: The project_id of this Pipe.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def shards(self):
        r"""Gets the shards of this Pipe.

        分区个数；默认创建1个，最大支持创建64个分区

        :return: The shards of this Pipe.
        :rtype: int
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        r"""Sets the shards of this Pipe.

        分区个数；默认创建1个，最大支持创建64个分区

        :param shards: The shards of this Pipe.
        :type shards: int
        """
        self._shards = shards

    @property
    def storage_period(self):
        r"""Gets the storage_period of this Pipe.

        数据的保存时间，单位为天；默认30天，取值范围为1~3600

        :return: The storage_period of this Pipe.
        :rtype: int
        """
        return self._storage_period

    @storage_period.setter
    def storage_period(self, storage_period):
        r"""Sets the storage_period of this Pipe.

        数据的保存时间，单位为天；默认30天，取值范围为1~3600

        :param storage_period: The storage_period of this Pipe.
        :type storage_period: int
        """
        self._storage_period = storage_period

    @property
    def update_by(self):
        r"""Gets the update_by of this Pipe.

        更新者

        :return: The update_by of this Pipe.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this Pipe.

        更新者

        :param update_by: The update_by of this Pipe.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this Pipe.

        更新时间

        :return: The update_time of this Pipe.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Pipe.

        更新时间

        :param update_time: The update_time of this Pipe.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, Pipe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
