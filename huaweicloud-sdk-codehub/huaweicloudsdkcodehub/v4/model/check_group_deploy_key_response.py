# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckGroupDeployKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exists': 'bool'
    }

    attribute_map = {
        'exists': 'exists'
    }

    def __init__(self, exists=None):
        r"""CheckGroupDeployKeyResponse

        The model defined in huaweicloud sdk

        :param exists: **参数解释：** 部署秘钥在上层代码组或项目是否配置。 **取值范围：** - true，上层代码组或项目已配置该密钥。 - false，上层代码组或项目未配置该密钥。
        :type exists: bool
        """
        
        super(CheckGroupDeployKeyResponse, self).__init__()

        self._exists = None
        self.discriminator = None

        if exists is not None:
            self.exists = exists

    @property
    def exists(self):
        r"""Gets the exists of this CheckGroupDeployKeyResponse.

        **参数解释：** 部署秘钥在上层代码组或项目是否配置。 **取值范围：** - true，上层代码组或项目已配置该密钥。 - false，上层代码组或项目未配置该密钥。

        :return: The exists of this CheckGroupDeployKeyResponse.
        :rtype: bool
        """
        return self._exists

    @exists.setter
    def exists(self, exists):
        r"""Sets the exists of this CheckGroupDeployKeyResponse.

        **参数解释：** 部署秘钥在上层代码组或项目是否配置。 **取值范围：** - true，上层代码组或项目已配置该密钥。 - false，上层代码组或项目未配置该密钥。

        :param exists: The exists of this CheckGroupDeployKeyResponse.
        :type exists: bool
        """
        self._exists = exists

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
        if not isinstance(other, CheckGroupDeployKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
