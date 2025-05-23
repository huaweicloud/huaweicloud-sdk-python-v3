# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThresholdData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'receiving': 'int',
        'receiving_default': 'int',
        'sending': 'int',
        'sending_default': 'int'
    }

    attribute_map = {
        'receiving': 'receiving',
        'receiving_default': 'receivingDefault',
        'sending': 'sending',
        'sending_default': 'sendingDefault'
    }

    def __init__(self, receiving=None, receiving_default=None, sending=None, sending_default=None):
        r"""ThresholdData

        The model defined in huaweicloud sdk

        :param receiving: 自定义接收方向阈值，单位为毫秒(ms)
        :type receiving: int
        :param receiving_default: 默认接收方向阈值，单位为毫秒(ms)
        :type receiving_default: int
        :param sending: 自定义发送方向阈值，单位为毫秒(ms)
        :type sending: int
        :param sending_default: 默认发送方向阈值，单位为毫秒(ms)
        :type sending_default: int
        """
        
        

        self._receiving = None
        self._receiving_default = None
        self._sending = None
        self._sending_default = None
        self.discriminator = None

        if receiving is not None:
            self.receiving = receiving
        if receiving_default is not None:
            self.receiving_default = receiving_default
        if sending is not None:
            self.sending = sending
        if sending_default is not None:
            self.sending_default = sending_default

    @property
    def receiving(self):
        r"""Gets the receiving of this ThresholdData.

        自定义接收方向阈值，单位为毫秒(ms)

        :return: The receiving of this ThresholdData.
        :rtype: int
        """
        return self._receiving

    @receiving.setter
    def receiving(self, receiving):
        r"""Sets the receiving of this ThresholdData.

        自定义接收方向阈值，单位为毫秒(ms)

        :param receiving: The receiving of this ThresholdData.
        :type receiving: int
        """
        self._receiving = receiving

    @property
    def receiving_default(self):
        r"""Gets the receiving_default of this ThresholdData.

        默认接收方向阈值，单位为毫秒(ms)

        :return: The receiving_default of this ThresholdData.
        :rtype: int
        """
        return self._receiving_default

    @receiving_default.setter
    def receiving_default(self, receiving_default):
        r"""Sets the receiving_default of this ThresholdData.

        默认接收方向阈值，单位为毫秒(ms)

        :param receiving_default: The receiving_default of this ThresholdData.
        :type receiving_default: int
        """
        self._receiving_default = receiving_default

    @property
    def sending(self):
        r"""Gets the sending of this ThresholdData.

        自定义发送方向阈值，单位为毫秒(ms)

        :return: The sending of this ThresholdData.
        :rtype: int
        """
        return self._sending

    @sending.setter
    def sending(self, sending):
        r"""Sets the sending of this ThresholdData.

        自定义发送方向阈值，单位为毫秒(ms)

        :param sending: The sending of this ThresholdData.
        :type sending: int
        """
        self._sending = sending

    @property
    def sending_default(self):
        r"""Gets the sending_default of this ThresholdData.

        默认发送方向阈值，单位为毫秒(ms)

        :return: The sending_default of this ThresholdData.
        :rtype: int
        """
        return self._sending_default

    @sending_default.setter
    def sending_default(self, sending_default):
        r"""Sets the sending_default of this ThresholdData.

        默认发送方向阈值，单位为毫秒(ms)

        :param sending_default: The sending_default of this ThresholdData.
        :type sending_default: int
        """
        self._sending_default = sending_default

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
        if not isinstance(other, ThresholdData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
