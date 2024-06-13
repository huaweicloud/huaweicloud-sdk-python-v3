# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIfTaskNameRepeatResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_no': 'int',
        'page_size': 'int',
        'total_page': 'int',
        'total_size': 'int',
        'page_list': 'list[AlarmTemplateInfo]'
    }

    attribute_map = {
        'page_no': 'pageNo',
        'page_size': 'pageSize',
        'total_page': 'totalPage',
        'total_size': 'totalSize',
        'page_list': 'pageList'
    }

    def __init__(self, page_no=None, page_size=None, total_page=None, total_size=None, page_list=None):
        """ShowIfTaskNameRepeatResponse

        The model defined in huaweicloud sdk

        :param page_no: 当前页
        :type page_no: int
        :param page_size: 每页大小
        :type page_size: int
        :param total_page: 总页数
        :type total_page: int
        :param total_size: 总条数
        :type total_size: int
        :param page_list: 查询到的告警模板
        :type page_list: list[:class:`huaweicloudsdkcloudtest.v1.AlarmTemplateInfo`]
        """
        
        super(ShowIfTaskNameRepeatResponse, self).__init__()

        self._page_no = None
        self._page_size = None
        self._total_page = None
        self._total_size = None
        self._page_list = None
        self.discriminator = None

        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if total_page is not None:
            self.total_page = total_page
        if total_size is not None:
            self.total_size = total_size
        if page_list is not None:
            self.page_list = page_list

    @property
    def page_no(self):
        """Gets the page_no of this ShowIfTaskNameRepeatResponse.

        当前页

        :return: The page_no of this ShowIfTaskNameRepeatResponse.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this ShowIfTaskNameRepeatResponse.

        当前页

        :param page_no: The page_no of this ShowIfTaskNameRepeatResponse.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this ShowIfTaskNameRepeatResponse.

        每页大小

        :return: The page_size of this ShowIfTaskNameRepeatResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowIfTaskNameRepeatResponse.

        每页大小

        :param page_size: The page_size of this ShowIfTaskNameRepeatResponse.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def total_page(self):
        """Gets the total_page of this ShowIfTaskNameRepeatResponse.

        总页数

        :return: The total_page of this ShowIfTaskNameRepeatResponse.
        :rtype: int
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        """Sets the total_page of this ShowIfTaskNameRepeatResponse.

        总页数

        :param total_page: The total_page of this ShowIfTaskNameRepeatResponse.
        :type total_page: int
        """
        self._total_page = total_page

    @property
    def total_size(self):
        """Gets the total_size of this ShowIfTaskNameRepeatResponse.

        总条数

        :return: The total_size of this ShowIfTaskNameRepeatResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this ShowIfTaskNameRepeatResponse.

        总条数

        :param total_size: The total_size of this ShowIfTaskNameRepeatResponse.
        :type total_size: int
        """
        self._total_size = total_size

    @property
    def page_list(self):
        """Gets the page_list of this ShowIfTaskNameRepeatResponse.

        查询到的告警模板

        :return: The page_list of this ShowIfTaskNameRepeatResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.AlarmTemplateInfo`]
        """
        return self._page_list

    @page_list.setter
    def page_list(self, page_list):
        """Sets the page_list of this ShowIfTaskNameRepeatResponse.

        查询到的告警模板

        :param page_list: The page_list of this ShowIfTaskNameRepeatResponse.
        :type page_list: list[:class:`huaweicloudsdkcloudtest.v1.AlarmTemplateInfo`]
        """
        self._page_list = page_list

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
        if not isinstance(other, ShowIfTaskNameRepeatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
