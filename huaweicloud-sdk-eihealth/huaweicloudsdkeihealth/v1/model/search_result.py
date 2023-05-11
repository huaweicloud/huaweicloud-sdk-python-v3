# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'smiles': 'str',
        'databases': 'list[str]',
        'top_n': 'int',
        'prop_names': 'list[str]',
        'query': 'PlainMoleculeItem',
        'result': 'list[SearchResultItem]'
    }

    attribute_map = {
        'smiles': 'smiles',
        'databases': 'databases',
        'top_n': 'top_n',
        'prop_names': 'prop_names',
        'query': 'query',
        'result': 'result'
    }

    def __init__(self, smiles=None, databases=None, top_n=None, prop_names=None, query=None, result=None):
        """SearchResult

        The model defined in huaweicloud sdk

        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param databases: 搜索使用到的数据库集合
        :type databases: list[str]
        :param top_n: 期望返回的条目数
        :type top_n: int
        :param prop_names: 分子ADMET属性名列表
        :type prop_names: list[str]
        :param query: 
        :type query: :class:`huaweicloudsdkeihealth.v1.PlainMoleculeItem`
        :param result: 查询结果列表
        :type result: list[:class:`huaweicloudsdkeihealth.v1.SearchResultItem`]
        """
        
        

        self._smiles = None
        self._databases = None
        self._top_n = None
        self._prop_names = None
        self._query = None
        self._result = None
        self.discriminator = None

        self.smiles = smiles
        self.databases = databases
        self.top_n = top_n
        self.prop_names = prop_names
        self.query = query
        self.result = result

    @property
    def smiles(self):
        """Gets the smiles of this SearchResult.

        分子SMILES表达式

        :return: The smiles of this SearchResult.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this SearchResult.

        分子SMILES表达式

        :param smiles: The smiles of this SearchResult.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def databases(self):
        """Gets the databases of this SearchResult.

        搜索使用到的数据库集合

        :return: The databases of this SearchResult.
        :rtype: list[str]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this SearchResult.

        搜索使用到的数据库集合

        :param databases: The databases of this SearchResult.
        :type databases: list[str]
        """
        self._databases = databases

    @property
    def top_n(self):
        """Gets the top_n of this SearchResult.

        期望返回的条目数

        :return: The top_n of this SearchResult.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        """Sets the top_n of this SearchResult.

        期望返回的条目数

        :param top_n: The top_n of this SearchResult.
        :type top_n: int
        """
        self._top_n = top_n

    @property
    def prop_names(self):
        """Gets the prop_names of this SearchResult.

        分子ADMET属性名列表

        :return: The prop_names of this SearchResult.
        :rtype: list[str]
        """
        return self._prop_names

    @prop_names.setter
    def prop_names(self, prop_names):
        """Sets the prop_names of this SearchResult.

        分子ADMET属性名列表

        :param prop_names: The prop_names of this SearchResult.
        :type prop_names: list[str]
        """
        self._prop_names = prop_names

    @property
    def query(self):
        """Gets the query of this SearchResult.

        :return: The query of this SearchResult.
        :rtype: :class:`huaweicloudsdkeihealth.v1.PlainMoleculeItem`
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchResult.

        :param query: The query of this SearchResult.
        :type query: :class:`huaweicloudsdkeihealth.v1.PlainMoleculeItem`
        """
        self._query = query

    @property
    def result(self):
        """Gets the result of this SearchResult.

        查询结果列表

        :return: The result of this SearchResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.SearchResultItem`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this SearchResult.

        查询结果列表

        :param result: The result of this SearchResult.
        :type result: list[:class:`huaweicloudsdkeihealth.v1.SearchResultItem`]
        """
        self._result = result

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
        if not isinstance(other, SearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
