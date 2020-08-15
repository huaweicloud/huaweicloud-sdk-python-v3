# coding: utf-8

import pprint
import re

import six





class ThrottleBindingResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publish_id': 'str',
        'scope': 'int',
        'strategy_id': 'str',
        'apply_time': 'datetime',
        'id': 'str'
    }

    attribute_map = {
        'publish_id': 'publish_id',
        'scope': 'scope',
        'strategy_id': 'strategy_id',
        'apply_time': 'apply_time',
        'id': 'id'
    }

    def __init__(self, publish_id=None, scope=None, strategy_id=None, apply_time=None, id=None):
        """ThrottleBindingResp - a model defined in huaweicloud sdk"""
        
        

        self._publish_id = None
        self._scope = None
        self._strategy_id = None
        self._apply_time = None
        self._id = None
        self.discriminator = None

        if publish_id is not None:
            self.publish_id = publish_id
        if scope is not None:
            self.scope = scope
        if strategy_id is not None:
            self.strategy_id = strategy_id
        if apply_time is not None:
            self.apply_time = apply_time
        if id is not None:
            self.id = id

    @property
    def publish_id(self):
        """Gets the publish_id of this ThrottleBindingResp.

        API的发布记录编号

        :return: The publish_id of this ThrottleBindingResp.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        """Sets the publish_id of this ThrottleBindingResp.

        API的发布记录编号

        :param publish_id: The publish_id of this ThrottleBindingResp.
        :type: str
        """
        self._publish_id = publish_id

    @property
    def scope(self):
        """Gets the scope of this ThrottleBindingResp.

        策略作用域，取值如下： - 1：整个API - 2： 单个用户 - 3：单个APP  目前只支持1

        :return: The scope of this ThrottleBindingResp.
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ThrottleBindingResp.

        策略作用域，取值如下： - 1：整个API - 2： 单个用户 - 3：单个APP  目前只支持1

        :param scope: The scope of this ThrottleBindingResp.
        :type: int
        """
        self._scope = scope

    @property
    def strategy_id(self):
        """Gets the strategy_id of this ThrottleBindingResp.

        流控策略的ID

        :return: The strategy_id of this ThrottleBindingResp.
        :rtype: str
        """
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, strategy_id):
        """Sets the strategy_id of this ThrottleBindingResp.

        流控策略的ID

        :param strategy_id: The strategy_id of this ThrottleBindingResp.
        :type: str
        """
        self._strategy_id = strategy_id

    @property
    def apply_time(self):
        """Gets the apply_time of this ThrottleBindingResp.

        绑定时间

        :return: The apply_time of this ThrottleBindingResp.
        :rtype: datetime
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this ThrottleBindingResp.

        绑定时间

        :param apply_time: The apply_time of this ThrottleBindingResp.
        :type: datetime
        """
        self._apply_time = apply_time

    @property
    def id(self):
        """Gets the id of this ThrottleBindingResp.

        绑定关系的ID

        :return: The id of this ThrottleBindingResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ThrottleBindingResp.

        绑定关系的ID

        :param id: The id of this ThrottleBindingResp.
        :type: str
        """
        self._id = id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ThrottleBindingResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
