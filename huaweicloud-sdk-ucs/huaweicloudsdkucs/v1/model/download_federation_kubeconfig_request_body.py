# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadFederationKubeconfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'duration': 'int'
    }

    attribute_map = {
        'duration': 'duration'
    }

    def __init__(self, duration=None):
        r"""DownloadFederationKubeconfigRequestBody

        The model defined in huaweicloud sdk

        :param duration: kubeconfig中证书的有效期
        :type duration: int
        """
        
        

        self._duration = None
        self.discriminator = None

        self.duration = duration

    @property
    def duration(self):
        r"""Gets the duration of this DownloadFederationKubeconfigRequestBody.

        kubeconfig中证书的有效期

        :return: The duration of this DownloadFederationKubeconfigRequestBody.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this DownloadFederationKubeconfigRequestBody.

        kubeconfig中证书的有效期

        :param duration: The duration of this DownloadFederationKubeconfigRequestBody.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, DownloadFederationKubeconfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
