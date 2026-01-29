# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionOrderRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'x_language': 'str',
        'offset': 'int',
        'limit': 'int',
        'page': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'x_language': 'X-Language',
        'offset': 'offset',
        'limit': 'limit',
        'page': 'page'
    }

    def __init__(self, project_id=None, x_language=None, offset=None, limit=None, page=None):
        r"""ListSubscriptionOrderRequest

        The model defined in huaweicloud sdk

        :param project_id: 租户projectId
        :type project_id: str
        :param x_language: 用户当前语言环境
        :type x_language: str
        :param offset: smn订阅偏移量
        :type offset: int
        :param limit: smn订阅返回数量
        :type limit: int
        :param page: 订单资源详情信息枚举，DEFAULT:默认缺省值，获取开通的资源列表，不包含套餐包；PURCHASE：在DEFAULT基础上返回租户名下ECS数量；RESOURCE_LIST在DEFAULT基础上返回套餐包列表；USAGE：返回资源用量信息；SMN：返回已订阅的smn topic列表
        :type page: str
        """
        
        

        self._project_id = None
        self._x_language = None
        self._offset = None
        self._limit = None
        self._page = None
        self.discriminator = None

        self.project_id = project_id
        self.x_language = x_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if page is not None:
            self.page = page

    @property
    def project_id(self):
        r"""Gets the project_id of this ListSubscriptionOrderRequest.

        租户projectId

        :return: The project_id of this ListSubscriptionOrderRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListSubscriptionOrderRequest.

        租户projectId

        :param project_id: The project_id of this ListSubscriptionOrderRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListSubscriptionOrderRequest.

        用户当前语言环境

        :return: The x_language of this ListSubscriptionOrderRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListSubscriptionOrderRequest.

        用户当前语言环境

        :param x_language: The x_language of this ListSubscriptionOrderRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def offset(self):
        r"""Gets the offset of this ListSubscriptionOrderRequest.

        smn订阅偏移量

        :return: The offset of this ListSubscriptionOrderRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubscriptionOrderRequest.

        smn订阅偏移量

        :param offset: The offset of this ListSubscriptionOrderRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubscriptionOrderRequest.

        smn订阅返回数量

        :return: The limit of this ListSubscriptionOrderRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubscriptionOrderRequest.

        smn订阅返回数量

        :param limit: The limit of this ListSubscriptionOrderRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page(self):
        r"""Gets the page of this ListSubscriptionOrderRequest.

        订单资源详情信息枚举，DEFAULT:默认缺省值，获取开通的资源列表，不包含套餐包；PURCHASE：在DEFAULT基础上返回租户名下ECS数量；RESOURCE_LIST在DEFAULT基础上返回套餐包列表；USAGE：返回资源用量信息；SMN：返回已订阅的smn topic列表

        :return: The page of this ListSubscriptionOrderRequest.
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListSubscriptionOrderRequest.

        订单资源详情信息枚举，DEFAULT:默认缺省值，获取开通的资源列表，不包含套餐包；PURCHASE：在DEFAULT基础上返回租户名下ECS数量；RESOURCE_LIST在DEFAULT基础上返回套餐包列表；USAGE：返回资源用量信息；SMN：返回已订阅的smn topic列表

        :param page: The page of this ListSubscriptionOrderRequest.
        :type page: str
        """
        self._page = page

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
        if not isinstance(other, ListSubscriptionOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
