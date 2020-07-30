# coding: utf-8

import pprint
import re

import six





class Resource:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'extra_info': 'ResourceExtraInfo',
        'id': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'extra_info': 'extra_info',
        'id': 'id',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, extra_info=None, id=None, name=None, type=None):
        """Resource - a model defined in huaweicloud sdk"""
        
        

        self._extra_info = None
        self._id = None
        self._name = None
        self._type = None
        self.discriminator = None

        if extra_info is not None:
            self.extra_info = extra_info
        self.id = id
        self.name = name
        self.type = type

    @property
    def extra_info(self):
        """Gets the extra_info of this Resource.


        :return: The extra_info of this Resource.
        :rtype: ResourceExtraInfo
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this Resource.


        :param extra_info: The extra_info of this Resource.
        :type: ResourceExtraInfo
        """
        self._extra_info = extra_info

    @property
    def id(self):
        """Gets the id of this Resource.

        待备份资源id

        :return: The id of this Resource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Resource.

        待备份资源id

        :param id: The id of this Resource.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Resource.

        待备份资源名称，长度限制：0-255

        :return: The name of this Resource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Resource.

        待备份资源名称，长度限制：0-255

        :param name: The name of this Resource.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this Resource.

        [待备份资源的类型: OS::Nova::Server, OS::Cinder::Volume, OS::Ironic::BareMetalServer, OS::Native::Server, OS::Sfs::Turbo](tag:hws,hws_hk,fcs_vm,ctc) [待备份资源的类型: OS::Nova::Server,  OS::Cinder::Volume](tag:dt,ocb,tlf,sbc)

        :return: The type of this Resource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Resource.

        [待备份资源的类型: OS::Nova::Server, OS::Cinder::Volume, OS::Ironic::BareMetalServer, OS::Native::Server, OS::Sfs::Turbo](tag:hws,hws_hk,fcs_vm,ctc) [待备份资源的类型: OS::Nova::Server,  OS::Cinder::Volume](tag:dt,ocb,tlf,sbc)

        :param type: The type of this Resource.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
