# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'connection_status': 'NetworkConnectionStatus'
    }

    attribute_map = {
        'phase': 'phase',
        'connection_status': 'connectionStatus'
    }

    def __init__(self, phase=None, connection_status=None):
        r"""NetworkStatus

        The model defined in huaweicloud sdk

        :param phase: **参数解释**：网络资源的当前状态。 **取值范围**：可选值如下： - Creating：网络创建中。 - Active：网络正常。 - Abnormal：网络异常。
        :type phase: str
        :param connection_status: 
        :type connection_status: :class:`huaweicloudsdkmodelarts.v1.NetworkConnectionStatus`
        """
        
        

        self._phase = None
        self._connection_status = None
        self.discriminator = None

        self.phase = phase
        if connection_status is not None:
            self.connection_status = connection_status

    @property
    def phase(self):
        r"""Gets the phase of this NetworkStatus.

        **参数解释**：网络资源的当前状态。 **取值范围**：可选值如下： - Creating：网络创建中。 - Active：网络正常。 - Abnormal：网络异常。

        :return: The phase of this NetworkStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this NetworkStatus.

        **参数解释**：网络资源的当前状态。 **取值范围**：可选值如下： - Creating：网络创建中。 - Active：网络正常。 - Abnormal：网络异常。

        :param phase: The phase of this NetworkStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def connection_status(self):
        r"""Gets the connection_status of this NetworkStatus.

        :return: The connection_status of this NetworkStatus.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NetworkConnectionStatus`
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        r"""Sets the connection_status of this NetworkStatus.

        :param connection_status: The connection_status of this NetworkStatus.
        :type connection_status: :class:`huaweicloudsdkmodelarts.v1.NetworkConnectionStatus`
        """
        self._connection_status = connection_status

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NetworkStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
