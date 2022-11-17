# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Event:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata': 'Metadata',
        'starts_at': 'int'
    }

    attribute_map = {
        'metadata': 'metadata',
        'starts_at': 'starts_at'
    }

    def __init__(self, metadata=None, starts_at=None):
        """Event

        The model defined in huaweicloud sdk

        :param metadata: 
        :type metadata: :class:`huaweicloudsdklts.v2.Metadata`
        :param starts_at: 告警产生时间(时间戳)
        :type starts_at: int
        """
        
        

        self._metadata = None
        self._starts_at = None
        self.discriminator = None

        self.metadata = metadata
        self.starts_at = starts_at

    @property
    def metadata(self):
        """Gets the metadata of this Event.

        :return: The metadata of this Event.
        :rtype: :class:`huaweicloudsdklts.v2.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Event.

        :param metadata: The metadata of this Event.
        :type metadata: :class:`huaweicloudsdklts.v2.Metadata`
        """
        self._metadata = metadata

    @property
    def starts_at(self):
        """Gets the starts_at of this Event.

        告警产生时间(时间戳)

        :return: The starts_at of this Event.
        :rtype: int
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """Sets the starts_at of this Event.

        告警产生时间(时间戳)

        :param starts_at: The starts_at of this Event.
        :type starts_at: int
        """
        self._starts_at = starts_at

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
