# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailOfEventSchemaVersionResponse(SdkResponse):

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
        'schema_id': 'str',
        'version': 'int',
        'format': 'str',
        'created_time': 'str',
        'updated_time': 'str',
        'data_sample': 'str',
        'definition': 'str'
    }

    attribute_map = {
        'id': 'id',
        'schema_id': 'schema_id',
        'version': 'version',
        'format': 'format',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'data_sample': 'data_sample',
        'definition': 'definition'
    }

    def __init__(self, id=None, schema_id=None, version=None, format=None, created_time=None, updated_time=None, data_sample=None, definition=None):
        """ShowDetailOfEventSchemaVersionResponse

        The model defined in huaweicloud sdk

        :param id: 事件模型版本ID
        :type id: str
        :param schema_id: 事件模型ID
        :type schema_id: str
        :param version: 事件模型版本号
        :type version: int
        :param format: 事件模型格式
        :type format: str
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 更新时间
        :type updated_time: str
        :param data_sample: 事件示例
        :type data_sample: str
        :param definition: 事件模型内容定义
        :type definition: str
        """
        
        super(ShowDetailOfEventSchemaVersionResponse, self).__init__()

        self._id = None
        self._schema_id = None
        self._version = None
        self._format = None
        self._created_time = None
        self._updated_time = None
        self._data_sample = None
        self._definition = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if schema_id is not None:
            self.schema_id = schema_id
        if version is not None:
            self.version = version
        if format is not None:
            self.format = format
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if data_sample is not None:
            self.data_sample = data_sample
        if definition is not None:
            self.definition = definition

    @property
    def id(self):
        """Gets the id of this ShowDetailOfEventSchemaVersionResponse.

        事件模型版本ID

        :return: The id of this ShowDetailOfEventSchemaVersionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDetailOfEventSchemaVersionResponse.

        事件模型版本ID

        :param id: The id of this ShowDetailOfEventSchemaVersionResponse.
        :type id: str
        """
        self._id = id

    @property
    def schema_id(self):
        """Gets the schema_id of this ShowDetailOfEventSchemaVersionResponse.

        事件模型ID

        :return: The schema_id of this ShowDetailOfEventSchemaVersionResponse.
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this ShowDetailOfEventSchemaVersionResponse.

        事件模型ID

        :param schema_id: The schema_id of this ShowDetailOfEventSchemaVersionResponse.
        :type schema_id: str
        """
        self._schema_id = schema_id

    @property
    def version(self):
        """Gets the version of this ShowDetailOfEventSchemaVersionResponse.

        事件模型版本号

        :return: The version of this ShowDetailOfEventSchemaVersionResponse.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowDetailOfEventSchemaVersionResponse.

        事件模型版本号

        :param version: The version of this ShowDetailOfEventSchemaVersionResponse.
        :type version: int
        """
        self._version = version

    @property
    def format(self):
        """Gets the format of this ShowDetailOfEventSchemaVersionResponse.

        事件模型格式

        :return: The format of this ShowDetailOfEventSchemaVersionResponse.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ShowDetailOfEventSchemaVersionResponse.

        事件模型格式

        :param format: The format of this ShowDetailOfEventSchemaVersionResponse.
        :type format: str
        """
        self._format = format

    @property
    def created_time(self):
        """Gets the created_time of this ShowDetailOfEventSchemaVersionResponse.

        创建时间

        :return: The created_time of this ShowDetailOfEventSchemaVersionResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowDetailOfEventSchemaVersionResponse.

        创建时间

        :param created_time: The created_time of this ShowDetailOfEventSchemaVersionResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this ShowDetailOfEventSchemaVersionResponse.

        更新时间

        :return: The updated_time of this ShowDetailOfEventSchemaVersionResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ShowDetailOfEventSchemaVersionResponse.

        更新时间

        :param updated_time: The updated_time of this ShowDetailOfEventSchemaVersionResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def data_sample(self):
        """Gets the data_sample of this ShowDetailOfEventSchemaVersionResponse.

        事件示例

        :return: The data_sample of this ShowDetailOfEventSchemaVersionResponse.
        :rtype: str
        """
        return self._data_sample

    @data_sample.setter
    def data_sample(self, data_sample):
        """Sets the data_sample of this ShowDetailOfEventSchemaVersionResponse.

        事件示例

        :param data_sample: The data_sample of this ShowDetailOfEventSchemaVersionResponse.
        :type data_sample: str
        """
        self._data_sample = data_sample

    @property
    def definition(self):
        """Gets the definition of this ShowDetailOfEventSchemaVersionResponse.

        事件模型内容定义

        :return: The definition of this ShowDetailOfEventSchemaVersionResponse.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this ShowDetailOfEventSchemaVersionResponse.

        事件模型内容定义

        :param definition: The definition of this ShowDetailOfEventSchemaVersionResponse.
        :type definition: str
        """
        self._definition = definition

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
        if not isinstance(other, ShowDetailOfEventSchemaVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
