# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbObjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'x_language': 'str',
        'offset': 'int',
        'limit': 'int',
        'type': 'str',
        'db_names': 'list[str]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'x_language': 'X-Language',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'db_names': 'db_names'
    }

    def __init__(self, job_id=None, x_language=None, offset=None, limit=None, type=None, db_names=None):
        """ListDbObjectsRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param offset: 偏移量，表示查询该偏移量后面的记录。
        :type offset: int
        :param limit: 查询返回记录的数量限制。
        :type limit: int
        :param type: 查询对象信息类型。 取值： - source：查询源库对象信息。 - modified：查询已选择的（已同步的和未下发的）对象信息。 - synchronized：查询已同步的（已下发的）对象信息 ， 使用场景在任务处于全量中或者增量中。
        :type type: str
        :param db_names: 查询指定库的信息。
        :type db_names: list[str]
        """
        
        

        self._job_id = None
        self._x_language = None
        self._offset = None
        self._limit = None
        self._type = None
        self._db_names = None
        self.discriminator = None

        self.job_id = job_id
        if x_language is not None:
            self.x_language = x_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.type = type
        if db_names is not None:
            self.db_names = db_names

    @property
    def job_id(self):
        """Gets the job_id of this ListDbObjectsRequest.

        任务ID。

        :return: The job_id of this ListDbObjectsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListDbObjectsRequest.

        任务ID。

        :param job_id: The job_id of this ListDbObjectsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_language(self):
        """Gets the x_language of this ListDbObjectsRequest.

        请求语言类型。

        :return: The x_language of this ListDbObjectsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListDbObjectsRequest.

        请求语言类型。

        :param x_language: The x_language of this ListDbObjectsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def offset(self):
        """Gets the offset of this ListDbObjectsRequest.

        偏移量，表示查询该偏移量后面的记录。

        :return: The offset of this ListDbObjectsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDbObjectsRequest.

        偏移量，表示查询该偏移量后面的记录。

        :param offset: The offset of this ListDbObjectsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDbObjectsRequest.

        查询返回记录的数量限制。

        :return: The limit of this ListDbObjectsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDbObjectsRequest.

        查询返回记录的数量限制。

        :param limit: The limit of this ListDbObjectsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        """Gets the type of this ListDbObjectsRequest.

        查询对象信息类型。 取值： - source：查询源库对象信息。 - modified：查询已选择的（已同步的和未下发的）对象信息。 - synchronized：查询已同步的（已下发的）对象信息 ， 使用场景在任务处于全量中或者增量中。

        :return: The type of this ListDbObjectsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListDbObjectsRequest.

        查询对象信息类型。 取值： - source：查询源库对象信息。 - modified：查询已选择的（已同步的和未下发的）对象信息。 - synchronized：查询已同步的（已下发的）对象信息 ， 使用场景在任务处于全量中或者增量中。

        :param type: The type of this ListDbObjectsRequest.
        :type type: str
        """
        self._type = type

    @property
    def db_names(self):
        """Gets the db_names of this ListDbObjectsRequest.

        查询指定库的信息。

        :return: The db_names of this ListDbObjectsRequest.
        :rtype: list[str]
        """
        return self._db_names

    @db_names.setter
    def db_names(self, db_names):
        """Sets the db_names of this ListDbObjectsRequest.

        查询指定库的信息。

        :param db_names: The db_names of this ListDbObjectsRequest.
        :type db_names: list[str]
        """
        self._db_names = db_names

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
        if not isinstance(other, ListDbObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
