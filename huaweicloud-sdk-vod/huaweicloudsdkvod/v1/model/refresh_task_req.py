# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RefreshTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id_list': 'list[str]',
        'urls': 'list[str]'
    }

    attribute_map = {
        'asset_id_list': 'asset_id_list',
        'urls': 'urls'
    }

    def __init__(self, asset_id_list=None, urls=None):
        r"""RefreshTaskReq

        The model defined in huaweicloud sdk

        :param asset_id_list: 完成态、删除态、发布态的媒资ID列表，一次性最多刷新10个媒资ID。
        :type asset_id_list: list[str]
        :param urls: 完成态、删除态、发布态的播放URL列表，一次性最多刷新10个URL。 单个URL的长度不能超过10240。 
        :type urls: list[str]
        """
        
        

        self._asset_id_list = None
        self._urls = None
        self.discriminator = None

        if asset_id_list is not None:
            self.asset_id_list = asset_id_list
        if urls is not None:
            self.urls = urls

    @property
    def asset_id_list(self):
        r"""Gets the asset_id_list of this RefreshTaskReq.

        完成态、删除态、发布态的媒资ID列表，一次性最多刷新10个媒资ID。

        :return: The asset_id_list of this RefreshTaskReq.
        :rtype: list[str]
        """
        return self._asset_id_list

    @asset_id_list.setter
    def asset_id_list(self, asset_id_list):
        r"""Sets the asset_id_list of this RefreshTaskReq.

        完成态、删除态、发布态的媒资ID列表，一次性最多刷新10个媒资ID。

        :param asset_id_list: The asset_id_list of this RefreshTaskReq.
        :type asset_id_list: list[str]
        """
        self._asset_id_list = asset_id_list

    @property
    def urls(self):
        r"""Gets the urls of this RefreshTaskReq.

        完成态、删除态、发布态的播放URL列表，一次性最多刷新10个URL。 单个URL的长度不能超过10240。 

        :return: The urls of this RefreshTaskReq.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        r"""Sets the urls of this RefreshTaskReq.

        完成态、删除态、发布态的播放URL列表，一次性最多刷新10个URL。 单个URL的长度不能超过10240。 

        :param urls: The urls of this RefreshTaskReq.
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
        if not isinstance(other, RefreshTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
