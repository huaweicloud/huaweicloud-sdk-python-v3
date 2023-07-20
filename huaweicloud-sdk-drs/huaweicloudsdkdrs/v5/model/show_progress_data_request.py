# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProgressDataRequest:

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
        'offset': 'int',
        'limit': 'int',
        'type': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_id': 'job_id',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type'
    }

    def __init__(self, x_language=None, job_id=None, offset=None, limit=None, type=None):
        """ShowProgressDataRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param job_id: 任务ID。
        :type job_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0
        :type offset: int
        :param limit: 每页显示的条目数量。默认为10，取值范围【1-1000】
        :type limit: int
        :param type: 迁移对象类型。 - table - event - table_structure - procedure - view - function - database - trigger - table_indexs
        :type type: str
        """
        
        

        self._x_language = None
        self._job_id = None
        self._offset = None
        self._limit = None
        self._type = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_id = job_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.type = type

    @property
    def x_language(self):
        """Gets the x_language of this ShowProgressDataRequest.

        请求语言类型。

        :return: The x_language of this ShowProgressDataRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowProgressDataRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowProgressDataRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def job_id(self):
        """Gets the job_id of this ShowProgressDataRequest.

        任务ID。

        :return: The job_id of this ShowProgressDataRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowProgressDataRequest.

        任务ID。

        :param job_id: The job_id of this ShowProgressDataRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def offset(self):
        """Gets the offset of this ShowProgressDataRequest.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :return: The offset of this ShowProgressDataRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowProgressDataRequest.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :param offset: The offset of this ShowProgressDataRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowProgressDataRequest.

        每页显示的条目数量。默认为10，取值范围【1-1000】

        :return: The limit of this ShowProgressDataRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowProgressDataRequest.

        每页显示的条目数量。默认为10，取值范围【1-1000】

        :param limit: The limit of this ShowProgressDataRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        """Gets the type of this ShowProgressDataRequest.

        迁移对象类型。 - table - event - table_structure - procedure - view - function - database - trigger - table_indexs

        :return: The type of this ShowProgressDataRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowProgressDataRequest.

        迁移对象类型。 - table - event - table_structure - procedure - view - function - database - trigger - table_indexs

        :param type: The type of this ShowProgressDataRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowProgressDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
