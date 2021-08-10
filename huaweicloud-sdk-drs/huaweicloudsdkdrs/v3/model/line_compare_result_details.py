# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LineCompareResultDetails:


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
        'line_compare_detail': 'list[LineCompareDetail]',
        'line_compare_detail_count': 'int'
    }

    attribute_map = {
        'source_db_name': 'source_db_name',
        'line_compare_detail': 'LineCompareDetail',
        'line_compare_detail_count': 'line_compare_detail_count'
    }

    def __init__(self, source_db_name=None, line_compare_detail=None, line_compare_detail_count=None):
        """LineCompareResultDetails - a model defined in huaweicloud sdk"""
        
        

        self._source_db_name = None
        self._line_compare_detail = None
        self._line_compare_detail_count = None
        self.discriminator = None

        self.source_db_name = source_db_name
        self.line_compare_detail = line_compare_detail
        self.line_compare_detail_count = line_compare_detail_count

    @property
    def source_db_name(self):
        """Gets the source_db_name of this LineCompareResultDetails.

        源库名称。

        :return: The source_db_name of this LineCompareResultDetails.
        :rtype: str
        """
        return self._source_db_name

    @source_db_name.setter
    def source_db_name(self, source_db_name):
        """Sets the source_db_name of this LineCompareResultDetails.

        源库名称。

        :param source_db_name: The source_db_name of this LineCompareResultDetails.
        :type: str
        """
        self._source_db_name = source_db_name

    @property
    def line_compare_detail(self):
        """Gets the line_compare_detail of this LineCompareResultDetails.

        该库的表的行对比详情。

        :return: The line_compare_detail of this LineCompareResultDetails.
        :rtype: list[LineCompareDetail]
        """
        return self._line_compare_detail

    @line_compare_detail.setter
    def line_compare_detail(self, line_compare_detail):
        """Sets the line_compare_detail of this LineCompareResultDetails.

        该库的表的行对比详情。

        :param line_compare_detail: The line_compare_detail of this LineCompareResultDetails.
        :type: list[LineCompareDetail]
        """
        self._line_compare_detail = line_compare_detail

    @property
    def line_compare_detail_count(self):
        """Gets the line_compare_detail_count of this LineCompareResultDetails.

        该库的行对比结果详情总数。

        :return: The line_compare_detail_count of this LineCompareResultDetails.
        :rtype: int
        """
        return self._line_compare_detail_count

    @line_compare_detail_count.setter
    def line_compare_detail_count(self, line_compare_detail_count):
        """Sets the line_compare_detail_count of this LineCompareResultDetails.

        该库的行对比结果详情总数。

        :param line_compare_detail_count: The line_compare_detail_count of this LineCompareResultDetails.
        :type: int
        """
        self._line_compare_detail_count = line_compare_detail_count

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
        if not isinstance(other, LineCompareResultDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
