# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableHistogramsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_from': 'int',
        'to': 'int',
        'query': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'query': 'query'
    }

    def __init__(self, _from=None, to=None, query=None):
        r"""ListTableHistogramsRequestBody

        The model defined in huaweicloud sdk

        :param _from: 毫秒时间戳
        :type _from: int
        :param to: 毫秒时间戳
        :type to: int
        :param query: 检索查询条件, 语法介绍请参考帮助文档。
        :type query: str
        """
        
        

        self.__from = None
        self._to = None
        self._query = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        self.query = query

    @property
    def _from(self):
        r"""Gets the _from of this ListTableHistogramsRequestBody.

        毫秒时间戳

        :return: The _from of this ListTableHistogramsRequestBody.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListTableHistogramsRequestBody.

        毫秒时间戳

        :param _from: The _from of this ListTableHistogramsRequestBody.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListTableHistogramsRequestBody.

        毫秒时间戳

        :return: The to of this ListTableHistogramsRequestBody.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListTableHistogramsRequestBody.

        毫秒时间戳

        :param to: The to of this ListTableHistogramsRequestBody.
        :type to: int
        """
        self._to = to

    @property
    def query(self):
        r"""Gets the query of this ListTableHistogramsRequestBody.

        检索查询条件, 语法介绍请参考帮助文档。

        :return: The query of this ListTableHistogramsRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this ListTableHistogramsRequestBody.

        检索查询条件, 语法介绍请参考帮助文档。

        :param query: The query of this ListTableHistogramsRequestBody.
        :type query: str
        """
        self._query = query

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
        if not isinstance(other, ListTableHistogramsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
