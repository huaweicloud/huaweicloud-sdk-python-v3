# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBucketAclRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "SetBucketAclRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'bucket_name': 'str',
        'acl': 'str',
        'x_obs_acl': 'str',
        'body': 'SetBucketAclRequestBody'
    }

    attribute_map = {
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'acl': 'acl',
        'x_obs_acl': 'x-obs-acl',
        'body': 'body'
    }

    def __init__(self, date=None, bucket_name=None, acl=None, x_obs_acl=None, body=None):
        r"""SetBucketAclRequest

        The model defined in huaweicloud sdk

        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param bucket_name: Name of the requested bucket
        :type bucket_name: str
        :param acl: Indicates the API for sending a request to the ACL.
        :type acl: str
        :param x_obs_acl: Uses a canned ACL for the bucket.Value options: **private**, **public-read**, **public-read-write**, **public-read-delivered**, or **public-read-write-delivered**
        :type x_obs_acl: str
        :param body: Body of the SetBucketAclRequest
        :type body: :class:`huaweicloudsdkobs.v1.SetBucketAclRequestBody`
        """
        
        

        self._date = None
        self._bucket_name = None
        self._acl = None
        self._x_obs_acl = None
        self._body = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        self.acl = acl
        if x_obs_acl is not None:
            self.x_obs_acl = x_obs_acl
        if body is not None:
            self.body = body

    @property
    def date(self):
        r"""Gets the date of this SetBucketAclRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this SetBucketAclRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this SetBucketAclRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this SetBucketAclRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this SetBucketAclRequest.

        Name of the requested bucket

        :return: The bucket_name of this SetBucketAclRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this SetBucketAclRequest.

        Name of the requested bucket

        :param bucket_name: The bucket_name of this SetBucketAclRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def acl(self):
        r"""Gets the acl of this SetBucketAclRequest.

        Indicates the API for sending a request to the ACL.

        :return: The acl of this SetBucketAclRequest.
        :rtype: str
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        r"""Sets the acl of this SetBucketAclRequest.

        Indicates the API for sending a request to the ACL.

        :param acl: The acl of this SetBucketAclRequest.
        :type acl: str
        """
        self._acl = acl

    @property
    def x_obs_acl(self):
        r"""Gets the x_obs_acl of this SetBucketAclRequest.

        Uses a canned ACL for the bucket.Value options: **private**, **public-read**, **public-read-write**, **public-read-delivered**, or **public-read-write-delivered**

        :return: The x_obs_acl of this SetBucketAclRequest.
        :rtype: str
        """
        return self._x_obs_acl

    @x_obs_acl.setter
    def x_obs_acl(self, x_obs_acl):
        r"""Sets the x_obs_acl of this SetBucketAclRequest.

        Uses a canned ACL for the bucket.Value options: **private**, **public-read**, **public-read-write**, **public-read-delivered**, or **public-read-write-delivered**

        :param x_obs_acl: The x_obs_acl of this SetBucketAclRequest.
        :type x_obs_acl: str
        """
        self._x_obs_acl = x_obs_acl

    @property
    def body(self):
        r"""Gets the body of this SetBucketAclRequest.

        :return: The body of this SetBucketAclRequest.
        :rtype: :class:`huaweicloudsdkobs.v1.SetBucketAclRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SetBucketAclRequest.

        :param body: The body of this SetBucketAclRequest.
        :type body: :class:`huaweicloudsdkobs.v1.SetBucketAclRequestBody`
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
        if not isinstance(other, SetBucketAclRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
