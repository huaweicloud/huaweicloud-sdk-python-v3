# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApisUnbindedToAppV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'apis': 'list[AppAuthUnBindedApiResp]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'apis': 'apis'
    }

    def __init__(self, size=None, total=None, apis=None):
        """ListApisUnbindedToAppV2Response - a model defined in huaweicloud sdk"""
        
        super(ListApisUnbindedToAppV2Response, self).__init__()

        self._size = None
        self._total = None
        self._apis = None
        self.discriminator = None

        self.size = size
        self.total = total
        if apis is not None:
            self.apis = apis

    @property
    def size(self):
        """Gets the size of this ListApisUnbindedToAppV2Response.

        本次返回的列表长度

        :return: The size of this ListApisUnbindedToAppV2Response.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListApisUnbindedToAppV2Response.

        本次返回的列表长度

        :param size: The size of this ListApisUnbindedToAppV2Response.
        :type: int
        """
        self._size = size

    @property
    def total(self):
        """Gets the total of this ListApisUnbindedToAppV2Response.

        满足条件的记录数

        :return: The total of this ListApisUnbindedToAppV2Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListApisUnbindedToAppV2Response.

        满足条件的记录数

        :param total: The total of this ListApisUnbindedToAppV2Response.
        :type: int
        """
        self._total = total

    @property
    def apis(self):
        """Gets the apis of this ListApisUnbindedToAppV2Response.

        本次返回的API列表

        :return: The apis of this ListApisUnbindedToAppV2Response.
        :rtype: list[AppAuthUnBindedApiResp]
        """
        return self._apis

    @apis.setter
    def apis(self, apis):
        """Sets the apis of this ListApisUnbindedToAppV2Response.

        本次返回的API列表

        :param apis: The apis of this ListApisUnbindedToAppV2Response.
        :type: list[AppAuthUnBindedApiResp]
        """
        self._apis = apis

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListApisUnbindedToAppV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
