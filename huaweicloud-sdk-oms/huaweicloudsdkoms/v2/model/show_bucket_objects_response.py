# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBucketObjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'next_page': 'bool',
        'next_marker': 'str',
        'records': 'list[ShowBucketRecord]'
    }

    attribute_map = {
        'next_page': 'next_page',
        'next_marker': 'next_marker',
        'records': 'records'
    }

    def __init__(self, next_page=None, next_marker=None, records=None):
        """ShowBucketObjectsResponse

        The model defined in huaweicloud sdk

        :param next_page: 是否存在下一页
        :type next_page: bool
        :param next_marker: 查询下一页所需要的标记（此页末尾对象名，偏移量）
        :type next_marker: str
        :param records: 查询桶信息返回的record
        :type records: list[:class:`huaweicloudsdkoms.v2.ShowBucketRecord`]
        """
        
        super(ShowBucketObjectsResponse, self).__init__()

        self._next_page = None
        self._next_marker = None
        self._records = None
        self.discriminator = None

        if next_page is not None:
            self.next_page = next_page
        if next_marker is not None:
            self.next_marker = next_marker
        if records is not None:
            self.records = records

    @property
    def next_page(self):
        """Gets the next_page of this ShowBucketObjectsResponse.

        是否存在下一页

        :return: The next_page of this ShowBucketObjectsResponse.
        :rtype: bool
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this ShowBucketObjectsResponse.

        是否存在下一页

        :param next_page: The next_page of this ShowBucketObjectsResponse.
        :type next_page: bool
        """
        self._next_page = next_page

    @property
    def next_marker(self):
        """Gets the next_marker of this ShowBucketObjectsResponse.

        查询下一页所需要的标记（此页末尾对象名，偏移量）

        :return: The next_marker of this ShowBucketObjectsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ShowBucketObjectsResponse.

        查询下一页所需要的标记（此页末尾对象名，偏移量）

        :param next_marker: The next_marker of this ShowBucketObjectsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def records(self):
        """Gets the records of this ShowBucketObjectsResponse.

        查询桶信息返回的record

        :return: The records of this ShowBucketObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkoms.v2.ShowBucketRecord`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this ShowBucketObjectsResponse.

        查询桶信息返回的record

        :param records: The records of this ShowBucketObjectsResponse.
        :type records: list[:class:`huaweicloudsdkoms.v2.ShowBucketRecord`]
        """
        self._records = records

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
        if not isinstance(other, ShowBucketObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
