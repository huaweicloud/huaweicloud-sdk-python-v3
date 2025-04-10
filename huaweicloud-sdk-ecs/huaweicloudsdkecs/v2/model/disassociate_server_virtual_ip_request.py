# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateServerVirtualIpRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nic_id': 'str',
        'body': 'DisassociateServerVirtualIpRequestBody'
    }

    attribute_map = {
        'nic_id': 'nic_id',
        'body': 'body'
    }

    def __init__(self, nic_id=None, body=None):
        r"""DisassociateServerVirtualIpRequest

        The model defined in huaweicloud sdk

        :param nic_id: 云服务器网卡ID。
        :type nic_id: str
        :param body: Body of the DisassociateServerVirtualIpRequest
        :type body: :class:`huaweicloudsdkecs.v2.DisassociateServerVirtualIpRequestBody`
        """
        
        

        self._nic_id = None
        self._body = None
        self.discriminator = None

        self.nic_id = nic_id
        if body is not None:
            self.body = body

    @property
    def nic_id(self):
        r"""Gets the nic_id of this DisassociateServerVirtualIpRequest.

        云服务器网卡ID。

        :return: The nic_id of this DisassociateServerVirtualIpRequest.
        :rtype: str
        """
        return self._nic_id

    @nic_id.setter
    def nic_id(self, nic_id):
        r"""Sets the nic_id of this DisassociateServerVirtualIpRequest.

        云服务器网卡ID。

        :param nic_id: The nic_id of this DisassociateServerVirtualIpRequest.
        :type nic_id: str
        """
        self._nic_id = nic_id

    @property
    def body(self):
        r"""Gets the body of this DisassociateServerVirtualIpRequest.

        :return: The body of this DisassociateServerVirtualIpRequest.
        :rtype: :class:`huaweicloudsdkecs.v2.DisassociateServerVirtualIpRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DisassociateServerVirtualIpRequest.

        :param body: The body of this DisassociateServerVirtualIpRequest.
        :type body: :class:`huaweicloudsdkecs.v2.DisassociateServerVirtualIpRequestBody`
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
        if not isinstance(other, DisassociateServerVirtualIpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
