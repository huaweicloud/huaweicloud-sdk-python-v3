# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceSearchParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'env_id': 'int',
        'page': 'int',
        'page_size': 'int',
        'keyword': 'str',
        'status': 'int',
        'return_count': 'bool'
    }

    attribute_map = {
        'env_id': 'env_id',
        'page': 'page',
        'page_size': 'page_size',
        'keyword': 'keyword',
        'status': 'status',
        'return_count': 'return_count'
    }

    def __init__(self, env_id=None, page=None, page_size=None, keyword=None, status=None, return_count=None):
        """InstanceSearchParam

        The model defined in huaweicloud sdk

        :param env_id: 环境id
        :type env_id: int
        :param page: 当前页码
        :type page: int
        :param page_size: 每页数据容量
        :type page_size: int
        :param keyword: 关键字
        :type keyword: str
        :param status: 实例状态
        :type status: int
        :param return_count: 是否返回计数结果
        :type return_count: bool
        """
        
        

        self._env_id = None
        self._page = None
        self._page_size = None
        self._keyword = None
        self._status = None
        self._return_count = None
        self.discriminator = None

        if env_id is not None:
            self.env_id = env_id
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if keyword is not None:
            self.keyword = keyword
        if status is not None:
            self.status = status
        if return_count is not None:
            self.return_count = return_count

    @property
    def env_id(self):
        """Gets the env_id of this InstanceSearchParam.

        环境id

        :return: The env_id of this InstanceSearchParam.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this InstanceSearchParam.

        环境id

        :param env_id: The env_id of this InstanceSearchParam.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def page(self):
        """Gets the page of this InstanceSearchParam.

        当前页码

        :return: The page of this InstanceSearchParam.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this InstanceSearchParam.

        当前页码

        :param page: The page of this InstanceSearchParam.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this InstanceSearchParam.

        每页数据容量

        :return: The page_size of this InstanceSearchParam.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this InstanceSearchParam.

        每页数据容量

        :param page_size: The page_size of this InstanceSearchParam.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def keyword(self):
        """Gets the keyword of this InstanceSearchParam.

        关键字

        :return: The keyword of this InstanceSearchParam.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this InstanceSearchParam.

        关键字

        :param keyword: The keyword of this InstanceSearchParam.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def status(self):
        """Gets the status of this InstanceSearchParam.

        实例状态

        :return: The status of this InstanceSearchParam.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceSearchParam.

        实例状态

        :param status: The status of this InstanceSearchParam.
        :type status: int
        """
        self._status = status

    @property
    def return_count(self):
        """Gets the return_count of this InstanceSearchParam.

        是否返回计数结果

        :return: The return_count of this InstanceSearchParam.
        :rtype: bool
        """
        return self._return_count

    @return_count.setter
    def return_count(self, return_count):
        """Sets the return_count of this InstanceSearchParam.

        是否返回计数结果

        :param return_count: The return_count of this InstanceSearchParam.
        :type return_count: bool
        """
        self._return_count = return_count

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
        if not isinstance(other, InstanceSearchParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
