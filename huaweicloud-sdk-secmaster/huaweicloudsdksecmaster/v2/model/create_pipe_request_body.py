# coding: utf-8

import six

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
        'pipe_name': 'str',
        'description': 'str',
        'storage_period': 'int',
        'shards': 'int',
        'timestamp_field': 'str',
        'mapping': 'dict(str, KeyIndex)'
    }

    attribute_map = {
        'dataspace_id': 'dataspace_id',
        'pipe_name': 'pipe_name',
        'description': 'description',
        'storage_period': 'storage_period',
        'shards': 'shards',
        'timestamp_field': 'timestamp_field',
        'mapping': 'mapping'
    }

    def __init__(self, dataspace_id=None, pipe_name=None, description=None, storage_period=None, shards=None, timestamp_field=None, mapping=None):
        """CreatePipeRequestBody

        The model defined in huaweicloud sdk

        :param dataspace_id: 工作空间ID
        :type dataspace_id: str
        :param pipe_name: 数据管道名称
        :type pipe_name: str
        :param description: 描述
        :type description: str
        :param storage_period: 数据的保存时间，单位为天；默认30天，取值范围为1~3600
        :type storage_period: int
        :param shards: 数据管道分区个数；默认创建1个，最大支持创建64个分区
        :type shards: int
        :param timestamp_field: 时间戳字段
        :type timestamp_field: str
        :param mapping: 索引字段映射；每个key对象承载一个字段的信息；存在多个key对象，key可变，表示字段名称；可嵌套
        :type mapping: dict(str, KeyIndex)
        """
        
        

        self._dataspace_id = None
        self._pipe_name = None
        self._description = None
        self._storage_period = None
        self._shards = None
        self._timestamp_field = None
        self._mapping = None
        self.discriminator = None

        self.dataspace_id = dataspace_id
        self.pipe_name = pipe_name
        if description is not None:
            self.description = description
        self.storage_period = storage_period
        self.shards = shards
        if timestamp_field is not None:
            self.timestamp_field = timestamp_field
        if mapping is not None:
            self.mapping = mapping

    @property
    def dataspace_id(self):
        """Gets the dataspace_id of this CreatePipeRequestBody.

        工作空间ID

        :return: The dataspace_id of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        """Sets the dataspace_id of this CreatePipeRequestBody.

        工作空间ID

        :param dataspace_id: The dataspace_id of this CreatePipeRequestBody.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def pipe_name(self):
        """Gets the pipe_name of this CreatePipeRequestBody.

        数据管道名称

        :return: The pipe_name of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._pipe_name

    @pipe_name.setter
    def pipe_name(self, pipe_name):
        """Sets the pipe_name of this CreatePipeRequestBody.

        数据管道名称

        :param pipe_name: The pipe_name of this CreatePipeRequestBody.
        :type pipe_name: str
        """
        self._pipe_name = pipe_name

    @property
    def description(self):
        """Gets the description of this CreatePipeRequestBody.

        描述

        :return: The description of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePipeRequestBody.

        描述

        :param description: The description of this CreatePipeRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def storage_period(self):
        """Gets the storage_period of this CreatePipeRequestBody.

        数据的保存时间，单位为天；默认30天，取值范围为1~3600

        :return: The storage_period of this CreatePipeRequestBody.
        :rtype: int
        """
        return self._storage_period

    @storage_period.setter
    def storage_period(self, storage_period):
        """Sets the storage_period of this CreatePipeRequestBody.

        数据的保存时间，单位为天；默认30天，取值范围为1~3600

        :param storage_period: The storage_period of this CreatePipeRequestBody.
        :type storage_period: int
        """
        self._storage_period = storage_period

    @property
    def shards(self):
        """Gets the shards of this CreatePipeRequestBody.

        数据管道分区个数；默认创建1个，最大支持创建64个分区

        :return: The shards of this CreatePipeRequestBody.
        :rtype: int
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        """Sets the shards of this CreatePipeRequestBody.

        数据管道分区个数；默认创建1个，最大支持创建64个分区

        :param shards: The shards of this CreatePipeRequestBody.
        :type shards: int
        """
        self._shards = shards

    @property
    def timestamp_field(self):
        """Gets the timestamp_field of this CreatePipeRequestBody.

        时间戳字段

        :return: The timestamp_field of this CreatePipeRequestBody.
        :rtype: str
        """
        return self._timestamp_field

    @timestamp_field.setter
    def timestamp_field(self, timestamp_field):
        """Sets the timestamp_field of this CreatePipeRequestBody.

        时间戳字段

        :param timestamp_field: The timestamp_field of this CreatePipeRequestBody.
        :type timestamp_field: str
        """
        self._timestamp_field = timestamp_field

    @property
    def mapping(self):
        """Gets the mapping of this CreatePipeRequestBody.

        索引字段映射；每个key对象承载一个字段的信息；存在多个key对象，key可变，表示字段名称；可嵌套

        :return: The mapping of this CreatePipeRequestBody.
        :rtype: dict(str, KeyIndex)
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this CreatePipeRequestBody.

        索引字段映射；每个key对象承载一个字段的信息；存在多个key对象，key可变，表示字段名称；可嵌套

        :param mapping: The mapping of this CreatePipeRequestBody.
        :type mapping: dict(str, KeyIndex)
        """
        self._mapping = mapping

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
        if not isinstance(other, CreatePipeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
