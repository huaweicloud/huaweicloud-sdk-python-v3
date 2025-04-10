# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdentificationRuleResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'DiagnoseResult',
        'count': 'int',
        'abnormal_info': 'list[SecurityLevelInfo]'
    }

    attribute_map = {
        'result': 'result',
        'count': 'count',
        'abnormal_info': 'abnormal_info'
    }

    def __init__(self, result=None, count=None, abnormal_info=None):
        r"""IdentificationRuleResult

        The model defined in huaweicloud sdk

        :param result: 
        :type result: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        :param count: 有风险的问题数量
        :type count: int
        :param abnormal_info: 没有配置识别规则的密级列表
        :type abnormal_info: list[:class:`huaweicloudsdkdataartsstudio.v1.SecurityLevelInfo`]
        """
        
        

        self._result = None
        self._count = None
        self._abnormal_info = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if count is not None:
            self.count = count
        if abnormal_info is not None:
            self.abnormal_info = abnormal_info

    @property
    def result(self):
        r"""Gets the result of this IdentificationRuleResult.

        :return: The result of this IdentificationRuleResult.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this IdentificationRuleResult.

        :param result: The result of this IdentificationRuleResult.
        :type result: :class:`huaweicloudsdkdataartsstudio.v1.DiagnoseResult`
        """
        self._result = result

    @property
    def count(self):
        r"""Gets the count of this IdentificationRuleResult.

        有风险的问题数量

        :return: The count of this IdentificationRuleResult.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this IdentificationRuleResult.

        有风险的问题数量

        :param count: The count of this IdentificationRuleResult.
        :type count: int
        """
        self._count = count

    @property
    def abnormal_info(self):
        r"""Gets the abnormal_info of this IdentificationRuleResult.

        没有配置识别规则的密级列表

        :return: The abnormal_info of this IdentificationRuleResult.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SecurityLevelInfo`]
        """
        return self._abnormal_info

    @abnormal_info.setter
    def abnormal_info(self, abnormal_info):
        r"""Sets the abnormal_info of this IdentificationRuleResult.

        没有配置识别规则的密级列表

        :param abnormal_info: The abnormal_info of this IdentificationRuleResult.
        :type abnormal_info: list[:class:`huaweicloudsdkdataartsstudio.v1.SecurityLevelInfo`]
        """
        self._abnormal_info = abnormal_info

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
        if not isinstance(other, IdentificationRuleResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
