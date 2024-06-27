# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesignSummaryVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issue_num': 'int',
        'issue_cover_num': 'int',
        'case_num': 'int'
    }

    attribute_map = {
        'issue_num': 'issue_num',
        'issue_cover_num': 'issue_cover_num',
        'case_num': 'case_num'
    }

    def __init__(self, issue_num=None, issue_cover_num=None, case_num=None):
        """DesignSummaryVo

        The model defined in huaweicloud sdk

        :param issue_num: 需求总数
        :type issue_num: int
        :param issue_cover_num: 已覆盖需求数
        :type issue_cover_num: int
        :param case_num: 用例数
        :type case_num: int
        """
        
        

        self._issue_num = None
        self._issue_cover_num = None
        self._case_num = None
        self.discriminator = None

        if issue_num is not None:
            self.issue_num = issue_num
        if issue_cover_num is not None:
            self.issue_cover_num = issue_cover_num
        if case_num is not None:
            self.case_num = case_num

    @property
    def issue_num(self):
        """Gets the issue_num of this DesignSummaryVo.

        需求总数

        :return: The issue_num of this DesignSummaryVo.
        :rtype: int
        """
        return self._issue_num

    @issue_num.setter
    def issue_num(self, issue_num):
        """Sets the issue_num of this DesignSummaryVo.

        需求总数

        :param issue_num: The issue_num of this DesignSummaryVo.
        :type issue_num: int
        """
        self._issue_num = issue_num

    @property
    def issue_cover_num(self):
        """Gets the issue_cover_num of this DesignSummaryVo.

        已覆盖需求数

        :return: The issue_cover_num of this DesignSummaryVo.
        :rtype: int
        """
        return self._issue_cover_num

    @issue_cover_num.setter
    def issue_cover_num(self, issue_cover_num):
        """Sets the issue_cover_num of this DesignSummaryVo.

        已覆盖需求数

        :param issue_cover_num: The issue_cover_num of this DesignSummaryVo.
        :type issue_cover_num: int
        """
        self._issue_cover_num = issue_cover_num

    @property
    def case_num(self):
        """Gets the case_num of this DesignSummaryVo.

        用例数

        :return: The case_num of this DesignSummaryVo.
        :rtype: int
        """
        return self._case_num

    @case_num.setter
    def case_num(self, case_num):
        """Sets the case_num of this DesignSummaryVo.

        用例数

        :param case_num: The case_num of this DesignSummaryVo.
        :type case_num: int
        """
        self._case_num = case_num

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
        if not isinstance(other, DesignSummaryVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
