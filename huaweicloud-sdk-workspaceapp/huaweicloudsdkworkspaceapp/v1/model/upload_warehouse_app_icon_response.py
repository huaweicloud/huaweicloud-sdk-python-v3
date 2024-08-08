# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadWarehouseAppIconResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'appicon_store_path': 'str'
    }

    attribute_map = {
        'appicon_store_path': 'appicon_store_path'
    }

    def __init__(self, appicon_store_path=None):
        """UploadWarehouseAppIconResponse

        The model defined in huaweicloud sdk

        :param appicon_store_path: 图标文件在obs桶经过cdn加速以后的地址。
        :type appicon_store_path: str
        """
        
        super(UploadWarehouseAppIconResponse, self).__init__()

        self._appicon_store_path = None
        self.discriminator = None

        if appicon_store_path is not None:
            self.appicon_store_path = appicon_store_path

    @property
    def appicon_store_path(self):
        """Gets the appicon_store_path of this UploadWarehouseAppIconResponse.

        图标文件在obs桶经过cdn加速以后的地址。

        :return: The appicon_store_path of this UploadWarehouseAppIconResponse.
        :rtype: str
        """
        return self._appicon_store_path

    @appicon_store_path.setter
    def appicon_store_path(self, appicon_store_path):
        """Sets the appicon_store_path of this UploadWarehouseAppIconResponse.

        图标文件在obs桶经过cdn加速以后的地址。

        :param appicon_store_path: The appicon_store_path of this UploadWarehouseAppIconResponse.
        :type appicon_store_path: str
        """
        self._appicon_store_path = appicon_store_path

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
        if not isinstance(other, UploadWarehouseAppIconResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
