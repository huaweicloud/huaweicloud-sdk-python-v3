# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DelOtpDevicesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'otp_ids': 'list[str]'
    }

    attribute_map = {
        'otp_ids': 'otp_ids'
    }

    def __init__(self, otp_ids=None):
        """DelOtpDevicesReq

        The model defined in huaweicloud sdk

        :param otp_ids: 待解绑的otp配置id数组。
        :type otp_ids: list[str]
        """
        
        

        self._otp_ids = None
        self.discriminator = None

        if otp_ids is not None:
            self.otp_ids = otp_ids

    @property
    def otp_ids(self):
        """Gets the otp_ids of this DelOtpDevicesReq.

        待解绑的otp配置id数组。

        :return: The otp_ids of this DelOtpDevicesReq.
        :rtype: list[str]
        """
        return self._otp_ids

    @otp_ids.setter
    def otp_ids(self, otp_ids):
        """Sets the otp_ids of this DelOtpDevicesReq.

        待解绑的otp配置id数组。

        :param otp_ids: The otp_ids of this DelOtpDevicesReq.
        :type otp_ids: list[str]
        """
        self._otp_ids = otp_ids

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
        if not isinstance(other, DelOtpDevicesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
