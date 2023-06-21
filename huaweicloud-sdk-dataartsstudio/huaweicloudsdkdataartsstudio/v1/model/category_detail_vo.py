# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CategoryDetailVO:

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
        'type': 'str',
        'pid': 'str',
        'sub_categories': 'list[SubCategoryDetailVO]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'pid': 'pid',
        'sub_categories': 'sub_categories'
    }

    def __init__(self, id=None, name=None, type=None, pid=None, sub_categories=None):
        """CategoryDetailVO

        The model defined in huaweicloud sdk

        :param id: 目录ID，根目录的ID为0
        :type id: int
        :param name: 名称
        :type name: str
        :param type: 类型 built_in:系统内置 user-defined: 用户自定义
        :type type: str
        :param pid: 父目录ID
        :type pid: str
        :param sub_categories: 子目录
        :type sub_categories: list[:class:`huaweicloudsdkdataartsstudio.v1.SubCategoryDetailVO`]
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._pid = None
        self._sub_categories = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if pid is not None:
            self.pid = pid
        if sub_categories is not None:
            self.sub_categories = sub_categories

    @property
    def id(self):
        """Gets the id of this CategoryDetailVO.

        目录ID，根目录的ID为0

        :return: The id of this CategoryDetailVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CategoryDetailVO.

        目录ID，根目录的ID为0

        :param id: The id of this CategoryDetailVO.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CategoryDetailVO.

        名称

        :return: The name of this CategoryDetailVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CategoryDetailVO.

        名称

        :param name: The name of this CategoryDetailVO.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CategoryDetailVO.

        类型 built_in:系统内置 user-defined: 用户自定义

        :return: The type of this CategoryDetailVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CategoryDetailVO.

        类型 built_in:系统内置 user-defined: 用户自定义

        :param type: The type of this CategoryDetailVO.
        :type type: str
        """
        self._type = type

    @property
    def pid(self):
        """Gets the pid of this CategoryDetailVO.

        父目录ID

        :return: The pid of this CategoryDetailVO.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this CategoryDetailVO.

        父目录ID

        :param pid: The pid of this CategoryDetailVO.
        :type pid: str
        """
        self._pid = pid

    @property
    def sub_categories(self):
        """Gets the sub_categories of this CategoryDetailVO.

        子目录

        :return: The sub_categories of this CategoryDetailVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SubCategoryDetailVO`]
        """
        return self._sub_categories

    @sub_categories.setter
    def sub_categories(self, sub_categories):
        """Sets the sub_categories of this CategoryDetailVO.

        子目录

        :param sub_categories: The sub_categories of this CategoryDetailVO.
        :type sub_categories: list[:class:`huaweicloudsdkdataartsstudio.v1.SubCategoryDetailVO`]
        """
        self._sub_categories = sub_categories

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
        if not isinstance(other, CategoryDetailVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
