# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePublicIpRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_id': 'str',
        'enable_ssl': 'bool',
        'elb_id': 'str'
    }

    attribute_map = {
        'publicip_id': 'publicip_id',
        'enable_ssl': 'enable_ssl',
        'elb_id': 'elb_id'
    }

    def __init__(self, publicip_id=None, enable_ssl=None, elb_id=None):
        r"""UpdatePublicIpRequestBody

        The model defined in huaweicloud sdk

        :param publicip_id: 公网访问绑定的ELB的EIP的ID，当Redis版本为3.0时，该参数为必填参数。
        :type publicip_id: str
        :param enable_ssl: 是否开启SSL，仅在开启SSL时有值，当Redis版本为3.0时，该参数为必填参数。
        :type enable_ssl: bool
        :param elb_id: 公网访问绑定的ELB ID，当Redis版本为4.0，5.0，6.0和企业版时，该参数为必填参数。
        :type elb_id: str
        """
        
        

        self._publicip_id = None
        self._enable_ssl = None
        self._elb_id = None
        self.discriminator = None

        if publicip_id is not None:
            self.publicip_id = publicip_id
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if elb_id is not None:
            self.elb_id = elb_id

    @property
    def publicip_id(self):
        r"""Gets the publicip_id of this UpdatePublicIpRequestBody.

        公网访问绑定的ELB的EIP的ID，当Redis版本为3.0时，该参数为必填参数。

        :return: The publicip_id of this UpdatePublicIpRequestBody.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        r"""Sets the publicip_id of this UpdatePublicIpRequestBody.

        公网访问绑定的ELB的EIP的ID，当Redis版本为3.0时，该参数为必填参数。

        :param publicip_id: The publicip_id of this UpdatePublicIpRequestBody.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def enable_ssl(self):
        r"""Gets the enable_ssl of this UpdatePublicIpRequestBody.

        是否开启SSL，仅在开启SSL时有值，当Redis版本为3.0时，该参数为必填参数。

        :return: The enable_ssl of this UpdatePublicIpRequestBody.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        r"""Sets the enable_ssl of this UpdatePublicIpRequestBody.

        是否开启SSL，仅在开启SSL时有值，当Redis版本为3.0时，该参数为必填参数。

        :param enable_ssl: The enable_ssl of this UpdatePublicIpRequestBody.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def elb_id(self):
        r"""Gets the elb_id of this UpdatePublicIpRequestBody.

        公网访问绑定的ELB ID，当Redis版本为4.0，5.0，6.0和企业版时，该参数为必填参数。

        :return: The elb_id of this UpdatePublicIpRequestBody.
        :rtype: str
        """
        return self._elb_id

    @elb_id.setter
    def elb_id(self, elb_id):
        r"""Sets the elb_id of this UpdatePublicIpRequestBody.

        公网访问绑定的ELB ID，当Redis版本为4.0，5.0，6.0和企业版时，该参数为必填参数。

        :param elb_id: The elb_id of this UpdatePublicIpRequestBody.
        :type elb_id: str
        """
        self._elb_id = elb_id

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
        if not isinstance(other, UpdatePublicIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
