# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFirewallListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_support_eps': 'bool',
        'has_ndr': 'bool',
        'is_support_postpaid': 'bool',
        'is_support_basic_version': 'bool',
        'is_support_buy_professional': 'bool',
        'data': 'HttpFirewallInstanceListResponseData'
    }

    attribute_map = {
        'user_support_eps': 'user_support_eps',
        'has_ndr': 'has_ndr',
        'is_support_postpaid': 'is_support_postpaid',
        'is_support_basic_version': 'is_support_basic_version',
        'is_support_buy_professional': 'is_support_buy_professional',
        'data': 'data'
    }

    def __init__(self, user_support_eps=None, has_ndr=None, is_support_postpaid=None, is_support_basic_version=None, is_support_buy_professional=None, data=None):
        """ListFirewallListResponse

        The model defined in huaweicloud sdk

        :param user_support_eps: 是否支持eps
        :type user_support_eps: bool
        :param has_ndr: 是否存在ndr
        :type has_ndr: bool
        :param is_support_postpaid: 是否支持按需购买
        :type is_support_postpaid: bool
        :param is_support_basic_version: 是否支持基础版
        :type is_support_basic_version: bool
        :param is_support_buy_professional: 是否支持购买专业版
        :type is_support_buy_professional: bool
        :param data: 
        :type data: :class:`huaweicloudsdkcfw.v1.HttpFirewallInstanceListResponseData`
        """
        
        super(ListFirewallListResponse, self).__init__()

        self._user_support_eps = None
        self._has_ndr = None
        self._is_support_postpaid = None
        self._is_support_basic_version = None
        self._is_support_buy_professional = None
        self._data = None
        self.discriminator = None

        if user_support_eps is not None:
            self.user_support_eps = user_support_eps
        if has_ndr is not None:
            self.has_ndr = has_ndr
        if is_support_postpaid is not None:
            self.is_support_postpaid = is_support_postpaid
        if is_support_basic_version is not None:
            self.is_support_basic_version = is_support_basic_version
        if is_support_buy_professional is not None:
            self.is_support_buy_professional = is_support_buy_professional
        if data is not None:
            self.data = data

    @property
    def user_support_eps(self):
        """Gets the user_support_eps of this ListFirewallListResponse.

        是否支持eps

        :return: The user_support_eps of this ListFirewallListResponse.
        :rtype: bool
        """
        return self._user_support_eps

    @user_support_eps.setter
    def user_support_eps(self, user_support_eps):
        """Sets the user_support_eps of this ListFirewallListResponse.

        是否支持eps

        :param user_support_eps: The user_support_eps of this ListFirewallListResponse.
        :type user_support_eps: bool
        """
        self._user_support_eps = user_support_eps

    @property
    def has_ndr(self):
        """Gets the has_ndr of this ListFirewallListResponse.

        是否存在ndr

        :return: The has_ndr of this ListFirewallListResponse.
        :rtype: bool
        """
        return self._has_ndr

    @has_ndr.setter
    def has_ndr(self, has_ndr):
        """Sets the has_ndr of this ListFirewallListResponse.

        是否存在ndr

        :param has_ndr: The has_ndr of this ListFirewallListResponse.
        :type has_ndr: bool
        """
        self._has_ndr = has_ndr

    @property
    def is_support_postpaid(self):
        """Gets the is_support_postpaid of this ListFirewallListResponse.

        是否支持按需购买

        :return: The is_support_postpaid of this ListFirewallListResponse.
        :rtype: bool
        """
        return self._is_support_postpaid

    @is_support_postpaid.setter
    def is_support_postpaid(self, is_support_postpaid):
        """Sets the is_support_postpaid of this ListFirewallListResponse.

        是否支持按需购买

        :param is_support_postpaid: The is_support_postpaid of this ListFirewallListResponse.
        :type is_support_postpaid: bool
        """
        self._is_support_postpaid = is_support_postpaid

    @property
    def is_support_basic_version(self):
        """Gets the is_support_basic_version of this ListFirewallListResponse.

        是否支持基础版

        :return: The is_support_basic_version of this ListFirewallListResponse.
        :rtype: bool
        """
        return self._is_support_basic_version

    @is_support_basic_version.setter
    def is_support_basic_version(self, is_support_basic_version):
        """Sets the is_support_basic_version of this ListFirewallListResponse.

        是否支持基础版

        :param is_support_basic_version: The is_support_basic_version of this ListFirewallListResponse.
        :type is_support_basic_version: bool
        """
        self._is_support_basic_version = is_support_basic_version

    @property
    def is_support_buy_professional(self):
        """Gets the is_support_buy_professional of this ListFirewallListResponse.

        是否支持购买专业版

        :return: The is_support_buy_professional of this ListFirewallListResponse.
        :rtype: bool
        """
        return self._is_support_buy_professional

    @is_support_buy_professional.setter
    def is_support_buy_professional(self, is_support_buy_professional):
        """Sets the is_support_buy_professional of this ListFirewallListResponse.

        是否支持购买专业版

        :param is_support_buy_professional: The is_support_buy_professional of this ListFirewallListResponse.
        :type is_support_buy_professional: bool
        """
        self._is_support_buy_professional = is_support_buy_professional

    @property
    def data(self):
        """Gets the data of this ListFirewallListResponse.

        :return: The data of this ListFirewallListResponse.
        :rtype: :class:`huaweicloudsdkcfw.v1.HttpFirewallInstanceListResponseData`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ListFirewallListResponse.

        :param data: The data of this ListFirewallListResponse.
        :type data: :class:`huaweicloudsdkcfw.v1.HttpFirewallInstanceListResponseData`
        """
        self._data = data

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
        if not isinstance(other, ListFirewallListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
