# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertAlertType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'alert_type': 'str'
    }

    attribute_map = {
        'category': 'category',
        'alert_type': 'alert_type'
    }

    def __init__(self, category=None, alert_type=None):
        r"""AlertAlertType

        The model defined in huaweicloud sdk

        :param category: 类别
        :type category: str
        :param alert_type: 告警类型
        :type alert_type: str
        """
        
        

        self._category = None
        self._alert_type = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if alert_type is not None:
            self.alert_type = alert_type

    @property
    def category(self):
        r"""Gets the category of this AlertAlertType.

        类别

        :return: The category of this AlertAlertType.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this AlertAlertType.

        类别

        :param category: The category of this AlertAlertType.
        :type category: str
        """
        self._category = category

    @property
    def alert_type(self):
        r"""Gets the alert_type of this AlertAlertType.

        告警类型

        :return: The alert_type of this AlertAlertType.
        :rtype: str
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        r"""Sets the alert_type of this AlertAlertType.

        告警类型

        :param alert_type: The alert_type of this AlertAlertType.
        :type alert_type: str
        """
        self._alert_type = alert_type

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
        if not isinstance(other, AlertAlertType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
