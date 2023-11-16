# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NewExtensionExecution:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target': 'str',
        'type': 'str',
        'sha256': 'str'
    }

    attribute_map = {
        'target': 'target',
        'type': 'type',
        'sha256': 'sha256'
    }

    def __init__(self, target=None, type=None, sha256=None):
        """NewExtensionExecution

        The model defined in huaweicloud sdk

        :param target: 入口
        :type target: str
        :param type: 类型
        :type type: str
        :param sha256: sha256
        :type sha256: str
        """
        
        

        self._target = None
        self._type = None
        self._sha256 = None
        self.discriminator = None

        if target is not None:
            self.target = target
        if type is not None:
            self.type = type
        if sha256 is not None:
            self.sha256 = sha256

    @property
    def target(self):
        """Gets the target of this NewExtensionExecution.

        入口

        :return: The target of this NewExtensionExecution.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this NewExtensionExecution.

        入口

        :param target: The target of this NewExtensionExecution.
        :type target: str
        """
        self._target = target

    @property
    def type(self):
        """Gets the type of this NewExtensionExecution.

        类型

        :return: The type of this NewExtensionExecution.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NewExtensionExecution.

        类型

        :param type: The type of this NewExtensionExecution.
        :type type: str
        """
        self._type = type

    @property
    def sha256(self):
        """Gets the sha256 of this NewExtensionExecution.

        sha256

        :return: The sha256 of this NewExtensionExecution.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this NewExtensionExecution.

        sha256

        :param sha256: The sha256 of this NewExtensionExecution.
        :type sha256: str
        """
        self._sha256 = sha256

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
        if not isinstance(other, NewExtensionExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
