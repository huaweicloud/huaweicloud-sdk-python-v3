# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSearchJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'DrugJobDto',
        'smiles': 'str',
        'scaffold': 'str',
        'top_n': 'int',
        'databases': 'list[str]',
        'custom_databases': 'list[str]',
        'models': 'list[BasicDrugModel]',
        'search_method': 'SearchType',
        'part_failed_reason': 'list[FailedReasonRecord]'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'smiles': 'smiles',
        'scaffold': 'scaffold',
        'top_n': 'top_n',
        'databases': 'databases',
        'custom_databases': 'custom_databases',
        'models': 'models',
        'search_method': 'search_method',
        'part_failed_reason': 'part_failed_reason'
    }

    def __init__(self, basic_info=None, smiles=None, scaffold=None, top_n=None, databases=None, custom_databases=None, models=None, search_method=None, part_failed_reason=None):
        """ShowSearchJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param scaffold: 分子骨架表达式
        :type scaffold: str
        :param top_n: 生成分子数量
        :type top_n: int
        :param databases: 可供搜索分子的公共数据库名称列表
        :type databases: list[str]
        :param custom_databases: 可供搜索分子的自定义数据库名称列表
        :type custom_databases: list[str]
        :param models: 模型信息
        :type models: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        :param search_method: 
        :type search_method: :class:`huaweicloudsdkeihealth.v1.SearchType`
        :param part_failed_reason: 部分失败原因和数量
        :type part_failed_reason: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        
        super(ShowSearchJobResponse, self).__init__()

        self._basic_info = None
        self._smiles = None
        self._scaffold = None
        self._top_n = None
        self._databases = None
        self._custom_databases = None
        self._models = None
        self._search_method = None
        self._part_failed_reason = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if smiles is not None:
            self.smiles = smiles
        if scaffold is not None:
            self.scaffold = scaffold
        if top_n is not None:
            self.top_n = top_n
        if databases is not None:
            self.databases = databases
        if custom_databases is not None:
            self.custom_databases = custom_databases
        if models is not None:
            self.models = models
        if search_method is not None:
            self.search_method = search_method
        if part_failed_reason is not None:
            self.part_failed_reason = part_failed_reason

    @property
    def basic_info(self):
        """Gets the basic_info of this ShowSearchJobResponse.

        :return: The basic_info of this ShowSearchJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this ShowSearchJobResponse.

        :param basic_info: The basic_info of this ShowSearchJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def smiles(self):
        """Gets the smiles of this ShowSearchJobResponse.

        分子SMILES表达式

        :return: The smiles of this ShowSearchJobResponse.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this ShowSearchJobResponse.

        分子SMILES表达式

        :param smiles: The smiles of this ShowSearchJobResponse.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def scaffold(self):
        """Gets the scaffold of this ShowSearchJobResponse.

        分子骨架表达式

        :return: The scaffold of this ShowSearchJobResponse.
        :rtype: str
        """
        return self._scaffold

    @scaffold.setter
    def scaffold(self, scaffold):
        """Sets the scaffold of this ShowSearchJobResponse.

        分子骨架表达式

        :param scaffold: The scaffold of this ShowSearchJobResponse.
        :type scaffold: str
        """
        self._scaffold = scaffold

    @property
    def top_n(self):
        """Gets the top_n of this ShowSearchJobResponse.

        生成分子数量

        :return: The top_n of this ShowSearchJobResponse.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        """Sets the top_n of this ShowSearchJobResponse.

        生成分子数量

        :param top_n: The top_n of this ShowSearchJobResponse.
        :type top_n: int
        """
        self._top_n = top_n

    @property
    def databases(self):
        """Gets the databases of this ShowSearchJobResponse.

        可供搜索分子的公共数据库名称列表

        :return: The databases of this ShowSearchJobResponse.
        :rtype: list[str]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this ShowSearchJobResponse.

        可供搜索分子的公共数据库名称列表

        :param databases: The databases of this ShowSearchJobResponse.
        :type databases: list[str]
        """
        self._databases = databases

    @property
    def custom_databases(self):
        """Gets the custom_databases of this ShowSearchJobResponse.

        可供搜索分子的自定义数据库名称列表

        :return: The custom_databases of this ShowSearchJobResponse.
        :rtype: list[str]
        """
        return self._custom_databases

    @custom_databases.setter
    def custom_databases(self, custom_databases):
        """Sets the custom_databases of this ShowSearchJobResponse.

        可供搜索分子的自定义数据库名称列表

        :param custom_databases: The custom_databases of this ShowSearchJobResponse.
        :type custom_databases: list[str]
        """
        self._custom_databases = custom_databases

    @property
    def models(self):
        """Gets the models of this ShowSearchJobResponse.

        模型信息

        :return: The models of this ShowSearchJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this ShowSearchJobResponse.

        模型信息

        :param models: The models of this ShowSearchJobResponse.
        :type models: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        self._models = models

    @property
    def search_method(self):
        """Gets the search_method of this ShowSearchJobResponse.

        :return: The search_method of this ShowSearchJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.SearchType`
        """
        return self._search_method

    @search_method.setter
    def search_method(self, search_method):
        """Sets the search_method of this ShowSearchJobResponse.

        :param search_method: The search_method of this ShowSearchJobResponse.
        :type search_method: :class:`huaweicloudsdkeihealth.v1.SearchType`
        """
        self._search_method = search_method

    @property
    def part_failed_reason(self):
        """Gets the part_failed_reason of this ShowSearchJobResponse.

        部分失败原因和数量

        :return: The part_failed_reason of this ShowSearchJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        return self._part_failed_reason

    @part_failed_reason.setter
    def part_failed_reason(self, part_failed_reason):
        """Sets the part_failed_reason of this ShowSearchJobResponse.

        部分失败原因和数量

        :param part_failed_reason: The part_failed_reason of this ShowSearchJobResponse.
        :type part_failed_reason: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        self._part_failed_reason = part_failed_reason

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
        if not isinstance(other, ShowSearchJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
