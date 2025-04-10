# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiTestParas:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_size': 'str',
        'page_num': 'str'
    }

    attribute_map = {
        'page_size': 'page_size',
        'page_num': 'page_num'
    }

    def __init__(self, page_size=None, page_num=None):
        r"""ApiTestParas

        The model defined in huaweicloud sdk

        :param page_size: page size
        :type page_size: str
        :param page_num: page num
        :type page_num: str
        """
        
        

        self._page_size = None
        self._page_num = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if page_num is not None:
            self.page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this ApiTestParas.

        page size

        :return: The page_size of this ApiTestParas.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ApiTestParas.

        page size

        :param page_size: The page_size of this ApiTestParas.
        :type page_size: str
        """
        self._page_size = page_size

    @property
    def page_num(self):
        r"""Gets the page_num of this ApiTestParas.

        page num

        :return: The page_num of this ApiTestParas.
        :rtype: str
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ApiTestParas.

        page num

        :param page_num: The page_num of this ApiTestParas.
        :type page_num: str
        """
        self._page_num = page_num

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
        if not isinstance(other, ApiTestParas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
