# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBusinessEnvResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_entry_list': 'list[EnvEntry]'
    }

    attribute_map = {
        'env_entry_list': 'env_entry_list'
    }

    def __init__(self, env_entry_list=None):
        """ListBusinessEnvResponse

        The model defined in huaweicloud sdk

        :param env_entry_list: 环境列表。
        :type env_entry_list: list[:class:`huaweicloudsdkapm.v1.EnvEntry`]
        """
        
        super(ListBusinessEnvResponse, self).__init__()

        self._env_entry_list = None
        self.discriminator = None

        if env_entry_list is not None:
            self.env_entry_list = env_entry_list

    @property
    def env_entry_list(self):
        """Gets the env_entry_list of this ListBusinessEnvResponse.

        环境列表。

        :return: The env_entry_list of this ListBusinessEnvResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.EnvEntry`]
        """
        return self._env_entry_list

    @env_entry_list.setter
    def env_entry_list(self, env_entry_list):
        """Sets the env_entry_list of this ListBusinessEnvResponse.

        环境列表。

        :param env_entry_list: The env_entry_list of this ListBusinessEnvResponse.
        :type env_entry_list: list[:class:`huaweicloudsdkapm.v1.EnvEntry`]
        """
        self._env_entry_list = env_entry_list

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
        if not isinstance(other, ListBusinessEnvResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
