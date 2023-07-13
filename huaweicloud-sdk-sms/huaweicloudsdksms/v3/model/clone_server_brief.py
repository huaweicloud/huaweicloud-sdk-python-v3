# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloneServerBrief:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vm_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'vm_id': 'vm_id',
        'name': 'name'
    }

    def __init__(self, vm_id=None, name=None):
        """CloneServerBrief

        The model defined in huaweicloud sdk

        :param vm_id: 克隆服务器ID
        :type vm_id: str
        :param name: 克隆虚拟机的名称
        :type name: str
        """
        
        

        self._vm_id = None
        self._name = None
        self.discriminator = None

        if vm_id is not None:
            self.vm_id = vm_id
        if name is not None:
            self.name = name

    @property
    def vm_id(self):
        """Gets the vm_id of this CloneServerBrief.

        克隆服务器ID

        :return: The vm_id of this CloneServerBrief.
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this CloneServerBrief.

        克隆服务器ID

        :param vm_id: The vm_id of this CloneServerBrief.
        :type vm_id: str
        """
        self._vm_id = vm_id

    @property
    def name(self):
        """Gets the name of this CloneServerBrief.

        克隆虚拟机的名称

        :return: The name of this CloneServerBrief.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloneServerBrief.

        克隆虚拟机的名称

        :param name: The name of this CloneServerBrief.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CloneServerBrief):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
