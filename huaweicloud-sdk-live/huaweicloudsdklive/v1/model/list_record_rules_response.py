# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordRulesResponse(SdkResponse):

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
        'record_config': 'list[RecordRule]'
    }

    attribute_map = {
        'total': 'total',
        'record_config': 'record_config'
    }

    def __init__(self, total=None, record_config=None):
        """ListRecordRulesResponse

        The model defined in huaweicloud sdk

        :param total: 查询结果的总元素数量
        :type total: int
        :param record_config: 录制配置数组
        :type record_config: list[:class:`huaweicloudsdklive.v1.RecordRule`]
        """
        
        super(ListRecordRulesResponse, self).__init__()

        self._total = None
        self._record_config = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if record_config is not None:
            self.record_config = record_config

    @property
    def total(self):
        """Gets the total of this ListRecordRulesResponse.

        查询结果的总元素数量

        :return: The total of this ListRecordRulesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListRecordRulesResponse.

        查询结果的总元素数量

        :param total: The total of this ListRecordRulesResponse.
        :type total: int
        """
        self._total = total

    @property
    def record_config(self):
        """Gets the record_config of this ListRecordRulesResponse.

        录制配置数组

        :return: The record_config of this ListRecordRulesResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.RecordRule`]
        """
        return self._record_config

    @record_config.setter
    def record_config(self, record_config):
        """Sets the record_config of this ListRecordRulesResponse.

        录制配置数组

        :param record_config: The record_config of this ListRecordRulesResponse.
        :type record_config: list[:class:`huaweicloudsdklive.v1.RecordRule`]
        """
        self._record_config = record_config

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
        if not isinstance(other, ListRecordRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
