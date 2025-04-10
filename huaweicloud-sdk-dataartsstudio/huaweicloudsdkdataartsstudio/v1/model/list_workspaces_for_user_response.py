# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkspacesForUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'total_page': 'int',
        'data': 'list[Workspacebody]'
    }

    attribute_map = {
        'count': 'count',
        'total_page': 'total_page',
        'data': 'data'
    }

    def __init__(self, count=None, total_page=None, data=None):
        r"""ListWorkspacesForUserResponse

        The model defined in huaweicloud sdk

        :param count: 当前工作空间用户记录数
        :type count: int
        :param total_page: 查询结果总页数
        :type total_page: int
        :param data: 工作空间列表
        :type data: list[:class:`huaweicloudsdkdataartsstudio.v1.Workspacebody`]
        """
        
        super(ListWorkspacesForUserResponse, self).__init__()

        self._count = None
        self._total_page = None
        self._data = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if total_page is not None:
            self.total_page = total_page
        if data is not None:
            self.data = data

    @property
    def count(self):
        r"""Gets the count of this ListWorkspacesForUserResponse.

        当前工作空间用户记录数

        :return: The count of this ListWorkspacesForUserResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListWorkspacesForUserResponse.

        当前工作空间用户记录数

        :param count: The count of this ListWorkspacesForUserResponse.
        :type count: int
        """
        self._count = count

    @property
    def total_page(self):
        r"""Gets the total_page of this ListWorkspacesForUserResponse.

        查询结果总页数

        :return: The total_page of this ListWorkspacesForUserResponse.
        :rtype: int
        """
        return self._total_page

    @total_page.setter
    def total_page(self, total_page):
        r"""Sets the total_page of this ListWorkspacesForUserResponse.

        查询结果总页数

        :param total_page: The total_page of this ListWorkspacesForUserResponse.
        :type total_page: int
        """
        self._total_page = total_page

    @property
    def data(self):
        r"""Gets the data of this ListWorkspacesForUserResponse.

        工作空间列表

        :return: The data of this ListWorkspacesForUserResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Workspacebody`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListWorkspacesForUserResponse.

        工作空间列表

        :param data: The data of this ListWorkspacesForUserResponse.
        :type data: list[:class:`huaweicloudsdkdataartsstudio.v1.Workspacebody`]
        """
        self._data = data

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
        if not isinstance(other, ListWorkspacesForUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
