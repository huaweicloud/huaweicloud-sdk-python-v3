# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentCompareResultDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_db_name': 'str',
        'content_compare_detail': 'list[ContentCompareDetail]',
        'content_compare_detail_count': 'int',
        'content_uncompare_detail': 'list[ContentCompareDetail]',
        'content_uncompare_detail_count': 'int'
    }

    attribute_map = {
        'source_db_name': 'source_db_name',
        'content_compare_detail': 'content_compare_detail',
        'content_compare_detail_count': 'content_compare_detail_count',
        'content_uncompare_detail': 'content_uncompare_detail',
        'content_uncompare_detail_count': 'content_uncompare_detail_count'
    }

    def __init__(self, source_db_name=None, content_compare_detail=None, content_compare_detail_count=None, content_uncompare_detail=None, content_uncompare_detail_count=None):
        """ContentCompareResultDetails

        The model defined in huaweicloud sdk

        :param source_db_name: 源库名称。
        :type source_db_name: str
        :param content_compare_detail: 该库的表的内容对比详情。
        :type content_compare_detail: list[:class:`huaweicloudsdkdrs.v3.ContentCompareDetail`]
        :param content_compare_detail_count: 内容对比结果详情总数。
        :type content_compare_detail_count: int
        :param content_uncompare_detail: 该库的表的内容对比详情(无法对比的表)。
        :type content_uncompare_detail: list[:class:`huaweicloudsdkdrs.v3.ContentCompareDetail`]
        :param content_uncompare_detail_count: 内容对比结果详情总数(无法对比的表)。
        :type content_uncompare_detail_count: int
        """
        
        

        self._source_db_name = None
        self._content_compare_detail = None
        self._content_compare_detail_count = None
        self._content_uncompare_detail = None
        self._content_uncompare_detail_count = None
        self.discriminator = None

        self.source_db_name = source_db_name
        self.content_compare_detail = content_compare_detail
        self.content_compare_detail_count = content_compare_detail_count
        if content_uncompare_detail is not None:
            self.content_uncompare_detail = content_uncompare_detail
        self.content_uncompare_detail_count = content_uncompare_detail_count

    @property
    def source_db_name(self):
        """Gets the source_db_name of this ContentCompareResultDetails.

        源库名称。

        :return: The source_db_name of this ContentCompareResultDetails.
        :rtype: str
        """
        return self._source_db_name

    @source_db_name.setter
    def source_db_name(self, source_db_name):
        """Sets the source_db_name of this ContentCompareResultDetails.

        源库名称。

        :param source_db_name: The source_db_name of this ContentCompareResultDetails.
        :type source_db_name: str
        """
        self._source_db_name = source_db_name

    @property
    def content_compare_detail(self):
        """Gets the content_compare_detail of this ContentCompareResultDetails.

        该库的表的内容对比详情。

        :return: The content_compare_detail of this ContentCompareResultDetails.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ContentCompareDetail`]
        """
        return self._content_compare_detail

    @content_compare_detail.setter
    def content_compare_detail(self, content_compare_detail):
        """Sets the content_compare_detail of this ContentCompareResultDetails.

        该库的表的内容对比详情。

        :param content_compare_detail: The content_compare_detail of this ContentCompareResultDetails.
        :type content_compare_detail: list[:class:`huaweicloudsdkdrs.v3.ContentCompareDetail`]
        """
        self._content_compare_detail = content_compare_detail

    @property
    def content_compare_detail_count(self):
        """Gets the content_compare_detail_count of this ContentCompareResultDetails.

        内容对比结果详情总数。

        :return: The content_compare_detail_count of this ContentCompareResultDetails.
        :rtype: int
        """
        return self._content_compare_detail_count

    @content_compare_detail_count.setter
    def content_compare_detail_count(self, content_compare_detail_count):
        """Sets the content_compare_detail_count of this ContentCompareResultDetails.

        内容对比结果详情总数。

        :param content_compare_detail_count: The content_compare_detail_count of this ContentCompareResultDetails.
        :type content_compare_detail_count: int
        """
        self._content_compare_detail_count = content_compare_detail_count

    @property
    def content_uncompare_detail(self):
        """Gets the content_uncompare_detail of this ContentCompareResultDetails.

        该库的表的内容对比详情(无法对比的表)。

        :return: The content_uncompare_detail of this ContentCompareResultDetails.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ContentCompareDetail`]
        """
        return self._content_uncompare_detail

    @content_uncompare_detail.setter
    def content_uncompare_detail(self, content_uncompare_detail):
        """Sets the content_uncompare_detail of this ContentCompareResultDetails.

        该库的表的内容对比详情(无法对比的表)。

        :param content_uncompare_detail: The content_uncompare_detail of this ContentCompareResultDetails.
        :type content_uncompare_detail: list[:class:`huaweicloudsdkdrs.v3.ContentCompareDetail`]
        """
        self._content_uncompare_detail = content_uncompare_detail

    @property
    def content_uncompare_detail_count(self):
        """Gets the content_uncompare_detail_count of this ContentCompareResultDetails.

        内容对比结果详情总数(无法对比的表)。

        :return: The content_uncompare_detail_count of this ContentCompareResultDetails.
        :rtype: int
        """
        return self._content_uncompare_detail_count

    @content_uncompare_detail_count.setter
    def content_uncompare_detail_count(self, content_uncompare_detail_count):
        """Sets the content_uncompare_detail_count of this ContentCompareResultDetails.

        内容对比结果详情总数(无法对比的表)。

        :param content_uncompare_detail_count: The content_uncompare_detail_count of this ContentCompareResultDetails.
        :type content_uncompare_detail_count: int
        """
        self._content_uncompare_detail_count = content_uncompare_detail_count

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
        if not isinstance(other, ContentCompareResultDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
