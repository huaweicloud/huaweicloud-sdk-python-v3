# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAgencyWithRoleTypeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_type': 'str'
    }

    attribute_map = {
        'role_type': 'role_type'
    }

    def __init__(self, role_type=None):
        r"""CreateAgencyWithRoleTypeRequest

        The model defined in huaweicloud sdk

        :param role_type: 委托授权类型 * CBS:对话机器人服务(CBS)访客 * SIS:语音交互服务(SIS)调用
        :type role_type: str
        """
        
        

        self._role_type = None
        self.discriminator = None

        self.role_type = role_type

    @property
    def role_type(self):
        r"""Gets the role_type of this CreateAgencyWithRoleTypeRequest.

        委托授权类型 * CBS:对话机器人服务(CBS)访客 * SIS:语音交互服务(SIS)调用

        :return: The role_type of this CreateAgencyWithRoleTypeRequest.
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        r"""Sets the role_type of this CreateAgencyWithRoleTypeRequest.

        委托授权类型 * CBS:对话机器人服务(CBS)访客 * SIS:语音交互服务(SIS)调用

        :param role_type: The role_type of this CreateAgencyWithRoleTypeRequest.
        :type role_type: str
        """
        self._role_type = role_type

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
        if not isinstance(other, CreateAgencyWithRoleTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
