# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStreamForbiddenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app_name': 'str',
        'stream_name': 'str',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'stream_name': 'stream_name',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, domain=None, app_name=None, stream_name=None, page=None, size=None):
        """ListStreamForbiddenRequest

        The model defined in huaweicloud sdk

        :param domain: 推流域名
        :type domain: str
        :param app_name: 应用名称，不指定则查询domain下所有应用的禁止直播推流信息
        :type app_name: str
        :param stream_name: 流名称
        :type stream_name: str
        :param page: 分页编号。 默认为0。 
        :type page: int
        :param size: 每页记录数。  取值范围：1-100。  默认为10。 
        :type size: int
        """
        
        

        self._domain = None
        self._app_name = None
        self._stream_name = None
        self._page = None
        self._size = None
        self.discriminator = None

        self.domain = domain
        if app_name is not None:
            self.app_name = app_name
        if stream_name is not None:
            self.stream_name = stream_name
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def domain(self):
        """Gets the domain of this ListStreamForbiddenRequest.

        推流域名

        :return: The domain of this ListStreamForbiddenRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListStreamForbiddenRequest.

        推流域名

        :param domain: The domain of this ListStreamForbiddenRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        """Gets the app_name of this ListStreamForbiddenRequest.

        应用名称，不指定则查询domain下所有应用的禁止直播推流信息

        :return: The app_name of this ListStreamForbiddenRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListStreamForbiddenRequest.

        应用名称，不指定则查询domain下所有应用的禁止直播推流信息

        :param app_name: The app_name of this ListStreamForbiddenRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def stream_name(self):
        """Gets the stream_name of this ListStreamForbiddenRequest.

        流名称

        :return: The stream_name of this ListStreamForbiddenRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this ListStreamForbiddenRequest.

        流名称

        :param stream_name: The stream_name of this ListStreamForbiddenRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def page(self):
        """Gets the page of this ListStreamForbiddenRequest.

        分页编号。 默认为0。 

        :return: The page of this ListStreamForbiddenRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListStreamForbiddenRequest.

        分页编号。 默认为0。 

        :param page: The page of this ListStreamForbiddenRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListStreamForbiddenRequest.

        每页记录数。  取值范围：1-100。  默认为10。 

        :return: The size of this ListStreamForbiddenRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListStreamForbiddenRequest.

        每页记录数。  取值范围：1-100。  默认为10。 

        :param size: The size of this ListStreamForbiddenRequest.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ListStreamForbiddenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
