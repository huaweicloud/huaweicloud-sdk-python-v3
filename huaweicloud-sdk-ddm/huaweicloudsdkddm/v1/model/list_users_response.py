# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'users': 'list[GetUsersListDetailResponses]',
        'page_no': 'int',
        'page_size': 'int',
        'total_record': 'int',
        'total_page': 'int'
    }

    attribute_map = {
        'users': 'users',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'total_record': 'total_record',
        'total_page': 'total_page'
    }

    def __init__(self, users=None, page_no=None, page_size=None, total_record=None, total_page=None):
        """ListUsersResponse

        The model defined in huaweicloud sdk

        :param users: DDM实例帐号相关信息的集合。
        :type users: list[:class:`huaweicloudsdkddm.v1.GetUsersListDetailResponses`]
        :param page_no: 当前页码
        :type page_no: int
        :param page_size: 当前页码的数据条数
        :type page_size: int
        :param total_record: 总条数
        :type total_record: int
        :param total_page: 总页数
        :type total_page: int
        """
        
        super(ListUsersResponse, self).__init__()

        self._users = None
        self._page_no = None
        self._page_size = None
        self._total_record = None
        self._total_page = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if total_record is not None:
            self.total_record = total_record
        if total_page is not None:
            self.total_page = total_page

    @property
    def users(self):
        """Gets the users of this ListUsersResponse.

        DDM实例帐号相关信息的集合。

        :return: The users of this ListUsersResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.GetUsersListDetailResponses`]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this ListUsersResponse.

        DDM实例帐号相关信息的集合。

        :param users: The users of this ListUsersResponse.
        :type users: list[:class:`huaweicloudsdkddm.v1.GetUsersListDetailResponses`]
        """
        self._users = users

    @property
    def page_no(self):
        """Gets the page_no of this ListUsersResponse.

        当前页码

        :return: The page_no of this ListUsersResponse.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this ListUsersResponse.

        当前页码

        :param page_no: The page_no of this ListUsersResponse.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this ListUsersResponse.

        当前页码的数据条数

        :return: The page_size of this ListUsersResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListUsersResponse.

        当前页码的数据条数

        :param page_size: The page_size of this ListUsersResponse.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def total_record(self):
        """Gets the total_record of this ListUsersResponse.

        总条数

        :return: The total_record of this ListUsersResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this ListUsersResponse.

        总条数

        :param total_record: The total_record of this ListUsersResponse.
        :type total_record: int
        """
        self._total_record = total_record

    @property
    def total_page(self):
        """Gets the total_page of this ListUsersResponse.

        总页数

        :return: The total_page of this ListUsersResponse.
        :rtype: int
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        """Sets the total_page of this ListUsersResponse.

        总页数

        :param total_page: The total_page of this ListUsersResponse.
        :type total_page: int
        """
        self._total_page = total_page

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
        if not isinstance(other, ListUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
