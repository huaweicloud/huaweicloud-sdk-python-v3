# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachVipBandwidthRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vport_id': 'str',
        'body': 'AttachVipBandwidthRequestBody'
    }

    attribute_map = {
        'vport_id': 'vport_id',
        'body': 'body'
    }

    def __init__(self, vport_id=None, body=None):
        r"""AttachVipBandwidthRequest

        The model defined in huaweicloud sdk

        :param vport_id: IPv6虚拟IP或者IPv6私网IP ID。
        :type vport_id: str
        :param body: Body of the AttachVipBandwidthRequest
        :type body: :class:`huaweicloudsdkiec.v1.AttachVipBandwidthRequestBody`
        """
        
        

        self._vport_id = None
        self._body = None
        self.discriminator = None

        self.vport_id = vport_id
        if body is not None:
            self.body = body

    @property
    def vport_id(self):
        r"""Gets the vport_id of this AttachVipBandwidthRequest.

        IPv6虚拟IP或者IPv6私网IP ID。

        :return: The vport_id of this AttachVipBandwidthRequest.
        :rtype: str
        """
        return self._vport_id

    @vport_id.setter
    def vport_id(self, vport_id):
        r"""Sets the vport_id of this AttachVipBandwidthRequest.

        IPv6虚拟IP或者IPv6私网IP ID。

        :param vport_id: The vport_id of this AttachVipBandwidthRequest.
        :type vport_id: str
        """
        self._vport_id = vport_id

    @property
    def body(self):
        r"""Gets the body of this AttachVipBandwidthRequest.

        :return: The body of this AttachVipBandwidthRequest.
        :rtype: :class:`huaweicloudsdkiec.v1.AttachVipBandwidthRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AttachVipBandwidthRequest.

        :param body: The body of this AttachVipBandwidthRequest.
        :type body: :class:`huaweicloudsdkiec.v1.AttachVipBandwidthRequestBody`
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
        if not isinstance(other, AttachVipBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
