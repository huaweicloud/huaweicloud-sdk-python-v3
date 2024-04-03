# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceProductDataObjectInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'str',
        'is_auto_renew': 'bool',
        'version_info': 'dict(str, list[ShowPeriodResponseInfo])'
    }

    attribute_map = {
        'charging_mode': 'charging_mode',
        'is_auto_renew': 'is_auto_renew',
        'version_info': 'version_info'
    }

    def __init__(self, charging_mode=None, is_auto_renew=None, version_info=None):
        """ResourceProductDataObjectInfo

        The model defined in huaweicloud sdk

        :param charging_mode: 计费模式   - packet_cycle : 包周期   - on_demand : 按需
        :type charging_mode: str
        :param is_auto_renew: 是否自动续费
        :type is_auto_renew: bool
        :param version_info: 版本信息,key对应的值为主机开通的版本，包含如下6种输入：   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。
        :type version_info: dict(str, list[ShowPeriodResponseInfo])
        """
        
        

        self._charging_mode = None
        self._is_auto_renew = None
        self._version_info = None
        self.discriminator = None

        if charging_mode is not None:
            self.charging_mode = charging_mode
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if version_info is not None:
            self.version_info = version_info

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ResourceProductDataObjectInfo.

        计费模式   - packet_cycle : 包周期   - on_demand : 按需

        :return: The charging_mode of this ResourceProductDataObjectInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ResourceProductDataObjectInfo.

        计费模式   - packet_cycle : 包周期   - on_demand : 按需

        :param charging_mode: The charging_mode of this ResourceProductDataObjectInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this ResourceProductDataObjectInfo.

        是否自动续费

        :return: The is_auto_renew of this ResourceProductDataObjectInfo.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this ResourceProductDataObjectInfo.

        是否自动续费

        :param is_auto_renew: The is_auto_renew of this ResourceProductDataObjectInfo.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def version_info(self):
        """Gets the version_info of this ResourceProductDataObjectInfo.

        版本信息,key对应的值为主机开通的版本，包含如下6种输入：   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :return: The version_info of this ResourceProductDataObjectInfo.
        :rtype: dict(str, list[ShowPeriodResponseInfo])
        """
        return self._version_info

    @version_info.setter
    def version_info(self, version_info):
        """Sets the version_info of this ResourceProductDataObjectInfo.

        版本信息,key对应的值为主机开通的版本，包含如下6种输入：   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :param version_info: The version_info of this ResourceProductDataObjectInfo.
        :type version_info: dict(str, list[ShowPeriodResponseInfo])
        """
        self._version_info = version_info

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
        if not isinstance(other, ResourceProductDataObjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
