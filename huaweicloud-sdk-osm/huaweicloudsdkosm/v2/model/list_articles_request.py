# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListArticlesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_service_key': 'str',
        'x_site': 'str',
        'x_language': 'str',
        'search_type': 'str',
        'body': 'SearchArticlesReq'
    }

    attribute_map = {
        'x_service_key': 'x-service-key',
        'x_site': 'x-site',
        'x_language': 'x-language',
        'search_type': 'search_type',
        'body': 'body'
    }

    def __init__(self, x_service_key=None, x_site=None, x_language=None, search_type=None, body=None):
        r"""ListArticlesRequest

        The model defined in huaweicloud sdk

        :param x_service_key: 调用智能客服服务标志。
        :type x_service_key: str
        :param x_site: 站点标记，0-中国站  1-国际站
        :type x_site: str
        :param x_language: 区域语言简写，en-us  zh-cn
        :type x_language: str
        :param search_type: 搜索类型：HOT-热点案例,RECOMMEND-推荐案例
        :type search_type: str
        :param body: Body of the ListArticlesRequest
        :type body: :class:`huaweicloudsdkosm.v2.SearchArticlesReq`
        """
        
        

        self._x_service_key = None
        self._x_site = None
        self._x_language = None
        self._search_type = None
        self._body = None
        self.discriminator = None

        if x_service_key is not None:
            self.x_service_key = x_service_key
        if x_site is not None:
            self.x_site = x_site
        if x_language is not None:
            self.x_language = x_language
        self.search_type = search_type
        if body is not None:
            self.body = body

    @property
    def x_service_key(self):
        r"""Gets the x_service_key of this ListArticlesRequest.

        调用智能客服服务标志。

        :return: The x_service_key of this ListArticlesRequest.
        :rtype: str
        """
        return self._x_service_key

    @x_service_key.setter
    def x_service_key(self, x_service_key):
        r"""Sets the x_service_key of this ListArticlesRequest.

        调用智能客服服务标志。

        :param x_service_key: The x_service_key of this ListArticlesRequest.
        :type x_service_key: str
        """
        self._x_service_key = x_service_key

    @property
    def x_site(self):
        r"""Gets the x_site of this ListArticlesRequest.

        站点标记，0-中国站  1-国际站

        :return: The x_site of this ListArticlesRequest.
        :rtype: str
        """
        return self._x_site

    @x_site.setter
    def x_site(self, x_site):
        r"""Sets the x_site of this ListArticlesRequest.

        站点标记，0-中国站  1-国际站

        :param x_site: The x_site of this ListArticlesRequest.
        :type x_site: str
        """
        self._x_site = x_site

    @property
    def x_language(self):
        r"""Gets the x_language of this ListArticlesRequest.

        区域语言简写，en-us  zh-cn

        :return: The x_language of this ListArticlesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListArticlesRequest.

        区域语言简写，en-us  zh-cn

        :param x_language: The x_language of this ListArticlesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def search_type(self):
        r"""Gets the search_type of this ListArticlesRequest.

        搜索类型：HOT-热点案例,RECOMMEND-推荐案例

        :return: The search_type of this ListArticlesRequest.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this ListArticlesRequest.

        搜索类型：HOT-热点案例,RECOMMEND-推荐案例

        :param search_type: The search_type of this ListArticlesRequest.
        :type search_type: str
        """
        self._search_type = search_type

    @property
    def body(self):
        r"""Gets the body of this ListArticlesRequest.

        :return: The body of this ListArticlesRequest.
        :rtype: :class:`huaweicloudsdkosm.v2.SearchArticlesReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListArticlesRequest.

        :param body: The body of this ListArticlesRequest.
        :type body: :class:`huaweicloudsdkosm.v2.SearchArticlesReq`
        """
        self._body = body

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
        if not isinstance(other, ListArticlesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
