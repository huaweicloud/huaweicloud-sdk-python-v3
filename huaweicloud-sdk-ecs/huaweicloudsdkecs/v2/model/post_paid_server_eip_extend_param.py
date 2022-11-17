# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidServerEipExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'str'
    }

    attribute_map = {
        'charging_mode': 'chargingMode'
    }

    def __init__(self, charging_mode=None):
        """PostPaidServerEipExtendParam

        The model defined in huaweicloud sdk

        :param charging_mode: 公网IP的计费模式。  取值范围：  - prePaid-预付费，即包年包月； - postPaid-后付费，即按需付费；  &gt; 说明： &gt;  &gt; 如果bandwidth对象中share_type是WHOLE且id有值，弹性IP只能创建为按需付费的，故该参数传参“prePaid”无效。
        :type charging_mode: str
        """
        
        

        self._charging_mode = None
        self.discriminator = None

        if charging_mode is not None:
            self.charging_mode = charging_mode

    @property
    def charging_mode(self):
        """Gets the charging_mode of this PostPaidServerEipExtendParam.

        公网IP的计费模式。  取值范围：  - prePaid-预付费，即包年包月； - postPaid-后付费，即按需付费；  > 说明： >  > 如果bandwidth对象中share_type是WHOLE且id有值，弹性IP只能创建为按需付费的，故该参数传参“prePaid”无效。

        :return: The charging_mode of this PostPaidServerEipExtendParam.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this PostPaidServerEipExtendParam.

        公网IP的计费模式。  取值范围：  - prePaid-预付费，即包年包月； - postPaid-后付费，即按需付费；  > 说明： >  > 如果bandwidth对象中share_type是WHOLE且id有值，弹性IP只能创建为按需付费的，故该参数传参“prePaid”无效。

        :param charging_mode: The charging_mode of this PostPaidServerEipExtendParam.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

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
        if not isinstance(other, PostPaidServerEipExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
