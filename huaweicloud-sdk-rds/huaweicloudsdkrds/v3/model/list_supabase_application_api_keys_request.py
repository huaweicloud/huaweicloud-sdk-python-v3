# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSupabaseApplicationApiKeysRequest:

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
        'application_id': 'str',
        'name': 'str',
        'id': 'str',
        'status': 'str',
        'type': 'str',
        'start_created_time': 'str',
        'end_created_time': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'application_id': 'application_id',
        'name': 'name',
        'id': 'id',
        'status': 'status',
        'type': 'type',
        'start_created_time': 'start_created_time',
        'end_created_time': 'end_created_time',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, application_id=None, name=None, id=None, status=None, type=None, start_created_time=None, end_created_time=None, sort_key=None, sort_dir=None, offset=None, limit=None):
        r"""ListSupabaseApplicationApiKeysRequest

        The model defined in huaweicloud sdk

        :param x_language: 
        :type x_language: str
        :param application_id: 
        :type application_id: str
        :param name: 
        :type name: str
        :param id: 
        :type id: str
        :param status: 
        :type status: str
        :param type: 
        :type type: str
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
        self._application_id = None
        self._name = None
        self._id = None
        self._status = None
        self._type = None
        self._start_created_time = None
        self._end_created_time = None
        self._sort_key = None
        self._sort_dir = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.application_id = application_id
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
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
        r"""Gets the x_language of this ListSupabaseApplicationApiKeysRequest.

        :return: The x_language of this ListSupabaseApplicationApiKeysRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListSupabaseApplicationApiKeysRequest.

        :param x_language: The x_language of this ListSupabaseApplicationApiKeysRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def application_id(self):
        r"""Gets the application_id of this ListSupabaseApplicationApiKeysRequest.

        :return: The application_id of this ListSupabaseApplicationApiKeysRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ListSupabaseApplicationApiKeysRequest.

        :param application_id: The application_id of this ListSupabaseApplicationApiKeysRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def name(self):
        r"""Gets the name of this ListSupabaseApplicationApiKeysRequest.

        :return: The name of this ListSupabaseApplicationApiKeysRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSupabaseApplicationApiKeysRequest.

        :param name: The name of this ListSupabaseApplicationApiKeysRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ListSupabaseApplicationApiKeysRequest.

        :return: The id of this ListSupabaseApplicationApiKeysRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSupabaseApplicationApiKeysRequest.

        :param id: The id of this ListSupabaseApplicationApiKeysRequest.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ListSupabaseApplicationApiKeysRequest.

        :return: The status of this ListSupabaseApplicationApiKeysRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSupabaseApplicationApiKeysRequest.

        :param status: The status of this ListSupabaseApplicationApiKeysRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListSupabaseApplicationApiKeysRequest.

        :return: The type of this ListSupabaseApplicationApiKeysRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListSupabaseApplicationApiKeysRequest.

        :param type: The type of this ListSupabaseApplicationApiKeysRequest.
        :type type: str
        """
        self._type = type

    @property
    def start_created_time(self):
        r"""Gets the start_created_time of this ListSupabaseApplicationApiKeysRequest.

        :return: The start_created_time of this ListSupabaseApplicationApiKeysRequest.
        :rtype: str
        """
        return self._start_created_time

    @start_created_time.setter
    def start_created_time(self, start_created_time):
        r"""Sets the start_created_time of this ListSupabaseApplicationApiKeysRequest.

        :param start_created_time: The start_created_time of this ListSupabaseApplicationApiKeysRequest.
        :type start_created_time: str
        """
        self._start_created_time = start_created_time

    @property
    def end_created_time(self):
        r"""Gets the end_created_time of this ListSupabaseApplicationApiKeysRequest.

        :return: The end_created_time of this ListSupabaseApplicationApiKeysRequest.
        :rtype: str
        """
        return self._end_created_time

    @end_created_time.setter
    def end_created_time(self, end_created_time):
        r"""Sets the end_created_time of this ListSupabaseApplicationApiKeysRequest.

        :param end_created_time: The end_created_time of this ListSupabaseApplicationApiKeysRequest.
        :type end_created_time: str
        """
        self._end_created_time = end_created_time

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListSupabaseApplicationApiKeysRequest.

        :return: The sort_key of this ListSupabaseApplicationApiKeysRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListSupabaseApplicationApiKeysRequest.

        :param sort_key: The sort_key of this ListSupabaseApplicationApiKeysRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListSupabaseApplicationApiKeysRequest.

        :return: The sort_dir of this ListSupabaseApplicationApiKeysRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListSupabaseApplicationApiKeysRequest.

        :param sort_dir: The sort_dir of this ListSupabaseApplicationApiKeysRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def offset(self):
        r"""Gets the offset of this ListSupabaseApplicationApiKeysRequest.

        :return: The offset of this ListSupabaseApplicationApiKeysRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSupabaseApplicationApiKeysRequest.

        :param offset: The offset of this ListSupabaseApplicationApiKeysRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSupabaseApplicationApiKeysRequest.

        :return: The limit of this ListSupabaseApplicationApiKeysRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSupabaseApplicationApiKeysRequest.

        :param limit: The limit of this ListSupabaseApplicationApiKeysRequest.
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
        if not isinstance(other, ListSupabaseApplicationApiKeysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
