# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberStatus:

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
        'operating_status': 'str'
    }

    attribute_map = {
        'listener_id': 'listener_id',
        'operating_status': 'operating_status'
    }

    def __init__(self, listener_id=None, operating_status=None):
        """MemberStatus

        The model defined in huaweicloud sdk

        :param listener_id: 监听器ID
        :type listener_id: str
        :param operating_status: 后端云服务器的健康状态。  取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。
        :type operating_status: str
        """
        
        

        self._listener_id = None
        self._operating_status = None
        self.discriminator = None

        self.listener_id = listener_id
        self.operating_status = operating_status

    @property
    def listener_id(self):
        """Gets the listener_id of this MemberStatus.

        监听器ID

        :return: The listener_id of this MemberStatus.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this MemberStatus.

        监听器ID

        :param listener_id: The listener_id of this MemberStatus.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def operating_status(self):
        """Gets the operating_status of this MemberStatus.

        后端云服务器的健康状态。  取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。

        :return: The operating_status of this MemberStatus.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this MemberStatus.

        后端云服务器的健康状态。  取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。

        :param operating_status: The operating_status of this MemberStatus.
        :type operating_status: str
        """
        self._operating_status = operating_status

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
        if not isinstance(other, MemberStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
