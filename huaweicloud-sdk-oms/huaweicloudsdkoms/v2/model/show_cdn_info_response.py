# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCdnInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_same_cloud_type': 'bool',
        'is_download_available': 'bool',
        'checked_keys': 'list[CheckedKey]'
    }

    attribute_map = {
        'is_same_cloud_type': 'is_same_cloud_type',
        'is_download_available': 'is_download_available',
        'checked_keys': 'checked_keys'
    }

    def __init__(self, is_same_cloud_type=None, is_download_available=None, checked_keys=None):
        """ShowCdnInfoResponse

        The model defined in huaweicloud sdk

        :param is_same_cloud_type: 是否相同云类型
        :type is_same_cloud_type: bool
        :param is_download_available: 是否下载可用
        :type is_download_available: bool
        :param checked_keys: 返回的已检查的对象数组
        :type checked_keys: list[:class:`huaweicloudsdkoms.v2.CheckedKey`]
        """
        
        super(ShowCdnInfoResponse, self).__init__()

        self._is_same_cloud_type = None
        self._is_download_available = None
        self._checked_keys = None
        self.discriminator = None

        if is_same_cloud_type is not None:
            self.is_same_cloud_type = is_same_cloud_type
        if is_download_available is not None:
            self.is_download_available = is_download_available
        if checked_keys is not None:
            self.checked_keys = checked_keys

    @property
    def is_same_cloud_type(self):
        """Gets the is_same_cloud_type of this ShowCdnInfoResponse.

        是否相同云类型

        :return: The is_same_cloud_type of this ShowCdnInfoResponse.
        :rtype: bool
        """
        return self._is_same_cloud_type

    @is_same_cloud_type.setter
    def is_same_cloud_type(self, is_same_cloud_type):
        """Sets the is_same_cloud_type of this ShowCdnInfoResponse.

        是否相同云类型

        :param is_same_cloud_type: The is_same_cloud_type of this ShowCdnInfoResponse.
        :type is_same_cloud_type: bool
        """
        self._is_same_cloud_type = is_same_cloud_type

    @property
    def is_download_available(self):
        """Gets the is_download_available of this ShowCdnInfoResponse.

        是否下载可用

        :return: The is_download_available of this ShowCdnInfoResponse.
        :rtype: bool
        """
        return self._is_download_available

    @is_download_available.setter
    def is_download_available(self, is_download_available):
        """Sets the is_download_available of this ShowCdnInfoResponse.

        是否下载可用

        :param is_download_available: The is_download_available of this ShowCdnInfoResponse.
        :type is_download_available: bool
        """
        self._is_download_available = is_download_available

    @property
    def checked_keys(self):
        """Gets the checked_keys of this ShowCdnInfoResponse.

        返回的已检查的对象数组

        :return: The checked_keys of this ShowCdnInfoResponse.
        :rtype: list[:class:`huaweicloudsdkoms.v2.CheckedKey`]
        """
        return self._checked_keys

    @checked_keys.setter
    def checked_keys(self, checked_keys):
        """Sets the checked_keys of this ShowCdnInfoResponse.

        返回的已检查的对象数组

        :param checked_keys: The checked_keys of this ShowCdnInfoResponse.
        :type checked_keys: list[:class:`huaweicloudsdkoms.v2.CheckedKey`]
        """
        self._checked_keys = checked_keys

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
        if not isinstance(other, ShowCdnInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
