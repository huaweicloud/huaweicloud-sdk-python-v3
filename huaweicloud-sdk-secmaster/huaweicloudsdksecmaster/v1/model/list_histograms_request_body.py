# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistogramsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataspace_id': 'str',
        '_from': 'int',
        'pipe_id': 'str',
        'query': 'str',
        'to': 'int'
    }

    attribute_map = {
        'dataspace_id': 'dataspace_id',
        '_from': 'from',
        'pipe_id': 'pipe_id',
        'query': 'query',
        'to': 'to'
    }

    def __init__(self, dataspace_id=None, _from=None, pipe_id=None, query=None, to=None):
        r"""ListHistogramsRequestBody

        The model defined in huaweicloud sdk

        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param _from: 查询开始时间点
        :type _from: int
        :param pipe_id: 数据管道ID
        :type pipe_id: str
        :param query: 查询语句
        :type query: str
        :param to: 查询结束时间点
        :type to: int
        """
        
        

        self._dataspace_id = None
        self.__from = None
        self._pipe_id = None
        self._query = None
        self._to = None
        self.discriminator = None

        self.dataspace_id = dataspace_id
        self._from = _from
        self.pipe_id = pipe_id
        self.query = query
        self.to = to

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this ListHistogramsRequestBody.

        数据空间ID

        :return: The dataspace_id of this ListHistogramsRequestBody.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this ListHistogramsRequestBody.

        数据空间ID

        :param dataspace_id: The dataspace_id of this ListHistogramsRequestBody.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def _from(self):
        r"""Gets the _from of this ListHistogramsRequestBody.

        查询开始时间点

        :return: The _from of this ListHistogramsRequestBody.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListHistogramsRequestBody.

        查询开始时间点

        :param _from: The _from of this ListHistogramsRequestBody.
        :type _from: int
        """
        self.__from = _from

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this ListHistogramsRequestBody.

        数据管道ID

        :return: The pipe_id of this ListHistogramsRequestBody.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this ListHistogramsRequestBody.

        数据管道ID

        :param pipe_id: The pipe_id of this ListHistogramsRequestBody.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def query(self):
        r"""Gets the query of this ListHistogramsRequestBody.

        查询语句

        :return: The query of this ListHistogramsRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this ListHistogramsRequestBody.

        查询语句

        :param query: The query of this ListHistogramsRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def to(self):
        r"""Gets the to of this ListHistogramsRequestBody.

        查询结束时间点

        :return: The to of this ListHistogramsRequestBody.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListHistogramsRequestBody.

        查询结束时间点

        :param to: The to of this ListHistogramsRequestBody.
        :type to: int
        """
        self._to = to

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
        if not isinstance(other, ListHistogramsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
