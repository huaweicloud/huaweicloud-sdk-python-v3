# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SSHReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_pair_names': 'list[str]'
    }

    attribute_map = {
        'key_pair_names': 'key_pair_names'
    }

    def __init__(self, key_pair_names=None):
        r"""SSHReq

        The model defined in huaweicloud sdk

        :param key_pair_names: SSH密钥对名称，可以在云服务器控制台（ECS）“密钥对”页面创建和查看。
        :type key_pair_names: list[str]
        """
        
        

        self._key_pair_names = None
        self.discriminator = None

        if key_pair_names is not None:
            self.key_pair_names = key_pair_names

    @property
    def key_pair_names(self):
        r"""Gets the key_pair_names of this SSHReq.

        SSH密钥对名称，可以在云服务器控制台（ECS）“密钥对”页面创建和查看。

        :return: The key_pair_names of this SSHReq.
        :rtype: list[str]
        """
        return self._key_pair_names

    @key_pair_names.setter
    def key_pair_names(self, key_pair_names):
        r"""Sets the key_pair_names of this SSHReq.

        SSH密钥对名称，可以在云服务器控制台（ECS）“密钥对”页面创建和查看。

        :param key_pair_names: The key_pair_names of this SSHReq.
        :type key_pair_names: list[str]
        """
        self._key_pair_names = key_pair_names

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
        if not isinstance(other, SSHReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
