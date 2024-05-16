# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHtapDataStoreResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastores': 'list[SrDataStoresDatastores]'
    }

    attribute_map = {
        'datastores': 'datastores'
    }

    def __init__(self, datastores=None):
        """ListHtapDataStoreResponse

        The model defined in huaweicloud sdk

        :param datastores: 数据库信息列表。
        :type datastores: list[:class:`huaweicloudsdkgaussdb.v3.SrDataStoresDatastores`]
        """
        
        super(ListHtapDataStoreResponse, self).__init__()

        self._datastores = None
        self.discriminator = None

        if datastores is not None:
            self.datastores = datastores

    @property
    def datastores(self):
        """Gets the datastores of this ListHtapDataStoreResponse.

        数据库信息列表。

        :return: The datastores of this ListHtapDataStoreResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.SrDataStoresDatastores`]
        """
        return self._datastores

    @datastores.setter
    def datastores(self, datastores):
        """Sets the datastores of this ListHtapDataStoreResponse.

        数据库信息列表。

        :param datastores: The datastores of this ListHtapDataStoreResponse.
        :type datastores: list[:class:`huaweicloudsdkgaussdb.v3.SrDataStoresDatastores`]
        """
        self._datastores = datastores

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
        if not isinstance(other, ListHtapDataStoreResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
