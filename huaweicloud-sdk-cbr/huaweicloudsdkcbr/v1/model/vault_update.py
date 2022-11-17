# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VaultUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'billing': 'BillingUpdate',
        'name': 'str',
        'auto_bind': 'bool',
        'bind_rules': 'VaultBindRules',
        'auto_expand': 'bool',
        'smn_notify': 'bool',
        'threshold': 'int'
    }

    attribute_map = {
        'billing': 'billing',
        'name': 'name',
        'auto_bind': 'auto_bind',
        'bind_rules': 'bind_rules',
        'auto_expand': 'auto_expand',
        'smn_notify': 'smn_notify',
        'threshold': 'threshold'
    }

    def __init__(self, billing=None, name=None, auto_bind=None, bind_rules=None, auto_expand=None, smn_notify=None, threshold=None):
        """VaultUpdate

        The model defined in huaweicloud sdk

        :param billing: 
        :type billing: :class:`huaweicloudsdkcbr.v1.BillingUpdate`
        :param name: 存储库名称
        :type name: str
        :param auto_bind: 是否支持自动挂载
        :type auto_bind: bool
        :param bind_rules: 
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        :param auto_expand: 是否自动扩容。按需存储库支持自动扩容，包周期存储库不支持扩容。
        :type auto_expand: bool
        :param smn_notify: 发送smn通知开关
        :type smn_notify: bool
        :param threshold: 存储库容量阈值，存储库已用容量和总容量的百分比超过该值，若smn_notify为开，将发送相关通知。
        :type threshold: int
        """
        
        

        self._billing = None
        self._name = None
        self._auto_bind = None
        self._bind_rules = None
        self._auto_expand = None
        self._smn_notify = None
        self._threshold = None
        self.discriminator = None

        if billing is not None:
            self.billing = billing
        if name is not None:
            self.name = name
        if auto_bind is not None:
            self.auto_bind = auto_bind
        if bind_rules is not None:
            self.bind_rules = bind_rules
        if auto_expand is not None:
            self.auto_expand = auto_expand
        if smn_notify is not None:
            self.smn_notify = smn_notify
        if threshold is not None:
            self.threshold = threshold

    @property
    def billing(self):
        """Gets the billing of this VaultUpdate.

        :return: The billing of this VaultUpdate.
        :rtype: :class:`huaweicloudsdkcbr.v1.BillingUpdate`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this VaultUpdate.

        :param billing: The billing of this VaultUpdate.
        :type billing: :class:`huaweicloudsdkcbr.v1.BillingUpdate`
        """
        self._billing = billing

    @property
    def name(self):
        """Gets the name of this VaultUpdate.

        存储库名称

        :return: The name of this VaultUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VaultUpdate.

        存储库名称

        :param name: The name of this VaultUpdate.
        :type name: str
        """
        self._name = name

    @property
    def auto_bind(self):
        """Gets the auto_bind of this VaultUpdate.

        是否支持自动挂载

        :return: The auto_bind of this VaultUpdate.
        :rtype: bool
        """
        return self._auto_bind

    @auto_bind.setter
    def auto_bind(self, auto_bind):
        """Sets the auto_bind of this VaultUpdate.

        是否支持自动挂载

        :param auto_bind: The auto_bind of this VaultUpdate.
        :type auto_bind: bool
        """
        self._auto_bind = auto_bind

    @property
    def bind_rules(self):
        """Gets the bind_rules of this VaultUpdate.

        :return: The bind_rules of this VaultUpdate.
        :rtype: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        return self._bind_rules

    @bind_rules.setter
    def bind_rules(self, bind_rules):
        """Sets the bind_rules of this VaultUpdate.

        :param bind_rules: The bind_rules of this VaultUpdate.
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        self._bind_rules = bind_rules

    @property
    def auto_expand(self):
        """Gets the auto_expand of this VaultUpdate.

        是否自动扩容。按需存储库支持自动扩容，包周期存储库不支持扩容。

        :return: The auto_expand of this VaultUpdate.
        :rtype: bool
        """
        return self._auto_expand

    @auto_expand.setter
    def auto_expand(self, auto_expand):
        """Sets the auto_expand of this VaultUpdate.

        是否自动扩容。按需存储库支持自动扩容，包周期存储库不支持扩容。

        :param auto_expand: The auto_expand of this VaultUpdate.
        :type auto_expand: bool
        """
        self._auto_expand = auto_expand

    @property
    def smn_notify(self):
        """Gets the smn_notify of this VaultUpdate.

        发送smn通知开关

        :return: The smn_notify of this VaultUpdate.
        :rtype: bool
        """
        return self._smn_notify

    @smn_notify.setter
    def smn_notify(self, smn_notify):
        """Sets the smn_notify of this VaultUpdate.

        发送smn通知开关

        :param smn_notify: The smn_notify of this VaultUpdate.
        :type smn_notify: bool
        """
        self._smn_notify = smn_notify

    @property
    def threshold(self):
        """Gets the threshold of this VaultUpdate.

        存储库容量阈值，存储库已用容量和总容量的百分比超过该值，若smn_notify为开，将发送相关通知。

        :return: The threshold of this VaultUpdate.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this VaultUpdate.

        存储库容量阈值，存储库已用容量和总容量的百分比超过该值，若smn_notify为开，将发送相关通知。

        :param threshold: The threshold of this VaultUpdate.
        :type threshold: int
        """
        self._threshold = threshold

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
        if not isinstance(other, VaultUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
