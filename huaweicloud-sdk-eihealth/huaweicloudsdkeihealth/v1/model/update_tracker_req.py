# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTrackerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_event': 'list[DataEvent]'
    }

    attribute_map = {
        'data_event': 'data_event'
    }

    def __init__(self, data_event=None):
        r"""UpdateTrackerReq

        The model defined in huaweicloud sdk

        :param data_event: 审计数据类型列表
        :type data_event: list[:class:`huaweicloudsdkeihealth.v1.DataEvent`]
        """
        
        

        self._data_event = None
        self.discriminator = None

        self.data_event = data_event

    @property
    def data_event(self):
        r"""Gets the data_event of this UpdateTrackerReq.

        审计数据类型列表

        :return: The data_event of this UpdateTrackerReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DataEvent`]
        """
        return self._data_event

    @data_event.setter
    def data_event(self, data_event):
        r"""Sets the data_event of this UpdateTrackerReq.

        审计数据类型列表

        :param data_event: The data_event of this UpdateTrackerReq.
        :type data_event: list[:class:`huaweicloudsdkeihealth.v1.DataEvent`]
        """
        self._data_event = data_event

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
        if not isinstance(other, UpdateTrackerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
