# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDcVncRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dc_vnc_ip': 'str',
        'center_subnet_id': 'str'
    }

    attribute_map = {
        'dc_vnc_ip': 'dc_vnc_ip',
        'center_subnet_id': 'center_subnet_id'
    }

    def __init__(self, dc_vnc_ip=None, center_subnet_id=None):
        r"""UpdateDcVncRequestBody

        The model defined in huaweicloud sdk

        :param dc_vnc_ip: - default: 自动开启 - close: 关闭
        :type dc_vnc_ip: str
        :param center_subnet_id: 中心可用区的子网id，当dc_vnc_ip为default，且站点属于边缘小站时必传
        :type center_subnet_id: str
        """
        
        

        self._dc_vnc_ip = None
        self._center_subnet_id = None
        self.discriminator = None

        self.dc_vnc_ip = dc_vnc_ip
        if center_subnet_id is not None:
            self.center_subnet_id = center_subnet_id

    @property
    def dc_vnc_ip(self):
        r"""Gets the dc_vnc_ip of this UpdateDcVncRequestBody.

        - default: 自动开启 - close: 关闭

        :return: The dc_vnc_ip of this UpdateDcVncRequestBody.
        :rtype: str
        """
        return self._dc_vnc_ip

    @dc_vnc_ip.setter
    def dc_vnc_ip(self, dc_vnc_ip):
        r"""Sets the dc_vnc_ip of this UpdateDcVncRequestBody.

        - default: 自动开启 - close: 关闭

        :param dc_vnc_ip: The dc_vnc_ip of this UpdateDcVncRequestBody.
        :type dc_vnc_ip: str
        """
        self._dc_vnc_ip = dc_vnc_ip

    @property
    def center_subnet_id(self):
        r"""Gets the center_subnet_id of this UpdateDcVncRequestBody.

        中心可用区的子网id，当dc_vnc_ip为default，且站点属于边缘小站时必传

        :return: The center_subnet_id of this UpdateDcVncRequestBody.
        :rtype: str
        """
        return self._center_subnet_id

    @center_subnet_id.setter
    def center_subnet_id(self, center_subnet_id):
        r"""Sets the center_subnet_id of this UpdateDcVncRequestBody.

        中心可用区的子网id，当dc_vnc_ip为default，且站点属于边缘小站时必传

        :param center_subnet_id: The center_subnet_id of this UpdateDcVncRequestBody.
        :type center_subnet_id: str
        """
        self._center_subnet_id = center_subnet_id

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
        if not isinstance(other, UpdateDcVncRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
