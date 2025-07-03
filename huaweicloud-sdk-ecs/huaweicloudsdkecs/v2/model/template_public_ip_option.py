# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplatePublicIpOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_type': 'str',
        'charging_mode': 'str',
        'bandwidth': 'TemplateBandwidthOption',
        'delete_on_termination': 'bool'
    }

    attribute_map = {
        'publicip_type': 'publicip_type',
        'charging_mode': 'charging_mode',
        'bandwidth': 'bandwidth',
        'delete_on_termination': 'delete_on_termination'
    }

    def __init__(self, publicip_type=None, charging_mode=None, bandwidth=None, delete_on_termination=None):
        r"""TemplatePublicIpOption

        The model defined in huaweicloud sdk

        :param publicip_type: 弹性公网IP类型
        :type publicip_type: str
        :param charging_mode: 弹性公网IP计费类型
        :type charging_mode: str
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkecs.v2.TemplateBandwidthOption`
        :param delete_on_termination: EIP是否随实例一同释放
        :type delete_on_termination: bool
        """
        
        

        self._publicip_type = None
        self._charging_mode = None
        self._bandwidth = None
        self._delete_on_termination = None
        self.discriminator = None

        if publicip_type is not None:
            self.publicip_type = publicip_type
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if delete_on_termination is not None:
            self.delete_on_termination = delete_on_termination

    @property
    def publicip_type(self):
        r"""Gets the publicip_type of this TemplatePublicIpOption.

        弹性公网IP类型

        :return: The publicip_type of this TemplatePublicIpOption.
        :rtype: str
        """
        return self._publicip_type

    @publicip_type.setter
    def publicip_type(self, publicip_type):
        r"""Sets the publicip_type of this TemplatePublicIpOption.

        弹性公网IP类型

        :param publicip_type: The publicip_type of this TemplatePublicIpOption.
        :type publicip_type: str
        """
        self._publicip_type = publicip_type

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this TemplatePublicIpOption.

        弹性公网IP计费类型

        :return: The charging_mode of this TemplatePublicIpOption.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this TemplatePublicIpOption.

        弹性公网IP计费类型

        :param charging_mode: The charging_mode of this TemplatePublicIpOption.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this TemplatePublicIpOption.

        :return: The bandwidth of this TemplatePublicIpOption.
        :rtype: :class:`huaweicloudsdkecs.v2.TemplateBandwidthOption`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this TemplatePublicIpOption.

        :param bandwidth: The bandwidth of this TemplatePublicIpOption.
        :type bandwidth: :class:`huaweicloudsdkecs.v2.TemplateBandwidthOption`
        """
        self._bandwidth = bandwidth

    @property
    def delete_on_termination(self):
        r"""Gets the delete_on_termination of this TemplatePublicIpOption.

        EIP是否随实例一同释放

        :return: The delete_on_termination of this TemplatePublicIpOption.
        :rtype: bool
        """
        return self._delete_on_termination

    @delete_on_termination.setter
    def delete_on_termination(self, delete_on_termination):
        r"""Sets the delete_on_termination of this TemplatePublicIpOption.

        EIP是否随实例一同释放

        :param delete_on_termination: The delete_on_termination of this TemplatePublicIpOption.
        :type delete_on_termination: bool
        """
        self._delete_on_termination = delete_on_termination

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
        if not isinstance(other, TemplatePublicIpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
