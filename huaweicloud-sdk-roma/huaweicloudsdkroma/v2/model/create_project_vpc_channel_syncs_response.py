# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProjectVpcChannelSyncsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_vpc_channels': 'list[ProjectVpcChannelInfo]'
    }

    attribute_map = {
        'project_vpc_channels': 'project_vpc_channels'
    }

    def __init__(self, project_vpc_channels=None):
        """CreateProjectVpcChannelSyncsResponse

        The model defined in huaweicloud sdk

        :param project_vpc_channels: 项目VPC通道列表
        :type project_vpc_channels: list[:class:`huaweicloudsdkroma.v2.ProjectVpcChannelInfo`]
        """
        
        super(CreateProjectVpcChannelSyncsResponse, self).__init__()

        self._project_vpc_channels = None
        self.discriminator = None

        if project_vpc_channels is not None:
            self.project_vpc_channels = project_vpc_channels

    @property
    def project_vpc_channels(self):
        """Gets the project_vpc_channels of this CreateProjectVpcChannelSyncsResponse.

        项目VPC通道列表

        :return: The project_vpc_channels of this CreateProjectVpcChannelSyncsResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.ProjectVpcChannelInfo`]
        """
        return self._project_vpc_channels

    @project_vpc_channels.setter
    def project_vpc_channels(self, project_vpc_channels):
        """Sets the project_vpc_channels of this CreateProjectVpcChannelSyncsResponse.

        项目VPC通道列表

        :param project_vpc_channels: The project_vpc_channels of this CreateProjectVpcChannelSyncsResponse.
        :type project_vpc_channels: list[:class:`huaweicloudsdkroma.v2.ProjectVpcChannelInfo`]
        """
        self._project_vpc_channels = project_vpc_channels

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
        if not isinstance(other, CreateProjectVpcChannelSyncsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
