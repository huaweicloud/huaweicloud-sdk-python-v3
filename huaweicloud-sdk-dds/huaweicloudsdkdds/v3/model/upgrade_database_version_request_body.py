# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeDatabaseVersionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upgrade_mode': 'str'
    }

    attribute_map = {
        'upgrade_mode': 'upgrade_mode'
    }

    def __init__(self, upgrade_mode=None):
        r"""UpgradeDatabaseVersionRequestBody

        The model defined in huaweicloud sdk

        :param upgrade_mode: 升级模式。  取值为“minimized_interrupt_time”为中断时间最短优先模式：升级过程对业务影响相对较小的升级方式  取值为“minimized_upgrade_time”为升级时长最短优先模式：升级过程时长相对较快的升级方式。  默认取值为“minimized_interrupt_time”。
        :type upgrade_mode: str
        """
        
        

        self._upgrade_mode = None
        self.discriminator = None

        if upgrade_mode is not None:
            self.upgrade_mode = upgrade_mode

    @property
    def upgrade_mode(self):
        r"""Gets the upgrade_mode of this UpgradeDatabaseVersionRequestBody.

        升级模式。  取值为“minimized_interrupt_time”为中断时间最短优先模式：升级过程对业务影响相对较小的升级方式  取值为“minimized_upgrade_time”为升级时长最短优先模式：升级过程时长相对较快的升级方式。  默认取值为“minimized_interrupt_time”。

        :return: The upgrade_mode of this UpgradeDatabaseVersionRequestBody.
        :rtype: str
        """
        return self._upgrade_mode

    @upgrade_mode.setter
    def upgrade_mode(self, upgrade_mode):
        r"""Sets the upgrade_mode of this UpgradeDatabaseVersionRequestBody.

        升级模式。  取值为“minimized_interrupt_time”为中断时间最短优先模式：升级过程对业务影响相对较小的升级方式  取值为“minimized_upgrade_time”为升级时长最短优先模式：升级过程时长相对较快的升级方式。  默认取值为“minimized_interrupt_time”。

        :param upgrade_mode: The upgrade_mode of this UpgradeDatabaseVersionRequestBody.
        :type upgrade_mode: str
        """
        self._upgrade_mode = upgrade_mode

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
        if not isinstance(other, UpgradeDatabaseVersionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
