# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConfTokenResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'TokenInfo',
        'address_token': 'str',
        'gloabl_public_ip': 'str'
    }

    attribute_map = {
        'data': 'data',
        'address_token': 'addressToken',
        'gloabl_public_ip': 'gloablPublicIP'
    }

    def __init__(self, data=None, address_token=None, gloabl_public_ip=None):
        """CreateConfTokenResponse

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkmeeting.v1.TokenInfo`
        :param address_token: 企业通讯录查询临时Token。
        :type address_token: str
        :param gloabl_public_ip: 华为云会议Portal地址。
        :type gloabl_public_ip: str
        """
        
        super(CreateConfTokenResponse, self).__init__()

        self._data = None
        self._address_token = None
        self._gloabl_public_ip = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if address_token is not None:
            self.address_token = address_token
        if gloabl_public_ip is not None:
            self.gloabl_public_ip = gloabl_public_ip

    @property
    def data(self):
        """Gets the data of this CreateConfTokenResponse.

        :return: The data of this CreateConfTokenResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.TokenInfo`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateConfTokenResponse.

        :param data: The data of this CreateConfTokenResponse.
        :type data: :class:`huaweicloudsdkmeeting.v1.TokenInfo`
        """
        self._data = data

    @property
    def address_token(self):
        """Gets the address_token of this CreateConfTokenResponse.

        企业通讯录查询临时Token。

        :return: The address_token of this CreateConfTokenResponse.
        :rtype: str
        """
        return self._address_token

    @address_token.setter
    def address_token(self, address_token):
        """Sets the address_token of this CreateConfTokenResponse.

        企业通讯录查询临时Token。

        :param address_token: The address_token of this CreateConfTokenResponse.
        :type address_token: str
        """
        self._address_token = address_token

    @property
    def gloabl_public_ip(self):
        """Gets the gloabl_public_ip of this CreateConfTokenResponse.

        华为云会议Portal地址。

        :return: The gloabl_public_ip of this CreateConfTokenResponse.
        :rtype: str
        """
        return self._gloabl_public_ip

    @gloabl_public_ip.setter
    def gloabl_public_ip(self, gloabl_public_ip):
        """Sets the gloabl_public_ip of this CreateConfTokenResponse.

        华为云会议Portal地址。

        :param gloabl_public_ip: The gloabl_public_ip of this CreateConfTokenResponse.
        :type gloabl_public_ip: str
        """
        self._gloabl_public_ip = gloabl_public_ip

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
        if not isinstance(other, CreateConfTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
