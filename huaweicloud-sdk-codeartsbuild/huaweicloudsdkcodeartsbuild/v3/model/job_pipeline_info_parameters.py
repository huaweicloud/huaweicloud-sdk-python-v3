# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobPipelineInfoParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'language': 'str',
        'name': 'str',
        'params': 'list[JobPipelineInfoParamsItems]'
    }

    attribute_map = {
        'region': 'region',
        'language': 'language',
        'name': 'name',
        'params': 'params'
    }

    def __init__(self, region=None, language=None, name=None, params=None):
        r"""JobPipelineInfoParameters

        The model defined in huaweicloud sdk

        :param region: 地域
        :type region: str
        :param language: 语言
        :type language: str
        :param name: 名称
        :type name: str
        :param params: 参数值
        :type params: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobPipelineInfoParamsItems`]
        """
        
        

        self._region = None
        self._language = None
        self._name = None
        self._params = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if language is not None:
            self.language = language
        if name is not None:
            self.name = name
        if params is not None:
            self.params = params

    @property
    def region(self):
        r"""Gets the region of this JobPipelineInfoParameters.

        地域

        :return: The region of this JobPipelineInfoParameters.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this JobPipelineInfoParameters.

        地域

        :param region: The region of this JobPipelineInfoParameters.
        :type region: str
        """
        self._region = region

    @property
    def language(self):
        r"""Gets the language of this JobPipelineInfoParameters.

        语言

        :return: The language of this JobPipelineInfoParameters.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this JobPipelineInfoParameters.

        语言

        :param language: The language of this JobPipelineInfoParameters.
        :type language: str
        """
        self._language = language

    @property
    def name(self):
        r"""Gets the name of this JobPipelineInfoParameters.

        名称

        :return: The name of this JobPipelineInfoParameters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobPipelineInfoParameters.

        名称

        :param name: The name of this JobPipelineInfoParameters.
        :type name: str
        """
        self._name = name

    @property
    def params(self):
        r"""Gets the params of this JobPipelineInfoParameters.

        参数值

        :return: The params of this JobPipelineInfoParameters.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobPipelineInfoParamsItems`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this JobPipelineInfoParameters.

        参数值

        :param params: The params of this JobPipelineInfoParameters.
        :type params: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobPipelineInfoParamsItems`]
        """
        self._params = params

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
        if not isinstance(other, JobPipelineInfoParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
