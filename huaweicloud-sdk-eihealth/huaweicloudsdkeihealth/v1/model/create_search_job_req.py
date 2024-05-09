# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSearchJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'CreateDrugJobBasicInfo',
        'smiles': 'str',
        'scaffold': 'str',
        'top_n': 'int',
        'databases': 'list[str]',
        'custom_databases': 'list[str]',
        'model_ids': 'list[str]',
        'search_method': 'SearchType'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'smiles': 'smiles',
        'scaffold': 'scaffold',
        'top_n': 'top_n',
        'databases': 'databases',
        'custom_databases': 'custom_databases',
        'model_ids': 'model_ids',
        'search_method': 'search_method'
    }

    def __init__(self, basic_info=None, smiles=None, scaffold=None, top_n=None, databases=None, custom_databases=None, model_ids=None, search_method=None):
        """CreateSearchJobReq

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param scaffold: 分子骨架表达式
        :type scaffold: str
        :param top_n: 最相似的top_n个
        :type top_n: int
        :param databases: 可供搜索分子的公共数据库名称列表
        :type databases: list[str]
        :param custom_databases: 可供搜索分子的自定义数据库id列表
        :type custom_databases: list[str]
        :param model_ids: 模型id列表
        :type model_ids: list[str]
        :param search_method: 
        :type search_method: :class:`huaweicloudsdkeihealth.v1.SearchType`
        """
        
        

        self._basic_info = None
        self._smiles = None
        self._scaffold = None
        self._top_n = None
        self._databases = None
        self._custom_databases = None
        self._model_ids = None
        self._search_method = None
        self.discriminator = None

        self.basic_info = basic_info
        self.smiles = smiles
        if scaffold is not None:
            self.scaffold = scaffold
        if top_n is not None:
            self.top_n = top_n
        if databases is not None:
            self.databases = databases
        if custom_databases is not None:
            self.custom_databases = custom_databases
        if model_ids is not None:
            self.model_ids = model_ids
        if search_method is not None:
            self.search_method = search_method

    @property
    def basic_info(self):
        """Gets the basic_info of this CreateSearchJobReq.

        :return: The basic_info of this CreateSearchJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this CreateSearchJobReq.

        :param basic_info: The basic_info of this CreateSearchJobReq.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        self._basic_info = basic_info

    @property
    def smiles(self):
        """Gets the smiles of this CreateSearchJobReq.

        分子SMILES表达式

        :return: The smiles of this CreateSearchJobReq.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this CreateSearchJobReq.

        分子SMILES表达式

        :param smiles: The smiles of this CreateSearchJobReq.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def scaffold(self):
        """Gets the scaffold of this CreateSearchJobReq.

        分子骨架表达式

        :return: The scaffold of this CreateSearchJobReq.
        :rtype: str
        """
        return self._scaffold

    @scaffold.setter
    def scaffold(self, scaffold):
        """Sets the scaffold of this CreateSearchJobReq.

        分子骨架表达式

        :param scaffold: The scaffold of this CreateSearchJobReq.
        :type scaffold: str
        """
        self._scaffold = scaffold

    @property
    def top_n(self):
        """Gets the top_n of this CreateSearchJobReq.

        最相似的top_n个

        :return: The top_n of this CreateSearchJobReq.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        """Sets the top_n of this CreateSearchJobReq.

        最相似的top_n个

        :param top_n: The top_n of this CreateSearchJobReq.
        :type top_n: int
        """
        self._top_n = top_n

    @property
    def databases(self):
        """Gets the databases of this CreateSearchJobReq.

        可供搜索分子的公共数据库名称列表

        :return: The databases of this CreateSearchJobReq.
        :rtype: list[str]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this CreateSearchJobReq.

        可供搜索分子的公共数据库名称列表

        :param databases: The databases of this CreateSearchJobReq.
        :type databases: list[str]
        """
        self._databases = databases

    @property
    def custom_databases(self):
        """Gets the custom_databases of this CreateSearchJobReq.

        可供搜索分子的自定义数据库id列表

        :return: The custom_databases of this CreateSearchJobReq.
        :rtype: list[str]
        """
        return self._custom_databases

    @custom_databases.setter
    def custom_databases(self, custom_databases):
        """Sets the custom_databases of this CreateSearchJobReq.

        可供搜索分子的自定义数据库id列表

        :param custom_databases: The custom_databases of this CreateSearchJobReq.
        :type custom_databases: list[str]
        """
        self._custom_databases = custom_databases

    @property
    def model_ids(self):
        """Gets the model_ids of this CreateSearchJobReq.

        模型id列表

        :return: The model_ids of this CreateSearchJobReq.
        :rtype: list[str]
        """
        return self._model_ids

    @model_ids.setter
    def model_ids(self, model_ids):
        """Sets the model_ids of this CreateSearchJobReq.

        模型id列表

        :param model_ids: The model_ids of this CreateSearchJobReq.
        :type model_ids: list[str]
        """
        self._model_ids = model_ids

    @property
    def search_method(self):
        """Gets the search_method of this CreateSearchJobReq.

        :return: The search_method of this CreateSearchJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.SearchType`
        """
        return self._search_method

    @search_method.setter
    def search_method(self, search_method):
        """Sets the search_method of this CreateSearchJobReq.

        :param search_method: The search_method of this CreateSearchJobReq.
        :type search_method: :class:`huaweicloudsdkeihealth.v1.SearchType`
        """
        self._search_method = search_method

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
        if not isinstance(other, CreateSearchJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
