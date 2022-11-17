# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppRulesBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_rules': 'list[AppRules]'
    }

    attribute_map = {
        'app_rules': 'appRules'
    }

    def __init__(self, app_rules=None):
        """AppRulesBody

        The model defined in huaweicloud sdk

        :param app_rules: 服务参数。
        :type app_rules: list[:class:`huaweicloudsdkaom.v2.AppRules`]
        """
        
        

        self._app_rules = None
        self.discriminator = None

        if app_rules is not None:
            self.app_rules = app_rules

    @property
    def app_rules(self):
        """Gets the app_rules of this AppRulesBody.

        服务参数。

        :return: The app_rules of this AppRulesBody.
        :rtype: list[:class:`huaweicloudsdkaom.v2.AppRules`]
        """
        return self._app_rules

    @app_rules.setter
    def app_rules(self, app_rules):
        """Sets the app_rules of this AppRulesBody.

        服务参数。

        :param app_rules: The app_rules of this AppRulesBody.
        :type app_rules: list[:class:`huaweicloudsdkaom.v2.AppRules`]
        """
        self._app_rules = app_rules

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
        if not isinstance(other, AppRulesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
