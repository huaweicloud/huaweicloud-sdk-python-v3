# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IotdaContentRuleRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'products': 'list[str]',
        'rule_actions': 'list[IotdaRuleAction]'
    }

    attribute_map = {
        'app_id': 'app_id',
        'products': 'products',
        'rule_actions': 'rule_actions'
    }

    def __init__(self, app_id=None, products=None, rule_actions=None):
        """IotdaContentRuleRsp

        The model defined in huaweicloud sdk

        :param app_id: IoTDA中的资源空间Id
        :type app_id: str
        :param products: IoTDA中某资源空间Id下的产品列表
        :type products: list[str]
        :param rule_actions: IoTDA中rule_id和action_id列表
        :type rule_actions: list[:class:`huaweicloudsdkiotanalytics.v1.IotdaRuleAction`]
        """
        
        

        self._app_id = None
        self._products = None
        self._rule_actions = None
        self.discriminator = None

        self.app_id = app_id
        self.products = products
        self.rule_actions = rule_actions

    @property
    def app_id(self):
        """Gets the app_id of this IotdaContentRuleRsp.

        IoTDA中的资源空间Id

        :return: The app_id of this IotdaContentRuleRsp.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this IotdaContentRuleRsp.

        IoTDA中的资源空间Id

        :param app_id: The app_id of this IotdaContentRuleRsp.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def products(self):
        """Gets the products of this IotdaContentRuleRsp.

        IoTDA中某资源空间Id下的产品列表

        :return: The products of this IotdaContentRuleRsp.
        :rtype: list[str]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this IotdaContentRuleRsp.

        IoTDA中某资源空间Id下的产品列表

        :param products: The products of this IotdaContentRuleRsp.
        :type products: list[str]
        """
        self._products = products

    @property
    def rule_actions(self):
        """Gets the rule_actions of this IotdaContentRuleRsp.

        IoTDA中rule_id和action_id列表

        :return: The rule_actions of this IotdaContentRuleRsp.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.IotdaRuleAction`]
        """
        return self._rule_actions

    @rule_actions.setter
    def rule_actions(self, rule_actions):
        """Sets the rule_actions of this IotdaContentRuleRsp.

        IoTDA中rule_id和action_id列表

        :param rule_actions: The rule_actions of this IotdaContentRuleRsp.
        :type rule_actions: list[:class:`huaweicloudsdkiotanalytics.v1.IotdaRuleAction`]
        """
        self._rule_actions = rule_actions

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
        if not isinstance(other, IotdaContentRuleRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
