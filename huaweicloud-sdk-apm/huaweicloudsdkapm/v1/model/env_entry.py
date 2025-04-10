# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvEntry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_id': 'int',
        'env_name': 'str'
    }

    attribute_map = {
        'env_id': 'env_id',
        'env_name': 'env_name'
    }

    def __init__(self, env_id=None, env_name=None):
        r"""EnvEntry

        The model defined in huaweicloud sdk

        :param env_id: 环境id。
        :type env_id: int
        :param env_name: 环境名称。
        :type env_name: str
        """
        
        

        self._env_id = None
        self._env_name = None
        self.discriminator = None

        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name

    @property
    def env_id(self):
        r"""Gets the env_id of this EnvEntry.

        环境id。

        :return: The env_id of this EnvEntry.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this EnvEntry.

        环境id。

        :param env_id: The env_id of this EnvEntry.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def env_name(self):
        r"""Gets the env_name of this EnvEntry.

        环境名称。

        :return: The env_name of this EnvEntry.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        r"""Sets the env_name of this EnvEntry.

        环境名称。

        :param env_name: The env_name of this EnvEntry.
        :type env_name: str
        """
        self._env_name = env_name

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
        if not isinstance(other, EnvEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
