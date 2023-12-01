# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaiureResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'str',
        'failure_info': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'failure_info': 'failure_info'
    }

    def __init__(self, resource=None, failure_info=None):
        """FaiureResource

        The model defined in huaweicloud sdk

        :param resource: 部署失败的资源信息,部署WAF与ELB时，此字段为资源ID，部署CDN时，本字段为加速域名。
        :type resource: str
        :param failure_info: 失败原因，一般为目标服务返回的错误码信息。
        :type failure_info: str
        """
        
        

        self._resource = None
        self._failure_info = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if failure_info is not None:
            self.failure_info = failure_info

    @property
    def resource(self):
        """Gets the resource of this FaiureResource.

        部署失败的资源信息,部署WAF与ELB时，此字段为资源ID，部署CDN时，本字段为加速域名。

        :return: The resource of this FaiureResource.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this FaiureResource.

        部署失败的资源信息,部署WAF与ELB时，此字段为资源ID，部署CDN时，本字段为加速域名。

        :param resource: The resource of this FaiureResource.
        :type resource: str
        """
        self._resource = resource

    @property
    def failure_info(self):
        """Gets the failure_info of this FaiureResource.

        失败原因，一般为目标服务返回的错误码信息。

        :return: The failure_info of this FaiureResource.
        :rtype: str
        """
        return self._failure_info

    @failure_info.setter
    def failure_info(self, failure_info):
        """Sets the failure_info of this FaiureResource.

        失败原因，一般为目标服务返回的错误码信息。

        :param failure_info: The failure_info of this FaiureResource.
        :type failure_info: str
        """
        self._failure_info = failure_info

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
        if not isinstance(other, FaiureResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
