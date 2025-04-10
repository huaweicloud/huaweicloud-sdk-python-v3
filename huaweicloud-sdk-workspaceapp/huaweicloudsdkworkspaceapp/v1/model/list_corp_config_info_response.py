# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCorpConfigInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_infos': 'list[CorpConfigInfo]'
    }

    attribute_map = {
        'config_infos': 'config_infos'
    }

    def __init__(self, config_infos=None):
        r"""ListCorpConfigInfoResponse

        The model defined in huaweicloud sdk

        :param config_infos: 批量配置项列表。
        :type config_infos: list[:class:`huaweicloudsdkworkspaceapp.v1.CorpConfigInfo`]
        """
        
        super(ListCorpConfigInfoResponse, self).__init__()

        self._config_infos = None
        self.discriminator = None

        if config_infos is not None:
            self.config_infos = config_infos

    @property
    def config_infos(self):
        r"""Gets the config_infos of this ListCorpConfigInfoResponse.

        批量配置项列表。

        :return: The config_infos of this ListCorpConfigInfoResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.CorpConfigInfo`]
        """
        return self._config_infos

    @config_infos.setter
    def config_infos(self, config_infos):
        r"""Sets the config_infos of this ListCorpConfigInfoResponse.

        批量配置项列表。

        :param config_infos: The config_infos of this ListCorpConfigInfoResponse.
        :type config_infos: list[:class:`huaweicloudsdkworkspaceapp.v1.CorpConfigInfo`]
        """
        self._config_infos = config_infos

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
        if not isinstance(other, ListCorpConfigInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
