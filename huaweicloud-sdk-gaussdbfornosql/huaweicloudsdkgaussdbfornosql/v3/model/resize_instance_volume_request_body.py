# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeInstanceVolumeRequestBody:

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
        r"""ResizeInstanceVolumeRequestBody

        The model defined in huaweicloud sdk

        :param size: 待扩容到的磁盘容量。取值为整数，并且大于当前磁盘容量。磁盘容量最大值的大小与所选引擎类型以及规格相关，具体请参见数据库实例规格。
        :type size: int
        :param is_auto_pay: 创建包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。
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
        r"""Gets the size of this ResizeInstanceVolumeRequestBody.

        待扩容到的磁盘容量。取值为整数，并且大于当前磁盘容量。磁盘容量最大值的大小与所选引擎类型以及规格相关，具体请参见数据库实例规格。

        :return: The size of this ResizeInstanceVolumeRequestBody.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ResizeInstanceVolumeRequestBody.

        待扩容到的磁盘容量。取值为整数，并且大于当前磁盘容量。磁盘容量最大值的大小与所选引擎类型以及规格相关，具体请参见数据库实例规格。

        :param size: The size of this ResizeInstanceVolumeRequestBody.
        :type size: int
        """
        self._size = size

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ResizeInstanceVolumeRequestBody.

        创建包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。

        :return: The is_auto_pay of this ResizeInstanceVolumeRequestBody.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ResizeInstanceVolumeRequestBody.

        创建包周期实例时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - true，表示自动从账户中支付。 - false，表示手动从账户中支付，默认为该方式。

        :param is_auto_pay: The is_auto_pay of this ResizeInstanceVolumeRequestBody.
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
        if not isinstance(other, ResizeInstanceVolumeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
