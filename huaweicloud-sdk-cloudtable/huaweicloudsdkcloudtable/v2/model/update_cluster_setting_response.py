# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClusterSettingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'modify_result': 'bool'
    }

    attribute_map = {
        'modify_result': 'modify_result'
    }

    def __init__(self, modify_result=None):
        r"""UpdateClusterSettingResponse

        The model defined in huaweicloud sdk

        :param modify_result: 配置修改结果
        :type modify_result: bool
        """
        
        super(UpdateClusterSettingResponse, self).__init__()

        self._modify_result = None
        self.discriminator = None

        if modify_result is not None:
            self.modify_result = modify_result

    @property
    def modify_result(self):
        r"""Gets the modify_result of this UpdateClusterSettingResponse.

        配置修改结果

        :return: The modify_result of this UpdateClusterSettingResponse.
        :rtype: bool
        """
        return self._modify_result

    @modify_result.setter
    def modify_result(self, modify_result):
        r"""Sets the modify_result of this UpdateClusterSettingResponse.

        配置修改结果

        :param modify_result: The modify_result of this UpdateClusterSettingResponse.
        :type modify_result: bool
        """
        self._modify_result = modify_result

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
        if not isinstance(other, UpdateClusterSettingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
