# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaReclaim:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_id': 'str',
        'quota_balance': 'decimal.Decimal'
    }

    attribute_map = {
        'quota_id': 'quota_id',
        'quota_balance': 'quota_balance'
    }

    def __init__(self, quota_id=None, quota_balance=None):
        r"""QuotaReclaim

        The model defined in huaweicloud sdk

        :param quota_id: 被回收的云经销商的代金券额度ID。
        :type quota_id: str
        :param quota_balance: 被回收额度后的代金券额度余额。单位：元。
        :type quota_balance: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        
        

        self._quota_id = None
        self._quota_balance = None
        self.discriminator = None

        if quota_id is not None:
            self.quota_id = quota_id
        if quota_balance is not None:
            self.quota_balance = quota_balance

    @property
    def quota_id(self):
        r"""Gets the quota_id of this QuotaReclaim.

        被回收的云经销商的代金券额度ID。

        :return: The quota_id of this QuotaReclaim.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        r"""Sets the quota_id of this QuotaReclaim.

        被回收的云经销商的代金券额度ID。

        :param quota_id: The quota_id of this QuotaReclaim.
        :type quota_id: str
        """
        self._quota_id = quota_id

    @property
    def quota_balance(self):
        r"""Gets the quota_balance of this QuotaReclaim.

        被回收额度后的代金券额度余额。单位：元。

        :return: The quota_balance of this QuotaReclaim.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._quota_balance

    @quota_balance.setter
    def quota_balance(self, quota_balance):
        r"""Sets the quota_balance of this QuotaReclaim.

        被回收额度后的代金券额度余额。单位：元。

        :param quota_balance: The quota_balance of this QuotaReclaim.
        :type quota_balance: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._quota_balance = quota_balance

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
        if not isinstance(other, QuotaReclaim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
