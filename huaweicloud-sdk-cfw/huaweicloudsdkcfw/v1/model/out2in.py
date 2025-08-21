# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Out2in:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dst_ip': 'list[ItemVO]',
        'dst_port': 'list[ItemVO]',
        'src_ip': 'list[ItemVO]'
    }

    attribute_map = {
        'dst_ip': 'dst_ip',
        'dst_port': 'dst_port',
        'src_ip': 'src_ip'
    }

    def __init__(self, dst_ip=None, dst_port=None, src_ip=None):
        r"""Out2in

        The model defined in huaweicloud sdk

        :param dst_ip: **参数解释**： TOP访问目的IP **取值范围**： 不涉及
        :type dst_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param dst_port: **参数解释**： TOP开放端口 **取值范围**： 不涉及
        :type dst_port: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param src_ip: **参数解释**： TOP访问源IP **取值范围**： 不涉及
        :type src_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        
        

        self._dst_ip = None
        self._dst_port = None
        self._src_ip = None
        self.discriminator = None

        if dst_ip is not None:
            self.dst_ip = dst_ip
        if dst_port is not None:
            self.dst_port = dst_port
        if src_ip is not None:
            self.src_ip = src_ip

    @property
    def dst_ip(self):
        r"""Gets the dst_ip of this Out2in.

        **参数解释**： TOP访问目的IP **取值范围**： 不涉及

        :return: The dst_ip of this Out2in.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        r"""Sets the dst_ip of this Out2in.

        **参数解释**： TOP访问目的IP **取值范围**： 不涉及

        :param dst_ip: The dst_ip of this Out2in.
        :type dst_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        r"""Gets the dst_port of this Out2in.

        **参数解释**： TOP开放端口 **取值范围**： 不涉及

        :return: The dst_port of this Out2in.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        r"""Sets the dst_port of this Out2in.

        **参数解释**： TOP开放端口 **取值范围**： 不涉及

        :param dst_port: The dst_port of this Out2in.
        :type dst_port: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._dst_port = dst_port

    @property
    def src_ip(self):
        r"""Gets the src_ip of this Out2in.

        **参数解释**： TOP访问源IP **取值范围**： 不涉及

        :return: The src_ip of this Out2in.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this Out2in.

        **参数解释**： TOP访问源IP **取值范围**： 不涉及

        :param src_ip: The src_ip of this Out2in.
        :type src_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._src_ip = src_ip

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
        if not isinstance(other, Out2in):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
