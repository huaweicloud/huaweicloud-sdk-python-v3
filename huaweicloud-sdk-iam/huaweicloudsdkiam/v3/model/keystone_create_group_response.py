# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneCreateGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group': 'KeystoneGroupResultWithLinksSelf'
    }

    attribute_map = {
        'group': 'group'
    }

    def __init__(self, group=None):
        """KeystoneCreateGroupResponse

        The model defined in huaweicloud sdk

        :param group: 
        :type group: :class:`huaweicloudsdkiam.v3.KeystoneGroupResultWithLinksSelf`
        """
        
        super(KeystoneCreateGroupResponse, self).__init__()

        self._group = None
        self.discriminator = None

        if group is not None:
            self.group = group

    @property
    def group(self):
        """Gets the group of this KeystoneCreateGroupResponse.

        :return: The group of this KeystoneCreateGroupResponse.
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneGroupResultWithLinksSelf`
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this KeystoneCreateGroupResponse.

        :param group: The group of this KeystoneCreateGroupResponse.
        :type group: :class:`huaweicloudsdkiam.v3.KeystoneGroupResultWithLinksSelf`
        """
        self._group = group

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
        if not isinstance(other, KeystoneCreateGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
