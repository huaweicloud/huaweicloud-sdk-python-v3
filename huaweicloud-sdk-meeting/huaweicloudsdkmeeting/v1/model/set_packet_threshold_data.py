# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetPacketThresholdData:

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
        'sending': 'int'
    }

    attribute_map = {
        'receiving': 'receiving',
        'sending': 'sending'
    }

    def __init__(self, receiving=None, sending=None):
        """SetPacketThresholdData

        The model defined in huaweicloud sdk

        :param receiving: 接收方向阈值设定值，单位为百分比(%)。 取值范围：0 - 100。
        :type receiving: int
        :param sending: 发送方向阈值设定值，单位为百分比(%)。 取值范围：0 - 100。
        :type sending: int
        """
        
        

        self._receiving = None
        self._sending = None
        self.discriminator = None

        if receiving is not None:
            self.receiving = receiving
        if sending is not None:
            self.sending = sending

    @property
    def receiving(self):
        """Gets the receiving of this SetPacketThresholdData.

        接收方向阈值设定值，单位为百分比(%)。 取值范围：0 - 100。

        :return: The receiving of this SetPacketThresholdData.
        :rtype: int
        """
        return self._receiving

    @receiving.setter
    def receiving(self, receiving):
        """Sets the receiving of this SetPacketThresholdData.

        接收方向阈值设定值，单位为百分比(%)。 取值范围：0 - 100。

        :param receiving: The receiving of this SetPacketThresholdData.
        :type receiving: int
        """
        self._receiving = receiving

    @property
    def sending(self):
        """Gets the sending of this SetPacketThresholdData.

        发送方向阈值设定值，单位为百分比(%)。 取值范围：0 - 100。

        :return: The sending of this SetPacketThresholdData.
        :rtype: int
        """
        return self._sending

    @sending.setter
    def sending(self, sending):
        """Sets the sending of this SetPacketThresholdData.

        发送方向阈值设定值，单位为百分比(%)。 取值范围：0 - 100。

        :param sending: The sending of this SetPacketThresholdData.
        :type sending: int
        """
        self._sending = sending

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
        if not isinstance(other, SetPacketThresholdData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
