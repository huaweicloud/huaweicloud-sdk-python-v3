# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchChangeServerImageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'items': 'list[ServerJobInfo]'
    }

    attribute_map = {
        'items': 'items'
    }

    def __init__(self, items=None):
        r"""BatchChangeServerImageResponse

        The model defined in huaweicloud sdk

        :param items: 服务器任务信息。
        :type items: list[:class:`huaweicloudsdkworkspaceapp.v1.ServerJobInfo`]
        """
        
        super(BatchChangeServerImageResponse, self).__init__()

        self._items = None
        self.discriminator = None

        if items is not None:
            self.items = items

    @property
    def items(self):
        r"""Gets the items of this BatchChangeServerImageResponse.

        服务器任务信息。

        :return: The items of this BatchChangeServerImageResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.ServerJobInfo`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this BatchChangeServerImageResponse.

        服务器任务信息。

        :param items: The items of this BatchChangeServerImageResponse.
        :type items: list[:class:`huaweicloudsdkworkspaceapp.v1.ServerJobInfo`]
        """
        self._items = items

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
        if not isinstance(other, BatchChangeServerImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
