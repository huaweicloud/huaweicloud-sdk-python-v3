# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateListenerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_group_id': 'str',
        'body': 'DisassociateListenerRequestBody'
    }

    attribute_map = {
        'ip_group_id': 'ip_group_id',
        'body': 'body'
    }

    def __init__(self, ip_group_id=None, body=None):
        r"""DisassociateListenerRequest

        The model defined in huaweicloud sdk

        :param ip_group_id: IP地址组ID。
        :type ip_group_id: str
        :param body: Body of the DisassociateListenerRequest
        :type body: :class:`huaweicloudsdkga.v1.DisassociateListenerRequestBody`
        """
        
        

        self._ip_group_id = None
        self._body = None
        self.discriminator = None

        self.ip_group_id = ip_group_id
        if body is not None:
            self.body = body

    @property
    def ip_group_id(self):
        r"""Gets the ip_group_id of this DisassociateListenerRequest.

        IP地址组ID。

        :return: The ip_group_id of this DisassociateListenerRequest.
        :rtype: str
        """
        return self._ip_group_id

    @ip_group_id.setter
    def ip_group_id(self, ip_group_id):
        r"""Sets the ip_group_id of this DisassociateListenerRequest.

        IP地址组ID。

        :param ip_group_id: The ip_group_id of this DisassociateListenerRequest.
        :type ip_group_id: str
        """
        self._ip_group_id = ip_group_id

    @property
    def body(self):
        r"""Gets the body of this DisassociateListenerRequest.

        :return: The body of this DisassociateListenerRequest.
        :rtype: :class:`huaweicloudsdkga.v1.DisassociateListenerRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DisassociateListenerRequest.

        :param body: The body of this DisassociateListenerRequest.
        :type body: :class:`huaweicloudsdkga.v1.DisassociateListenerRequestBody`
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
        if not isinstance(other, DisassociateListenerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
