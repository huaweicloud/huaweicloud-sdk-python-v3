# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentSearchParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_id': 'int',
        'env_id': 'int',
        'status': 'str',
        'region': 'str',
        'order_by_status': 'str',
        'page': 'int',
        'page_size': 'int',
        'keyword': 'str'
    }

    attribute_map = {
        'business_id': 'business_id',
        'env_id': 'env_id',
        'status': 'status',
        'region': 'region',
        'order_by_status': 'order_by_status',
        'page': 'page',
        'page_size': 'page_size',
        'keyword': 'keyword'
    }

    def __init__(self, business_id=None, env_id=None, status=None, region=None, order_by_status=None, page=None, page_size=None, keyword=None):
        """AgentSearchParam

        The model defined in huaweicloud sdk

        :param business_id: 应用id。
        :type business_id: int
        :param env_id: 环境id
        :type env_id: int
        :param status: 探针状态。
        :type status: str
        :param region: region英文名称。
        :type region: str
        :param order_by_status: 是否按照采集状态排序,默认不填则不按状态排序，填y则按照状态排序。
        :type order_by_status: str
        :param page: 需要查询的页码，最小数为1。
        :type page: int
        :param page_size: 查询结果每页最多显示的条数。
        :type page_size: int
        :param keyword: 关键字。
        :type keyword: str
        """
        
        

        self._business_id = None
        self._env_id = None
        self._status = None
        self._region = None
        self._order_by_status = None
        self._page = None
        self._page_size = None
        self._keyword = None
        self.discriminator = None

        self.business_id = business_id
        if env_id is not None:
            self.env_id = env_id
        if status is not None:
            self.status = status
        self.region = region
        if order_by_status is not None:
            self.order_by_status = order_by_status
        self.page = page
        self.page_size = page_size
        if keyword is not None:
            self.keyword = keyword

    @property
    def business_id(self):
        """Gets the business_id of this AgentSearchParam.

        应用id。

        :return: The business_id of this AgentSearchParam.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this AgentSearchParam.

        应用id。

        :param business_id: The business_id of this AgentSearchParam.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def env_id(self):
        """Gets the env_id of this AgentSearchParam.

        环境id

        :return: The env_id of this AgentSearchParam.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this AgentSearchParam.

        环境id

        :param env_id: The env_id of this AgentSearchParam.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def status(self):
        """Gets the status of this AgentSearchParam.

        探针状态。

        :return: The status of this AgentSearchParam.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AgentSearchParam.

        探针状态。

        :param status: The status of this AgentSearchParam.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        """Gets the region of this AgentSearchParam.

        region英文名称。

        :return: The region of this AgentSearchParam.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AgentSearchParam.

        region英文名称。

        :param region: The region of this AgentSearchParam.
        :type region: str
        """
        self._region = region

    @property
    def order_by_status(self):
        """Gets the order_by_status of this AgentSearchParam.

        是否按照采集状态排序,默认不填则不按状态排序，填y则按照状态排序。

        :return: The order_by_status of this AgentSearchParam.
        :rtype: str
        """
        return self._order_by_status

    @order_by_status.setter
    def order_by_status(self, order_by_status):
        """Sets the order_by_status of this AgentSearchParam.

        是否按照采集状态排序,默认不填则不按状态排序，填y则按照状态排序。

        :param order_by_status: The order_by_status of this AgentSearchParam.
        :type order_by_status: str
        """
        self._order_by_status = order_by_status

    @property
    def page(self):
        """Gets the page of this AgentSearchParam.

        需要查询的页码，最小数为1。

        :return: The page of this AgentSearchParam.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this AgentSearchParam.

        需要查询的页码，最小数为1。

        :param page: The page of this AgentSearchParam.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this AgentSearchParam.

        查询结果每页最多显示的条数。

        :return: The page_size of this AgentSearchParam.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this AgentSearchParam.

        查询结果每页最多显示的条数。

        :param page_size: The page_size of this AgentSearchParam.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def keyword(self):
        """Gets the keyword of this AgentSearchParam.

        关键字。

        :return: The keyword of this AgentSearchParam.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this AgentSearchParam.

        关键字。

        :param keyword: The keyword of this AgentSearchParam.
        :type keyword: str
        """
        self._keyword = keyword

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
        if not isinstance(other, AgentSearchParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
