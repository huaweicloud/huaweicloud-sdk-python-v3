# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBucketCustomedomainRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "SetBucketCustomedomainRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'customdomain': 'str',
        'body': 'SetBucketCustomDomainBody'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'customdomain': 'customdomain',
        'body': 'body'
    }

    def __init__(self, date=None, bucket_name=None, customdomain=None, body=None):
        r"""SetBucketCustomedomainRequest

        The model defined in huaweicloud sdk

        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param bucket_name: Name of the requested bucket
        :type bucket_name: str
        :param customdomain: Custom domain name of the bucket.  Type: string, which must meet the naming conventions of domain names.  Specifications: The value contains a maximum of 256 bytes.  Default value: none  Restriction: A bucket can have a maximum of 30 domain names. A custom domain name can be used for only one bucket.
        :type customdomain: str
        :param body: Body of the SetBucketCustomedomainRequest
        :type body: :class:`huaweicloudsdkobs.v1.SetBucketCustomDomainBody`
        """
        
        

        self._date = None
        self._bucket_name = None
        self._customdomain = None
        self._body = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        self.customdomain = customdomain
        if body is not None:
            self.body = body

    @property
    def date(self):
        r"""Gets the date of this SetBucketCustomedomainRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this SetBucketCustomedomainRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this SetBucketCustomedomainRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this SetBucketCustomedomainRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this SetBucketCustomedomainRequest.

        Name of the requested bucket

        :return: The bucket_name of this SetBucketCustomedomainRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this SetBucketCustomedomainRequest.

        Name of the requested bucket

        :param bucket_name: The bucket_name of this SetBucketCustomedomainRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def customdomain(self):
        r"""Gets the customdomain of this SetBucketCustomedomainRequest.

        Custom domain name of the bucket.  Type: string, which must meet the naming conventions of domain names.  Specifications: The value contains a maximum of 256 bytes.  Default value: none  Restriction: A bucket can have a maximum of 30 domain names. A custom domain name can be used for only one bucket.

        :return: The customdomain of this SetBucketCustomedomainRequest.
        :rtype: str
        """
        return self._customdomain

    @customdomain.setter
    def customdomain(self, customdomain):
        r"""Sets the customdomain of this SetBucketCustomedomainRequest.

        Custom domain name of the bucket.  Type: string, which must meet the naming conventions of domain names.  Specifications: The value contains a maximum of 256 bytes.  Default value: none  Restriction: A bucket can have a maximum of 30 domain names. A custom domain name can be used for only one bucket.

        :param customdomain: The customdomain of this SetBucketCustomedomainRequest.
        :type customdomain: str
        """
        self._customdomain = customdomain

    @property
    def body(self):
        r"""Gets the body of this SetBucketCustomedomainRequest.

        :return: The body of this SetBucketCustomedomainRequest.
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketCustomDomainBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SetBucketCustomedomainRequest.

        :param body: The body of this SetBucketCustomedomainRequest.
        :type body: :class:`huaweicloudsdkobs.v1.SetBucketCustomDomainBody`
        """
        self._body = body

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
        if not isinstance(other, SetBucketCustomedomainRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
