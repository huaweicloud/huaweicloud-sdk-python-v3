# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckMobileCapabilityResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'supported_mobiles': 'list[str]',
        'unsupported_mobiles': 'list[str]',
        'tpl_id': 'str'
    }

    attribute_map = {
        'supported_mobiles': 'supported_mobiles',
        'unsupported_mobiles': 'unsupported_mobiles',
        'tpl_id': 'tpl_id'
    }

    def __init__(self, supported_mobiles=None, unsupported_mobiles=None, tpl_id=None):
        """CheckMobileCapabilityResponse

        The model defined in huaweicloud sdk

        :param supported_mobiles: 支持智能信息手机号码列表。
        :type supported_mobiles: list[str]
        :param unsupported_mobiles: 不支持智能信息手机号码列表。
        :type unsupported_mobiles: list[str]
        :param tpl_id: 智能信息模板ID，由9位数字组成。 
        :type tpl_id: str
        """
        
        super(CheckMobileCapabilityResponse, self).__init__()

        self._supported_mobiles = None
        self._unsupported_mobiles = None
        self._tpl_id = None
        self.discriminator = None

        if supported_mobiles is not None:
            self.supported_mobiles = supported_mobiles
        if unsupported_mobiles is not None:
            self.unsupported_mobiles = unsupported_mobiles
        if tpl_id is not None:
            self.tpl_id = tpl_id

    @property
    def supported_mobiles(self):
        """Gets the supported_mobiles of this CheckMobileCapabilityResponse.

        支持智能信息手机号码列表。

        :return: The supported_mobiles of this CheckMobileCapabilityResponse.
        :rtype: list[str]
        """
        return self._supported_mobiles

    @supported_mobiles.setter
    def supported_mobiles(self, supported_mobiles):
        """Sets the supported_mobiles of this CheckMobileCapabilityResponse.

        支持智能信息手机号码列表。

        :param supported_mobiles: The supported_mobiles of this CheckMobileCapabilityResponse.
        :type supported_mobiles: list[str]
        """
        self._supported_mobiles = supported_mobiles

    @property
    def unsupported_mobiles(self):
        """Gets the unsupported_mobiles of this CheckMobileCapabilityResponse.

        不支持智能信息手机号码列表。

        :return: The unsupported_mobiles of this CheckMobileCapabilityResponse.
        :rtype: list[str]
        """
        return self._unsupported_mobiles

    @unsupported_mobiles.setter
    def unsupported_mobiles(self, unsupported_mobiles):
        """Sets the unsupported_mobiles of this CheckMobileCapabilityResponse.

        不支持智能信息手机号码列表。

        :param unsupported_mobiles: The unsupported_mobiles of this CheckMobileCapabilityResponse.
        :type unsupported_mobiles: list[str]
        """
        self._unsupported_mobiles = unsupported_mobiles

    @property
    def tpl_id(self):
        """Gets the tpl_id of this CheckMobileCapabilityResponse.

        智能信息模板ID，由9位数字组成。 

        :return: The tpl_id of this CheckMobileCapabilityResponse.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this CheckMobileCapabilityResponse.

        智能信息模板ID，由9位数字组成。 

        :param tpl_id: The tpl_id of this CheckMobileCapabilityResponse.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

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
        if not isinstance(other, CheckMobileCapabilityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
