# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsDataRepository:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'endpoint': 'str',
        'policy': 'ObsDataRepositoryPolicy',
        'attributes': 'ObsTargetAttributes'
    }

    attribute_map = {
        'bucket': 'bucket',
        'endpoint': 'endpoint',
        'policy': 'policy',
        'attributes': 'attributes'
    }

    def __init__(self, bucket=None, endpoint=None, policy=None, attributes=None):
        r"""ObsDataRepository

        The model defined in huaweicloud sdk

        :param bucket: OBS桶名称
        :type bucket: str
        :param endpoint: OBS桶所在的区域域名
        :type endpoint: str
        :param policy: 
        :type policy: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepositoryPolicy`
        :param attributes: 
        :type attributes: :class:`huaweicloudsdksfsturbo.v1.ObsTargetAttributes`
        """
        
        

        self._bucket = None
        self._endpoint = None
        self._policy = None
        self._attributes = None
        self.discriminator = None

        self.bucket = bucket
        self.endpoint = endpoint
        if policy is not None:
            self.policy = policy
        if attributes is not None:
            self.attributes = attributes

    @property
    def bucket(self):
        r"""Gets the bucket of this ObsDataRepository.

        OBS桶名称

        :return: The bucket of this ObsDataRepository.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this ObsDataRepository.

        OBS桶名称

        :param bucket: The bucket of this ObsDataRepository.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def endpoint(self):
        r"""Gets the endpoint of this ObsDataRepository.

        OBS桶所在的区域域名

        :return: The endpoint of this ObsDataRepository.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this ObsDataRepository.

        OBS桶所在的区域域名

        :param endpoint: The endpoint of this ObsDataRepository.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def policy(self):
        r"""Gets the policy of this ObsDataRepository.

        :return: The policy of this ObsDataRepository.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepositoryPolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ObsDataRepository.

        :param policy: The policy of this ObsDataRepository.
        :type policy: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepositoryPolicy`
        """
        self._policy = policy

    @property
    def attributes(self):
        r"""Gets the attributes of this ObsDataRepository.

        :return: The attributes of this ObsDataRepository.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ObsTargetAttributes`
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this ObsDataRepository.

        :param attributes: The attributes of this ObsDataRepository.
        :type attributes: :class:`huaweicloudsdksfsturbo.v1.ObsTargetAttributes`
        """
        self._attributes = attributes

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
        if not isinstance(other, ObsDataRepository):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
