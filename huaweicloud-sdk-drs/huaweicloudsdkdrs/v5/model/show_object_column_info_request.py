# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowObjectColumnInfoRequest:

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
        'job_id': 'str',
        'object_id': 'str',
        'is_refresh': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_id': 'job_id',
        'object_id': 'object_id',
        'is_refresh': 'is_refresh',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, x_language=None, job_id=None, object_id=None, is_refresh=None, limit=None, offset=None):
        r"""ShowObjectColumnInfoRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param job_id: 任务ID。
        :type job_id: str
        :param object_id: 对象id。不填时默认查询库级的对象。
        :type object_id: str
        :param is_refresh: 是否强制刷新查询结果
        :type is_refresh: bool
        :param limit: 查询返回记录的数量限制，默认为10。
        :type limit: int
        :param offset: 偏移量，表示查询该偏移量后面的记录，默认为0。
        :type offset: int
        """
        
        

        self._x_language = None
        self._job_id = None
        self._object_id = None
        self._is_refresh = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_id = job_id
        if object_id is not None:
            self.object_id = object_id
        if is_refresh is not None:
            self.is_refresh = is_refresh
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowObjectColumnInfoRequest.

        请求语言类型。

        :return: The x_language of this ShowObjectColumnInfoRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowObjectColumnInfoRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowObjectColumnInfoRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowObjectColumnInfoRequest.

        任务ID。

        :return: The job_id of this ShowObjectColumnInfoRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowObjectColumnInfoRequest.

        任务ID。

        :param job_id: The job_id of this ShowObjectColumnInfoRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def object_id(self):
        r"""Gets the object_id of this ShowObjectColumnInfoRequest.

        对象id。不填时默认查询库级的对象。

        :return: The object_id of this ShowObjectColumnInfoRequest.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ShowObjectColumnInfoRequest.

        对象id。不填时默认查询库级的对象。

        :param object_id: The object_id of this ShowObjectColumnInfoRequest.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def is_refresh(self):
        r"""Gets the is_refresh of this ShowObjectColumnInfoRequest.

        是否强制刷新查询结果

        :return: The is_refresh of this ShowObjectColumnInfoRequest.
        :rtype: bool
        """
        return self._is_refresh

    @is_refresh.setter
    def is_refresh(self, is_refresh):
        r"""Sets the is_refresh of this ShowObjectColumnInfoRequest.

        是否强制刷新查询结果

        :param is_refresh: The is_refresh of this ShowObjectColumnInfoRequest.
        :type is_refresh: bool
        """
        self._is_refresh = is_refresh

    @property
    def limit(self):
        r"""Gets the limit of this ShowObjectColumnInfoRequest.

        查询返回记录的数量限制，默认为10。

        :return: The limit of this ShowObjectColumnInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowObjectColumnInfoRequest.

        查询返回记录的数量限制，默认为10。

        :param limit: The limit of this ShowObjectColumnInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowObjectColumnInfoRequest.

        偏移量，表示查询该偏移量后面的记录，默认为0。

        :return: The offset of this ShowObjectColumnInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowObjectColumnInfoRequest.

        偏移量，表示查询该偏移量后面的记录，默认为0。

        :param offset: The offset of this ShowObjectColumnInfoRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowObjectColumnInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
