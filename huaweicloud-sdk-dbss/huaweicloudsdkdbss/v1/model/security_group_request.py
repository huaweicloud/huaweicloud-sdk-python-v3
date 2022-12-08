# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'securitygroup_ids': 'list[str]'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'securitygroup_ids': 'securitygroup_ids'
    }

    def __init__(self, resource_id=None, securitygroup_ids=None):
        """SecurityGroupRequest

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID
        :type resource_id: str
        :param securitygroup_ids: 安全组ID列表(目前只支持传一个ID)
        :type securitygroup_ids: list[str]
        """
        
        

        self._resource_id = None
        self._securitygroup_ids = None
        self.discriminator = None

        self.resource_id = resource_id
        self.securitygroup_ids = securitygroup_ids

    @property
    def resource_id(self):
        """Gets the resource_id of this SecurityGroupRequest.

        资源ID

        :return: The resource_id of this SecurityGroupRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this SecurityGroupRequest.

        资源ID

        :param resource_id: The resource_id of this SecurityGroupRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def securitygroup_ids(self):
        """Gets the securitygroup_ids of this SecurityGroupRequest.

        安全组ID列表(目前只支持传一个ID)

        :return: The securitygroup_ids of this SecurityGroupRequest.
        :rtype: list[str]
        """
        return self._securitygroup_ids

    @securitygroup_ids.setter
    def securitygroup_ids(self, securitygroup_ids):
        """Sets the securitygroup_ids of this SecurityGroupRequest.

        安全组ID列表(目前只支持传一个ID)

        :param securitygroup_ids: The securitygroup_ids of this SecurityGroupRequest.
        :type securitygroup_ids: list[str]
        """
        self._securitygroup_ids = securitygroup_ids

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
        if not isinstance(other, SecurityGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
