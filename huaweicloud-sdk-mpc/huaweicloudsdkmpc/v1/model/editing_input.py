# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditingInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input': 'ObsObjInfo',
        'timeline_start': 'str',
        'timeline_end': 'str'
    }

    attribute_map = {
        'input': 'input',
        'timeline_start': 'timeline_start',
        'timeline_end': 'timeline_end'
    }

    def __init__(self, input=None, timeline_start=None, timeline_end=None):
        """EditingInput

        The model defined in huaweicloud sdk

        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param timeline_start: 剪切开始时间，单位：秒。 
        :type timeline_start: str
        :param timeline_end: 剪切结束时间，单位：秒。 
        :type timeline_end: str
        """
        
        

        self._input = None
        self._timeline_start = None
        self._timeline_end = None
        self.discriminator = None

        self.input = input
        if timeline_start is not None:
            self.timeline_start = timeline_start
        if timeline_end is not None:
            self.timeline_end = timeline_end

    @property
    def input(self):
        """Gets the input of this EditingInput.

        :return: The input of this EditingInput.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this EditingInput.

        :param input: The input of this EditingInput.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def timeline_start(self):
        """Gets the timeline_start of this EditingInput.

        剪切开始时间，单位：秒。 

        :return: The timeline_start of this EditingInput.
        :rtype: str
        """
        return self._timeline_start

    @timeline_start.setter
    def timeline_start(self, timeline_start):
        """Sets the timeline_start of this EditingInput.

        剪切开始时间，单位：秒。 

        :param timeline_start: The timeline_start of this EditingInput.
        :type timeline_start: str
        """
        self._timeline_start = timeline_start

    @property
    def timeline_end(self):
        """Gets the timeline_end of this EditingInput.

        剪切结束时间，单位：秒。 

        :return: The timeline_end of this EditingInput.
        :rtype: str
        """
        return self._timeline_end

    @timeline_end.setter
    def timeline_end(self, timeline_end):
        """Sets the timeline_end of this EditingInput.

        剪切结束时间，单位：秒。 

        :param timeline_end: The timeline_end of this EditingInput.
        :type timeline_end: str
        """
        self._timeline_end = timeline_end

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
        if not isinstance(other, EditingInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
