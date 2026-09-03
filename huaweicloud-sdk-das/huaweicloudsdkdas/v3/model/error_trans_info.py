# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorTransInfo:

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
        'object_key': 'str',
        'begin_position': 'int',
        'end_position': 'int',
        'db_name': 'str',
        'tb_name': 'str',
        'create_time': 'datetime',
        'error_msg': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'file_name',
        'object_key': 'object_key',
        'begin_position': 'begin_position',
        'end_position': 'end_position',
        'db_name': 'db_name',
        'tb_name': 'tb_name',
        'create_time': 'create_time',
        'error_msg': 'error_msg'
    }

    def __init__(self, id=None, file_name=None, object_key=None, begin_position=None, end_position=None, db_name=None, tb_name=None, create_time=None, error_msg=None):
        r"""ErrorTransInfo

        The model defined in huaweicloud sdk

        :param id: 解析任务ID
        :type id: int
        :param file_name: 文件名称
        :type file_name: str
        :param object_key: 对象键
        :type object_key: str
        :param begin_position: 解析开始位置
        :type begin_position: int
        :param end_position: 解析结束位置
        :type end_position: int
        :param db_name: 数据库名称
        :type db_name: str
        :param tb_name: 表名称
        :type tb_name: str
        :param create_time: 任务创建时间，单位毫秒
        :type create_time: datetime
        :param error_msg: 错误信息
        :type error_msg: str
        """
        
        

        self._id = None
        self._file_name = None
        self._object_key = None
        self._begin_position = None
        self._end_position = None
        self._db_name = None
        self._tb_name = None
        self._create_time = None
        self._error_msg = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file_name is not None:
            self.file_name = file_name
        if object_key is not None:
            self.object_key = object_key
        if begin_position is not None:
            self.begin_position = begin_position
        if end_position is not None:
            self.end_position = end_position
        if db_name is not None:
            self.db_name = db_name
        if tb_name is not None:
            self.tb_name = tb_name
        if create_time is not None:
            self.create_time = create_time
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def id(self):
        r"""Gets the id of this ErrorTransInfo.

        解析任务ID

        :return: The id of this ErrorTransInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ErrorTransInfo.

        解析任务ID

        :param id: The id of this ErrorTransInfo.
        :type id: int
        """
        self._id = id

    @property
    def file_name(self):
        r"""Gets the file_name of this ErrorTransInfo.

        文件名称

        :return: The file_name of this ErrorTransInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ErrorTransInfo.

        文件名称

        :param file_name: The file_name of this ErrorTransInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def object_key(self):
        r"""Gets the object_key of this ErrorTransInfo.

        对象键

        :return: The object_key of this ErrorTransInfo.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        r"""Sets the object_key of this ErrorTransInfo.

        对象键

        :param object_key: The object_key of this ErrorTransInfo.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def begin_position(self):
        r"""Gets the begin_position of this ErrorTransInfo.

        解析开始位置

        :return: The begin_position of this ErrorTransInfo.
        :rtype: int
        """
        return self._begin_position

    @begin_position.setter
    def begin_position(self, begin_position):
        r"""Sets the begin_position of this ErrorTransInfo.

        解析开始位置

        :param begin_position: The begin_position of this ErrorTransInfo.
        :type begin_position: int
        """
        self._begin_position = begin_position

    @property
    def end_position(self):
        r"""Gets the end_position of this ErrorTransInfo.

        解析结束位置

        :return: The end_position of this ErrorTransInfo.
        :rtype: int
        """
        return self._end_position

    @end_position.setter
    def end_position(self, end_position):
        r"""Sets the end_position of this ErrorTransInfo.

        解析结束位置

        :param end_position: The end_position of this ErrorTransInfo.
        :type end_position: int
        """
        self._end_position = end_position

    @property
    def db_name(self):
        r"""Gets the db_name of this ErrorTransInfo.

        数据库名称

        :return: The db_name of this ErrorTransInfo.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ErrorTransInfo.

        数据库名称

        :param db_name: The db_name of this ErrorTransInfo.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def tb_name(self):
        r"""Gets the tb_name of this ErrorTransInfo.

        表名称

        :return: The tb_name of this ErrorTransInfo.
        :rtype: str
        """
        return self._tb_name

    @tb_name.setter
    def tb_name(self, tb_name):
        r"""Sets the tb_name of this ErrorTransInfo.

        表名称

        :param tb_name: The tb_name of this ErrorTransInfo.
        :type tb_name: str
        """
        self._tb_name = tb_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ErrorTransInfo.

        任务创建时间，单位毫秒

        :return: The create_time of this ErrorTransInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ErrorTransInfo.

        任务创建时间，单位毫秒

        :param create_time: The create_time of this ErrorTransInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ErrorTransInfo.

        错误信息

        :return: The error_msg of this ErrorTransInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ErrorTransInfo.

        错误信息

        :param error_msg: The error_msg of this ErrorTransInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ErrorTransInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
