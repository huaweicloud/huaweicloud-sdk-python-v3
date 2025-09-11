# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportGetReportsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, name=None, page=None, size=None):
        r"""ReportGetReportsRequest

        The model defined in huaweicloud sdk

        :param name: 报表名称
        :type name: str
        :param page: 当前页码
        :type page: int
        :param size: 每页条数
        :type size: int
        """
        
        

        self._name = None
        self._page = None
        self._size = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.page = page
        self.size = size

    @property
    def name(self):
        r"""Gets the name of this ReportGetReportsRequest.

        报表名称

        :return: The name of this ReportGetReportsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ReportGetReportsRequest.

        报表名称

        :param name: The name of this ReportGetReportsRequest.
        :type name: str
        """
        self._name = name

    @property
    def page(self):
        r"""Gets the page of this ReportGetReportsRequest.

        当前页码

        :return: The page of this ReportGetReportsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ReportGetReportsRequest.

        当前页码

        :param page: The page of this ReportGetReportsRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this ReportGetReportsRequest.

        每页条数

        :return: The size of this ReportGetReportsRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ReportGetReportsRequest.

        每页条数

        :param size: The size of this ReportGetReportsRequest.
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
        if not isinstance(other, ReportGetReportsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
