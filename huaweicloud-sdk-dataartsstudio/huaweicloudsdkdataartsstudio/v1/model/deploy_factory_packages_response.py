# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployFactoryPackagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deploy_package_details': 'list[DeployPackagesResponseDeployPackageDetails]'
    }

    attribute_map = {
        'deploy_package_details': 'deploy_package_details'
    }

    def __init__(self, deploy_package_details=None):
        """DeployFactoryPackagesResponse

        The model defined in huaweicloud sdk

        :param deploy_package_details: 发布包信息
        :type deploy_package_details: list[:class:`huaweicloudsdkdataartsstudio.v1.DeployPackagesResponseDeployPackageDetails`]
        """
        
        super(DeployFactoryPackagesResponse, self).__init__()

        self._deploy_package_details = None
        self.discriminator = None

        if deploy_package_details is not None:
            self.deploy_package_details = deploy_package_details

    @property
    def deploy_package_details(self):
        """Gets the deploy_package_details of this DeployFactoryPackagesResponse.

        发布包信息

        :return: The deploy_package_details of this DeployFactoryPackagesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DeployPackagesResponseDeployPackageDetails`]
        """
        return self._deploy_package_details

    @deploy_package_details.setter
    def deploy_package_details(self, deploy_package_details):
        """Sets the deploy_package_details of this DeployFactoryPackagesResponse.

        发布包信息

        :param deploy_package_details: The deploy_package_details of this DeployFactoryPackagesResponse.
        :type deploy_package_details: list[:class:`huaweicloudsdkdataartsstudio.v1.DeployPackagesResponseDeployPackageDetails`]
        """
        self._deploy_package_details = deploy_package_details

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
        if not isinstance(other, DeployFactoryPackagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
