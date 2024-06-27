# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsingGetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'name': 'str',
        'page_number': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'service_id': 'service_id',
        'name': 'name',
        'page_number': 'page_number',
        'page_size': 'page_size'
    }

    def __init__(self, service_id=None, name=None, page_number=None, page_size=None):
        """ListUsingGetRequest

        The model defined in huaweicloud sdk

        :param service_id: 服务id
        :type service_id: str
        :param name: 看板名称，精确匹配
        :type name: str
        :param page_number: 页码
        :type page_number: int
        :param page_size: 每页数量
        :type page_size: int
        """
        
        

        self._service_id = None
        self._name = None
        self._page_number = None
        self._page_size = None
        self.discriminator = None

        self.service_id = service_id
        if name is not None:
            self.name = name
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size

    @property
    def service_id(self):
        """Gets the service_id of this ListUsingGetRequest.

        服务id

        :return: The service_id of this ListUsingGetRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ListUsingGetRequest.

        服务id

        :param service_id: The service_id of this ListUsingGetRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def name(self):
        """Gets the name of this ListUsingGetRequest.

        看板名称，精确匹配

        :return: The name of this ListUsingGetRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListUsingGetRequest.

        看板名称，精确匹配

        :param name: The name of this ListUsingGetRequest.
        :type name: str
        """
        self._name = name

    @property
    def page_number(self):
        """Gets the page_number of this ListUsingGetRequest.

        页码

        :return: The page_number of this ListUsingGetRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListUsingGetRequest.

        页码

        :param page_number: The page_number of this ListUsingGetRequest.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListUsingGetRequest.

        每页数量

        :return: The page_size of this ListUsingGetRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListUsingGetRequest.

        每页数量

        :param page_size: The page_size of this ListUsingGetRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ListUsingGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
