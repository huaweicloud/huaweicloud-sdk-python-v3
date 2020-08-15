# coding: utf-8

import pprint
import re

import six





class ReferResources:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'ResourceType',
        'refer_alias': 'str',
        'parameters': 'object'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'refer_alias': 'refer_alias',
        'parameters': 'parameters'
    }

    def __init__(self, id=None, type=None, refer_alias=None, parameters=None):
        """ReferResources - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._type = None
        self._refer_alias = None
        self._parameters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if refer_alias is not None:
            self.refer_alias = refer_alias
        if parameters is not None:
            self.parameters = parameters

    @property
    def id(self):
        """Gets the id of this ReferResources.

        资源ID。

        :return: The id of this ReferResources.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReferResources.

        资源ID。

        :param id: The id of this ReferResources.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this ReferResources.


        :return: The type of this ReferResources.
        :rtype: ResourceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReferResources.


        :param type: The type of this ReferResources.
        :type: ResourceType
        """
        self._type = type

    @property
    def refer_alias(self):
        """Gets the refer_alias of this ReferResources.

        应用别名，dcs时才提供，支持“distributed_session”、“distributed_cache”、“distributed_session, distributed_cache”，  默认值是“distributed_session, distributed_cache”。 

        :return: The refer_alias of this ReferResources.
        :rtype: str
        """
        return self._refer_alias

    @refer_alias.setter
    def refer_alias(self, refer_alias):
        """Sets the refer_alias of this ReferResources.

        应用别名，dcs时才提供，支持“distributed_session”、“distributed_cache”、“distributed_session, distributed_cache”，  默认值是“distributed_session, distributed_cache”。 

        :param refer_alias: The refer_alias of this ReferResources.
        :type: str
        """
        self._refer_alias = refer_alias

    @property
    def parameters(self):
        """Gets the parameters of this ReferResources.

        引用资源参数。

        :return: The parameters of this ReferResources.
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ReferResources.

        引用资源参数。

        :param parameters: The parameters of this ReferResources.
        :type: object
        """
        self._parameters = parameters

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
        if not isinstance(other, ReferResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
