# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioModerationResultRequestParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_type': 'str',
        'data': 'AudioModerationResultRequestParamsData',
        'param_callback': 'str',
        'categories': 'list[str]'
    }

    attribute_map = {
        'event_type': 'event_type',
        'data': 'data',
        'param_callback': 'callback',
        'categories': 'categories'
    }

    def __init__(self, event_type=None, data=None, param_callback=None, categories=None):
        """AudioModerationResultRequestParams

        The model defined in huaweicloud sdk

        :param event_type: 创建作业时传的event_type参数
        :type event_type: str
        :param data: 
        :type data: :class:`huaweicloudsdkmoderation.v3.AudioModerationResultRequestParamsData`
        :param param_callback: 创建作业时传的callback参数
        :type param_callback: str
        :param categories: 创建作业时传的categories参数
        :type categories: list[str]
        """
        
        

        self._event_type = None
        self._data = None
        self._param_callback = None
        self._categories = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if data is not None:
            self.data = data
        if param_callback is not None:
            self.param_callback = param_callback
        if categories is not None:
            self.categories = categories

    @property
    def event_type(self):
        """Gets the event_type of this AudioModerationResultRequestParams.

        创建作业时传的event_type参数

        :return: The event_type of this AudioModerationResultRequestParams.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this AudioModerationResultRequestParams.

        创建作业时传的event_type参数

        :param event_type: The event_type of this AudioModerationResultRequestParams.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def data(self):
        """Gets the data of this AudioModerationResultRequestParams.

        :return: The data of this AudioModerationResultRequestParams.
        :rtype: :class:`huaweicloudsdkmoderation.v3.AudioModerationResultRequestParamsData`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AudioModerationResultRequestParams.

        :param data: The data of this AudioModerationResultRequestParams.
        :type data: :class:`huaweicloudsdkmoderation.v3.AudioModerationResultRequestParamsData`
        """
        self._data = data

    @property
    def param_callback(self):
        """Gets the param_callback of this AudioModerationResultRequestParams.

        创建作业时传的callback参数

        :return: The param_callback of this AudioModerationResultRequestParams.
        :rtype: str
        """
        return self._param_callback

    @param_callback.setter
    def param_callback(self, param_callback):
        """Sets the param_callback of this AudioModerationResultRequestParams.

        创建作业时传的callback参数

        :param param_callback: The param_callback of this AudioModerationResultRequestParams.
        :type param_callback: str
        """
        self._param_callback = param_callback

    @property
    def categories(self):
        """Gets the categories of this AudioModerationResultRequestParams.

        创建作业时传的categories参数

        :return: The categories of this AudioModerationResultRequestParams.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this AudioModerationResultRequestParams.

        创建作业时传的categories参数

        :param categories: The categories of this AudioModerationResultRequestParams.
        :type categories: list[str]
        """
        self._categories = categories

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
        if not isinstance(other, AudioModerationResultRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
