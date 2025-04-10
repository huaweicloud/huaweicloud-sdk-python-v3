# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTenantAccessInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_open': 'bool',
        'agreement_version': 'int'
    }

    attribute_map = {
        'is_open': 'is_open',
        'agreement_version': 'agreement_version'
    }

    def __init__(self, is_open=None, agreement_version=None):
        r"""UpdateTenantAccessInfoReq

        The model defined in huaweicloud sdk

        :param is_open: 是否已开通服务 - false：未开通 - true：已开通 
        :type is_open: bool
        :param agreement_version: 服务协议版本 
        :type agreement_version: int
        """
        
        

        self._is_open = None
        self._agreement_version = None
        self.discriminator = None

        if is_open is not None:
            self.is_open = is_open
        if agreement_version is not None:
            self.agreement_version = agreement_version

    @property
    def is_open(self):
        r"""Gets the is_open of this UpdateTenantAccessInfoReq.

        是否已开通服务 - false：未开通 - true：已开通 

        :return: The is_open of this UpdateTenantAccessInfoReq.
        :rtype: bool
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        r"""Sets the is_open of this UpdateTenantAccessInfoReq.

        是否已开通服务 - false：未开通 - true：已开通 

        :param is_open: The is_open of this UpdateTenantAccessInfoReq.
        :type is_open: bool
        """
        self._is_open = is_open

    @property
    def agreement_version(self):
        r"""Gets the agreement_version of this UpdateTenantAccessInfoReq.

        服务协议版本 

        :return: The agreement_version of this UpdateTenantAccessInfoReq.
        :rtype: int
        """
        return self._agreement_version

    @agreement_version.setter
    def agreement_version(self, agreement_version):
        r"""Sets the agreement_version of this UpdateTenantAccessInfoReq.

        服务协议版本 

        :param agreement_version: The agreement_version of this UpdateTenantAccessInfoReq.
        :type agreement_version: int
        """
        self._agreement_version = agreement_version

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
        if not isinstance(other, UpdateTenantAccessInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
