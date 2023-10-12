# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NewCustomerTagItem:

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
        'customer_tag_type': 'str',
        'new_customer_tag': 'str',
        'effective_time': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'customer_tag_type': 'customer_tag_type',
        'new_customer_tag': 'new_customer_tag',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time'
    }

    def __init__(self, customer_id=None, customer_tag_type=None, new_customer_tag=None, effective_time=None, expire_time=None):
        """NewCustomerTagItem

        The model defined in huaweicloud sdk

        :param customer_id: 客户ID。
        :type customer_id: str
        :param customer_tag_type: 新客标签类型。 SMB：SMB新客标签。
        :type customer_tag_type: str
        :param new_customer_tag: 新客标签。 Y：合格新客N：非新客UNDETERMINED：未达标新客，即有新客资格但尚未成为新客
        :type new_customer_tag: str
        :param effective_time: 生效月份。 格式为YYYY-MM。
        :type effective_time: str
        :param expire_time: 失效月份。 格式为YYYY-MM。
        :type expire_time: str
        """
        
        

        self._customer_id = None
        self._customer_tag_type = None
        self._new_customer_tag = None
        self._effective_time = None
        self._expire_time = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if customer_tag_type is not None:
            self.customer_tag_type = customer_tag_type
        if new_customer_tag is not None:
            self.new_customer_tag = new_customer_tag
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def customer_id(self):
        """Gets the customer_id of this NewCustomerTagItem.

        客户ID。

        :return: The customer_id of this NewCustomerTagItem.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this NewCustomerTagItem.

        客户ID。

        :param customer_id: The customer_id of this NewCustomerTagItem.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def customer_tag_type(self):
        """Gets the customer_tag_type of this NewCustomerTagItem.

        新客标签类型。 SMB：SMB新客标签。

        :return: The customer_tag_type of this NewCustomerTagItem.
        :rtype: str
        """
        return self._customer_tag_type

    @customer_tag_type.setter
    def customer_tag_type(self, customer_tag_type):
        """Sets the customer_tag_type of this NewCustomerTagItem.

        新客标签类型。 SMB：SMB新客标签。

        :param customer_tag_type: The customer_tag_type of this NewCustomerTagItem.
        :type customer_tag_type: str
        """
        self._customer_tag_type = customer_tag_type

    @property
    def new_customer_tag(self):
        """Gets the new_customer_tag of this NewCustomerTagItem.

        新客标签。 Y：合格新客N：非新客UNDETERMINED：未达标新客，即有新客资格但尚未成为新客

        :return: The new_customer_tag of this NewCustomerTagItem.
        :rtype: str
        """
        return self._new_customer_tag

    @new_customer_tag.setter
    def new_customer_tag(self, new_customer_tag):
        """Sets the new_customer_tag of this NewCustomerTagItem.

        新客标签。 Y：合格新客N：非新客UNDETERMINED：未达标新客，即有新客资格但尚未成为新客

        :param new_customer_tag: The new_customer_tag of this NewCustomerTagItem.
        :type new_customer_tag: str
        """
        self._new_customer_tag = new_customer_tag

    @property
    def effective_time(self):
        """Gets the effective_time of this NewCustomerTagItem.

        生效月份。 格式为YYYY-MM。

        :return: The effective_time of this NewCustomerTagItem.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this NewCustomerTagItem.

        生效月份。 格式为YYYY-MM。

        :param effective_time: The effective_time of this NewCustomerTagItem.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this NewCustomerTagItem.

        失效月份。 格式为YYYY-MM。

        :return: The expire_time of this NewCustomerTagItem.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this NewCustomerTagItem.

        失效月份。 格式为YYYY-MM。

        :param expire_time: The expire_time of this NewCustomerTagItem.
        :type expire_time: str
        """
        self._expire_time = expire_time

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
        if not isinstance(other, NewCustomerTagItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
