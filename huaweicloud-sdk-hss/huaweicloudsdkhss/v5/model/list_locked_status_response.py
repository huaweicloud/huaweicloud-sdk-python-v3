# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLockedStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'locked_status': 'bool'
    }

    attribute_map = {
        'locked_status': 'locked_status'
    }

    def __init__(self, locked_status=None):
        r"""ListLockedStatusResponse

        The model defined in huaweicloud sdk

        :param locked_status: **参数解释**: 主机安全防护配额资源的锁定状态。 **取值范围**: - true：已锁定，不可将按需计费的防护配额转为包年/包月。 - false：未锁定，可将按需计费的防护配额转为包年/包月。 
        :type locked_status: bool
        """
        
        super(ListLockedStatusResponse, self).__init__()

        self._locked_status = None
        self.discriminator = None

        if locked_status is not None:
            self.locked_status = locked_status

    @property
    def locked_status(self):
        r"""Gets the locked_status of this ListLockedStatusResponse.

        **参数解释**: 主机安全防护配额资源的锁定状态。 **取值范围**: - true：已锁定，不可将按需计费的防护配额转为包年/包月。 - false：未锁定，可将按需计费的防护配额转为包年/包月。 

        :return: The locked_status of this ListLockedStatusResponse.
        :rtype: bool
        """
        return self._locked_status

    @locked_status.setter
    def locked_status(self, locked_status):
        r"""Sets the locked_status of this ListLockedStatusResponse.

        **参数解释**: 主机安全防护配额资源的锁定状态。 **取值范围**: - true：已锁定，不可将按需计费的防护配额转为包年/包月。 - false：未锁定，可将按需计费的防护配额转为包年/包月。 

        :param locked_status: The locked_status of this ListLockedStatusResponse.
        :type locked_status: bool
        """
        self._locked_status = locked_status

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
        if not isinstance(other, ListLockedStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
