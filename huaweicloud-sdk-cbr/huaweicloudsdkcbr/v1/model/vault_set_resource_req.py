# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VaultSetResourceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_ids': 'list[str]',
        'action': 'str'
    }

    attribute_map = {
        'resource_ids': 'resource_ids',
        'action': 'action'
    }

    def __init__(self, resource_ids=None, action=None):
        r"""VaultSetResourceReq

        The model defined in huaweicloud sdk

        :param resource_ids: 需要设置的资源id。
        :type resource_ids: list[str]
        :param action: 设置存储库资源动作
        :type action: str
        """
        
        

        self._resource_ids = None
        self._action = None
        self.discriminator = None

        self.resource_ids = resource_ids
        self.action = action

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this VaultSetResourceReq.

        需要设置的资源id。

        :return: The resource_ids of this VaultSetResourceReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this VaultSetResourceReq.

        需要设置的资源id。

        :param resource_ids: The resource_ids of this VaultSetResourceReq.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def action(self):
        r"""Gets the action of this VaultSetResourceReq.

        设置存储库资源动作

        :return: The action of this VaultSetResourceReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this VaultSetResourceReq.

        设置存储库资源动作

        :param action: The action of this VaultSetResourceReq.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, VaultSetResourceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
