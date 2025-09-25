# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataCategoryInsertDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category_name': 'str',
        'description': 'str',
        'parent_id': 'str'
    }

    attribute_map = {
        'category_name': 'category_name',
        'description': 'description',
        'parent_id': 'parent_id'
    }

    def __init__(self, category_name=None, description=None, parent_id=None):
        r"""DataCategoryInsertDTO

        The model defined in huaweicloud sdk

        :param category_name: 数据分类名称。
        :type category_name: str
        :param description: 数据分类描述。
        :type description: str
        :param parent_id: 父数据分类id，通过调用查询数据分类列表接口获取，最外层数据分类的父数据分类id为-1。默认为-1
        :type parent_id: str
        """
        
        

        self._category_name = None
        self._description = None
        self._parent_id = None
        self.discriminator = None

        self.category_name = category_name
        if description is not None:
            self.description = description
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def category_name(self):
        r"""Gets the category_name of this DataCategoryInsertDTO.

        数据分类名称。

        :return: The category_name of this DataCategoryInsertDTO.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        r"""Sets the category_name of this DataCategoryInsertDTO.

        数据分类名称。

        :param category_name: The category_name of this DataCategoryInsertDTO.
        :type category_name: str
        """
        self._category_name = category_name

    @property
    def description(self):
        r"""Gets the description of this DataCategoryInsertDTO.

        数据分类描述。

        :return: The description of this DataCategoryInsertDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DataCategoryInsertDTO.

        数据分类描述。

        :param description: The description of this DataCategoryInsertDTO.
        :type description: str
        """
        self._description = description

    @property
    def parent_id(self):
        r"""Gets the parent_id of this DataCategoryInsertDTO.

        父数据分类id，通过调用查询数据分类列表接口获取，最外层数据分类的父数据分类id为-1。默认为-1

        :return: The parent_id of this DataCategoryInsertDTO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this DataCategoryInsertDTO.

        父数据分类id，通过调用查询数据分类列表接口获取，最外层数据分类的父数据分类id为-1。默认为-1

        :param parent_id: The parent_id of this DataCategoryInsertDTO.
        :type parent_id: str
        """
        self._parent_id = parent_id

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
        if not isinstance(other, DataCategoryInsertDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
