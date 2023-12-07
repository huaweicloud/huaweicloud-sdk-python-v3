# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseCompletionRateVo:

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
        'completion_rate': 'str',
        'status_number_list': 'list[NameAndValueVo]'
    }

    attribute_map = {
        'total': 'total',
        'completion_rate': 'completion_rate',
        'status_number_list': 'status_number_list'
    }

    def __init__(self, total=None, completion_rate=None, status_number_list=None):
        """CaseCompletionRateVo

        The model defined in huaweicloud sdk

        :param total: 总用例数
        :type total: int
        :param completion_rate: 用例完成率
        :type completion_rate: str
        :param status_number_list: 用户自定义状态对应的用例数目
        :type status_number_list: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        
        

        self._total = None
        self._completion_rate = None
        self._status_number_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if completion_rate is not None:
            self.completion_rate = completion_rate
        if status_number_list is not None:
            self.status_number_list = status_number_list

    @property
    def total(self):
        """Gets the total of this CaseCompletionRateVo.

        总用例数

        :return: The total of this CaseCompletionRateVo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CaseCompletionRateVo.

        总用例数

        :param total: The total of this CaseCompletionRateVo.
        :type total: int
        """
        self._total = total

    @property
    def completion_rate(self):
        """Gets the completion_rate of this CaseCompletionRateVo.

        用例完成率

        :return: The completion_rate of this CaseCompletionRateVo.
        :rtype: str
        """
        return self._completion_rate

    @completion_rate.setter
    def completion_rate(self, completion_rate):
        """Sets the completion_rate of this CaseCompletionRateVo.

        用例完成率

        :param completion_rate: The completion_rate of this CaseCompletionRateVo.
        :type completion_rate: str
        """
        self._completion_rate = completion_rate

    @property
    def status_number_list(self):
        """Gets the status_number_list of this CaseCompletionRateVo.

        用户自定义状态对应的用例数目

        :return: The status_number_list of this CaseCompletionRateVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        return self._status_number_list

    @status_number_list.setter
    def status_number_list(self, status_number_list):
        """Sets the status_number_list of this CaseCompletionRateVo.

        用户自定义状态对应的用例数目

        :param status_number_list: The status_number_list of this CaseCompletionRateVo.
        :type status_number_list: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        self._status_number_list = status_number_list

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
        if not isinstance(other, CaseCompletionRateVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
