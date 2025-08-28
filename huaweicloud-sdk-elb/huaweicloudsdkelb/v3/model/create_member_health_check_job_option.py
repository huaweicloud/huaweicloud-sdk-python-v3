# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMemberHealthCheckJobOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'listener_id': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'listener_id': 'listener_id',
        'subject': 'subject'
    }

    def __init__(self, listener_id=None, subject=None):
        r"""CreateMemberHealthCheckJobOption

        The model defined in huaweicloud sdk

        :param listener_id: **参数解释**：后端服务器所关联的监听器，查询在该监听器下后端服务器的状态。  **取值范围**：不涉及
        :type listener_id: str
        :param subject: 参数法解释：检查项。  **取值范围**： - securityGroup：安全组检查。 - networkAcl：子网ACL配置检查。 - config：健康检查端口配置检查。 - all：所有检查项。
        :type subject: str
        """
        
        

        self._listener_id = None
        self._subject = None
        self.discriminator = None

        self.listener_id = listener_id
        self.subject = subject

    @property
    def listener_id(self):
        r"""Gets the listener_id of this CreateMemberHealthCheckJobOption.

        **参数解释**：后端服务器所关联的监听器，查询在该监听器下后端服务器的状态。  **取值范围**：不涉及

        :return: The listener_id of this CreateMemberHealthCheckJobOption.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this CreateMemberHealthCheckJobOption.

        **参数解释**：后端服务器所关联的监听器，查询在该监听器下后端服务器的状态。  **取值范围**：不涉及

        :param listener_id: The listener_id of this CreateMemberHealthCheckJobOption.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def subject(self):
        r"""Gets the subject of this CreateMemberHealthCheckJobOption.

        参数法解释：检查项。  **取值范围**： - securityGroup：安全组检查。 - networkAcl：子网ACL配置检查。 - config：健康检查端口配置检查。 - all：所有检查项。

        :return: The subject of this CreateMemberHealthCheckJobOption.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this CreateMemberHealthCheckJobOption.

        参数法解释：检查项。  **取值范围**： - securityGroup：安全组检查。 - networkAcl：子网ACL配置检查。 - config：健康检查端口配置检查。 - all：所有检查项。

        :param subject: The subject of this CreateMemberHealthCheckJobOption.
        :type subject: str
        """
        self._subject = subject

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
        if not isinstance(other, CreateMemberHealthCheckJobOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
