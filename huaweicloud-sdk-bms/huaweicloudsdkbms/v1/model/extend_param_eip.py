# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtendParamEip:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'chargingmode': 'str'
    }

    attribute_map = {
        'chargingmode': 'chargingmode'
    }

    def __init__(self, chargingmode=None):
        """ExtendParamEip

        The model defined in huaweicloud sdk

        :param chargingmode: 弹性公网IP的计费模式。若带宽计费类型为bandwidth，则支持prePaid和postPaid；若带宽计费类型为traffic，仅支持postPaid。取值范围：prePaid：预付费，即包年包月postPaid：后付费，即按需付费 说明：如果bandwidth对象中sharetype是WHOLE且id有值，弹性公网IP只能创建为按需付费的，故该参数传参“prePaid”无效。
        :type chargingmode: str
        """
        
        

        self._chargingmode = None
        self.discriminator = None

        self.chargingmode = chargingmode

    @property
    def chargingmode(self):
        """Gets the chargingmode of this ExtendParamEip.

        弹性公网IP的计费模式。若带宽计费类型为bandwidth，则支持prePaid和postPaid；若带宽计费类型为traffic，仅支持postPaid。取值范围：prePaid：预付费，即包年包月postPaid：后付费，即按需付费 说明：如果bandwidth对象中sharetype是WHOLE且id有值，弹性公网IP只能创建为按需付费的，故该参数传参“prePaid”无效。

        :return: The chargingmode of this ExtendParamEip.
        :rtype: str
        """
        return self._chargingmode

    @chargingmode.setter
    def chargingmode(self, chargingmode):
        """Sets the chargingmode of this ExtendParamEip.

        弹性公网IP的计费模式。若带宽计费类型为bandwidth，则支持prePaid和postPaid；若带宽计费类型为traffic，仅支持postPaid。取值范围：prePaid：预付费，即包年包月postPaid：后付费，即按需付费 说明：如果bandwidth对象中sharetype是WHOLE且id有值，弹性公网IP只能创建为按需付费的，故该参数传参“prePaid”无效。

        :param chargingmode: The chargingmode of this ExtendParamEip.
        :type chargingmode: str
        """
        self._chargingmode = chargingmode

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
        if not isinstance(other, ExtendParamEip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
