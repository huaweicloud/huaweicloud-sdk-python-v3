# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WafProductInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'period_type': 'str',
        'period_num': 'int'
    }

    attribute_map = {
        'resource_spec_code': 'resource_spec_code',
        'period_type': 'period_type',
        'period_num': 'period_num'
    }

    def __init__(self, resource_spec_code=None, period_type=None, period_num=None):
        """WafProductInfo

        The model defined in huaweicloud sdk

        :param resource_spec_code: waf规格   - detection: 入门   -  professional：标准   - enterprise：专业   - ultimate：铂金版
        :type resource_spec_code: str
        :param period_type: 订购周期类型 month: 月；year: 年
        :type period_type: str
        :param period_num: 订购周期数
        :type period_num: int
        """
        
        

        self._resource_spec_code = None
        self._period_type = None
        self._period_num = None
        self.discriminator = None

        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this WafProductInfo.

        waf规格   - detection: 入门   -  professional：标准   - enterprise：专业   - ultimate：铂金版

        :return: The resource_spec_code of this WafProductInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this WafProductInfo.

        waf规格   - detection: 入门   -  professional：标准   - enterprise：专业   - ultimate：铂金版

        :param resource_spec_code: The resource_spec_code of this WafProductInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def period_type(self):
        """Gets the period_type of this WafProductInfo.

        订购周期类型 month: 月；year: 年

        :return: The period_type of this WafProductInfo.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this WafProductInfo.

        订购周期类型 month: 月；year: 年

        :param period_type: The period_type of this WafProductInfo.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this WafProductInfo.

        订购周期数

        :return: The period_num of this WafProductInfo.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this WafProductInfo.

        订购周期数

        :param period_num: The period_num of this WafProductInfo.
        :type period_num: int
        """
        self._period_num = period_num

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
        if not isinstance(other, WafProductInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
