# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'timeline_start': 'str',
        'timeline_end': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'timeline_start': 'timeline_start',
        'timeline_end': 'timeline_end'
    }

    def __init__(self, asset_id=None, timeline_start=None, timeline_end=None):
        r"""EditInput

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID 
        :type asset_id: str
        :param timeline_start: 剪切开始时间，单位：秒，最大长度支持32。 
        :type timeline_start: str
        :param timeline_end: 剪切结束时间，单位：秒，最大长度支持32。 
        :type timeline_end: str
        """
        
        

        self._asset_id = None
        self._timeline_start = None
        self._timeline_end = None
        self.discriminator = None

        self.asset_id = asset_id
        self.timeline_start = timeline_start
        self.timeline_end = timeline_end

    @property
    def asset_id(self):
        r"""Gets the asset_id of this EditInput.

        媒资ID 

        :return: The asset_id of this EditInput.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this EditInput.

        媒资ID 

        :param asset_id: The asset_id of this EditInput.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def timeline_start(self):
        r"""Gets the timeline_start of this EditInput.

        剪切开始时间，单位：秒，最大长度支持32。 

        :return: The timeline_start of this EditInput.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        r"""Sets the timeline_start of this EditInput.

        剪切开始时间，单位：秒，最大长度支持32。 

        :param timeline_start: The timeline_start of this EditInput.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_end(self):
        r"""Gets the timeline_end of this EditInput.

        剪切结束时间，单位：秒，最大长度支持32。 

        :return: The timeline_end of this EditInput.
        :rtype: str
        """
        return self._timeline_end

    @timeline_end.setter
    def timeline_end(self, timeline_end):
        r"""Sets the timeline_end of this EditInput.

        剪切结束时间，单位：秒，最大长度支持32。 

        :param timeline_end: The timeline_end of this EditInput.
        :type timeline_end: str
        """
        self._timeline_end = timeline_end

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EditInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
