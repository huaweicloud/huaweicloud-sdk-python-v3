# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetBucketPolicyPublicStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "GetBucketPolicyPublicStatusRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'policy_status': 'str'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'policy_status': 'policyStatus'
    }

    def __init__(self, date=None, bucket_name=None, policy_status=None):
        r"""GetBucketPolicyPublicStatusRequest

        The model defined in huaweicloud sdk

        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param bucket_name: Name of the requested bucket
        :type bucket_name: str
        :param policy_status: Indicates the API for obtains the public access status of an OBS bucket policy.
        :type policy_status: str
        """
        
        

        self._date = None
        self._bucket_name = None
        self._policy_status = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        if policy_status is not None:
            self.policy_status = policy_status

    @property
    def date(self):
        r"""Gets the date of this GetBucketPolicyPublicStatusRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this GetBucketPolicyPublicStatusRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this GetBucketPolicyPublicStatusRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this GetBucketPolicyPublicStatusRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this GetBucketPolicyPublicStatusRequest.

        Name of the requested bucket

        :return: The bucket_name of this GetBucketPolicyPublicStatusRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this GetBucketPolicyPublicStatusRequest.

        Name of the requested bucket

        :param bucket_name: The bucket_name of this GetBucketPolicyPublicStatusRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def policy_status(self):
        r"""Gets the policy_status of this GetBucketPolicyPublicStatusRequest.

        Indicates the API for obtains the public access status of an OBS bucket policy.

        :return: The policy_status of this GetBucketPolicyPublicStatusRequest.
        :rtype: str
        """
        return self._policy_status

    @policy_status.setter
    def policy_status(self, policy_status):
        r"""Sets the policy_status of this GetBucketPolicyPublicStatusRequest.

        Indicates the API for obtains the public access status of an OBS bucket policy.

        :param policy_status: The policy_status of this GetBucketPolicyPublicStatusRequest.
        :type policy_status: str
        """
        self._policy_status = policy_status

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
        if not isinstance(other, GetBucketPolicyPublicStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
