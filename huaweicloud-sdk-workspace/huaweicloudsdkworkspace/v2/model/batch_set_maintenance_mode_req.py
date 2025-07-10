# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetMaintenanceModeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_ids': 'list[str]',
        'in_maintenance_mode': 'bool'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'in_maintenance_mode': 'in_maintenance_mode'
    }

    def __init__(self, desktop_ids=None, in_maintenance_mode=None):
        r"""BatchSetMaintenanceModeReq

        The model defined in huaweicloud sdk

        :param desktop_ids: 需要设置维护模式的desktopId列表。
        :type desktop_ids: list[str]
        :param in_maintenance_mode: 进入或退出管理员维护模式 false:  退出维护模式 true: 维护模式
        :type in_maintenance_mode: bool
        """
        
        

        self._desktop_ids = None
        self._in_maintenance_mode = None
        self.discriminator = None

        self.desktop_ids = desktop_ids
        self.in_maintenance_mode = in_maintenance_mode

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this BatchSetMaintenanceModeReq.

        需要设置维护模式的desktopId列表。

        :return: The desktop_ids of this BatchSetMaintenanceModeReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this BatchSetMaintenanceModeReq.

        需要设置维护模式的desktopId列表。

        :param desktop_ids: The desktop_ids of this BatchSetMaintenanceModeReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def in_maintenance_mode(self):
        r"""Gets the in_maintenance_mode of this BatchSetMaintenanceModeReq.

        进入或退出管理员维护模式 false:  退出维护模式 true: 维护模式

        :return: The in_maintenance_mode of this BatchSetMaintenanceModeReq.
        :rtype: bool
        """
        return self._in_maintenance_mode

    @in_maintenance_mode.setter
    def in_maintenance_mode(self, in_maintenance_mode):
        r"""Sets the in_maintenance_mode of this BatchSetMaintenanceModeReq.

        进入或退出管理员维护模式 false:  退出维护模式 true: 维护模式

        :param in_maintenance_mode: The in_maintenance_mode of this BatchSetMaintenanceModeReq.
        :type in_maintenance_mode: bool
        """
        self._in_maintenance_mode = in_maintenance_mode

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
        if not isinstance(other, BatchSetMaintenanceModeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
