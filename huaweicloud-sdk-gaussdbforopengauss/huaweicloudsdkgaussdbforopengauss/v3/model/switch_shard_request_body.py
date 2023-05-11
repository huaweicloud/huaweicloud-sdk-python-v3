# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchShardRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shards': 'list[Shards]'
    }

    attribute_map = {
        'shards': 'shards'
    }

    def __init__(self, shards=None):
        """SwitchShardRequestBody

        The model defined in huaweicloud sdk

        :param shards: 节点列表，支持对单个或者多个DN分片做主备切换。节点信息为将要升主的备DN分片对应的节点id和组件id。
        :type shards: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Shards`]
        """
        
        

        self._shards = None
        self.discriminator = None

        self.shards = shards

    @property
    def shards(self):
        """Gets the shards of this SwitchShardRequestBody.

        节点列表，支持对单个或者多个DN分片做主备切换。节点信息为将要升主的备DN分片对应的节点id和组件id。

        :return: The shards of this SwitchShardRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Shards`]
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        """Sets the shards of this SwitchShardRequestBody.

        节点列表，支持对单个或者多个DN分片做主备切换。节点信息为将要升主的备DN分片对应的节点id和组件id。

        :param shards: The shards of this SwitchShardRequestBody.
        :type shards: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.Shards`]
        """
        self._shards = shards

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
        if not isinstance(other, SwitchShardRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
