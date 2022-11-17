# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiscoverEventSchemaFromDataReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'format': 'str',
        'event': 'str'
    }

    attribute_map = {
        'format': 'format',
        'event': 'event'
    }

    def __init__(self, format=None, event=None):
        """DiscoverEventSchemaFromDataReq

        The model defined in huaweicloud sdk

        :param format: 事件模型格式类型
        :type format: str
        :param event: 事件数据内容
        :type event: str
        """
        
        

        self._format = None
        self._event = None
        self.discriminator = None

        if format is not None:
            self.format = format
        self.event = event

    @property
    def format(self):
        """Gets the format of this DiscoverEventSchemaFromDataReq.

        事件模型格式类型

        :return: The format of this DiscoverEventSchemaFromDataReq.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this DiscoverEventSchemaFromDataReq.

        事件模型格式类型

        :param format: The format of this DiscoverEventSchemaFromDataReq.
        :type format: str
        """
        self._format = format

    @property
    def event(self):
        """Gets the event of this DiscoverEventSchemaFromDataReq.

        事件数据内容

        :return: The event of this DiscoverEventSchemaFromDataReq.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this DiscoverEventSchemaFromDataReq.

        事件数据内容

        :param event: The event of this DiscoverEventSchemaFromDataReq.
        :type event: str
        """
        self._event = event

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
        if not isinstance(other, DiscoverEventSchemaFromDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
