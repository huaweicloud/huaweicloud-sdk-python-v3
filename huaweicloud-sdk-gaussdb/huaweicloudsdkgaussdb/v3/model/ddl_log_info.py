# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DdlLogInfo:

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
        'file_name': 'str',
        'file_size': 'int',
        'create_time': 'str',
        'end_time': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'file_name',
        'file_size': 'file_size',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'status': 'status'
    }

    def __init__(self, id=None, file_name=None, file_size=None, create_time=None, end_time=None, status=None):
        r"""DdlLogInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  日志文件ID。  **取值范围**：  不涉及。 
        :type id: str
        :param file_name: **参数解释**：  日志文件名称。  **取值范围**：  不涉及。 
        :type file_name: str
        :param file_size: **参数解释**：  日志文件大小，单位为字节。  **取值范围**：  不涉及。 
        :type file_size: int
        :param create_time: **参数解释**：  日志文件上传的创建时间。  **取值范围**：  不涉及。 
        :type create_time: str
        :param end_time: **参数解释**：  日志文件上传的结束时间。  **取值范围**：  不涉及。 
        :type end_time: str
        :param status: **参数解释**：  日志文件的状态。  **取值范围**：  - Active：表示正常。 - Disable：表示不可用。 
        :type status: str
        """
        
        

        self._id = None
        self._file_name = None
        self._file_size = None
        self._create_time = None
        self._end_time = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.file_name = file_name
        self.file_size = file_size
        self.create_time = create_time
        self.end_time = end_time
        self.status = status

    @property
    def id(self):
        r"""Gets the id of this DdlLogInfo.

        **参数解释**：  日志文件ID。  **取值范围**：  不涉及。 

        :return: The id of this DdlLogInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DdlLogInfo.

        **参数解释**：  日志文件ID。  **取值范围**：  不涉及。 

        :param id: The id of this DdlLogInfo.
        :type id: str
        """
        self._id = id

    @property
    def file_name(self):
        r"""Gets the file_name of this DdlLogInfo.

        **参数解释**：  日志文件名称。  **取值范围**：  不涉及。 

        :return: The file_name of this DdlLogInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this DdlLogInfo.

        **参数解释**：  日志文件名称。  **取值范围**：  不涉及。 

        :param file_name: The file_name of this DdlLogInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_size(self):
        r"""Gets the file_size of this DdlLogInfo.

        **参数解释**：  日志文件大小，单位为字节。  **取值范围**：  不涉及。 

        :return: The file_size of this DdlLogInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this DdlLogInfo.

        **参数解释**：  日志文件大小，单位为字节。  **取值范围**：  不涉及。 

        :param file_size: The file_size of this DdlLogInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def create_time(self):
        r"""Gets the create_time of this DdlLogInfo.

        **参数解释**：  日志文件上传的创建时间。  **取值范围**：  不涉及。 

        :return: The create_time of this DdlLogInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DdlLogInfo.

        **参数解释**：  日志文件上传的创建时间。  **取值范围**：  不涉及。 

        :param create_time: The create_time of this DdlLogInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this DdlLogInfo.

        **参数解释**：  日志文件上传的结束时间。  **取值范围**：  不涉及。 

        :return: The end_time of this DdlLogInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this DdlLogInfo.

        **参数解释**：  日志文件上传的结束时间。  **取值范围**：  不涉及。 

        :param end_time: The end_time of this DdlLogInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this DdlLogInfo.

        **参数解释**：  日志文件的状态。  **取值范围**：  - Active：表示正常。 - Disable：表示不可用。 

        :return: The status of this DdlLogInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DdlLogInfo.

        **参数解释**：  日志文件的状态。  **取值范围**：  - Active：表示正常。 - Disable：表示不可用。 

        :param status: The status of this DdlLogInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, DdlLogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
