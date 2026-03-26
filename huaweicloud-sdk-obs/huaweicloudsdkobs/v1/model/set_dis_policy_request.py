# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetDisPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "SetDisPolicyRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'dis_policy': 'str',
        'host': 'str',
        'body': 'SetBucketDisPolicyRequestBody'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'dis_policy': 'disPolicy',
        'host': 'Host',
        'body': 'body'
    }

    def __init__(self, date=None, bucket_name=None, dis_policy=None, host=None, body=None):
        r"""SetDisPolicyRequest

        The model defined in huaweicloud sdk

        :param date: The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field can be omitted; otherwise, it is required.
        :type date: str
        :param bucket_name: The name of the requested bucket.
        :type bucket_name: str
        :param dis_policy: policy indicates a request to the DIS notification policy API.
        :type dis_policy: str
        :param host: Parameter description, The bucket&#39;s access domain name, in the format BucketName, for example,examplebucketname.obs.cn-north-4.myhuaweicloud.com.
        :type host: str
        :param body: Body of the SetDisPolicyRequest
        :type body: :class:`huaweicloudsdkobs.v1.SetBucketDisPolicyRequestBody`
        """
        
        

        self._date = None
        self._bucket_name = None
        self._dis_policy = None
        self._host = None
        self._body = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        if dis_policy is not None:
            self.dis_policy = dis_policy
        if host is not None:
            self.host = host
        if body is not None:
            self.body = body

    @property
    def date(self):
        r"""Gets the date of this SetDisPolicyRequest.

        The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field can be omitted; otherwise, it is required.

        :return: The date of this SetDisPolicyRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this SetDisPolicyRequest.

        The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field can be omitted; otherwise, it is required.

        :param date: The date of this SetDisPolicyRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this SetDisPolicyRequest.

        The name of the requested bucket.

        :return: The bucket_name of this SetDisPolicyRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this SetDisPolicyRequest.

        The name of the requested bucket.

        :param bucket_name: The bucket_name of this SetDisPolicyRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def dis_policy(self):
        r"""Gets the dis_policy of this SetDisPolicyRequest.

        policy indicates a request to the DIS notification policy API.

        :return: The dis_policy of this SetDisPolicyRequest.
        :rtype: str
        """
        return self._dis_policy

    @dis_policy.setter
    def dis_policy(self, dis_policy):
        r"""Sets the dis_policy of this SetDisPolicyRequest.

        policy indicates a request to the DIS notification policy API.

        :param dis_policy: The dis_policy of this SetDisPolicyRequest.
        :type dis_policy: str
        """
        self._dis_policy = dis_policy

    @property
    def host(self):
        r"""Gets the host of this SetDisPolicyRequest.

        Parameter description, The bucket's access domain name, in the format BucketName, for example,examplebucketname.obs.cn-north-4.myhuaweicloud.com.

        :return: The host of this SetDisPolicyRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this SetDisPolicyRequest.

        Parameter description, The bucket's access domain name, in the format BucketName, for example,examplebucketname.obs.cn-north-4.myhuaweicloud.com.

        :param host: The host of this SetDisPolicyRequest.
        :type host: str
        """
        self._host = host

    @property
    def body(self):
        r"""Gets the body of this SetDisPolicyRequest.

        :return: The body of this SetDisPolicyRequest.
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketDisPolicyRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SetDisPolicyRequest.

        :param body: The body of this SetDisPolicyRequest.
        :type body: :class:`huaweicloudsdkobs.v1.SetBucketDisPolicyRequestBody`
        """
        self._body = body

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
        if not isinstance(other, SetDisPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
