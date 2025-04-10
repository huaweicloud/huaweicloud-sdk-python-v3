# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchTaskData:

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
        'top_n': 'int'
    }

    attribute_map = {
        'smiles': 'smiles',
        'databases': 'databases',
        'top_n': 'top_n'
    }

    def __init__(self, smiles=None, databases=None, top_n=None):
        r"""SearchTaskData

        The model defined in huaweicloud sdk

        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param databases: 搜索使用到的数据库集合
        :type databases: list[str]
        :param top_n: 期望最大返回条目数（排序后取Top）
        :type top_n: int
        """
        
        

        self._smiles = None
        self._databases = None
        self._top_n = None
        self.discriminator = None

        self.smiles = smiles
        self.databases = databases
        if top_n is not None:
            self.top_n = top_n

    @property
    def smiles(self):
        r"""Gets the smiles of this SearchTaskData.

        分子SMILES表达式

        :return: The smiles of this SearchTaskData.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        r"""Sets the smiles of this SearchTaskData.

        分子SMILES表达式

        :param smiles: The smiles of this SearchTaskData.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def databases(self):
        r"""Gets the databases of this SearchTaskData.

        搜索使用到的数据库集合

        :return: The databases of this SearchTaskData.
        :rtype: list[str]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this SearchTaskData.

        搜索使用到的数据库集合

        :param databases: The databases of this SearchTaskData.
        :type databases: list[str]
        """
        self._databases = databases

    @property
    def top_n(self):
        r"""Gets the top_n of this SearchTaskData.

        期望最大返回条目数（排序后取Top）

        :return: The top_n of this SearchTaskData.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        r"""Sets the top_n of this SearchTaskData.

        期望最大返回条目数（排序后取Top）

        :param top_n: The top_n of this SearchTaskData.
        :type top_n: int
        """
        self._top_n = top_n

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
        if not isinstance(other, SearchTaskData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
