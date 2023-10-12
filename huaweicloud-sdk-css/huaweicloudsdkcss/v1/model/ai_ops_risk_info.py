# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIOpsRiskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_type': 'str',
        'level': 'str',
        'desc': 'str',
        'suggestion': 'str'
    }

    attribute_map = {
        'risk_type': 'riskType',
        'level': 'level',
        'desc': 'desc',
        'suggestion': 'suggestion'
    }

    def __init__(self, risk_type=None, level=None, desc=None, suggestion=None):
        """AIOpsRiskInfo

        The model defined in huaweicloud sdk

        :param risk_type: 检测项介绍。
        :type risk_type: str
        :param level: 风险等级。 - high - medium - suggestion
        :type level: str
        :param desc: 风险描述。
        :type desc: str
        :param suggestion: 风险建议。
        :type suggestion: str
        """
        
        

        self._risk_type = None
        self._level = None
        self._desc = None
        self._suggestion = None
        self.discriminator = None

        if risk_type is not None:
            self.risk_type = risk_type
        if level is not None:
            self.level = level
        if desc is not None:
            self.desc = desc
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def risk_type(self):
        """Gets the risk_type of this AIOpsRiskInfo.

        检测项介绍。

        :return: The risk_type of this AIOpsRiskInfo.
        :rtype: str
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        """Sets the risk_type of this AIOpsRiskInfo.

        检测项介绍。

        :param risk_type: The risk_type of this AIOpsRiskInfo.
        :type risk_type: str
        """
        self._risk_type = risk_type

    @property
    def level(self):
        """Gets the level of this AIOpsRiskInfo.

        风险等级。 - high - medium - suggestion

        :return: The level of this AIOpsRiskInfo.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this AIOpsRiskInfo.

        风险等级。 - high - medium - suggestion

        :param level: The level of this AIOpsRiskInfo.
        :type level: str
        """
        self._level = level

    @property
    def desc(self):
        """Gets the desc of this AIOpsRiskInfo.

        风险描述。

        :return: The desc of this AIOpsRiskInfo.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this AIOpsRiskInfo.

        风险描述。

        :param desc: The desc of this AIOpsRiskInfo.
        :type desc: str
        """
        self._desc = desc

    @property
    def suggestion(self):
        """Gets the suggestion of this AIOpsRiskInfo.

        风险建议。

        :return: The suggestion of this AIOpsRiskInfo.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this AIOpsRiskInfo.

        风险建议。

        :param suggestion: The suggestion of this AIOpsRiskInfo.
        :type suggestion: str
        """
        self._suggestion = suggestion

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
        if not isinstance(other, AIOpsRiskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
