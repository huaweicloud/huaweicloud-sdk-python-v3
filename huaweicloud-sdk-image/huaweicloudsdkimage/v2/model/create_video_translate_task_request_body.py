# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVideoTranslateTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input': 'VideoTranslateTaskInput',
        'output': 'TaskOutput',
        'param_callback': 'TaskCallback',
        'config': 'VideoTranslateConfig'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output',
        'param_callback': 'callback',
        'config': 'config'
    }

    def __init__(self, input=None, output=None, param_callback=None, config=None):
        """CreateVideoTranslateTaskRequestBody

        The model defined in huaweicloud sdk

        :param input: 
        :type input: :class:`huaweicloudsdkimage.v2.VideoTranslateTaskInput`
        :param output: 
        :type output: :class:`huaweicloudsdkimage.v2.TaskOutput`
        :param param_callback: 
        :type param_callback: :class:`huaweicloudsdkimage.v2.TaskCallback`
        :param config: 
        :type config: :class:`huaweicloudsdkimage.v2.VideoTranslateConfig`
        """
        
        

        self._input = None
        self._output = None
        self._param_callback = None
        self._config = None
        self.discriminator = None

        self.input = input
        self.output = output
        if param_callback is not None:
            self.param_callback = param_callback
        if config is not None:
            self.config = config

    @property
    def input(self):
        """Gets the input of this CreateVideoTranslateTaskRequestBody.

        :return: The input of this CreateVideoTranslateTaskRequestBody.
        :rtype: :class:`huaweicloudsdkimage.v2.VideoTranslateTaskInput`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateVideoTranslateTaskRequestBody.

        :param input: The input of this CreateVideoTranslateTaskRequestBody.
        :type input: :class:`huaweicloudsdkimage.v2.VideoTranslateTaskInput`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CreateVideoTranslateTaskRequestBody.

        :return: The output of this CreateVideoTranslateTaskRequestBody.
        :rtype: :class:`huaweicloudsdkimage.v2.TaskOutput`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateVideoTranslateTaskRequestBody.

        :param output: The output of this CreateVideoTranslateTaskRequestBody.
        :type output: :class:`huaweicloudsdkimage.v2.TaskOutput`
        """
        self._output = output

    @property
    def param_callback(self):
        """Gets the param_callback of this CreateVideoTranslateTaskRequestBody.

        :return: The param_callback of this CreateVideoTranslateTaskRequestBody.
        :rtype: :class:`huaweicloudsdkimage.v2.TaskCallback`
        """
        return self._param_callback

    @param_callback.setter
    def param_callback(self, param_callback):
        """Sets the param_callback of this CreateVideoTranslateTaskRequestBody.

        :param param_callback: The param_callback of this CreateVideoTranslateTaskRequestBody.
        :type param_callback: :class:`huaweicloudsdkimage.v2.TaskCallback`
        """
        self._param_callback = param_callback

    @property
    def config(self):
        """Gets the config of this CreateVideoTranslateTaskRequestBody.

        :return: The config of this CreateVideoTranslateTaskRequestBody.
        :rtype: :class:`huaweicloudsdkimage.v2.VideoTranslateConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this CreateVideoTranslateTaskRequestBody.

        :param config: The config of this CreateVideoTranslateTaskRequestBody.
        :type config: :class:`huaweicloudsdkimage.v2.VideoTranslateConfig`
        """
        self._config = config

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
        if not isinstance(other, CreateVideoTranslateTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other