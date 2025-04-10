# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMultiTenantResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'multi_tenant_switch': 'bool'
    }

    attribute_map = {
        'multi_tenant_switch': 'multi_tenant_switch'
    }

    def __init__(self, multi_tenant_switch=None):
        r"""ShowMultiTenantResponse

        The model defined in huaweicloud sdk

        :param multi_tenant_switch: 实例多租特性开关。 - true:开启 - false:关闭。
        :type multi_tenant_switch: bool
        """
        
        super(ShowMultiTenantResponse, self).__init__()

        self._multi_tenant_switch = None
        self.discriminator = None

        if multi_tenant_switch is not None:
            self.multi_tenant_switch = multi_tenant_switch

    @property
    def multi_tenant_switch(self):
        r"""Gets the multi_tenant_switch of this ShowMultiTenantResponse.

        实例多租特性开关。 - true:开启 - false:关闭。

        :return: The multi_tenant_switch of this ShowMultiTenantResponse.
        :rtype: bool
        """
        return self._multi_tenant_switch

    @multi_tenant_switch.setter
    def multi_tenant_switch(self, multi_tenant_switch):
        r"""Sets the multi_tenant_switch of this ShowMultiTenantResponse.

        实例多租特性开关。 - true:开启 - false:关闭。

        :param multi_tenant_switch: The multi_tenant_switch of this ShowMultiTenantResponse.
        :type multi_tenant_switch: bool
        """
        self._multi_tenant_switch = multi_tenant_switch

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
        if not isinstance(other, ShowMultiTenantResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
