# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FilterFactor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        r"""FilterFactor

        The model defined in huaweicloud sdk

        :param key: 维度分组条件。CLOUD_SERVICE_TYPE：产品类型ASSOCIATED_ACCOUNT：关联账号REGION_CODE：区域RES_SPEC_CODE：规格编码USAGE_TYPE：使用量类型ENTERPRISE_PROJECT_ID：企业项目RESOURCE_ID：资源CHARGING_MODE：计费模式BILL_TYPE：账单类型RESOURCE_TYPE：产品AZ_CODE：可用区BE_ID：运营实体（beid）PAYER_ACCOUNT_ID：交易账号RESOURCE_TAG：成本标签COST_UNIT：成本单元
        :type key: str
        :param value: 过滤器值
        :type value: list[str]
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this FilterFactor.

        维度分组条件。CLOUD_SERVICE_TYPE：产品类型ASSOCIATED_ACCOUNT：关联账号REGION_CODE：区域RES_SPEC_CODE：规格编码USAGE_TYPE：使用量类型ENTERPRISE_PROJECT_ID：企业项目RESOURCE_ID：资源CHARGING_MODE：计费模式BILL_TYPE：账单类型RESOURCE_TYPE：产品AZ_CODE：可用区BE_ID：运营实体（beid）PAYER_ACCOUNT_ID：交易账号RESOURCE_TAG：成本标签COST_UNIT：成本单元

        :return: The key of this FilterFactor.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this FilterFactor.

        维度分组条件。CLOUD_SERVICE_TYPE：产品类型ASSOCIATED_ACCOUNT：关联账号REGION_CODE：区域RES_SPEC_CODE：规格编码USAGE_TYPE：使用量类型ENTERPRISE_PROJECT_ID：企业项目RESOURCE_ID：资源CHARGING_MODE：计费模式BILL_TYPE：账单类型RESOURCE_TYPE：产品AZ_CODE：可用区BE_ID：运营实体（beid）PAYER_ACCOUNT_ID：交易账号RESOURCE_TAG：成本标签COST_UNIT：成本单元

        :param key: The key of this FilterFactor.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this FilterFactor.

        过滤器值

        :return: The value of this FilterFactor.
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this FilterFactor.

        过滤器值

        :param value: The value of this FilterFactor.
        :type value: list[str]
        """
        self._value = value

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
        if not isinstance(other, FilterFactor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
