# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOrderInformationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone': 'list[UserPhone]',
        'sop': 'list[DefaultSop]'
    }

    attribute_map = {
        'phone': 'phone',
        'sop': 'sop'
    }

    def __init__(self, phone=None, sop=None):
        r"""ShowOrderInformationResponse

        The model defined in huaweicloud sdk

        :param phone: 联系号码
        :type phone: list[:class:`huaweicloudsdkdcos.v1.UserPhone`]
        :param sop: sop信息
        :type sop: list[:class:`huaweicloudsdkdcos.v1.DefaultSop`]
        """
        
        super(ShowOrderInformationResponse, self).__init__()

        self._phone = None
        self._sop = None
        self.discriminator = None

        if phone is not None:
            self.phone = phone
        if sop is not None:
            self.sop = sop

    @property
    def phone(self):
        r"""Gets the phone of this ShowOrderInformationResponse.

        联系号码

        :return: The phone of this ShowOrderInformationResponse.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.UserPhone`]
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this ShowOrderInformationResponse.

        联系号码

        :param phone: The phone of this ShowOrderInformationResponse.
        :type phone: list[:class:`huaweicloudsdkdcos.v1.UserPhone`]
        """
        self._phone = phone

    @property
    def sop(self):
        r"""Gets the sop of this ShowOrderInformationResponse.

        sop信息

        :return: The sop of this ShowOrderInformationResponse.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.DefaultSop`]
        """
        return self._sop

    @sop.setter
    def sop(self, sop):
        r"""Sets the sop of this ShowOrderInformationResponse.

        sop信息

        :param sop: The sop of this ShowOrderInformationResponse.
        :type sop: list[:class:`huaweicloudsdkdcos.v1.DefaultSop`]
        """
        self._sop = sop

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
        if not isinstance(other, ShowOrderInformationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
