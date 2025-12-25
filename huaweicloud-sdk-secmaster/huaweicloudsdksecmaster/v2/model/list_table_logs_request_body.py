# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableLogsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query': 'str',
        '_from': 'int',
        'to': 'int',
        'limit': 'int',
        'offset': 'int',
        'script_params': 'list[SearchScriptParam]'
    }

    attribute_map = {
        'query': 'query',
        '_from': 'from',
        'to': 'to',
        'limit': 'limit',
        'offset': 'offset',
        'script_params': 'script_params'
    }

    def __init__(self, query=None, _from=None, to=None, limit=None, offset=None, script_params=None):
        r"""ListTableLogsRequestBody

        The model defined in huaweicloud sdk

        :param query: 检索查询条件, 语法介绍请参考帮助文档。
        :type query: str
        :param _from: 毫秒时间戳
        :type _from: int
        :param to: 毫秒时间戳
        :type to: int
        :param limit: 每页数量
        :type limit: int
        :param offset: 页号
        :type offset: int
        :param script_params: 脚本参数列表
        :type script_params: list[:class:`huaweicloudsdksecmaster.v2.SearchScriptParam`]
        """
        
        

        self._query = None
        self.__from = None
        self._to = None
        self._limit = None
        self._offset = None
        self._script_params = None
        self.discriminator = None

        self.query = query
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        self.limit = limit
        if offset is not None:
            self.offset = offset
        if script_params is not None:
            self.script_params = script_params

    @property
    def query(self):
        r"""Gets the query of this ListTableLogsRequestBody.

        检索查询条件, 语法介绍请参考帮助文档。

        :return: The query of this ListTableLogsRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this ListTableLogsRequestBody.

        检索查询条件, 语法介绍请参考帮助文档。

        :param query: The query of this ListTableLogsRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def _from(self):
        r"""Gets the _from of this ListTableLogsRequestBody.

        毫秒时间戳

        :return: The _from of this ListTableLogsRequestBody.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListTableLogsRequestBody.

        毫秒时间戳

        :param _from: The _from of this ListTableLogsRequestBody.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListTableLogsRequestBody.

        毫秒时间戳

        :return: The to of this ListTableLogsRequestBody.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListTableLogsRequestBody.

        毫秒时间戳

        :param to: The to of this ListTableLogsRequestBody.
        :type to: int
        """
        self._to = to

    @property
    def limit(self):
        r"""Gets the limit of this ListTableLogsRequestBody.

        每页数量

        :return: The limit of this ListTableLogsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTableLogsRequestBody.

        每页数量

        :param limit: The limit of this ListTableLogsRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTableLogsRequestBody.

        页号

        :return: The offset of this ListTableLogsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTableLogsRequestBody.

        页号

        :param offset: The offset of this ListTableLogsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def script_params(self):
        r"""Gets the script_params of this ListTableLogsRequestBody.

        脚本参数列表

        :return: The script_params of this ListTableLogsRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.SearchScriptParam`]
        """
        return self._script_params

    @script_params.setter
    def script_params(self, script_params):
        r"""Sets the script_params of this ListTableLogsRequestBody.

        脚本参数列表

        :param script_params: The script_params of this ListTableLogsRequestBody.
        :type script_params: list[:class:`huaweicloudsdksecmaster.v2.SearchScriptParam`]
        """
        self._script_params = script_params

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
        if not isinstance(other, ListTableLogsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
