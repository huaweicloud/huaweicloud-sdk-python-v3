# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackLogInfo:

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
        'instance_id': 'str',
        'size': 'float',
        'size_unit': 'str',
        'status': 'str',
        'query_start_time': 'int',
        'query_end_time': 'int',
        'file_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'size': 'size',
        'size_unit': 'size_unit',
        'status': 'status',
        'query_start_time': 'query_start_time',
        'query_end_time': 'query_end_time',
        'file_name': 'file_name'
    }

    def __init__(self, id=None, instance_id=None, size=None, size_unit=None, status=None, query_start_time=None, query_end_time=None, file_name=None):
        r"""PackLogInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  文件唯一ID标识。  **约束限制**：  不涉及。
        :type id: str
        :param instance_id: **参数解释**：  实例id。  **约束限制**：  不涉及。
        :type instance_id: str
        :param size: **参数解释**：  文件大小。  **约束限制**：  不涉及。
        :type size: float
        :param size_unit: **参数解释**：  文件大小单位。  **约束限制**：  不涉及。
        :type size_unit: str
        :param status: **参数解释**：  状态。  **约束限制**：  不涉及。
        :type status: str
        :param query_start_time: **参数解释**：  合并时间段起始时间戳。  **约束限制**：  不涉及。
        :type query_start_time: int
        :param query_end_time: **参数解释**：  合并时间段结束时间戳。  **约束限制**：  不涉及。
        :type query_end_time: int
        :param file_name: **参数解释**：  文件名。  **约束限制**：  不涉及。
        :type file_name: str
        """
        
        

        self._id = None
        self._instance_id = None
        self._size = None
        self._size_unit = None
        self._status = None
        self._query_start_time = None
        self._query_end_time = None
        self._file_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if size is not None:
            self.size = size
        if size_unit is not None:
            self.size_unit = size_unit
        if status is not None:
            self.status = status
        if query_start_time is not None:
            self.query_start_time = query_start_time
        if query_end_time is not None:
            self.query_end_time = query_end_time
        if file_name is not None:
            self.file_name = file_name

    @property
    def id(self):
        r"""Gets the id of this PackLogInfo.

        **参数解释**：  文件唯一ID标识。  **约束限制**：  不涉及。

        :return: The id of this PackLogInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PackLogInfo.

        **参数解释**：  文件唯一ID标识。  **约束限制**：  不涉及。

        :param id: The id of this PackLogInfo.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this PackLogInfo.

        **参数解释**：  实例id。  **约束限制**：  不涉及。

        :return: The instance_id of this PackLogInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this PackLogInfo.

        **参数解释**：  实例id。  **约束限制**：  不涉及。

        :param instance_id: The instance_id of this PackLogInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def size(self):
        r"""Gets the size of this PackLogInfo.

        **参数解释**：  文件大小。  **约束限制**：  不涉及。

        :return: The size of this PackLogInfo.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this PackLogInfo.

        **参数解释**：  文件大小。  **约束限制**：  不涉及。

        :param size: The size of this PackLogInfo.
        :type size: float
        """
        self._size = size

    @property
    def size_unit(self):
        r"""Gets the size_unit of this PackLogInfo.

        **参数解释**：  文件大小单位。  **约束限制**：  不涉及。

        :return: The size_unit of this PackLogInfo.
        :rtype: str
        """
        return self._size_unit

    @size_unit.setter
    def size_unit(self, size_unit):
        r"""Sets the size_unit of this PackLogInfo.

        **参数解释**：  文件大小单位。  **约束限制**：  不涉及。

        :param size_unit: The size_unit of this PackLogInfo.
        :type size_unit: str
        """
        self._size_unit = size_unit

    @property
    def status(self):
        r"""Gets the status of this PackLogInfo.

        **参数解释**：  状态。  **约束限制**：  不涉及。

        :return: The status of this PackLogInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PackLogInfo.

        **参数解释**：  状态。  **约束限制**：  不涉及。

        :param status: The status of this PackLogInfo.
        :type status: str
        """
        self._status = status

    @property
    def query_start_time(self):
        r"""Gets the query_start_time of this PackLogInfo.

        **参数解释**：  合并时间段起始时间戳。  **约束限制**：  不涉及。

        :return: The query_start_time of this PackLogInfo.
        :rtype: int
        """
        return self._query_start_time

    @query_start_time.setter
    def query_start_time(self, query_start_time):
        r"""Sets the query_start_time of this PackLogInfo.

        **参数解释**：  合并时间段起始时间戳。  **约束限制**：  不涉及。

        :param query_start_time: The query_start_time of this PackLogInfo.
        :type query_start_time: int
        """
        self._query_start_time = query_start_time

    @property
    def query_end_time(self):
        r"""Gets the query_end_time of this PackLogInfo.

        **参数解释**：  合并时间段结束时间戳。  **约束限制**：  不涉及。

        :return: The query_end_time of this PackLogInfo.
        :rtype: int
        """
        return self._query_end_time

    @query_end_time.setter
    def query_end_time(self, query_end_time):
        r"""Sets the query_end_time of this PackLogInfo.

        **参数解释**：  合并时间段结束时间戳。  **约束限制**：  不涉及。

        :param query_end_time: The query_end_time of this PackLogInfo.
        :type query_end_time: int
        """
        self._query_end_time = query_end_time

    @property
    def file_name(self):
        r"""Gets the file_name of this PackLogInfo.

        **参数解释**：  文件名。  **约束限制**：  不涉及。

        :return: The file_name of this PackLogInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this PackLogInfo.

        **参数解释**：  文件名。  **约束限制**：  不涉及。

        :param file_name: The file_name of this PackLogInfo.
        :type file_name: str
        """
        self._file_name = file_name

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
        if not isinstance(other, PackLogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
