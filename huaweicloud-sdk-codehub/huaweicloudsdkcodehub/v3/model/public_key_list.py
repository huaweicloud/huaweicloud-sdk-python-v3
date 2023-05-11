# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicKeyList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sshkey': 'list[PublicKey]',
        'total': 'int'
    }

    attribute_map = {
        'sshkey': 'sshkey',
        'total': 'total'
    }

    def __init__(self, sshkey=None, total=None):
        """PublicKeyList

        The model defined in huaweicloud sdk

        :param sshkey: 密钥列表
        :type sshkey: list[:class:`huaweicloudsdkcodehub.v3.PublicKey`]
        :param total: 密钥总数
        :type total: int
        """
        
        

        self._sshkey = None
        self._total = None
        self.discriminator = None

        if sshkey is not None:
            self.sshkey = sshkey
        if total is not None:
            self.total = total

    @property
    def sshkey(self):
        """Gets the sshkey of this PublicKeyList.

        密钥列表

        :return: The sshkey of this PublicKeyList.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.PublicKey`]
        """
        return self._sshkey

    @sshkey.setter
    def sshkey(self, sshkey):
        """Sets the sshkey of this PublicKeyList.

        密钥列表

        :param sshkey: The sshkey of this PublicKeyList.
        :type sshkey: list[:class:`huaweicloudsdkcodehub.v3.PublicKey`]
        """
        self._sshkey = sshkey

    @property
    def total(self):
        """Gets the total of this PublicKeyList.

        密钥总数

        :return: The total of this PublicKeyList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PublicKeyList.

        密钥总数

        :param total: The total of this PublicKeyList.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, PublicKeyList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
