# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBucketsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "ListBucketsRequest"

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'x_obs_bucket_type': 'str'
    }

    attribute_map = {
        'date': 'Date',
        'x_obs_bucket_type': 'x-obs-bucket-type'
    }

    def __init__(self, date=None, x_obs_bucket_type=None):
        r"""ListBucketsRequest

        The model defined in huaweicloud sdk

        :param date: Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.
        :type date: str
        :param x_obs_bucket_type: Specifies the content to obtain. Possible values: **OBJECT**: A list of all buckets is returned. **POSIX**: A list of all parallel file systems is returned. If this header is not carried, a list of all buckets and parallel file systems is returned.
        :type x_obs_bucket_type: str
        """
        
        

        self._date = None
        self._x_obs_bucket_type = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if x_obs_bucket_type is not None:
            self.x_obs_bucket_type = x_obs_bucket_type

    @property
    def date(self):
        r"""Gets the date of this ListBucketsRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :return: The date of this ListBucketsRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this ListBucketsRequest.

        Time when a request was initiated, for example, **Wed, 27 Jun 2018 13:39:15 +0000**. Default value: none Restriction: This header is optional if the **x-obs-date** header is contained in the request, but mandatory in other circumstances.

        :param date: The date of this ListBucketsRequest.
        :type date: str
        """
        self._date = date

    @property
    def x_obs_bucket_type(self):
        r"""Gets the x_obs_bucket_type of this ListBucketsRequest.

        Specifies the content to obtain. Possible values: **OBJECT**: A list of all buckets is returned. **POSIX**: A list of all parallel file systems is returned. If this header is not carried, a list of all buckets and parallel file systems is returned.

        :return: The x_obs_bucket_type of this ListBucketsRequest.
        :rtype: str
        """
        return self._x_obs_bucket_type

    @x_obs_bucket_type.setter
    def x_obs_bucket_type(self, x_obs_bucket_type):
        r"""Sets the x_obs_bucket_type of this ListBucketsRequest.

        Specifies the content to obtain. Possible values: **OBJECT**: A list of all buckets is returned. **POSIX**: A list of all parallel file systems is returned. If this header is not carried, a list of all buckets and parallel file systems is returned.

        :param x_obs_bucket_type: The x_obs_bucket_type of this ListBucketsRequest.
        :type x_obs_bucket_type: str
        """
        self._x_obs_bucket_type = x_obs_bucket_type

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
        if not isinstance(other, ListBucketsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
