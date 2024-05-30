# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticStandardCoverageVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_col_num': 'str',
        'col_num': 'str',
        'coverage': 'float',
        'details': 'list[AllTableVO]'
    }

    attribute_map = {
        'all_col_num': 'all_col_num',
        'col_num': 'col_num',
        'coverage': 'coverage',
        'details': 'details'
    }

    def __init__(self, all_col_num=None, col_num=None, coverage=None, details=None):
        """StatisticStandardCoverageVO

        The model defined in huaweicloud sdk

        :param all_col_num: 字段总数，填写String类型替代Long类型。
        :type all_col_num: str
        :param col_num: 关联标准字段数，填写String类型替代Long类型。
        :type col_num: str
        :param coverage: 标准覆盖率。
        :type coverage: float
        :param details: 引用表数组。
        :type details: list[:class:`huaweicloudsdkdataartsstudio.v1.AllTableVO`]
        """
        
        

        self._all_col_num = None
        self._col_num = None
        self._coverage = None
        self._details = None
        self.discriminator = None

        if all_col_num is not None:
            self.all_col_num = all_col_num
        if col_num is not None:
            self.col_num = col_num
        if coverage is not None:
            self.coverage = coverage
        if details is not None:
            self.details = details

    @property
    def all_col_num(self):
        """Gets the all_col_num of this StatisticStandardCoverageVO.

        字段总数，填写String类型替代Long类型。

        :return: The all_col_num of this StatisticStandardCoverageVO.
        :rtype: str
        """
        return self._all_col_num

    @all_col_num.setter
    def all_col_num(self, all_col_num):
        """Sets the all_col_num of this StatisticStandardCoverageVO.

        字段总数，填写String类型替代Long类型。

        :param all_col_num: The all_col_num of this StatisticStandardCoverageVO.
        :type all_col_num: str
        """
        self._all_col_num = all_col_num

    @property
    def col_num(self):
        """Gets the col_num of this StatisticStandardCoverageVO.

        关联标准字段数，填写String类型替代Long类型。

        :return: The col_num of this StatisticStandardCoverageVO.
        :rtype: str
        """
        return self._col_num

    @col_num.setter
    def col_num(self, col_num):
        """Sets the col_num of this StatisticStandardCoverageVO.

        关联标准字段数，填写String类型替代Long类型。

        :param col_num: The col_num of this StatisticStandardCoverageVO.
        :type col_num: str
        """
        self._col_num = col_num

    @property
    def coverage(self):
        """Gets the coverage of this StatisticStandardCoverageVO.

        标准覆盖率。

        :return: The coverage of this StatisticStandardCoverageVO.
        :rtype: float
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        """Sets the coverage of this StatisticStandardCoverageVO.

        标准覆盖率。

        :param coverage: The coverage of this StatisticStandardCoverageVO.
        :type coverage: float
        """
        self._coverage = coverage

    @property
    def details(self):
        """Gets the details of this StatisticStandardCoverageVO.

        引用表数组。

        :return: The details of this StatisticStandardCoverageVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.AllTableVO`]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this StatisticStandardCoverageVO.

        引用表数组。

        :param details: The details of this StatisticStandardCoverageVO.
        :type details: list[:class:`huaweicloudsdkdataartsstudio.v1.AllTableVO`]
        """
        self._details = details

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
        if not isinstance(other, StatisticStandardCoverageVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
