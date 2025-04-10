# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployCertificateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_name': 'str',
        'service_name': 'str',
        'resources': 'list[DeployedResource]'
    }

    attribute_map = {
        'project_name': 'project_name',
        'service_name': 'service_name',
        'resources': 'resources'
    }

    def __init__(self, project_name=None, service_name=None, resources=None):
        r"""DeployCertificateRequestBody

        The model defined in huaweicloud sdk

        :param project_name: 部署的资源所在的项目名称，若在主项目下，则该值为region id。
        :type project_name: str
        :param service_name: 证书推送的目标服务，当前仅支持：CDN、WAF、ELB。
        :type service_name: str
        :param resources: 所要部署的资源列表。
        :type resources: list[:class:`huaweicloudsdkscm.v3.DeployedResource`]
        """
        
        

        self._project_name = None
        self._service_name = None
        self._resources = None
        self.discriminator = None

        if project_name is not None:
            self.project_name = project_name
        self.service_name = service_name
        self.resources = resources

    @property
    def project_name(self):
        r"""Gets the project_name of this DeployCertificateRequestBody.

        部署的资源所在的项目名称，若在主项目下，则该值为region id。

        :return: The project_name of this DeployCertificateRequestBody.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this DeployCertificateRequestBody.

        部署的资源所在的项目名称，若在主项目下，则该值为region id。

        :param project_name: The project_name of this DeployCertificateRequestBody.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def service_name(self):
        r"""Gets the service_name of this DeployCertificateRequestBody.

        证书推送的目标服务，当前仅支持：CDN、WAF、ELB。

        :return: The service_name of this DeployCertificateRequestBody.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this DeployCertificateRequestBody.

        证书推送的目标服务，当前仅支持：CDN、WAF、ELB。

        :param service_name: The service_name of this DeployCertificateRequestBody.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def resources(self):
        r"""Gets the resources of this DeployCertificateRequestBody.

        所要部署的资源列表。

        :return: The resources of this DeployCertificateRequestBody.
        :rtype: list[:class:`huaweicloudsdkscm.v3.DeployedResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this DeployCertificateRequestBody.

        所要部署的资源列表。

        :param resources: The resources of this DeployCertificateRequestBody.
        :type resources: list[:class:`huaweicloudsdkscm.v3.DeployedResource`]
        """
        self._resources = resources

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
        if not isinstance(other, DeployCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
