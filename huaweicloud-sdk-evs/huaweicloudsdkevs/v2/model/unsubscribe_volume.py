# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnsubscribeVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_id': 'str',
        'order_id': 'str',
        'result': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'volume_id': 'volume_id',
        'order_id': 'order_id',
        'result': 'result',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, volume_id=None, order_id=None, result=None, fail_reason=None):
        r"""UnsubscribeVolume

        The model defined in huaweicloud sdk

        :param volume_id: 卷id对应的结果
        :type volume_id: str
        :param order_id: 卷id对应的退订订单id，如果是已到期的云硬盘退订，则不显示此字段。
        :type order_id: str
        :param result: volume_id对应的退订结果，只有SUCCESS 和 FAIL两种结果。
        :type result: str
        :param fail_reason: 当result为FAIL时，此字段显示具体的失败原因。 result为SUCCESS时，不显示此字段。
        :type fail_reason: str
        """
        
        

        self._volume_id = None
        self._order_id = None
        self._result = None
        self._fail_reason = None
        self.discriminator = None

        self.volume_id = volume_id
        if order_id is not None:
            self.order_id = order_id
        self.result = result
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def volume_id(self):
        r"""Gets the volume_id of this UnsubscribeVolume.

        卷id对应的结果

        :return: The volume_id of this UnsubscribeVolume.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this UnsubscribeVolume.

        卷id对应的结果

        :param volume_id: The volume_id of this UnsubscribeVolume.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def order_id(self):
        r"""Gets the order_id of this UnsubscribeVolume.

        卷id对应的退订订单id，如果是已到期的云硬盘退订，则不显示此字段。

        :return: The order_id of this UnsubscribeVolume.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this UnsubscribeVolume.

        卷id对应的退订订单id，如果是已到期的云硬盘退订，则不显示此字段。

        :param order_id: The order_id of this UnsubscribeVolume.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def result(self):
        r"""Gets the result of this UnsubscribeVolume.

        volume_id对应的退订结果，只有SUCCESS 和 FAIL两种结果。

        :return: The result of this UnsubscribeVolume.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this UnsubscribeVolume.

        volume_id对应的退订结果，只有SUCCESS 和 FAIL两种结果。

        :param result: The result of this UnsubscribeVolume.
        :type result: str
        """
        self._result = result

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this UnsubscribeVolume.

        当result为FAIL时，此字段显示具体的失败原因。 result为SUCCESS时，不显示此字段。

        :return: The fail_reason of this UnsubscribeVolume.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this UnsubscribeVolume.

        当result为FAIL时，此字段显示具体的失败原因。 result为SUCCESS时，不显示此字段。

        :param fail_reason: The fail_reason of this UnsubscribeVolume.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, UnsubscribeVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
