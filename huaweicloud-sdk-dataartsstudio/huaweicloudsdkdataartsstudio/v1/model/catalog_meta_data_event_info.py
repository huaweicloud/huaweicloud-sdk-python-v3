# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogMetaDataEventInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_ts': 'int',
        'event_type': 'str',
        'event_message': 'object'
    }

    attribute_map = {
        'event_ts': 'event_ts',
        'event_type': 'event_type',
        'event_message': 'event_message'
    }

    def __init__(self, event_ts=None, event_type=None, event_message=None):
        """CatalogMetaDataEventInfo

        The model defined in huaweicloud sdk

        :param event_ts: 事件发生时的时间戳
        :type event_ts: int
        :param event_type: 事件类型
        :type event_type: str
        :param event_message: 事件消息，Map&lt;String,Object&gt;结构
        :type event_message: object
        """
        
        

        self._event_ts = None
        self._event_type = None
        self._event_message = None
        self.discriminator = None

        if event_ts is not None:
            self.event_ts = event_ts
        if event_type is not None:
            self.event_type = event_type
        if event_message is not None:
            self.event_message = event_message

    @property
    def event_ts(self):
        """Gets the event_ts of this CatalogMetaDataEventInfo.

        事件发生时的时间戳

        :return: The event_ts of this CatalogMetaDataEventInfo.
        :rtype: int
        """
        return self._event_ts

    @event_ts.setter
    def event_ts(self, event_ts):
        """Sets the event_ts of this CatalogMetaDataEventInfo.

        事件发生时的时间戳

        :param event_ts: The event_ts of this CatalogMetaDataEventInfo.
        :type event_ts: int
        """
        self._event_ts = event_ts

    @property
    def event_type(self):
        """Gets the event_type of this CatalogMetaDataEventInfo.

        事件类型

        :return: The event_type of this CatalogMetaDataEventInfo.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this CatalogMetaDataEventInfo.

        事件类型

        :param event_type: The event_type of this CatalogMetaDataEventInfo.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_message(self):
        """Gets the event_message of this CatalogMetaDataEventInfo.

        事件消息，Map<String,Object>结构

        :return: The event_message of this CatalogMetaDataEventInfo.
        :rtype: object
        """
        return self._event_message

    @event_message.setter
    def event_message(self, event_message):
        """Sets the event_message of this CatalogMetaDataEventInfo.

        事件消息，Map<String,Object>结构

        :param event_message: The event_message of this CatalogMetaDataEventInfo.
        :type event_message: object
        """
        self._event_message = event_message

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
        if not isinstance(other, CatalogMetaDataEventInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
