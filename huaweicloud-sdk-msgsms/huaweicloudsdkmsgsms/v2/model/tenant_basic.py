# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TenantBasic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'customer_name': 'str',
        'enterprise_name': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'customer_name': 'customer_name',
        'enterprise_name': 'enterprise_name'
    }

    def __init__(self, customer_id=None, customer_name=None, enterprise_name=None):
        r"""TenantBasic

        The model defined in huaweicloud sdk

        :param customer_id: 租户custom id
        :type customer_id: str
        :param customer_name: 租户custom name
        :type customer_name: str
        :param enterprise_name: 租户企业名称
        :type enterprise_name: str
        """
        
        

        self._customer_id = None
        self._customer_name = None
        self._enterprise_name = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if customer_name is not None:
            self.customer_name = customer_name
        if enterprise_name is not None:
            self.enterprise_name = enterprise_name

    @property
    def customer_id(self):
        r"""Gets the customer_id of this TenantBasic.

        租户custom id

        :return: The customer_id of this TenantBasic.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this TenantBasic.

        租户custom id

        :param customer_id: The customer_id of this TenantBasic.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def customer_name(self):
        r"""Gets the customer_name of this TenantBasic.

        租户custom name

        :return: The customer_name of this TenantBasic.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        r"""Sets the customer_name of this TenantBasic.

        租户custom name

        :param customer_name: The customer_name of this TenantBasic.
        :type customer_name: str
        """
        self._customer_name = customer_name

    @property
    def enterprise_name(self):
        r"""Gets the enterprise_name of this TenantBasic.

        租户企业名称

        :return: The enterprise_name of this TenantBasic.
        :rtype: str
        """
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, enterprise_name):
        r"""Sets the enterprise_name of this TenantBasic.

        租户企业名称

        :param enterprise_name: The enterprise_name of this TenantBasic.
        :type enterprise_name: str
        """
        self._enterprise_name = enterprise_name

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
        if not isinstance(other, TenantBasic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
