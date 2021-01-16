# coding: utf-8

import pprint
import re

import six





class BasicInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'owner': 'str',
        'priority': 'str',
        'execute_user': 'str',
        'instance_timeout': 'str',
        'custom_fields': 'object'
    }

    attribute_map = {
        'owner': 'owner',
        'priority': 'priority',
        'execute_user': 'executeUser',
        'instance_timeout': 'instanceTimeout',
        'custom_fields': 'customFields'
    }

    def __init__(self, owner=None, priority=None, execute_user=None, instance_timeout=None, custom_fields=None):
        """BasicInfo - a model defined in huaweicloud sdk"""
        
        

        self._owner = None
        self._priority = None
        self._execute_user = None
        self._instance_timeout = None
        self._custom_fields = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if priority is not None:
            self.priority = priority
        if execute_user is not None:
            self.execute_user = execute_user
        if instance_timeout is not None:
            self.instance_timeout = instance_timeout
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def owner(self):
        """Gets the owner of this BasicInfo.

        作业责任人

        :return: The owner of this BasicInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this BasicInfo.

        作业责任人

        :param owner: The owner of this BasicInfo.
        :type: str
        """
        self._owner = owner

    @property
    def priority(self):
        """Gets the priority of this BasicInfo.

        作业优先级

        :return: The priority of this BasicInfo.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this BasicInfo.

        作业优先级

        :param priority: The priority of this BasicInfo.
        :type: str
        """
        self._priority = priority

    @property
    def execute_user(self):
        """Gets the execute_user of this BasicInfo.

        作业执行用户

        :return: The execute_user of this BasicInfo.
        :rtype: str
        """
        return self._execute_user

    @execute_user.setter
    def execute_user(self, execute_user):
        """Sets the execute_user of this BasicInfo.

        作业执行用户

        :param execute_user: The execute_user of this BasicInfo.
        :type: str
        """
        self._execute_user = execute_user

    @property
    def instance_timeout(self):
        """Gets the instance_timeout of this BasicInfo.

        实例超时时间

        :return: The instance_timeout of this BasicInfo.
        :rtype: str
        """
        return self._instance_timeout

    @instance_timeout.setter
    def instance_timeout(self, instance_timeout):
        """Sets the instance_timeout of this BasicInfo.

        实例超时时间

        :param instance_timeout: The instance_timeout of this BasicInfo.
        :type: str
        """
        self._instance_timeout = instance_timeout

    @property
    def custom_fields(self):
        """Gets the custom_fields of this BasicInfo.

        用户自定义属性字段

        :return: The custom_fields of this BasicInfo.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this BasicInfo.

        用户自定义属性字段

        :param custom_fields: The custom_fields of this BasicInfo.
        :type: object
        """
        self._custom_fields = custom_fields

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
        if not isinstance(other, BasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
