# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiApplicationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'name': 'str',
        'id': 'str',
        'type': 'str',
        'mode': 'str',
        'status': 'str',
        'managed_instance_id': 'str',
        'managed_instance_name': 'str',
        'enable_ssl': 'bool',
        'start_created_time': 'str',
        'end_created_time': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'name': 'name',
        'id': 'id',
        'type': 'type',
        'mode': 'mode',
        'status': 'status',
        'managed_instance_id': 'managed_instance_id',
        'managed_instance_name': 'managed_instance_name',
        'enable_ssl': 'enable_ssl',
        'start_created_time': 'start_created_time',
        'end_created_time': 'end_created_time',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, name=None, id=None, type=None, mode=None, status=None, managed_instance_id=None, managed_instance_name=None, enable_ssl=None, start_created_time=None, end_created_time=None, sort_key=None, sort_dir=None, offset=None, limit=None):
        r"""ListAiApplicationsRequest

        The model defined in huaweicloud sdk

        :param x_language: 
        :type x_language: str
        :param name: 按应用名称查询。
        :type name: str
        :param id: 按应用ID查询。
        :type id: str
        :param type: 按应用类型查询。Supabase传supabase。
        :type type: str
        :param mode: 按部署模式查询。
        :type mode: str
        :param status: 按状态查询。
        :type status: str
        :param managed_instance_id: 按关联PG实例ID查询。
        :type managed_instance_id: str
        :param managed_instance_name: 按关联PG实例名称查询。
        :type managed_instance_name: str
        :param enable_ssl: 按是否开启SSL查询。
        :type enable_ssl: bool
        :param start_created_time: 
        :type start_created_time: str
        :param end_created_time: 
        :type end_created_time: str
        :param sort_key: 
        :type sort_key: str
        :param sort_dir: 
        :type sort_dir: str
        :param offset: 
        :type offset: int
        :param limit: 
        :type limit: int
        """
        
        

        self._x_language = None
        self._name = None
        self._id = None
        self._type = None
        self._mode = None
        self._status = None
        self._managed_instance_id = None
        self._managed_instance_name = None
        self._enable_ssl = None
        self._start_created_time = None
        self._end_created_time = None
        self._sort_key = None
        self._sort_dir = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if mode is not None:
            self.mode = mode
        if status is not None:
            self.status = status
        if managed_instance_id is not None:
            self.managed_instance_id = managed_instance_id
        if managed_instance_name is not None:
            self.managed_instance_name = managed_instance_name
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if start_created_time is not None:
            self.start_created_time = start_created_time
        if end_created_time is not None:
            self.end_created_time = end_created_time
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListAiApplicationsRequest.

        :return: The x_language of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListAiApplicationsRequest.

        :param x_language: The x_language of this ListAiApplicationsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def name(self):
        r"""Gets the name of this ListAiApplicationsRequest.

        按应用名称查询。

        :return: The name of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAiApplicationsRequest.

        按应用名称查询。

        :param name: The name of this ListAiApplicationsRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ListAiApplicationsRequest.

        按应用ID查询。

        :return: The id of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAiApplicationsRequest.

        按应用ID查询。

        :param id: The id of this ListAiApplicationsRequest.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ListAiApplicationsRequest.

        按应用类型查询。Supabase传supabase。

        :return: The type of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAiApplicationsRequest.

        按应用类型查询。Supabase传supabase。

        :param type: The type of this ListAiApplicationsRequest.
        :type type: str
        """
        self._type = type

    @property
    def mode(self):
        r"""Gets the mode of this ListAiApplicationsRequest.

        按部署模式查询。

        :return: The mode of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ListAiApplicationsRequest.

        按部署模式查询。

        :param mode: The mode of this ListAiApplicationsRequest.
        :type mode: str
        """
        self._mode = mode

    @property
    def status(self):
        r"""Gets the status of this ListAiApplicationsRequest.

        按状态查询。

        :return: The status of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAiApplicationsRequest.

        按状态查询。

        :param status: The status of this ListAiApplicationsRequest.
        :type status: str
        """
        self._status = status

    @property
    def managed_instance_id(self):
        r"""Gets the managed_instance_id of this ListAiApplicationsRequest.

        按关联PG实例ID查询。

        :return: The managed_instance_id of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        r"""Sets the managed_instance_id of this ListAiApplicationsRequest.

        按关联PG实例ID查询。

        :param managed_instance_id: The managed_instance_id of this ListAiApplicationsRequest.
        :type managed_instance_id: str
        """
        self._managed_instance_id = managed_instance_id

    @property
    def managed_instance_name(self):
        r"""Gets the managed_instance_name of this ListAiApplicationsRequest.

        按关联PG实例名称查询。

        :return: The managed_instance_name of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._managed_instance_name

    @managed_instance_name.setter
    def managed_instance_name(self, managed_instance_name):
        r"""Sets the managed_instance_name of this ListAiApplicationsRequest.

        按关联PG实例名称查询。

        :param managed_instance_name: The managed_instance_name of this ListAiApplicationsRequest.
        :type managed_instance_name: str
        """
        self._managed_instance_name = managed_instance_name

    @property
    def enable_ssl(self):
        r"""Gets the enable_ssl of this ListAiApplicationsRequest.

        按是否开启SSL查询。

        :return: The enable_ssl of this ListAiApplicationsRequest.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        r"""Sets the enable_ssl of this ListAiApplicationsRequest.

        按是否开启SSL查询。

        :param enable_ssl: The enable_ssl of this ListAiApplicationsRequest.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def start_created_time(self):
        r"""Gets the start_created_time of this ListAiApplicationsRequest.

        :return: The start_created_time of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._start_created_time

    @start_created_time.setter
    def start_created_time(self, start_created_time):
        r"""Sets the start_created_time of this ListAiApplicationsRequest.

        :param start_created_time: The start_created_time of this ListAiApplicationsRequest.
        :type start_created_time: str
        """
        self._start_created_time = start_created_time

    @property
    def end_created_time(self):
        r"""Gets the end_created_time of this ListAiApplicationsRequest.

        :return: The end_created_time of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._end_created_time

    @end_created_time.setter
    def end_created_time(self, end_created_time):
        r"""Sets the end_created_time of this ListAiApplicationsRequest.

        :param end_created_time: The end_created_time of this ListAiApplicationsRequest.
        :type end_created_time: str
        """
        self._end_created_time = end_created_time

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListAiApplicationsRequest.

        :return: The sort_key of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListAiApplicationsRequest.

        :param sort_key: The sort_key of this ListAiApplicationsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListAiApplicationsRequest.

        :return: The sort_dir of this ListAiApplicationsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListAiApplicationsRequest.

        :param sort_dir: The sort_dir of this ListAiApplicationsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def offset(self):
        r"""Gets the offset of this ListAiApplicationsRequest.

        :return: The offset of this ListAiApplicationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAiApplicationsRequest.

        :param offset: The offset of this ListAiApplicationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAiApplicationsRequest.

        :return: The limit of this ListAiApplicationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAiApplicationsRequest.

        :param limit: The limit of this ListAiApplicationsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAiApplicationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
