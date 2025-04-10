# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetDisasterRecoverySettingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'successed_instance_ids': 'list[str]'
    }

    attribute_map = {
        'successed_instance_ids': 'successed_instance_ids'
    }

    def __init__(self, successed_instance_ids=None):
        r"""SetDisasterRecoverySettingsResponse

        The model defined in huaweicloud sdk

        :param successed_instance_ids: 设置容灾切换故障节点比例成功的实例列表。
        :type successed_instance_ids: list[str]
        """
        
        super(SetDisasterRecoverySettingsResponse, self).__init__()

        self._successed_instance_ids = None
        self.discriminator = None

        if successed_instance_ids is not None:
            self.successed_instance_ids = successed_instance_ids

    @property
    def successed_instance_ids(self):
        r"""Gets the successed_instance_ids of this SetDisasterRecoverySettingsResponse.

        设置容灾切换故障节点比例成功的实例列表。

        :return: The successed_instance_ids of this SetDisasterRecoverySettingsResponse.
        :rtype: list[str]
        """
        return self._successed_instance_ids

    @successed_instance_ids.setter
    def successed_instance_ids(self, successed_instance_ids):
        r"""Sets the successed_instance_ids of this SetDisasterRecoverySettingsResponse.

        设置容灾切换故障节点比例成功的实例列表。

        :param successed_instance_ids: The successed_instance_ids of this SetDisasterRecoverySettingsResponse.
        :type successed_instance_ids: list[str]
        """
        self._successed_instance_ids = successed_instance_ids

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
        if not isinstance(other, SetDisasterRecoverySettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
