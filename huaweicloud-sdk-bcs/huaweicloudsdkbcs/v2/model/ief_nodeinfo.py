# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IefNodeinfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'public_ip_address': 'str',
        'id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'public_ip_address': 'public_ip_address',
        'id': 'id'
    }

    def __init__(self, status=None, public_ip_address=None, id=None):
        """IefNodeinfo

        The model defined in huaweicloud sdk

        :param status: 节点状态，要使用此节点的话，该状态值必须为ACTIVE
        :type status: str
        :param public_ip_address: 节点IP，填写节点所在的EIP地址
        :type public_ip_address: str
        :param id: ief节点id值
        :type id: str
        """
        
        

        self._status = None
        self._public_ip_address = None
        self._id = None
        self.discriminator = None

        self.status = status
        self.public_ip_address = public_ip_address
        self.id = id

    @property
    def status(self):
        """Gets the status of this IefNodeinfo.

        节点状态，要使用此节点的话，该状态值必须为ACTIVE

        :return: The status of this IefNodeinfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IefNodeinfo.

        节点状态，要使用此节点的话，该状态值必须为ACTIVE

        :param status: The status of this IefNodeinfo.
        :type status: str
        """
        self._status = status

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this IefNodeinfo.

        节点IP，填写节点所在的EIP地址

        :return: The public_ip_address of this IefNodeinfo.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this IefNodeinfo.

        节点IP，填写节点所在的EIP地址

        :param public_ip_address: The public_ip_address of this IefNodeinfo.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def id(self):
        """Gets the id of this IefNodeinfo.

        ief节点id值

        :return: The id of this IefNodeinfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IefNodeinfo.

        ief节点id值

        :param id: The id of this IefNodeinfo.
        :type id: str
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
        if not isinstance(other, IefNodeinfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
