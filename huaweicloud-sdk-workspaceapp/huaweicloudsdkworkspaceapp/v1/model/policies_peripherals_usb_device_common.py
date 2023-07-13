# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsUsbDeviceCommon:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pcsc_smart_card_enable': 'str',
        'common_options': 'PoliciesPeripheralsUsbDeviceCommonCommonOptions'
    }

    attribute_map = {
        'pcsc_smart_card_enable': 'pcsc_smart_card_enable',
        'common_options': 'common_options'
    }

    def __init__(self, pcsc_smart_card_enable=None, common_options=None):
        """PoliciesPeripheralsUsbDeviceCommon

        The model defined in huaweicloud sdk

        :param pcsc_smart_card_enable: 是否开启PC/SC智能卡重定向。取值为： Enable：表示已启动。 Closed：表示已关闭。 Disable：表示已禁用。
        :type pcsc_smart_card_enable: str
        :param common_options: 
        :type common_options: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsUsbDeviceCommonCommonOptions`
        """
        
        

        self._pcsc_smart_card_enable = None
        self._common_options = None
        self.discriminator = None

        if pcsc_smart_card_enable is not None:
            self.pcsc_smart_card_enable = pcsc_smart_card_enable
        if common_options is not None:
            self.common_options = common_options

    @property
    def pcsc_smart_card_enable(self):
        """Gets the pcsc_smart_card_enable of this PoliciesPeripheralsUsbDeviceCommon.

        是否开启PC/SC智能卡重定向。取值为： Enable：表示已启动。 Closed：表示已关闭。 Disable：表示已禁用。

        :return: The pcsc_smart_card_enable of this PoliciesPeripheralsUsbDeviceCommon.
        :rtype: str
        """
        return self._pcsc_smart_card_enable

    @pcsc_smart_card_enable.setter
    def pcsc_smart_card_enable(self, pcsc_smart_card_enable):
        """Sets the pcsc_smart_card_enable of this PoliciesPeripheralsUsbDeviceCommon.

        是否开启PC/SC智能卡重定向。取值为： Enable：表示已启动。 Closed：表示已关闭。 Disable：表示已禁用。

        :param pcsc_smart_card_enable: The pcsc_smart_card_enable of this PoliciesPeripheralsUsbDeviceCommon.
        :type pcsc_smart_card_enable: str
        """
        self._pcsc_smart_card_enable = pcsc_smart_card_enable

    @property
    def common_options(self):
        """Gets the common_options of this PoliciesPeripheralsUsbDeviceCommon.

        :return: The common_options of this PoliciesPeripheralsUsbDeviceCommon.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsUsbDeviceCommonCommonOptions`
        """
        return self._common_options

    @common_options.setter
    def common_options(self, common_options):
        """Sets the common_options of this PoliciesPeripheralsUsbDeviceCommon.

        :param common_options: The common_options of this PoliciesPeripheralsUsbDeviceCommon.
        :type common_options: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsUsbDeviceCommonCommonOptions`
        """
        self._common_options = common_options

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
        if not isinstance(other, PoliciesPeripheralsUsbDeviceCommon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
