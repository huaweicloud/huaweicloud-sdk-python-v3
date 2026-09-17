# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowObsBucketAclResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_risk': 'str',
        'message': 'str',
        'obs_acl': 'str'
    }

    attribute_map = {
        'bucket_risk': 'bucket_risk',
        'message': 'message',
        'obs_acl': 'obs_acl'
    }

    def __init__(self, bucket_risk=None, message=None, obs_acl=None):
        r"""ShowObsBucketAclResponse

        The model defined in huaweicloud sdk

        :param bucket_risk: 桶风险
        :type bucket_risk: str
        :param message: 信息
        :type message: str
        :param obs_acl: 桶ACL
        :type obs_acl: str
        """
        
        super().__init__()

        self._bucket_risk = None
        self._message = None
        self._obs_acl = None
        self.discriminator = None

        if bucket_risk is not None:
            self.bucket_risk = bucket_risk
        if message is not None:
            self.message = message
        if obs_acl is not None:
            self.obs_acl = obs_acl

    @property
    def bucket_risk(self):
        r"""Gets the bucket_risk of this ShowObsBucketAclResponse.

        桶风险

        :return: The bucket_risk of this ShowObsBucketAclResponse.
        :rtype: str
        """
        return self._bucket_risk

    @bucket_risk.setter
    def bucket_risk(self, bucket_risk):
        r"""Sets the bucket_risk of this ShowObsBucketAclResponse.

        桶风险

        :param bucket_risk: The bucket_risk of this ShowObsBucketAclResponse.
        :type bucket_risk: str
        """
        self._bucket_risk = bucket_risk

    @property
    def message(self):
        r"""Gets the message of this ShowObsBucketAclResponse.

        信息

        :return: The message of this ShowObsBucketAclResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowObsBucketAclResponse.

        信息

        :param message: The message of this ShowObsBucketAclResponse.
        :type message: str
        """
        self._message = message

    @property
    def obs_acl(self):
        r"""Gets the obs_acl of this ShowObsBucketAclResponse.

        桶ACL

        :return: The obs_acl of this ShowObsBucketAclResponse.
        :rtype: str
        """
        return self._obs_acl

    @obs_acl.setter
    def obs_acl(self, obs_acl):
        r"""Sets the obs_acl of this ShowObsBucketAclResponse.

        桶ACL

        :param obs_acl: The obs_acl of this ShowObsBucketAclResponse.
        :type obs_acl: str
        """
        self._obs_acl = obs_acl

    def to_dict(self):
        import warnings
        warnings.warn("ShowObsBucketAclResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowObsBucketAclResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
