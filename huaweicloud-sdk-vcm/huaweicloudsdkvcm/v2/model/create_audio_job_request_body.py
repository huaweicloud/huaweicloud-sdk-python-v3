# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAudioJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'input': 'CreateAudioJobRequestBodyInput',
        'output': 'AudioOutput',
        'service_config': 'AudioServiceConfig',
        'service_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'input': 'input',
        'output': 'output',
        'service_config': 'service_config',
        'service_version': 'service_version'
    }

    def __init__(self, name=None, description=None, input=None, output=None, service_config=None, service_version=None):
        """CreateAudioJobRequestBody

        The model defined in huaweicloud sdk

        :param name: 作业名称，只能由字母（a～zA～Z）、数字（0～9）、中划线（-）、下划线（_）组成，长度范围为[1，100]。
        :type name: str
        :param description: 作业描述信息，最大长度为500字符长度。
        :type description: str
        :param input: 
        :type input: :class:`huaweicloudsdkvcm.v2.CreateAudioJobRequestBodyInput`
        :param output: 
        :type output: :class:`huaweicloudsdkvcm.v2.AudioOutput`
        :param service_config: 
        :type service_config: :class:`huaweicloudsdkvcm.v2.AudioServiceConfig`
        :param service_version: 功能版本为“1.0”。
        :type service_version: str
        """
        
        

        self._name = None
        self._description = None
        self._input = None
        self._output = None
        self._service_config = None
        self._service_version = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.input = input
        self.output = output
        if service_config is not None:
            self.service_config = service_config
        self.service_version = service_version

    @property
    def name(self):
        """Gets the name of this CreateAudioJobRequestBody.

        作业名称，只能由字母（a～zA～Z）、数字（0～9）、中划线（-）、下划线（_）组成，长度范围为[1，100]。

        :return: The name of this CreateAudioJobRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAudioJobRequestBody.

        作业名称，只能由字母（a～zA～Z）、数字（0～9）、中划线（-）、下划线（_）组成，长度范围为[1，100]。

        :param name: The name of this CreateAudioJobRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateAudioJobRequestBody.

        作业描述信息，最大长度为500字符长度。

        :return: The description of this CreateAudioJobRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAudioJobRequestBody.

        作业描述信息，最大长度为500字符长度。

        :param description: The description of this CreateAudioJobRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def input(self):
        """Gets the input of this CreateAudioJobRequestBody.

        :return: The input of this CreateAudioJobRequestBody.
        :rtype: :class:`huaweicloudsdkvcm.v2.CreateAudioJobRequestBodyInput`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this CreateAudioJobRequestBody.

        :param input: The input of this CreateAudioJobRequestBody.
        :type input: :class:`huaweicloudsdkvcm.v2.CreateAudioJobRequestBodyInput`
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this CreateAudioJobRequestBody.

        :return: The output of this CreateAudioJobRequestBody.
        :rtype: :class:`huaweicloudsdkvcm.v2.AudioOutput`
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this CreateAudioJobRequestBody.

        :param output: The output of this CreateAudioJobRequestBody.
        :type output: :class:`huaweicloudsdkvcm.v2.AudioOutput`
        """
        self._output = output

    @property
    def service_config(self):
        """Gets the service_config of this CreateAudioJobRequestBody.

        :return: The service_config of this CreateAudioJobRequestBody.
        :rtype: :class:`huaweicloudsdkvcm.v2.AudioServiceConfig`
        """
        return self._service_config

    @service_config.setter
    def service_config(self, service_config):
        """Sets the service_config of this CreateAudioJobRequestBody.

        :param service_config: The service_config of this CreateAudioJobRequestBody.
        :type service_config: :class:`huaweicloudsdkvcm.v2.AudioServiceConfig`
        """
        self._service_config = service_config

    @property
    def service_version(self):
        """Gets the service_version of this CreateAudioJobRequestBody.

        功能版本为“1.0”。

        :return: The service_version of this CreateAudioJobRequestBody.
        :rtype: str
        """
        return self._service_version

    @service_version.setter
    def service_version(self, service_version):
        """Sets the service_version of this CreateAudioJobRequestBody.

        功能版本为“1.0”。

        :param service_version: The service_version of this CreateAudioJobRequestBody.
        :type service_version: str
        """
        self._service_version = service_version

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
        if not isinstance(other, CreateAudioJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
