# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CadDomainSwitchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'waf_switch': 'int',
        'cc_switch': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'waf_switch': 'waf_switch',
        'cc_switch': 'cc_switch'
    }

    def __init__(self, domain_id=None, waf_switch=None, cc_switch=None):
        r"""CadDomainSwitchRequest

        The model defined in huaweicloud sdk

        :param domain_id: 域名id
        :type domain_id: str
        :param waf_switch: 是否开启WEB基础防护开关。0 - 开启， 1 - 关闭
        :type waf_switch: int
        :param cc_switch: 是否开启CC防护开关。0 - 开启， 1 - 关闭。开启CC开关必须同时开启WEB基础防护开关
        :type cc_switch: int
        """
        
        

        self._domain_id = None
        self._waf_switch = None
        self._cc_switch = None
        self.discriminator = None

        self.domain_id = domain_id
        self.waf_switch = waf_switch
        self.cc_switch = cc_switch

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CadDomainSwitchRequest.

        域名id

        :return: The domain_id of this CadDomainSwitchRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CadDomainSwitchRequest.

        域名id

        :param domain_id: The domain_id of this CadDomainSwitchRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def waf_switch(self):
        r"""Gets the waf_switch of this CadDomainSwitchRequest.

        是否开启WEB基础防护开关。0 - 开启， 1 - 关闭

        :return: The waf_switch of this CadDomainSwitchRequest.
        :rtype: int
        """
        return self._waf_switch

    @waf_switch.setter
    def waf_switch(self, waf_switch):
        r"""Sets the waf_switch of this CadDomainSwitchRequest.

        是否开启WEB基础防护开关。0 - 开启， 1 - 关闭

        :param waf_switch: The waf_switch of this CadDomainSwitchRequest.
        :type waf_switch: int
        """
        self._waf_switch = waf_switch

    @property
    def cc_switch(self):
        r"""Gets the cc_switch of this CadDomainSwitchRequest.

        是否开启CC防护开关。0 - 开启， 1 - 关闭。开启CC开关必须同时开启WEB基础防护开关

        :return: The cc_switch of this CadDomainSwitchRequest.
        :rtype: int
        """
        return self._cc_switch

    @cc_switch.setter
    def cc_switch(self, cc_switch):
        r"""Sets the cc_switch of this CadDomainSwitchRequest.

        是否开启CC防护开关。0 - 开启， 1 - 关闭。开启CC开关必须同时开启WEB基础防护开关

        :param cc_switch: The cc_switch of this CadDomainSwitchRequest.
        :type cc_switch: int
        """
        self._cc_switch = cc_switch

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
        if not isinstance(other, CadDomainSwitchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
