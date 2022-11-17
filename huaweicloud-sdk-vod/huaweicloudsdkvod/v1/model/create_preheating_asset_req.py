# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePreheatingAssetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'urls': 'list[str]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'urls': 'urls'
    }

    def __init__(self, asset_id=None, urls=None):
        """CreatePreheatingAssetReq

        The model defined in huaweicloud sdk

        :param asset_id: 已发布媒资的ID。
        :type asset_id: str
        :param urls: 已发布媒资的播放URL列表，一次最多只能预热10个URL。
        :type urls: list[str]
        """
        
        

        self._asset_id = None
        self._urls = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if urls is not None:
            self.urls = urls

    @property
    def asset_id(self):
        """Gets the asset_id of this CreatePreheatingAssetReq.

        已发布媒资的ID。

        :return: The asset_id of this CreatePreheatingAssetReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this CreatePreheatingAssetReq.

        已发布媒资的ID。

        :param asset_id: The asset_id of this CreatePreheatingAssetReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def urls(self):
        """Gets the urls of this CreatePreheatingAssetReq.

        已发布媒资的播放URL列表，一次最多只能预热10个URL。

        :return: The urls of this CreatePreheatingAssetReq.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this CreatePreheatingAssetReq.

        已发布媒资的播放URL列表，一次最多只能预热10个URL。

        :param urls: The urls of this CreatePreheatingAssetReq.
        :type urls: list[str]
        """
        self._urls = urls

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
        if not isinstance(other, CreatePreheatingAssetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
