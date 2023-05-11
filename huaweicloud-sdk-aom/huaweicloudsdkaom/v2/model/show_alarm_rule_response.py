# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlarmRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'meta_data': 'MetaData',
        'thresholds': 'list[QueryAlarmResult]'
    }

    attribute_map = {
        'meta_data': 'meta_data',
        'thresholds': 'thresholds'
    }

    def __init__(self, meta_data=None, thresholds=None):
        """ShowAlarmRuleResponse

        The model defined in huaweicloud sdk

        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkaom.v2.MetaData`
        :param thresholds: 阈值规则列表。
        :type thresholds: list[:class:`huaweicloudsdkaom.v2.QueryAlarmResult`]
        """
        
        super(ShowAlarmRuleResponse, self).__init__()

        self._meta_data = None
        self._thresholds = None
        self.discriminator = None

        if meta_data is not None:
            self.meta_data = meta_data
        if thresholds is not None:
            self.thresholds = thresholds

    @property
    def meta_data(self):
        """Gets the meta_data of this ShowAlarmRuleResponse.

        :return: The meta_data of this ShowAlarmRuleResponse.
        :rtype: :class:`huaweicloudsdkaom.v2.MetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ShowAlarmRuleResponse.

        :param meta_data: The meta_data of this ShowAlarmRuleResponse.
        :type meta_data: :class:`huaweicloudsdkaom.v2.MetaData`
        """
        self._meta_data = meta_data

    @property
    def thresholds(self):
        """Gets the thresholds of this ShowAlarmRuleResponse.

        阈值规则列表。

        :return: The thresholds of this ShowAlarmRuleResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.QueryAlarmResult`]
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this ShowAlarmRuleResponse.

        阈值规则列表。

        :param thresholds: The thresholds of this ShowAlarmRuleResponse.
        :type thresholds: list[:class:`huaweicloudsdkaom.v2.QueryAlarmResult`]
        """
        self._thresholds = thresholds

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
        if not isinstance(other, ShowAlarmRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
