# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetVaultResourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_resource_ids': 'list[str]'
    }

    attribute_map = {
        'set_resource_ids': 'set_resource_ids'
    }

    def __init__(self, set_resource_ids=None):
        """SetVaultResourceResponse

        The model defined in huaweicloud sdk

        :param set_resource_ids: 本次设置的资源id列表。
        :type set_resource_ids: list[str]
        """
        
        super(SetVaultResourceResponse, self).__init__()

        self._set_resource_ids = None
        self.discriminator = None

        if set_resource_ids is not None:
            self.set_resource_ids = set_resource_ids

    @property
    def set_resource_ids(self):
        """Gets the set_resource_ids of this SetVaultResourceResponse.

        本次设置的资源id列表。

        :return: The set_resource_ids of this SetVaultResourceResponse.
        :rtype: list[str]
        """
        return self._set_resource_ids

    @set_resource_ids.setter
    def set_resource_ids(self, set_resource_ids):
        """Sets the set_resource_ids of this SetVaultResourceResponse.

        本次设置的资源id列表。

        :param set_resource_ids: The set_resource_ids of this SetVaultResourceResponse.
        :type set_resource_ids: list[str]
        """
        self._set_resource_ids = set_resource_ids

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
        if not isinstance(other, SetVaultResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
