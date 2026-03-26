# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDisPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "DeleteDisPolicyRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'dis_policy': 'str',
        'host': 'str'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'dis_policy': 'disPolicy',
        'host': 'Host'
    }

    def __init__(self, date=None, bucket_name=None, dis_policy=None, host=None):
        r"""DeleteDisPolicyRequest

        The model defined in huaweicloud sdk

        :param date: The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field is optional; otherwise, it is required.
        :type date: str
        :param bucket_name: The name of the requested bucket.
        :type bucket_name: str
        :param dis_policy: disPolicy indicates a request to the DIS notification policy API.
        :type dis_policy: str
        :param host: Parameter description, The access domain name of the bucket, in the format BucketName.Endpoint, for example, examplebucketname.obs.cn-north-4.myhuaweicloud.com.
        :type host: str
        """
        
        

        self._date = None
        self._bucket_name = None
        self._dis_policy = None
        self._host = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        if dis_policy is not None:
            self.dis_policy = dis_policy
        if host is not None:
            self.host = host

    @property
    def date(self):
        r"""Gets the date of this DeleteDisPolicyRequest.

        The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field is optional; otherwise, it is required.

        :return: The date of this DeleteDisPolicyRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this DeleteDisPolicyRequest.

        The date and time when the request is initiated, for example: Wed, 27 Jun 2018 13:39:15 +0000. Default value: None. Condition: If the x-obs-date header is included in the request, this field is optional; otherwise, it is required.

        :param date: The date of this DeleteDisPolicyRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this DeleteDisPolicyRequest.

        The name of the requested bucket.

        :return: The bucket_name of this DeleteDisPolicyRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this DeleteDisPolicyRequest.

        The name of the requested bucket.

        :param bucket_name: The bucket_name of this DeleteDisPolicyRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def dis_policy(self):
        r"""Gets the dis_policy of this DeleteDisPolicyRequest.

        disPolicy indicates a request to the DIS notification policy API.

        :return: The dis_policy of this DeleteDisPolicyRequest.
        :rtype: str
        """
        return self._dis_policy

    @dis_policy.setter
    def dis_policy(self, dis_policy):
        r"""Sets the dis_policy of this DeleteDisPolicyRequest.

        disPolicy indicates a request to the DIS notification policy API.

        :param dis_policy: The dis_policy of this DeleteDisPolicyRequest.
        :type dis_policy: str
        """
        self._dis_policy = dis_policy

    @property
    def host(self):
        r"""Gets the host of this DeleteDisPolicyRequest.

        Parameter description, The access domain name of the bucket, in the format BucketName.Endpoint, for example, examplebucketname.obs.cn-north-4.myhuaweicloud.com.

        :return: The host of this DeleteDisPolicyRequest.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this DeleteDisPolicyRequest.

        Parameter description, The access domain name of the bucket, in the format BucketName.Endpoint, for example, examplebucketname.obs.cn-north-4.myhuaweicloud.com.

        :param host: The host of this DeleteDisPolicyRequest.
        :type host: str
        """
        self._host = host

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
        if not isinstance(other, DeleteDisPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
