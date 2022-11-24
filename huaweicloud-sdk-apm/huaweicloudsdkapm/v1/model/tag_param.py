# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_id': 'int',
        'tag_name': 'str',
        'env_id': 'int',
        'descp': 'str',
        'business_id': 'int',
        'env_id_list': 'list[int]',
        'tag_id_list': 'list[int]',
        'keyword': 'str',
        'page_enable': 'bool',
        'page_number': 'int',
        'page_size': 'int',
        'add_env_id_list': 'list[int]',
        'add_tag_id_list': 'list[int]',
        'remove_tag_id_list': 'list[int]',
        'remove_env_id_list': 'list[int]'
    }

    attribute_map = {
        'tag_id': 'tag_id',
        'tag_name': 'tag_name',
        'env_id': 'env_id',
        'descp': 'descp',
        'business_id': 'business_id',
        'env_id_list': 'env_id_list',
        'tag_id_list': 'tag_id_list',
        'keyword': 'keyword',
        'page_enable': 'page_enable',
        'page_number': 'page_number',
        'page_size': 'page_size',
        'add_env_id_list': 'add_env_id_list',
        'add_tag_id_list': 'add_tag_id_list',
        'remove_tag_id_list': 'remove_tag_id_list',
        'remove_env_id_list': 'remove_env_id_list'
    }

    def __init__(self, tag_id=None, tag_name=None, env_id=None, descp=None, business_id=None, env_id_list=None, tag_id_list=None, keyword=None, page_enable=None, page_number=None, page_size=None, add_env_id_list=None, add_tag_id_list=None, remove_tag_id_list=None, remove_env_id_list=None):
        """TagParam

        The model defined in huaweicloud sdk

        :param tag_id: 环境标签id。
        :type tag_id: int
        :param tag_name: 环境标签名称。
        :type tag_name: str
        :param env_id: 环境id。
        :type env_id: int
        :param descp: 描述信息。
        :type descp: str
        :param business_id: 应用id。
        :type business_id: int
        :param env_id_list: 环境id列表。
        :type env_id_list: list[int]
        :param tag_id_list: 环境标签id列表。
        :type tag_id_list: list[int]
        :param keyword: 关键字。
        :type keyword: str
        :param page_enable: 是否分页。
        :type page_enable: bool
        :param page_number: 每页容量。
        :type page_number: int
        :param page_size: 当前页码。
        :type page_size: int
        :param add_env_id_list: 新增环境id列表。
        :type add_env_id_list: list[int]
        :param add_tag_id_list: 新增环境标签id列表。
        :type add_tag_id_list: list[int]
        :param remove_tag_id_list: 移除环境标签id列表。
        :type remove_tag_id_list: list[int]
        :param remove_env_id_list: 移除的环境id列表。
        :type remove_env_id_list: list[int]
        """
        
        

        self._tag_id = None
        self._tag_name = None
        self._env_id = None
        self._descp = None
        self._business_id = None
        self._env_id_list = None
        self._tag_id_list = None
        self._keyword = None
        self._page_enable = None
        self._page_number = None
        self._page_size = None
        self._add_env_id_list = None
        self._add_tag_id_list = None
        self._remove_tag_id_list = None
        self._remove_env_id_list = None
        self.discriminator = None

        if tag_id is not None:
            self.tag_id = tag_id
        if tag_name is not None:
            self.tag_name = tag_name
        if env_id is not None:
            self.env_id = env_id
        if descp is not None:
            self.descp = descp
        self.business_id = business_id
        if env_id_list is not None:
            self.env_id_list = env_id_list
        if tag_id_list is not None:
            self.tag_id_list = tag_id_list
        if keyword is not None:
            self.keyword = keyword
        if page_enable is not None:
            self.page_enable = page_enable
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if add_env_id_list is not None:
            self.add_env_id_list = add_env_id_list
        if add_tag_id_list is not None:
            self.add_tag_id_list = add_tag_id_list
        if remove_tag_id_list is not None:
            self.remove_tag_id_list = remove_tag_id_list
        if remove_env_id_list is not None:
            self.remove_env_id_list = remove_env_id_list

    @property
    def tag_id(self):
        """Gets the tag_id of this TagParam.

        环境标签id。

        :return: The tag_id of this TagParam.
        :rtype: int
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this TagParam.

        环境标签id。

        :param tag_id: The tag_id of this TagParam.
        :type tag_id: int
        """
        self._tag_id = tag_id

    @property
    def tag_name(self):
        """Gets the tag_name of this TagParam.

        环境标签名称。

        :return: The tag_name of this TagParam.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this TagParam.

        环境标签名称。

        :param tag_name: The tag_name of this TagParam.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def env_id(self):
        """Gets the env_id of this TagParam.

        环境id。

        :return: The env_id of this TagParam.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this TagParam.

        环境id。

        :param env_id: The env_id of this TagParam.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def descp(self):
        """Gets the descp of this TagParam.

        描述信息。

        :return: The descp of this TagParam.
        :rtype: str
        """
        return self._descp

    @descp.setter
    def descp(self, descp):
        """Sets the descp of this TagParam.

        描述信息。

        :param descp: The descp of this TagParam.
        :type descp: str
        """
        self._descp = descp

    @property
    def business_id(self):
        """Gets the business_id of this TagParam.

        应用id。

        :return: The business_id of this TagParam.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this TagParam.

        应用id。

        :param business_id: The business_id of this TagParam.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def env_id_list(self):
        """Gets the env_id_list of this TagParam.

        环境id列表。

        :return: The env_id_list of this TagParam.
        :rtype: list[int]
        """
        return self._env_id_list

    @env_id_list.setter
    def env_id_list(self, env_id_list):
        """Sets the env_id_list of this TagParam.

        环境id列表。

        :param env_id_list: The env_id_list of this TagParam.
        :type env_id_list: list[int]
        """
        self._env_id_list = env_id_list

    @property
    def tag_id_list(self):
        """Gets the tag_id_list of this TagParam.

        环境标签id列表。

        :return: The tag_id_list of this TagParam.
        :rtype: list[int]
        """
        return self._tag_id_list

    @tag_id_list.setter
    def tag_id_list(self, tag_id_list):
        """Sets the tag_id_list of this TagParam.

        环境标签id列表。

        :param tag_id_list: The tag_id_list of this TagParam.
        :type tag_id_list: list[int]
        """
        self._tag_id_list = tag_id_list

    @property
    def keyword(self):
        """Gets the keyword of this TagParam.

        关键字。

        :return: The keyword of this TagParam.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this TagParam.

        关键字。

        :param keyword: The keyword of this TagParam.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def page_enable(self):
        """Gets the page_enable of this TagParam.

        是否分页。

        :return: The page_enable of this TagParam.
        :rtype: bool
        """
        return self._page_enable

    @page_enable.setter
    def page_enable(self, page_enable):
        """Sets the page_enable of this TagParam.

        是否分页。

        :param page_enable: The page_enable of this TagParam.
        :type page_enable: bool
        """
        self._page_enable = page_enable

    @property
    def page_number(self):
        """Gets the page_number of this TagParam.

        每页容量。

        :return: The page_number of this TagParam.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this TagParam.

        每页容量。

        :param page_number: The page_number of this TagParam.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this TagParam.

        当前页码。

        :return: The page_size of this TagParam.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this TagParam.

        当前页码。

        :param page_size: The page_size of this TagParam.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def add_env_id_list(self):
        """Gets the add_env_id_list of this TagParam.

        新增环境id列表。

        :return: The add_env_id_list of this TagParam.
        :rtype: list[int]
        """
        return self._add_env_id_list

    @add_env_id_list.setter
    def add_env_id_list(self, add_env_id_list):
        """Sets the add_env_id_list of this TagParam.

        新增环境id列表。

        :param add_env_id_list: The add_env_id_list of this TagParam.
        :type add_env_id_list: list[int]
        """
        self._add_env_id_list = add_env_id_list

    @property
    def add_tag_id_list(self):
        """Gets the add_tag_id_list of this TagParam.

        新增环境标签id列表。

        :return: The add_tag_id_list of this TagParam.
        :rtype: list[int]
        """
        return self._add_tag_id_list

    @add_tag_id_list.setter
    def add_tag_id_list(self, add_tag_id_list):
        """Sets the add_tag_id_list of this TagParam.

        新增环境标签id列表。

        :param add_tag_id_list: The add_tag_id_list of this TagParam.
        :type add_tag_id_list: list[int]
        """
        self._add_tag_id_list = add_tag_id_list

    @property
    def remove_tag_id_list(self):
        """Gets the remove_tag_id_list of this TagParam.

        移除环境标签id列表。

        :return: The remove_tag_id_list of this TagParam.
        :rtype: list[int]
        """
        return self._remove_tag_id_list

    @remove_tag_id_list.setter
    def remove_tag_id_list(self, remove_tag_id_list):
        """Sets the remove_tag_id_list of this TagParam.

        移除环境标签id列表。

        :param remove_tag_id_list: The remove_tag_id_list of this TagParam.
        :type remove_tag_id_list: list[int]
        """
        self._remove_tag_id_list = remove_tag_id_list

    @property
    def remove_env_id_list(self):
        """Gets the remove_env_id_list of this TagParam.

        移除的环境id列表。

        :return: The remove_env_id_list of this TagParam.
        :rtype: list[int]
        """
        return self._remove_env_id_list

    @remove_env_id_list.setter
    def remove_env_id_list(self, remove_env_id_list):
        """Sets the remove_env_id_list of this TagParam.

        移除的环境id列表。

        :param remove_env_id_list: The remove_env_id_list of this TagParam.
        :type remove_env_id_list: list[int]
        """
        self._remove_env_id_list = remove_env_id_list

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
        if not isinstance(other, TagParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
