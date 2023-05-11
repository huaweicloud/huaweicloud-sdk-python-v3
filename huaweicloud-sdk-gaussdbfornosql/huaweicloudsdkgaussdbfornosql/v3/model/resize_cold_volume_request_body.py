# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeColdVolumeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'size': 'size',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, size=None, is_auto_pay=None):
        """ResizeColdVolumeRequestBody

        The model defined in huaweicloud sdk

        :param size: 待扩容后冷存储空间大小,单位：GB。用户每次至少选择1GB扩容量，且必须为整数。待扩容后的最大存储空间为100000GB。
        :type size: int
        :param is_auto_pay: 扩容包年包月实例的冷数据存储容量时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 ·true，表示自动从账户中支付。 ·false，表示手动从账户中支付，默认为该方式。
        :type is_auto_pay: str
        """
        
        

        self._size = None
        self._is_auto_pay = None
        self.discriminator = None

        self.size = size
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def size(self):
        """Gets the size of this ResizeColdVolumeRequestBody.

        待扩容后冷存储空间大小,单位：GB。用户每次至少选择1GB扩容量，且必须为整数。待扩容后的最大存储空间为100000GB。

        :return: The size of this ResizeColdVolumeRequestBody.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ResizeColdVolumeRequestBody.

        待扩容后冷存储空间大小,单位：GB。用户每次至少选择1GB扩容量，且必须为整数。待扩容后的最大存储空间为100000GB。

        :param size: The size of this ResizeColdVolumeRequestBody.
        :type size: int
        """
        self._size = size

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ResizeColdVolumeRequestBody.

        扩容包年包月实例的冷数据存储容量时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 ·true，表示自动从账户中支付。 ·false，表示手动从账户中支付，默认为该方式。

        :return: The is_auto_pay of this ResizeColdVolumeRequestBody.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ResizeColdVolumeRequestBody.

        扩容包年包月实例的冷数据存储容量时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 ·true，表示自动从账户中支付。 ·false，表示手动从账户中支付，默认为该方式。

        :param is_auto_pay: The is_auto_pay of this ResizeColdVolumeRequestBody.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, ResizeColdVolumeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
