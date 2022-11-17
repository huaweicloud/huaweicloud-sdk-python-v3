# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckNetAclRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        't_project_id': 'str',
        't_network_id': 'str',
        'region_id': 'str',
        'os_type': 'str'
    }

    attribute_map = {
        't_project_id': 't_project_id',
        't_network_id': 't_network_id',
        'region_id': 'region_id',
        'os_type': 'os_type'
    }

    def __init__(self, t_project_id=None, t_network_id=None, region_id=None, os_type=None):
        """CheckNetAclRequest

        The model defined in huaweicloud sdk

        :param t_project_id: 目的虚拟机所属project_id
        :type t_project_id: str
        :param t_network_id: 目的端子网ID
        :type t_network_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param os_type: 操作系统类型
        :type os_type: str
        """
        
        

        self._t_project_id = None
        self._t_network_id = None
        self._region_id = None
        self._os_type = None
        self.discriminator = None

        self.t_project_id = t_project_id
        self.t_network_id = t_network_id
        self.region_id = region_id
        self.os_type = os_type

    @property
    def t_project_id(self):
        """Gets the t_project_id of this CheckNetAclRequest.

        目的虚拟机所属project_id

        :return: The t_project_id of this CheckNetAclRequest.
        :rtype: str
        """
        return self._t_project_id

    @t_project_id.setter
    def t_project_id(self, t_project_id):
        """Sets the t_project_id of this CheckNetAclRequest.

        目的虚拟机所属project_id

        :param t_project_id: The t_project_id of this CheckNetAclRequest.
        :type t_project_id: str
        """
        self._t_project_id = t_project_id

    @property
    def t_network_id(self):
        """Gets the t_network_id of this CheckNetAclRequest.

        目的端子网ID

        :return: The t_network_id of this CheckNetAclRequest.
        :rtype: str
        """
        return self._t_network_id

    @t_network_id.setter
    def t_network_id(self, t_network_id):
        """Sets the t_network_id of this CheckNetAclRequest.

        目的端子网ID

        :param t_network_id: The t_network_id of this CheckNetAclRequest.
        :type t_network_id: str
        """
        self._t_network_id = t_network_id

    @property
    def region_id(self):
        """Gets the region_id of this CheckNetAclRequest.

        区域ID

        :return: The region_id of this CheckNetAclRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CheckNetAclRequest.

        区域ID

        :param region_id: The region_id of this CheckNetAclRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def os_type(self):
        """Gets the os_type of this CheckNetAclRequest.

        操作系统类型

        :return: The os_type of this CheckNetAclRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this CheckNetAclRequest.

        操作系统类型

        :param os_type: The os_type of this CheckNetAclRequest.
        :type os_type: str
        """
        self._os_type = os_type

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
        if not isinstance(other, CheckNetAclRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
