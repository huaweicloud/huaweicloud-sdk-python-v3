# coding: utf-8

import pprint
import re

import six





class ProtectablesResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'children': 'list[object]',
        'detail': 'object',
        'id': 'str',
        'name': 'str',
        'protectable': 'ProtectableResult',
        'size': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'children': 'children',
        'detail': 'detail',
        'id': 'id',
        'name': 'name',
        'protectable': 'protectable',
        'size': 'size',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, children=None, detail=None, id=None, name=None, protectable=None, size=None, status=None, type=None):
        """ProtectablesResp - a model defined in huaweicloud sdk"""
        
        

        self._children = None
        self._detail = None
        self._id = None
        self._name = None
        self._protectable = None
        self._size = None
        self._status = None
        self._type = None
        self.discriminator = None

        self.children = children
        if detail is not None:
            self.detail = detail
        self.id = id
        self.name = name
        self.protectable = protectable
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        self.type = type

    @property
    def children(self):
        """Gets the children of this ProtectablesResp.

        子资源

        :return: The children of this ProtectablesResp.
        :rtype: list[object]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ProtectablesResp.

        子资源

        :param children: The children of this ProtectablesResp.
        :type: list[object]
        """
        self._children = children

    @property
    def detail(self):
        """Gets the detail of this ProtectablesResp.

        资源详情

        :return: The detail of this ProtectablesResp.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ProtectablesResp.

        资源详情

        :param detail: The detail of this ProtectablesResp.
        :type: object
        """
        self._detail = detail

    @property
    def id(self):
        """Gets the id of this ProtectablesResp.

        id

        :return: The id of this ProtectablesResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProtectablesResp.

        id

        :param id: The id of this ProtectablesResp.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ProtectablesResp.

        名称

        :return: The name of this ProtectablesResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProtectablesResp.

        名称

        :param name: The name of this ProtectablesResp.
        :type: str
        """
        self._name = name

    @property
    def protectable(self):
        """Gets the protectable of this ProtectablesResp.


        :return: The protectable of this ProtectablesResp.
        :rtype: ProtectableResult
        """
        return self._protectable

    @protectable.setter
    def protectable(self, protectable):
        """Sets the protectable of this ProtectablesResp.


        :param protectable: The protectable of this ProtectablesResp.
        :type: ProtectableResult
        """
        self._protectable = protectable

    @property
    def size(self):
        """Gets the size of this ProtectablesResp.

        大小，单位GB

        :return: The size of this ProtectablesResp.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ProtectablesResp.

        大小，单位GB

        :param size: The size of this ProtectablesResp.
        :type: str
        """
        self._size = size

    @property
    def status(self):
        """Gets the status of this ProtectablesResp.

        资源状态

        :return: The status of this ProtectablesResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProtectablesResp.

        资源状态

        :param status: The status of this ProtectablesResp.
        :type: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ProtectablesResp.

        [待备份资源的类型: OS::Nova::Server, OS::Cinder::Volume, OS::Ironic::BareMetalServer, OS::Native::Server, OS::Sfs::Turbo](tag:hws,hws_hk,fcs_vm,ctc) [待备份资源的类型: OS::Nova::Server,  OS::Cinder::Volume](tag:dt,ocb,tlf,sbc)

        :return: The type of this ProtectablesResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProtectablesResp.

        [待备份资源的类型: OS::Nova::Server, OS::Cinder::Volume, OS::Ironic::BareMetalServer, OS::Native::Server, OS::Sfs::Turbo](tag:hws,hws_hk,fcs_vm,ctc) [待备份资源的类型: OS::Nova::Server,  OS::Cinder::Volume](tag:dt,ocb,tlf,sbc)

        :param type: The type of this ProtectablesResp.
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
        if not isinstance(other, ProtectablesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
