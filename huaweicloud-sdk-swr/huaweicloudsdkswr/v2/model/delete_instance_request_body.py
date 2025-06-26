# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_obs': 'bool',
        'delete_dns': 'bool'
    }

    attribute_map = {
        'delete_obs': 'delete_obs',
        'delete_dns': 'delete_dns'
    }

    def __init__(self, delete_obs=None, delete_dns=None):
        r"""DeleteInstanceRequestBody

        The model defined in huaweicloud sdk

        :param delete_obs: 是否删除obs桶
        :type delete_obs: bool
        :param delete_dns: 是否删除DNS域名信息
        :type delete_dns: bool
        """
        
        

        self._delete_obs = None
        self._delete_dns = None
        self.discriminator = None

        if delete_obs is not None:
            self.delete_obs = delete_obs
        if delete_dns is not None:
            self.delete_dns = delete_dns

    @property
    def delete_obs(self):
        r"""Gets the delete_obs of this DeleteInstanceRequestBody.

        是否删除obs桶

        :return: The delete_obs of this DeleteInstanceRequestBody.
        :rtype: bool
        """
        return self._delete_obs

    @delete_obs.setter
    def delete_obs(self, delete_obs):
        r"""Sets the delete_obs of this DeleteInstanceRequestBody.

        是否删除obs桶

        :param delete_obs: The delete_obs of this DeleteInstanceRequestBody.
        :type delete_obs: bool
        """
        self._delete_obs = delete_obs

    @property
    def delete_dns(self):
        r"""Gets the delete_dns of this DeleteInstanceRequestBody.

        是否删除DNS域名信息

        :return: The delete_dns of this DeleteInstanceRequestBody.
        :rtype: bool
        """
        return self._delete_dns

    @delete_dns.setter
    def delete_dns(self, delete_dns):
        r"""Sets the delete_dns of this DeleteInstanceRequestBody.

        是否删除DNS域名信息

        :param delete_dns: The delete_dns of this DeleteInstanceRequestBody.
        :type delete_dns: bool
        """
        self._delete_dns = delete_dns

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
        if not isinstance(other, DeleteInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
