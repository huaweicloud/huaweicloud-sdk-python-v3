# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'pagesize': 'int'
    }

    attribute_map = {
        'page': 'page',
        'pagesize': 'pagesize'
    }

    def __init__(self, page=None, pagesize=None):
        r"""ListEventLogRequest

        The model defined in huaweicloud sdk

        :param page: 页数
        :type page: int
        :param pagesize: 单页显示数
        :type pagesize: int
        """
        
        

        self._page = None
        self._pagesize = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize

    @property
    def page(self):
        r"""Gets the page of this ListEventLogRequest.

        页数

        :return: The page of this ListEventLogRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListEventLogRequest.

        页数

        :param page: The page of this ListEventLogRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        r"""Gets the pagesize of this ListEventLogRequest.

        单页显示数

        :return: The pagesize of this ListEventLogRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        r"""Sets the pagesize of this ListEventLogRequest.

        单页显示数

        :param pagesize: The pagesize of this ListEventLogRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

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
        if not isinstance(other, ListEventLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
