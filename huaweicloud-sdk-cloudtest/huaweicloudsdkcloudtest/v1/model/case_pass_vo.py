# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CasePassVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pass_rate': 'str',
        'result_number_list': 'list[NameAndValueVo]'
    }

    attribute_map = {
        'pass_rate': 'pass_rate',
        'result_number_list': 'result_number_list'
    }

    def __init__(self, pass_rate=None, result_number_list=None):
        """CasePassVo

        The model defined in huaweicloud sdk

        :param pass_rate: 需求关联用例通过率
        :type pass_rate: str
        :param result_number_list: 需求关联用例结果与对应的用例数目列表
        :type result_number_list: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        
        

        self._pass_rate = None
        self._result_number_list = None
        self.discriminator = None

        if pass_rate is not None:
            self.pass_rate = pass_rate
        if result_number_list is not None:
            self.result_number_list = result_number_list

    @property
    def pass_rate(self):
        """Gets the pass_rate of this CasePassVo.

        需求关联用例通过率

        :return: The pass_rate of this CasePassVo.
        :rtype: str
        """
        return self._pass_rate

    @pass_rate.setter
    def pass_rate(self, pass_rate):
        """Sets the pass_rate of this CasePassVo.

        需求关联用例通过率

        :param pass_rate: The pass_rate of this CasePassVo.
        :type pass_rate: str
        """
        self._pass_rate = pass_rate

    @property
    def result_number_list(self):
        """Gets the result_number_list of this CasePassVo.

        需求关联用例结果与对应的用例数目列表

        :return: The result_number_list of this CasePassVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        return self._result_number_list

    @result_number_list.setter
    def result_number_list(self, result_number_list):
        """Sets the result_number_list of this CasePassVo.

        需求关联用例结果与对应的用例数目列表

        :param result_number_list: The result_number_list of this CasePassVo.
        :type result_number_list: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        self._result_number_list = result_number_list

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
        if not isinstance(other, CasePassVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
