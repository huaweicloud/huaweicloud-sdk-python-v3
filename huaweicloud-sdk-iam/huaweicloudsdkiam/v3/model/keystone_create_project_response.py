# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneCreateProjectResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project': 'AuthProjectResult'
    }

    attribute_map = {
        'project': 'project'
    }

    def __init__(self, project=None):
        r"""KeystoneCreateProjectResponse

        The model defined in huaweicloud sdk

        :param project: 
        :type project: :class:`huaweicloudsdkiam.v3.AuthProjectResult`
        """
        
        super().__init__()

        self._project = None
        self.discriminator = None

        if project is not None:
            self.project = project

    @property
    def project(self):
        r"""Gets the project of this KeystoneCreateProjectResponse.

        :return: The project of this KeystoneCreateProjectResponse.
        :rtype: :class:`huaweicloudsdkiam.v3.AuthProjectResult`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this KeystoneCreateProjectResponse.

        :param project: The project of this KeystoneCreateProjectResponse.
        :type project: :class:`huaweicloudsdkiam.v3.AuthProjectResult`
        """
        self._project = project

    def to_dict(self):
        import warnings
        warnings.warn("KeystoneCreateProjectResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, KeystoneCreateProjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
