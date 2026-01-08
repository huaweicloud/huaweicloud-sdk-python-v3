# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCategoryInfoRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'sub_categories': 'list[CategoryInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'sub_categories': 'sub_categories'
    }

    def __init__(self, id=None, name=None, sub_categories=None):
        r"""QueryCategoryInfoRsp

        The model defined in huaweicloud sdk

        :param id: 查询的分类ID，-1表示默认的其他分类 
        :type id: int
        :param name: 查询的分类名称 
        :type name: str
        :param sub_categories: 子层分类信息 
        :type sub_categories: list[:class:`huaweicloudsdkvod.v1.CategoryInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._sub_categories = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if sub_categories is not None:
            self.sub_categories = sub_categories

    @property
    def id(self):
        r"""Gets the id of this QueryCategoryInfoRsp.

        查询的分类ID，-1表示默认的其他分类 

        :return: The id of this QueryCategoryInfoRsp.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QueryCategoryInfoRsp.

        查询的分类ID，-1表示默认的其他分类 

        :param id: The id of this QueryCategoryInfoRsp.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this QueryCategoryInfoRsp.

        查询的分类名称 

        :return: The name of this QueryCategoryInfoRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueryCategoryInfoRsp.

        查询的分类名称 

        :param name: The name of this QueryCategoryInfoRsp.
        :type name: str
        """
        self._name = name

    @property
    def sub_categories(self):
        r"""Gets the sub_categories of this QueryCategoryInfoRsp.

        子层分类信息 

        :return: The sub_categories of this QueryCategoryInfoRsp.
        :rtype: list[:class:`huaweicloudsdkvod.v1.CategoryInfo`]
        """
        return self._sub_categories

    @sub_categories.setter
    def sub_categories(self, sub_categories):
        r"""Sets the sub_categories of this QueryCategoryInfoRsp.

        子层分类信息 

        :param sub_categories: The sub_categories of this QueryCategoryInfoRsp.
        :type sub_categories: list[:class:`huaweicloudsdkvod.v1.CategoryInfo`]
        """
        self._sub_categories = sub_categories

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
        if not isinstance(other, QueryCategoryInfoRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
