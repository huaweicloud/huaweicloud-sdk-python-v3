# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchPushCertificateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_projects': 'list[str]',
        'target_service': 'str'
    }

    attribute_map = {
        'target_projects': 'target_projects',
        'target_service': 'target_service'
    }

    def __init__(self, target_projects=None, target_service=None):
        """BatchPushCertificateRequestBody

        The model defined in huaweicloud sdk

        :param target_projects: 推送到的目标服务所在的区域，CDN支持区域固定为：Global。
        :type target_projects: list[str]
        :param target_service: 证书推送的目标服务，当前仅支持：CDN、WAF、ELB。
        :type target_service: str
        """
        
        

        self._target_projects = None
        self._target_service = None
        self.discriminator = None

        self.target_projects = target_projects
        self.target_service = target_service

    @property
    def target_projects(self):
        """Gets the target_projects of this BatchPushCertificateRequestBody.

        推送到的目标服务所在的区域，CDN支持区域固定为：Global。

        :return: The target_projects of this BatchPushCertificateRequestBody.
        :rtype: list[str]
        """
        return self._target_projects

    @target_projects.setter
    def target_projects(self, target_projects):
        """Sets the target_projects of this BatchPushCertificateRequestBody.

        推送到的目标服务所在的区域，CDN支持区域固定为：Global。

        :param target_projects: The target_projects of this BatchPushCertificateRequestBody.
        :type target_projects: list[str]
        """
        self._target_projects = target_projects

    @property
    def target_service(self):
        """Gets the target_service of this BatchPushCertificateRequestBody.

        证书推送的目标服务，当前仅支持：CDN、WAF、ELB。

        :return: The target_service of this BatchPushCertificateRequestBody.
        :rtype: str
        """
        return self._target_service

    @target_service.setter
    def target_service(self, target_service):
        """Sets the target_service of this BatchPushCertificateRequestBody.

        证书推送的目标服务，当前仅支持：CDN、WAF、ELB。

        :param target_service: The target_service of this BatchPushCertificateRequestBody.
        :type target_service: str
        """
        self._target_service = target_service

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
        if not isinstance(other, BatchPushCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
