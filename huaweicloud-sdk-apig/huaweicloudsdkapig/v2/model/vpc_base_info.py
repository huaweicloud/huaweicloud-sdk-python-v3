# coding: utf-8

import pprint
import re

import six





class VpcBaseInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ecs_id': 'str',
        'ecs_name': 'int',
        'cascade_flag': 'bool'
    }

    attribute_map = {
        'ecs_id': 'ecs_id',
        'ecs_name': 'ecs_name',
        'cascade_flag': 'cascade_flag'
    }

    def __init__(self, ecs_id=None, ecs_name=None, cascade_flag=None):
        """VpcBaseInfo - a model defined in huaweicloud sdk"""
        
        

        self._ecs_id = None
        self._ecs_name = None
        self._cascade_flag = None
        self.discriminator = None

        if ecs_id is not None:
            self.ecs_id = ecs_id
        if ecs_name is not None:
            self.ecs_name = ecs_name
        if cascade_flag is not None:
            self.cascade_flag = cascade_flag

    @property
    def ecs_id(self):
        """Gets the ecs_id of this VpcBaseInfo.

        云服务器ID

        :return: The ecs_id of this VpcBaseInfo.
        :rtype: str
        """
        return self._ecs_id

    @ecs_id.setter
    def ecs_id(self, ecs_id):
        """Sets the ecs_id of this VpcBaseInfo.

        云服务器ID

        :param ecs_id: The ecs_id of this VpcBaseInfo.
        :type: str
        """
        self._ecs_id = ecs_id

    @property
    def ecs_name(self):
        """Gets the ecs_name of this VpcBaseInfo.

        云服务器名称

        :return: The ecs_name of this VpcBaseInfo.
        :rtype: int
        """
        return self._ecs_name

    @ecs_name.setter
    def ecs_name(self, ecs_name):
        """Sets the ecs_name of this VpcBaseInfo.

        云服务器名称

        :param ecs_name: The ecs_name of this VpcBaseInfo.
        :type: int
        """
        self._ecs_name = ecs_name

    @property
    def cascade_flag(self):
        """Gets the cascade_flag of this VpcBaseInfo.

        是否使用级联方式  暂不支持

        :return: The cascade_flag of this VpcBaseInfo.
        :rtype: bool
        """
        return self._cascade_flag

    @cascade_flag.setter
    def cascade_flag(self, cascade_flag):
        """Sets the cascade_flag of this VpcBaseInfo.

        是否使用级联方式  暂不支持

        :param cascade_flag: The cascade_flag of this VpcBaseInfo.
        :type: bool
        """
        self._cascade_flag = cascade_flag

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
        if not isinstance(other, VpcBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
