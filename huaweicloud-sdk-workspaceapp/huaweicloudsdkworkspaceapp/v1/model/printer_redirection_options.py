# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrinterRedirectionOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sync_client_default_printer_enable': 'bool',
        'universal_printer_driver': 'str'
    }

    attribute_map = {
        'sync_client_default_printer_enable': 'sync_client_default_printer_enable',
        'universal_printer_driver': 'universal_printer_driver'
    }

    def __init__(self, sync_client_default_printer_enable=None, universal_printer_driver=None):
        """PrinterRedirectionOptions

        The model defined in huaweicloud sdk

        :param sync_client_default_printer_enable: 是否开启同步客户端默认打印机。取值为： false：表示关闭。 true：表示开启。
        :type sync_client_default_printer_enable: bool
        :param universal_printer_driver: 通用打印机驱动。取值为：- Default：linux客户端选择Universal Printing- PS，windows客户端选择HDP XPSDrv Driver。- HDP XPSDrv Driver。- Universal Printing PCL 5。- Universal Printing PCL 6。- Universal Printing PS。
        :type universal_printer_driver: str
        """
        
        

        self._sync_client_default_printer_enable = None
        self._universal_printer_driver = None
        self.discriminator = None

        if sync_client_default_printer_enable is not None:
            self.sync_client_default_printer_enable = sync_client_default_printer_enable
        if universal_printer_driver is not None:
            self.universal_printer_driver = universal_printer_driver

    @property
    def sync_client_default_printer_enable(self):
        """Gets the sync_client_default_printer_enable of this PrinterRedirectionOptions.

        是否开启同步客户端默认打印机。取值为： false：表示关闭。 true：表示开启。

        :return: The sync_client_default_printer_enable of this PrinterRedirectionOptions.
        :rtype: bool
        """
        return self._sync_client_default_printer_enable

    @sync_client_default_printer_enable.setter
    def sync_client_default_printer_enable(self, sync_client_default_printer_enable):
        """Sets the sync_client_default_printer_enable of this PrinterRedirectionOptions.

        是否开启同步客户端默认打印机。取值为： false：表示关闭。 true：表示开启。

        :param sync_client_default_printer_enable: The sync_client_default_printer_enable of this PrinterRedirectionOptions.
        :type sync_client_default_printer_enable: bool
        """
        self._sync_client_default_printer_enable = sync_client_default_printer_enable

    @property
    def universal_printer_driver(self):
        """Gets the universal_printer_driver of this PrinterRedirectionOptions.

        通用打印机驱动。取值为：- Default：linux客户端选择Universal Printing- PS，windows客户端选择HDP XPSDrv Driver。- HDP XPSDrv Driver。- Universal Printing PCL 5。- Universal Printing PCL 6。- Universal Printing PS。

        :return: The universal_printer_driver of this PrinterRedirectionOptions.
        :rtype: str
        """
        return self._universal_printer_driver

    @universal_printer_driver.setter
    def universal_printer_driver(self, universal_printer_driver):
        """Sets the universal_printer_driver of this PrinterRedirectionOptions.

        通用打印机驱动。取值为：- Default：linux客户端选择Universal Printing- PS，windows客户端选择HDP XPSDrv Driver。- HDP XPSDrv Driver。- Universal Printing PCL 5。- Universal Printing PCL 6。- Universal Printing PS。

        :param universal_printer_driver: The universal_printer_driver of this PrinterRedirectionOptions.
        :type universal_printer_driver: str
        """
        self._universal_printer_driver = universal_printer_driver

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
        if not isinstance(other, PrinterRedirectionOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
