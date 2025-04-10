# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHtapStorageTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_type': 'list[HtapStorageTypeStorageType]'
    }

    attribute_map = {
        'storage_type': 'storage_type'
    }

    def __init__(self, storage_type=None):
        r"""ListHtapStorageTypeResponse

        The model defined in huaweicloud sdk

        :param storage_type: 存储类型。
        :type storage_type: list[:class:`huaweicloudsdkgaussdb.v3.HtapStorageTypeStorageType`]
        """
        
        super(ListHtapStorageTypeResponse, self).__init__()

        self._storage_type = None
        self.discriminator = None

        if storage_type is not None:
            self.storage_type = storage_type

    @property
    def storage_type(self):
        r"""Gets the storage_type of this ListHtapStorageTypeResponse.

        存储类型。

        :return: The storage_type of this ListHtapStorageTypeResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.HtapStorageTypeStorageType`]
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this ListHtapStorageTypeResponse.

        存储类型。

        :param storage_type: The storage_type of this ListHtapStorageTypeResponse.
        :type storage_type: list[:class:`huaweicloudsdkgaussdb.v3.HtapStorageTypeStorageType`]
        """
        self._storage_type = storage_type

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
        if not isinstance(other, ListHtapStorageTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
