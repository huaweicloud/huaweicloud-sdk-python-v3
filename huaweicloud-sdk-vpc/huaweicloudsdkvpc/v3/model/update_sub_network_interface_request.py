# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubNetworkInterfaceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_network_interface_id': 'str',
        'body': 'UpdateSubNetworkInterfaceRequestBody'
    }

    attribute_map = {
        'sub_network_interface_id': 'sub_network_interface_id',
        'body': 'body'
    }

    def __init__(self, sub_network_interface_id=None, body=None):
        r"""UpdateSubNetworkInterfaceRequest

        The model defined in huaweicloud sdk

        :param sub_network_interface_id: 辅助弹性网卡的唯一标识
        :type sub_network_interface_id: str
        :param body: Body of the UpdateSubNetworkInterfaceRequest
        :type body: :class:`huaweicloudsdkvpc.v3.UpdateSubNetworkInterfaceRequestBody`
        """
        
        

        self._sub_network_interface_id = None
        self._body = None
        self.discriminator = None

        self.sub_network_interface_id = sub_network_interface_id
        if body is not None:
            self.body = body

    @property
    def sub_network_interface_id(self):
        r"""Gets the sub_network_interface_id of this UpdateSubNetworkInterfaceRequest.

        辅助弹性网卡的唯一标识

        :return: The sub_network_interface_id of this UpdateSubNetworkInterfaceRequest.
        :rtype: str
        """
        return self._sub_network_interface_id

    @sub_network_interface_id.setter
    def sub_network_interface_id(self, sub_network_interface_id):
        r"""Sets the sub_network_interface_id of this UpdateSubNetworkInterfaceRequest.

        辅助弹性网卡的唯一标识

        :param sub_network_interface_id: The sub_network_interface_id of this UpdateSubNetworkInterfaceRequest.
        :type sub_network_interface_id: str
        """
        self._sub_network_interface_id = sub_network_interface_id

    @property
    def body(self):
        r"""Gets the body of this UpdateSubNetworkInterfaceRequest.

        :return: The body of this UpdateSubNetworkInterfaceRequest.
        :rtype: :class:`huaweicloudsdkvpc.v3.UpdateSubNetworkInterfaceRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateSubNetworkInterfaceRequest.

        :param body: The body of this UpdateSubNetworkInterfaceRequest.
        :type body: :class:`huaweicloudsdkvpc.v3.UpdateSubNetworkInterfaceRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateSubNetworkInterfaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
