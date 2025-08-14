# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_config': 'ProjectConfig'
    }

    attribute_map = {
        'project_config': 'project_config'
    }

    def __init__(self, project_config=None):
        r"""ShowProjectConfigResponse

        The model defined in huaweicloud sdk

        :param project_config: 
        :type project_config: :class:`huaweicloudsdkworkspaceapp.v1.ProjectConfig`
        """
        
        super(ShowProjectConfigResponse, self).__init__()

        self._project_config = None
        self.discriminator = None

        if project_config is not None:
            self.project_config = project_config

    @property
    def project_config(self):
        r"""Gets the project_config of this ShowProjectConfigResponse.

        :return: The project_config of this ShowProjectConfigResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ProjectConfig`
        """
        return self._project_config

    @project_config.setter
    def project_config(self, project_config):
        r"""Sets the project_config of this ShowProjectConfigResponse.

        :param project_config: The project_config of this ShowProjectConfigResponse.
        :type project_config: :class:`huaweicloudsdkworkspaceapp.v1.ProjectConfig`
        """
        self._project_config = project_config

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
        if not isinstance(other, ShowProjectConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
