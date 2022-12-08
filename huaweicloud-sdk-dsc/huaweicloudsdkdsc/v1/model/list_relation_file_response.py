# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRelationFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'current_page': 'int',
        'file_list': 'list[RelationSimpleInfo]'
    }

    attribute_map = {
        'total': 'total',
        'current_page': 'current_page',
        'file_list': 'file_list'
    }

    def __init__(self, total=None, current_page=None, file_list=None):
        """ListRelationFileResponse

        The model defined in huaweicloud sdk

        :param total: 关系信息总数
        :type total: int
        :param current_page: 当前页
        :type current_page: int
        :param file_list: 关系信息列表
        :type file_list: list[:class:`huaweicloudsdkdsc.v1.RelationSimpleInfo`]
        """
        
        super(ListRelationFileResponse, self).__init__()

        self._total = None
        self._current_page = None
        self._file_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if current_page is not None:
            self.current_page = current_page
        if file_list is not None:
            self.file_list = file_list

    @property
    def total(self):
        """Gets the total of this ListRelationFileResponse.

        关系信息总数

        :return: The total of this ListRelationFileResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListRelationFileResponse.

        关系信息总数

        :param total: The total of this ListRelationFileResponse.
        :type total: int
        """
        self._total = total

    @property
    def current_page(self):
        """Gets the current_page of this ListRelationFileResponse.

        当前页

        :return: The current_page of this ListRelationFileResponse.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this ListRelationFileResponse.

        当前页

        :param current_page: The current_page of this ListRelationFileResponse.
        :type current_page: int
        """
        self._current_page = current_page

    @property
    def file_list(self):
        """Gets the file_list of this ListRelationFileResponse.

        关系信息列表

        :return: The file_list of this ListRelationFileResponse.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.RelationSimpleInfo`]
        """
        return self._file_list

    @file_list.setter
    def file_list(self, file_list):
        """Sets the file_list of this ListRelationFileResponse.

        关系信息列表

        :param file_list: The file_list of this ListRelationFileResponse.
        :type file_list: list[:class:`huaweicloudsdkdsc.v1.RelationSimpleInfo`]
        """
        self._file_list = file_list

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
        if not isinstance(other, ListRelationFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
