# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachEipRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_ip_id': 'str',
        'public_ip': 'str'
    }

    attribute_map = {
        'public_ip_id': 'public_ip_id',
        'public_ip': 'public_ip'
    }

    def __init__(self, public_ip_id=None, public_ip=None):
        r"""AttachEipRequestBody

        The model defined in huaweicloud sdk

        :param public_ip_id: 公网IP的ID。
        :type public_ip_id: str
        :param public_ip: 公网IP。
        :type public_ip: str
        """
        
        

        self._public_ip_id = None
        self._public_ip = None
        self.discriminator = None

        self.public_ip_id = public_ip_id
        self.public_ip = public_ip

    @property
    def public_ip_id(self):
        r"""Gets the public_ip_id of this AttachEipRequestBody.

        公网IP的ID。

        :return: The public_ip_id of this AttachEipRequestBody.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        r"""Sets the public_ip_id of this AttachEipRequestBody.

        公网IP的ID。

        :param public_ip_id: The public_ip_id of this AttachEipRequestBody.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this AttachEipRequestBody.

        公网IP。

        :return: The public_ip of this AttachEipRequestBody.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this AttachEipRequestBody.

        公网IP。

        :param public_ip: The public_ip of this AttachEipRequestBody.
        :type public_ip: str
        """
        self._public_ip = public_ip

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
        if not isinstance(other, AttachEipRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
