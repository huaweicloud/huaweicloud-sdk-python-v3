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
        """ListBucketsRequest

        The model defined in huaweicloud sdk

        :param date: 请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 
        :type date: str
        :param x_obs_bucket_type: 通过此消息头明确获取的列表内容。 取值： OBJECT：获取所有桶列表。 POSIX：获取所有并行文件系统列表。 不带此消息头则获取所有桶和并行文件系统列表。 
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
        """Gets the date of this ListBucketsRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :return: The date of this ListBucketsRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ListBucketsRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :param date: The date of this ListBucketsRequest.
        :type date: str
        """
        self._date = date

    @property
    def x_obs_bucket_type(self):
        """Gets the x_obs_bucket_type of this ListBucketsRequest.

        通过此消息头明确获取的列表内容。 取值： OBJECT：获取所有桶列表。 POSIX：获取所有并行文件系统列表。 不带此消息头则获取所有桶和并行文件系统列表。 

        :return: The x_obs_bucket_type of this ListBucketsRequest.
        :rtype: str
        """
        return self._x_obs_bucket_type

    @x_obs_bucket_type.setter
    def x_obs_bucket_type(self, x_obs_bucket_type):
        """Sets the x_obs_bucket_type of this ListBucketsRequest.

        通过此消息头明确获取的列表内容。 取值： OBJECT：获取所有桶列表。 POSIX：获取所有并行文件系统列表。 不带此消息头则获取所有桶和并行文件系统列表。 

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
