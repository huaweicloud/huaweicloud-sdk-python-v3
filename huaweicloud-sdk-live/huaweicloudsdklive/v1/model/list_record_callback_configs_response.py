# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordCallbackConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'callback_config': 'list[RecordCallbackConfig]'
    }

    attribute_map = {
        'total': 'total',
        'callback_config': 'callback_config'
    }

    def __init__(self, total=None, callback_config=None):
        """ListRecordCallbackConfigsResponse

        The model defined in huaweicloud sdk

        :param total: 查询结果的总元素数量
        :type total: int
        :param callback_config: 回调配置
        :type callback_config: list[:class:`huaweicloudsdklive.v1.RecordCallbackConfig`]
        """
        
        super(ListRecordCallbackConfigsResponse, self).__init__()

        self._total = None
        self._callback_config = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if callback_config is not None:
            self.callback_config = callback_config

    @property
    def total(self):
        """Gets the total of this ListRecordCallbackConfigsResponse.

        查询结果的总元素数量

        :return: The total of this ListRecordCallbackConfigsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListRecordCallbackConfigsResponse.

        查询结果的总元素数量

        :param total: The total of this ListRecordCallbackConfigsResponse.
        :type total: int
        """
        self._total = total

    @property
    def callback_config(self):
        """Gets the callback_config of this ListRecordCallbackConfigsResponse.

        回调配置

        :return: The callback_config of this ListRecordCallbackConfigsResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.RecordCallbackConfig`]
        """
        return self._callback_config

    @callback_config.setter
    def callback_config(self, callback_config):
        """Sets the callback_config of this ListRecordCallbackConfigsResponse.

        回调配置

        :param callback_config: The callback_config of this ListRecordCallbackConfigsResponse.
        :type callback_config: list[:class:`huaweicloudsdklive.v1.RecordCallbackConfig`]
        """
        self._callback_config = callback_config

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
        if not isinstance(other, ListRecordCallbackConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
