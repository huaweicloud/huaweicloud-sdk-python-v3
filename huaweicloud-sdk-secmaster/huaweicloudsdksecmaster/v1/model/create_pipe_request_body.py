# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePipeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataspace_id': 'str',
        'description': 'str',
        'mapping': 'dict(str, KeyIndex)',
        'pipe_name': 'str',
        'shards': 'int',
        'storage_period': 'int',
        'timestamp_field': 'str'
    }

    attribute_map = {
        'dataspace_id': 'dataspace_id',
        'description': 'description',
        'mapping': 'mapping',
        'pipe_name': 'pipe_name',
        'shards': 'shards',
        'storage_period': 'storage_period',
        'timestamp_field': 'timestamp_field'
    }

    def __init__(self, dataspace_id=None, description=None, mapping=None, pipe_name=None, shards=None, storage_period=None, timestamp_field=None):
        r"""CreatePipeRequestBody

        The model defined in huaweicloud sdk

        :param dataspace_id: 工作空间ID
        :type dataspace_id: str
        :param description: 描述
        :type description: str
        :param mapping: 索引字段映射；每个key对象承载一个字段的信息；存在多个key对象，key可变，表示字段名称；可嵌套
        :type mapping: dict(str, KeyIndex)
        :param pipe_name: 数据管道名称
        :type pipe_name: str
        :param shards: 数据管道分区个数；默认创建1个，最大支持创建64个分区
        :type shards: int
        :param storage_period: 数据的保存时间，单位为天；默认30天，取值范围为7~180. 配置180天需提工单申请
        :type storage_period: int
        :param timestamp_field: 时间戳字段
        :type timestamp_field: str
        """
        
        

        self._dataspace_id = None
        self._description = None
        self._mapping = None
        self._pipe_name = None
        self._shards = None
        self._storage_period = None
        self._timestamp_field = None
        self.discriminator = None

        self.dataspace_id = dataspace_id
        if description is not None:
            self.description = description
        if mapping is not None:
            self.mapping = mapping
        self.pipe_name = pipe_name
        self.shards = shards
        self.storage_period = storage_period
        if timestamp_field is not None:
            self.timestamp_field = timestamp_field

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this CreatePipeRequestBody.

        工作空间ID

        :return: The dataspace_id of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this CreatePipeRequestBody.

        工作空间ID

        :param dataspace_id: The dataspace_id of this CreatePipeRequestBody.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def description(self):
        r"""Gets the description of this CreatePipeRequestBody.

        描述

        :return: The description of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePipeRequestBody.

        描述

        :param description: The description of this CreatePipeRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def mapping(self):
        r"""Gets the mapping of this CreatePipeRequestBody.

        索引字段映射；每个key对象承载一个字段的信息；存在多个key对象，key可变，表示字段名称；可嵌套

        :return: The mapping of this CreatePipeRequestBody.
        :rtype: dict(str, KeyIndex)
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        r"""Sets the mapping of this CreatePipeRequestBody.

        索引字段映射；每个key对象承载一个字段的信息；存在多个key对象，key可变，表示字段名称；可嵌套

        :param mapping: The mapping of this CreatePipeRequestBody.
        :type mapping: dict(str, KeyIndex)
        """
        self._mapping = mapping

    @property
    def pipe_name(self):
        r"""Gets the pipe_name of this CreatePipeRequestBody.

        数据管道名称

        :return: The pipe_name of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        r"""Sets the pipe_name of this CreatePipeRequestBody.

        数据管道名称

        :param pipe_name: The pipe_name of this CreatePipeRequestBody.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def shards(self):
        r"""Gets the shards of this CreatePipeRequestBody.

        数据管道分区个数；默认创建1个，最大支持创建64个分区

        :return: The shards of this CreatePipeRequestBody.
        :rtype: int
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        r"""Sets the shards of this CreatePipeRequestBody.

        数据管道分区个数；默认创建1个，最大支持创建64个分区

        :param shards: The shards of this CreatePipeRequestBody.
        :type shards: int
        """
        self._shards = shards

    @property
    def storage_period(self):
        r"""Gets the storage_period of this CreatePipeRequestBody.

        数据的保存时间，单位为天；默认30天，取值范围为7~180. 配置180天需提工单申请

        :return: The storage_period of this CreatePipeRequestBody.
        :rtype: int
        """
        return self._storage_period

    @storage_period.setter
    def storage_period(self, storage_period):
        r"""Sets the storage_period of this CreatePipeRequestBody.

        数据的保存时间，单位为天；默认30天，取值范围为7~180. 配置180天需提工单申请

        :param storage_period: The storage_period of this CreatePipeRequestBody.
        :type storage_period: int
        """
        self._storage_period = storage_period

    @property
    def timestamp_field(self):
        r"""Gets the timestamp_field of this CreatePipeRequestBody.

        时间戳字段

        :return: The timestamp_field of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._timestamp_field

    @timestamp_field.setter
    def timestamp_field(self, timestamp_field):
        r"""Sets the timestamp_field of this CreatePipeRequestBody.

        时间戳字段

        :param timestamp_field: The timestamp_field of this CreatePipeRequestBody.
        :type timestamp_field: str
        """
        self._timestamp_field = timestamp_field

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
        if not isinstance(other, CreatePipeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
