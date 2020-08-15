# coding: utf-8

import pprint
import re

import six





class Stacks:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'arm_config': 'StacksConfig',
        'config': 'StacksConfig',
        'creator': 'str',
        'description': 'str',
        'disable': 'bool',
        'id': 'int',
        'label': 'str',
        'logo': 'str',
        'name': 'str',
        'scope': 'str',
        'stack_id': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'arm_config': 'arm_config',
        'config': 'config',
        'creator': 'creator',
        'description': 'description',
        'disable': 'disable',
        'id': 'id',
        'label': 'label',
        'logo': 'logo',
        'name': 'name',
        'scope': 'scope',
        'stack_id': 'stack_id',
        'tags': 'tags'
    }

    def __init__(self, arm_config=None, config=None, creator=None, description=None, disable=None, id=None, label=None, logo=None, name=None, scope=None, stack_id=None, tags=None):
        """Stacks - a model defined in huaweicloud sdk"""
        
        

        self._arm_config = None
        self._config = None
        self._creator = None
        self._description = None
        self._disable = None
        self._id = None
        self._label = None
        self._logo = None
        self._name = None
        self._scope = None
        self._stack_id = None
        self._tags = None
        self.discriminator = None

        if arm_config is not None:
            self.arm_config = arm_config
        if config is not None:
            self.config = config
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if disable is not None:
            self.disable = disable
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if logo is not None:
            self.logo = logo
        if name is not None:
            self.name = name
        if scope is not None:
            self.scope = scope
        if stack_id is not None:
            self.stack_id = stack_id
        if tags is not None:
            self.tags = tags

    @property
    def arm_config(self):
        """Gets the arm_config of this Stacks.


        :return: The arm_config of this Stacks.
        :rtype: StacksConfig
        """
        return self._arm_config

    @arm_config.setter
    def arm_config(self, arm_config):
        """Sets the arm_config of this Stacks.


        :param arm_config: The arm_config of this Stacks.
        :type: StacksConfig
        """
        self._arm_config = arm_config

    @property
    def config(self):
        """Gets the config of this Stacks.


        :return: The config of this Stacks.
        :rtype: StacksConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Stacks.


        :param config: The config of this Stacks.
        :type: StacksConfig
        """
        self._config = config

    @property
    def creator(self):
        """Gets the creator of this Stacks.

        创建人

        :return: The creator of this Stacks.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Stacks.

        创建人

        :param creator: The creator of this Stacks.
        :type: str
        """
        self._creator = creator

    @property
    def description(self):
        """Gets the description of this Stacks.

        描述

        :return: The description of this Stacks.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Stacks.

        描述

        :param description: The description of this Stacks.
        :type: str
        """
        self._description = description

    @property
    def disable(self):
        """Gets the disable of this Stacks.

        是否可用

        :return: The disable of this Stacks.
        :rtype: bool
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        """Sets the disable of this Stacks.

        是否可用

        :param disable: The disable of this Stacks.
        :type: bool
        """
        self._disable = disable

    @property
    def id(self):
        """Gets the id of this Stacks.

        id

        :return: The id of this Stacks.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Stacks.

        id

        :param id: The id of this Stacks.
        :type: int
        """
        self._id = id

    @property
    def label(self):
        """Gets the label of this Stacks.

        标签

        :return: The label of this Stacks.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Stacks.

        标签

        :param label: The label of this Stacks.
        :type: str
        """
        self._label = label

    @property
    def logo(self):
        """Gets the logo of this Stacks.

        图标

        :return: The logo of this Stacks.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Stacks.

        图标

        :param logo: The logo of this Stacks.
        :type: str
        """
        self._logo = logo

    @property
    def name(self):
        """Gets the name of this Stacks.

        技术栈名称

        :return: The name of this Stacks.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Stacks.

        技术栈名称

        :param name: The name of this Stacks.
        :type: str
        """
        self._name = name

    @property
    def scope(self):
        """Gets the scope of this Stacks.

        范围

        :return: The scope of this Stacks.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Stacks.

        范围

        :param scope: The scope of this Stacks.
        :type: str
        """
        self._scope = scope

    @property
    def stack_id(self):
        """Gets the stack_id of this Stacks.

        技术栈ID 目前可取值all，java，go，python，cpp，nodejs，quantum，blockchain，dcn，vue，ruby。

        :return: The stack_id of this Stacks.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this Stacks.

        技术栈ID 目前可取值all，java，go，python，cpp，nodejs，quantum，blockchain，dcn，vue，ruby。

        :param stack_id: The stack_id of this Stacks.
        :type: str
        """
        self._stack_id = stack_id

    @property
    def tags(self):
        """Gets the tags of this Stacks.

        tags

        :return: The tags of this Stacks.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Stacks.

        tags

        :param tags: The tags of this Stacks.
        :type: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, Stacks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
