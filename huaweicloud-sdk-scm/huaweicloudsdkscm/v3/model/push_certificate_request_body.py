# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PushCertificateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_project': 'str',
        'target_service': 'str'
    }

    attribute_map = {
        'target_project': 'target_project',
        'target_service': 'target_service'
    }

    def __init__(self, target_project=None, target_service=None):
        r"""PushCertificateRequestBody

        The model defined in huaweicloud sdk

        :param target_project: 推送到的目标服务所在的区域。
        :type target_project: str
        :param target_service: 证书推送的目标服务，当前仅支持：CDN、WAF、ELB。
        :type target_service: str
        """
        
        

        self._target_project = None
        self._target_service = None
        self.discriminator = None

        self.target_project = target_project
        self.target_service = target_service

    @property
    def target_project(self):
        r"""Gets the target_project of this PushCertificateRequestBody.

        推送到的目标服务所在的区域。

        :return: The target_project of this PushCertificateRequestBody.
        :rtype: str
        """
        return self._target_project

    @target_project.setter
    def target_project(self, target_project):
        r"""Sets the target_project of this PushCertificateRequestBody.

        推送到的目标服务所在的区域。

        :param target_project: The target_project of this PushCertificateRequestBody.
        :type target_project: str
        """
        self._target_project = target_project

    @property
    def target_service(self):
        r"""Gets the target_service of this PushCertificateRequestBody.

        证书推送的目标服务，当前仅支持：CDN、WAF、ELB。

        :return: The target_service of this PushCertificateRequestBody.
        :rtype: str
        """
        return self._target_service

    @target_service.setter
    def target_service(self, target_service):
        r"""Sets the target_service of this PushCertificateRequestBody.

        证书推送的目标服务，当前仅支持：CDN、WAF、ELB。

        :param target_service: The target_service of this PushCertificateRequestBody.
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
        if not isinstance(other, PushCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
