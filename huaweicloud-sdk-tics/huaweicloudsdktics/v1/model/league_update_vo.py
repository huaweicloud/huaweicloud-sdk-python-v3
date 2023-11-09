# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LeagueUpdateVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'dp_enabled': 'bool',
        'privacy_protection_type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'dp_enabled': 'dp_enabled',
        'privacy_protection_type': 'privacy_protection_type'
    }

    def __init__(self, description=None, dp_enabled=None, privacy_protection_type=None):
        """LeagueUpdateVo

        The model defined in huaweicloud sdk

        :param description: 描述
        :type description: str
        :param dp_enabled: 差分隐私开关
        :type dp_enabled: bool
        :param privacy_protection_type: 隐私保护类别，HIGH.高，STANDARD.标准
        :type privacy_protection_type: str
        """
        
        

        self._description = None
        self._dp_enabled = None
        self._privacy_protection_type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if dp_enabled is not None:
            self.dp_enabled = dp_enabled
        if privacy_protection_type is not None:
            self.privacy_protection_type = privacy_protection_type

    @property
    def description(self):
        """Gets the description of this LeagueUpdateVo.

        描述

        :return: The description of this LeagueUpdateVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LeagueUpdateVo.

        描述

        :param description: The description of this LeagueUpdateVo.
        :type description: str
        """
        self._description = description

    @property
    def dp_enabled(self):
        """Gets the dp_enabled of this LeagueUpdateVo.

        差分隐私开关

        :return: The dp_enabled of this LeagueUpdateVo.
        :rtype: bool
        """
        return self._dp_enabled

    @dp_enabled.setter
    def dp_enabled(self, dp_enabled):
        """Sets the dp_enabled of this LeagueUpdateVo.

        差分隐私开关

        :param dp_enabled: The dp_enabled of this LeagueUpdateVo.
        :type dp_enabled: bool
        """
        self._dp_enabled = dp_enabled

    @property
    def privacy_protection_type(self):
        """Gets the privacy_protection_type of this LeagueUpdateVo.

        隐私保护类别，HIGH.高，STANDARD.标准

        :return: The privacy_protection_type of this LeagueUpdateVo.
        :rtype: str
        """
        return self._privacy_protection_type

    @privacy_protection_type.setter
    def privacy_protection_type(self, privacy_protection_type):
        """Sets the privacy_protection_type of this LeagueUpdateVo.

        隐私保护类别，HIGH.高，STANDARD.标准

        :param privacy_protection_type: The privacy_protection_type of this LeagueUpdateVo.
        :type privacy_protection_type: str
        """
        self._privacy_protection_type = privacy_protection_type

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
        if not isinstance(other, LeagueUpdateVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
