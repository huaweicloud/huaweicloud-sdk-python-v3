# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigMapsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configmaps': 'list[ConfigMapResp]',
        'count': 'int'
    }

    attribute_map = {
        'configmaps': 'configmaps',
        'count': 'count'
    }

    def __init__(self, configmaps=None, count=None):
        """ListConfigMapsResponse

        The model defined in huaweicloud sdk

        :param configmaps: 配置项
        :type configmaps: list[:class:`huaweicloudsdkief.v1.ConfigMapResp`]
        :param count: 满足条件的个数
        :type count: int
        """
        
        super(ListConfigMapsResponse, self).__init__()

        self._configmaps = None
        self._count = None
        self.discriminator = None

        if configmaps is not None:
            self.configmaps = configmaps
        if count is not None:
            self.count = count

    @property
    def configmaps(self):
        """Gets the configmaps of this ListConfigMapsResponse.

        配置项

        :return: The configmaps of this ListConfigMapsResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.ConfigMapResp`]
        """
        return self._configmaps

    @configmaps.setter
    def configmaps(self, configmaps):
        """Sets the configmaps of this ListConfigMapsResponse.

        配置项

        :param configmaps: The configmaps of this ListConfigMapsResponse.
        :type configmaps: list[:class:`huaweicloudsdkief.v1.ConfigMapResp`]
        """
        self._configmaps = configmaps

    @property
    def count(self):
        """Gets the count of this ListConfigMapsResponse.

        满足条件的个数

        :return: The count of this ListConfigMapsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListConfigMapsResponse.

        满足条件的个数

        :param count: The count of this ListConfigMapsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListConfigMapsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
