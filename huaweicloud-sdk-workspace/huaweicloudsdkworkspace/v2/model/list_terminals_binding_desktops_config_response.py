# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTerminalsBindingDesktopsConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tc_bind_switch': 'str'
    }

    attribute_map = {
        'tc_bind_switch': 'tc_bind_switch'
    }

    def __init__(self, tc_bind_switch=None):
        """ListTerminalsBindingDesktopsConfigResponse

        The model defined in huaweicloud sdk

        :param tc_bind_switch: 绑定开关,只取值on或off
        :type tc_bind_switch: str
        """
        
        super(ListTerminalsBindingDesktopsConfigResponse, self).__init__()

        self._tc_bind_switch = None
        self.discriminator = None

        if tc_bind_switch is not None:
            self.tc_bind_switch = tc_bind_switch

    @property
    def tc_bind_switch(self):
        """Gets the tc_bind_switch of this ListTerminalsBindingDesktopsConfigResponse.

        绑定开关,只取值on或off

        :return: The tc_bind_switch of this ListTerminalsBindingDesktopsConfigResponse.
        :rtype: str
        """
        return self._tc_bind_switch

    @tc_bind_switch.setter
    def tc_bind_switch(self, tc_bind_switch):
        """Sets the tc_bind_switch of this ListTerminalsBindingDesktopsConfigResponse.

        绑定开关,只取值on或off

        :param tc_bind_switch: The tc_bind_switch of this ListTerminalsBindingDesktopsConfigResponse.
        :type tc_bind_switch: str
        """
        self._tc_bind_switch = tc_bind_switch

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
        if not isinstance(other, ListTerminalsBindingDesktopsConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
