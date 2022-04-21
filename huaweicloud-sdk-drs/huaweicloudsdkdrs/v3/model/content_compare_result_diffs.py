# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentCompareResultDiffs:

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
        'source_table_name': 'str',
        'content_compare_diff': 'list[ContentCompareDiff]',
        'content_compare_diff_count': 'int'
    }

    attribute_map = {
        'source_db_name': 'source_db_name',
        'source_table_name': 'source_table_name',
        'content_compare_diff': 'ContentCompareDiff',
        'content_compare_diff_count': 'content_compare_diff_count'
    }

    def __init__(self, source_db_name=None, source_table_name=None, content_compare_diff=None, content_compare_diff_count=None):
        """ContentCompareResultDiffs

        The model defined in huaweicloud sdk

        :param source_db_name: 源库名称。
        :type source_db_name: str
        :param source_table_name: 源库的表名称。
        :type source_table_name: str
        :param content_compare_diff: 内容对比结果差异。
        :type content_compare_diff: list[:class:`huaweicloudsdkdrs.v3.ContentCompareDiff`]
        :param content_compare_diff_count: 内容对比结果差异总数。
        :type content_compare_diff_count: int
        """
        
        

        self._source_db_name = None
        self._source_table_name = None
        self._content_compare_diff = None
        self._content_compare_diff_count = None
        self.discriminator = None

        self.source_db_name = source_db_name
        self.source_table_name = source_table_name
        self.content_compare_diff = content_compare_diff
        self.content_compare_diff_count = content_compare_diff_count

    @property
    def source_db_name(self):
        """Gets the source_db_name of this ContentCompareResultDiffs.

        源库名称。

        :return: The source_db_name of this ContentCompareResultDiffs.
        :rtype: str
        """
        return self._source_db_name

    @source_db_name.setter
    def source_db_name(self, source_db_name):
        """Sets the source_db_name of this ContentCompareResultDiffs.

        源库名称。

        :param source_db_name: The source_db_name of this ContentCompareResultDiffs.
        :type source_db_name: str
        """
        self._source_db_name = source_db_name

    @property
    def source_table_name(self):
        """Gets the source_table_name of this ContentCompareResultDiffs.

        源库的表名称。

        :return: The source_table_name of this ContentCompareResultDiffs.
        :rtype: str
        """
        return self._source_table_name

    @source_table_name.setter
    def source_table_name(self, source_table_name):
        """Sets the source_table_name of this ContentCompareResultDiffs.

        源库的表名称。

        :param source_table_name: The source_table_name of this ContentCompareResultDiffs.
        :type source_table_name: str
        """
        self._source_table_name = source_table_name

    @property
    def content_compare_diff(self):
        """Gets the content_compare_diff of this ContentCompareResultDiffs.

        内容对比结果差异。

        :return: The content_compare_diff of this ContentCompareResultDiffs.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.ContentCompareDiff`]
        """
        return self._content_compare_diff

    @content_compare_diff.setter
    def content_compare_diff(self, content_compare_diff):
        """Sets the content_compare_diff of this ContentCompareResultDiffs.

        内容对比结果差异。

        :param content_compare_diff: The content_compare_diff of this ContentCompareResultDiffs.
        :type content_compare_diff: list[:class:`huaweicloudsdkdrs.v3.ContentCompareDiff`]
        """
        self._content_compare_diff = content_compare_diff

    @property
    def content_compare_diff_count(self):
        """Gets the content_compare_diff_count of this ContentCompareResultDiffs.

        内容对比结果差异总数。

        :return: The content_compare_diff_count of this ContentCompareResultDiffs.
        :rtype: int
        """
        return self._content_compare_diff_count

    @content_compare_diff_count.setter
    def content_compare_diff_count(self, content_compare_diff_count):
        """Sets the content_compare_diff_count of this ContentCompareResultDiffs.

        内容对比结果差异总数。

        :param content_compare_diff_count: The content_compare_diff_count of this ContentCompareResultDiffs.
        :type content_compare_diff_count: int
        """
        self._content_compare_diff_count = content_compare_diff_count

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
        if not isinstance(other, ContentCompareResultDiffs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
