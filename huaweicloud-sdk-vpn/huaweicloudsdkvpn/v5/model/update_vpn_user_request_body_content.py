# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpnUserRequestBodyContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'user_group_id': 'str',
        'static_ip': 'str'
    }

    attribute_map = {
        'description': 'description',
        'user_group_id': 'user_group_id',
        'static_ip': 'static_ip'
    }

    def __init__(self, description=None, user_group_id=None, static_ip=None):
        r"""UpdateVpnUserRequestBodyContent

        The model defined in huaweicloud sdk

        :param description: 用户描述
        :type description: str
        :param user_group_id: 所属用户组ID
        :type user_group_id: str
        :param static_ip: 静态客户端IP地址，disable表示随机分配客户端IP
        :type static_ip: str
        """
        
        

        self._description = None
        self._user_group_id = None
        self._static_ip = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if user_group_id is not None:
            self.user_group_id = user_group_id
        if static_ip is not None:
            self.static_ip = static_ip

    @property
    def description(self):
        r"""Gets the description of this UpdateVpnUserRequestBodyContent.

        用户描述

        :return: The description of this UpdateVpnUserRequestBodyContent.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateVpnUserRequestBodyContent.

        用户描述

        :param description: The description of this UpdateVpnUserRequestBodyContent.
        :type description: str
        """
        self._description = description

    @property
    def user_group_id(self):
        r"""Gets the user_group_id of this UpdateVpnUserRequestBodyContent.

        所属用户组ID

        :return: The user_group_id of this UpdateVpnUserRequestBodyContent.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        r"""Sets the user_group_id of this UpdateVpnUserRequestBodyContent.

        所属用户组ID

        :param user_group_id: The user_group_id of this UpdateVpnUserRequestBodyContent.
        :type user_group_id: str
        """
        self._user_group_id = user_group_id

    @property
    def static_ip(self):
        r"""Gets the static_ip of this UpdateVpnUserRequestBodyContent.

        静态客户端IP地址，disable表示随机分配客户端IP

        :return: The static_ip of this UpdateVpnUserRequestBodyContent.
        :rtype: str
        """
        return self._static_ip

    @static_ip.setter
    def static_ip(self, static_ip):
        r"""Sets the static_ip of this UpdateVpnUserRequestBodyContent.

        静态客户端IP地址，disable表示随机分配客户端IP

        :param static_ip: The static_ip of this UpdateVpnUserRequestBodyContent.
        :type static_ip: str
        """
        self._static_ip = static_ip

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
        if not isinstance(other, UpdateVpnUserRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
