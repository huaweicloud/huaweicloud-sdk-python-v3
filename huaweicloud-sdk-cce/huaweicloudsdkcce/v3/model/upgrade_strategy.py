# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'in_place_rolling_update': 'InPlaceRollingUpdate'
    }

    attribute_map = {
        'type': 'type',
        'in_place_rolling_update': 'inPlaceRollingUpdate'
    }

    def __init__(self, type=None, in_place_rolling_update=None):
        """UpgradeStrategy

        The model defined in huaweicloud sdk

        :param type: 升级策略类型，当前仅支持原地升级类型\&quot;inPlaceRollingUpdate\&quot;
        :type type: str
        :param in_place_rolling_update: 
        :type in_place_rolling_update: :class:`huaweicloudsdkcce.v3.InPlaceRollingUpdate`
        """
        
        

        self._type = None
        self._in_place_rolling_update = None
        self.discriminator = None

        self.type = type
        if in_place_rolling_update is not None:
            self.in_place_rolling_update = in_place_rolling_update

    @property
    def type(self):
        """Gets the type of this UpgradeStrategy.

        升级策略类型，当前仅支持原地升级类型\"inPlaceRollingUpdate\"

        :return: The type of this UpgradeStrategy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpgradeStrategy.

        升级策略类型，当前仅支持原地升级类型\"inPlaceRollingUpdate\"

        :param type: The type of this UpgradeStrategy.
        :type type: str
        """
        self._type = type

    @property
    def in_place_rolling_update(self):
        """Gets the in_place_rolling_update of this UpgradeStrategy.

        :return: The in_place_rolling_update of this UpgradeStrategy.
        :rtype: :class:`huaweicloudsdkcce.v3.InPlaceRollingUpdate`
        """
        return self._in_place_rolling_update

    @in_place_rolling_update.setter
    def in_place_rolling_update(self, in_place_rolling_update):
        """Sets the in_place_rolling_update of this UpgradeStrategy.

        :param in_place_rolling_update: The in_place_rolling_update of this UpgradeStrategy.
        :type in_place_rolling_update: :class:`huaweicloudsdkcce.v3.InPlaceRollingUpdate`
        """
        self._in_place_rolling_update = in_place_rolling_update

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
        if not isinstance(other, UpgradeStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
