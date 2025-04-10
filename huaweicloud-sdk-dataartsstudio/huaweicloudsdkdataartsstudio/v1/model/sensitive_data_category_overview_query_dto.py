# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SensitiveDataCategoryOverviewQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'root_id': 'str',
        'parent_id': 'str',
        'category_id': 'str',
        'category_name': 'str',
        'category_path': 'str',
        'count': 'int',
        'children': 'list[SensitiveDataCategoryOverviewQueryDTO]'
    }

    attribute_map = {
        'root_id': 'root_id',
        'parent_id': 'parent_id',
        'category_id': 'category_id',
        'category_name': 'category_name',
        'category_path': 'category_path',
        'count': 'count',
        'children': 'children'
    }

    def __init__(self, root_id=None, parent_id=None, category_id=None, category_name=None, category_path=None, count=None, children=None):
        r"""SensitiveDataCategoryOverviewQueryDTO

        The model defined in huaweicloud sdk

        :param root_id: 当前分类节点的根节点id,根节点的
        :type root_id: str
        :param parent_id: 当前分类节点的父节点id
        :type parent_id: str
        :param category_id: 分类的Id
        :type category_id: str
        :param category_name: 分类的名称
        :type category_name: str
        :param category_path: 分类path
        :type category_path: str
        :param count: 当前分类下的敏感字段数量
        :type count: int
        :param children: 当前分类的子节点
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataCategoryOverviewQueryDTO`]
        """
        
        

        self._root_id = None
        self._parent_id = None
        self._category_id = None
        self._category_name = None
        self._category_path = None
        self._count = None
        self._children = None
        self.discriminator = None

        if root_id is not None:
            self.root_id = root_id
        if parent_id is not None:
            self.parent_id = parent_id
        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name
        if category_path is not None:
            self.category_path = category_path
        if count is not None:
            self.count = count
        if children is not None:
            self.children = children

    @property
    def root_id(self):
        r"""Gets the root_id of this SensitiveDataCategoryOverviewQueryDTO.

        当前分类节点的根节点id,根节点的

        :return: The root_id of this SensitiveDataCategoryOverviewQueryDTO.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this SensitiveDataCategoryOverviewQueryDTO.

        当前分类节点的根节点id,根节点的

        :param root_id: The root_id of this SensitiveDataCategoryOverviewQueryDTO.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this SensitiveDataCategoryOverviewQueryDTO.

        当前分类节点的父节点id

        :return: The parent_id of this SensitiveDataCategoryOverviewQueryDTO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this SensitiveDataCategoryOverviewQueryDTO.

        当前分类节点的父节点id

        :param parent_id: The parent_id of this SensitiveDataCategoryOverviewQueryDTO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def category_id(self):
        r"""Gets the category_id of this SensitiveDataCategoryOverviewQueryDTO.

        分类的Id

        :return: The category_id of this SensitiveDataCategoryOverviewQueryDTO.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this SensitiveDataCategoryOverviewQueryDTO.

        分类的Id

        :param category_id: The category_id of this SensitiveDataCategoryOverviewQueryDTO.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def category_name(self):
        r"""Gets the category_name of this SensitiveDataCategoryOverviewQueryDTO.

        分类的名称

        :return: The category_name of this SensitiveDataCategoryOverviewQueryDTO.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        r"""Sets the category_name of this SensitiveDataCategoryOverviewQueryDTO.

        分类的名称

        :param category_name: The category_name of this SensitiveDataCategoryOverviewQueryDTO.
        :type category_name: str
        """
        self._category_name = category_name

    @property
    def category_path(self):
        r"""Gets the category_path of this SensitiveDataCategoryOverviewQueryDTO.

        分类path

        :return: The category_path of this SensitiveDataCategoryOverviewQueryDTO.
        :rtype: str
        """
        return self._category_path

    @category_path.setter
    def category_path(self, category_path):
        r"""Sets the category_path of this SensitiveDataCategoryOverviewQueryDTO.

        分类path

        :param category_path: The category_path of this SensitiveDataCategoryOverviewQueryDTO.
        :type category_path: str
        """
        self._category_path = category_path

    @property
    def count(self):
        r"""Gets the count of this SensitiveDataCategoryOverviewQueryDTO.

        当前分类下的敏感字段数量

        :return: The count of this SensitiveDataCategoryOverviewQueryDTO.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this SensitiveDataCategoryOverviewQueryDTO.

        当前分类下的敏感字段数量

        :param count: The count of this SensitiveDataCategoryOverviewQueryDTO.
        :type count: int
        """
        self._count = count

    @property
    def children(self):
        r"""Gets the children of this SensitiveDataCategoryOverviewQueryDTO.

        当前分类的子节点

        :return: The children of this SensitiveDataCategoryOverviewQueryDTO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataCategoryOverviewQueryDTO`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this SensitiveDataCategoryOverviewQueryDTO.

        当前分类的子节点

        :param children: The children of this SensitiveDataCategoryOverviewQueryDTO.
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataCategoryOverviewQueryDTO`]
        """
        self._children = children

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
        if not isinstance(other, SensitiveDataCategoryOverviewQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
