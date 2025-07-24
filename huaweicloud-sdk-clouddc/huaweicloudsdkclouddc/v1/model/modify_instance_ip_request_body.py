# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyInstanceIpRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'nics': 'list[ModifyInstanceIpRequestBodyNics]'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'nics': 'nics'
    }

    def __init__(self, vpc_id=None, nics=None):
        r"""ModifyInstanceIpRequestBody

        The model defined in huaweicloud sdk

        :param vpc_id: 创建网卡所属的 VPC ID，可通过 VPC API 查询：https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html。
        :type vpc_id: str
        :param nics: 网卡信息
        :type nics: list[:class:`huaweicloudsdkclouddc.v1.ModifyInstanceIpRequestBodyNics`]
        """
        
        

        self._vpc_id = None
        self._nics = None
        self.discriminator = None

        if vpc_id is not None:
            self.vpc_id = vpc_id
        if nics is not None:
            self.nics = nics

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ModifyInstanceIpRequestBody.

        创建网卡所属的 VPC ID，可通过 VPC API 查询：https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html。

        :return: The vpc_id of this ModifyInstanceIpRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ModifyInstanceIpRequestBody.

        创建网卡所属的 VPC ID，可通过 VPC API 查询：https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html。

        :param vpc_id: The vpc_id of this ModifyInstanceIpRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def nics(self):
        r"""Gets the nics of this ModifyInstanceIpRequestBody.

        网卡信息

        :return: The nics of this ModifyInstanceIpRequestBody.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.ModifyInstanceIpRequestBodyNics`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        r"""Sets the nics of this ModifyInstanceIpRequestBody.

        网卡信息

        :param nics: The nics of this ModifyInstanceIpRequestBody.
        :type nics: list[:class:`huaweicloudsdkclouddc.v1.ModifyInstanceIpRequestBodyNics`]
        """
        self._nics = nics

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
        if not isinstance(other, ModifyInstanceIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
