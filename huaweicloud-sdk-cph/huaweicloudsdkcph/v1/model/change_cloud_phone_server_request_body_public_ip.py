# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeCloudPhoneServerRequestBodyPublicIp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'eip': 'CreateNet2CloudPhoneServerRequestBodyPublicIpEip',
        'count': 'int'
    }

    attribute_map = {
        'ids': 'ids',
        'eip': 'eip',
        'count': 'count'
    }

    def __init__(self, ids=None, eip=None, count=None):
        r"""ChangeCloudPhoneServerRequestBodyPublicIp

        The model defined in huaweicloud sdk

        :param ids: 指定已有的EIP进行服务器创建，当前只支持传入一个已有的EIP ID。
        :type ids: list[str]
        :param eip: 
        :type eip: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyPublicIpEip`
        :param count: Eip数量。默认为1，不需要Eip可设置为0，取值范围为0到手机IP数。
        :type count: int
        """
        
        

        self._ids = None
        self._eip = None
        self._count = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if eip is not None:
            self.eip = eip
        if count is not None:
            self.count = count

    @property
    def ids(self):
        r"""Gets the ids of this ChangeCloudPhoneServerRequestBodyPublicIp.

        指定已有的EIP进行服务器创建，当前只支持传入一个已有的EIP ID。

        :return: The ids of this ChangeCloudPhoneServerRequestBodyPublicIp.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this ChangeCloudPhoneServerRequestBodyPublicIp.

        指定已有的EIP进行服务器创建，当前只支持传入一个已有的EIP ID。

        :param ids: The ids of this ChangeCloudPhoneServerRequestBodyPublicIp.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def eip(self):
        r"""Gets the eip of this ChangeCloudPhoneServerRequestBodyPublicIp.

        :return: The eip of this ChangeCloudPhoneServerRequestBodyPublicIp.
        :rtype: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyPublicIpEip`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this ChangeCloudPhoneServerRequestBodyPublicIp.

        :param eip: The eip of this ChangeCloudPhoneServerRequestBodyPublicIp.
        :type eip: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyPublicIpEip`
        """
        self._eip = eip

    @property
    def count(self):
        r"""Gets the count of this ChangeCloudPhoneServerRequestBodyPublicIp.

        Eip数量。默认为1，不需要Eip可设置为0，取值范围为0到手机IP数。

        :return: The count of this ChangeCloudPhoneServerRequestBodyPublicIp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ChangeCloudPhoneServerRequestBodyPublicIp.

        Eip数量。默认为1，不需要Eip可设置为0，取值范围为0到手机IP数。

        :param count: The count of this ChangeCloudPhoneServerRequestBodyPublicIp.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ChangeCloudPhoneServerRequestBodyPublicIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
