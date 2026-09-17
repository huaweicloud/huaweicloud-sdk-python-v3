# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLogArchiveDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'file_name': 'str',
        'log_start_time': 'int',
        'log_end_time': 'int',
        'file_size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'file_name',
        'log_start_time': 'log_start_time',
        'log_end_time': 'log_end_time',
        'file_size': 'file_size'
    }

    def __init__(self, id=None, file_name=None, log_start_time=None, log_end_time=None, file_size=None):
        r"""SlowLogArchiveDto

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: int
        :param file_name: 文件名
        :type file_name: str
        :param log_start_time: 日志开始时间
        :type log_start_time: int
        :param log_end_time: 日志结束时间
        :type log_end_time: int
        :param file_size: 文件大小
        :type file_size: int
        """
        
        

        self._id = None
        self._file_name = None
        self._log_start_time = None
        self._log_end_time = None
        self._file_size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file_name is not None:
            self.file_name = file_name
        if log_start_time is not None:
            self.log_start_time = log_start_time
        if log_end_time is not None:
            self.log_end_time = log_end_time
        if file_size is not None:
            self.file_size = file_size

    @property
    def id(self):
        r"""Gets the id of this SlowLogArchiveDto.

        ID

        :return: The id of this SlowLogArchiveDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SlowLogArchiveDto.

        ID

        :param id: The id of this SlowLogArchiveDto.
        :type id: int
        """
        self._id = id

    @property
    def file_name(self):
        r"""Gets the file_name of this SlowLogArchiveDto.

        文件名

        :return: The file_name of this SlowLogArchiveDto.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this SlowLogArchiveDto.

        文件名

        :param file_name: The file_name of this SlowLogArchiveDto.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def log_start_time(self):
        r"""Gets the log_start_time of this SlowLogArchiveDto.

        日志开始时间

        :return: The log_start_time of this SlowLogArchiveDto.
        :rtype: int
        """
        return self._log_start_time

    @log_start_time.setter
    def log_start_time(self, log_start_time):
        r"""Sets the log_start_time of this SlowLogArchiveDto.

        日志开始时间

        :param log_start_time: The log_start_time of this SlowLogArchiveDto.
        :type log_start_time: int
        """
        self._log_start_time = log_start_time

    @property
    def log_end_time(self):
        r"""Gets the log_end_time of this SlowLogArchiveDto.

        日志结束时间

        :return: The log_end_time of this SlowLogArchiveDto.
        :rtype: int
        """
        return self._log_end_time

    @log_end_time.setter
    def log_end_time(self, log_end_time):
        r"""Sets the log_end_time of this SlowLogArchiveDto.

        日志结束时间

        :param log_end_time: The log_end_time of this SlowLogArchiveDto.
        :type log_end_time: int
        """
        self._log_end_time = log_end_time

    @property
    def file_size(self):
        r"""Gets the file_size of this SlowLogArchiveDto.

        文件大小

        :return: The file_size of this SlowLogArchiveDto.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this SlowLogArchiveDto.

        文件大小

        :param file_size: The file_size of this SlowLogArchiveDto.
        :type file_size: int
        """
        self._file_size = file_size

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
        if not isinstance(other, SlowLogArchiveDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
