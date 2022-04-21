# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeploymentHostDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'host_id': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'host_id': 'host_id'
    }

    def __init__(self, group_id=None, host_id=None):
        """ShowDeploymentHostDetailRequest

        The model defined in huaweicloud sdk

        :param group_id: 主机组id
        :type group_id: str
        :param host_id: 主机id
        :type host_id: str
        """
        
        

        self._group_id = None
        self._host_id = None
        self.discriminator = None

        self.group_id = group_id
        self.host_id = host_id

    @property
    def group_id(self):
        """Gets the group_id of this ShowDeploymentHostDetailRequest.

        主机组id

        :return: The group_id of this ShowDeploymentHostDetailRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowDeploymentHostDetailRequest.

        主机组id

        :param group_id: The group_id of this ShowDeploymentHostDetailRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def host_id(self):
        """Gets the host_id of this ShowDeploymentHostDetailRequest.

        主机id

        :return: The host_id of this ShowDeploymentHostDetailRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ShowDeploymentHostDetailRequest.

        主机id

        :param host_id: The host_id of this ShowDeploymentHostDetailRequest.
        :type host_id: str
        """
        self._host_id = host_id

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
        if not isinstance(other, ShowDeploymentHostDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
