# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecretRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'projectname': 'str',
        'duration_seconds': 'int'
    }

    attribute_map = {
        'projectname': 'projectname',
        'duration_seconds': 'duration_seconds'
    }

    def __init__(self, projectname=None, duration_seconds=None):
        r"""CreateSecretRequest

        The model defined in huaweicloud sdk

        :param projectname: 项目名称，缺省值默认为区域名称，例如：cn-north-1。 
        :type projectname: str
        :param duration_seconds: 自定义临时凭证有效期，单位秒，取值范围15min-24h
        :type duration_seconds: int
        """
        
        

        self._projectname = None
        self._duration_seconds = None
        self.discriminator = None

        if projectname is not None:
            self.projectname = projectname
        if duration_seconds is not None:
            self.duration_seconds = duration_seconds

    @property
    def projectname(self):
        r"""Gets the projectname of this CreateSecretRequest.

        项目名称，缺省值默认为区域名称，例如：cn-north-1。 

        :return: The projectname of this CreateSecretRequest.
        :rtype: str
        """
        return self._projectname

    @projectname.setter
    def projectname(self, projectname):
        r"""Sets the projectname of this CreateSecretRequest.

        项目名称，缺省值默认为区域名称，例如：cn-north-1。 

        :param projectname: The projectname of this CreateSecretRequest.
        :type projectname: str
        """
        self._projectname = projectname

    @property
    def duration_seconds(self):
        r"""Gets the duration_seconds of this CreateSecretRequest.

        自定义临时凭证有效期，单位秒，取值范围15min-24h

        :return: The duration_seconds of this CreateSecretRequest.
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        r"""Sets the duration_seconds of this CreateSecretRequest.

        自定义临时凭证有效期，单位秒，取值范围15min-24h

        :param duration_seconds: The duration_seconds of this CreateSecretRequest.
        :type duration_seconds: int
        """
        self._duration_seconds = duration_seconds

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
        if not isinstance(other, CreateSecretRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
