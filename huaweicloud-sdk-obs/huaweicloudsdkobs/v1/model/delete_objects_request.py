# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteObjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "DeleteObjectsRequest"

    sensitive_list = []

    openapi_types = {
        'content_md5': 'str',
        'date': 'str',
        'bucket_name': 'str',
        'delete': 'str',
        'body': 'DeleteObjectsRequestBody'
    }

    attribute_map = {
        'content_md5': 'Content-MD5',
        'date': 'Date',
        'bucket_name': 'bucket_name',
        'delete': 'delete',
        'body': 'body'
    }

    def __init__(self, content_md5=None, date=None, bucket_name=None, delete=None, body=None):
        """DeleteObjectsRequest

        The model defined in huaweicloud sdk

        :param content_md5: 按照RFC 1864标准计算出消息体的MD5摘要字符串，即消息体128-bit MD5值经过base64编码后得到的字符串。 
        :type content_md5: str
        :param date: 请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 
        :type date: str
        :param bucket_name: 请求的桶名称。 
        :type bucket_name: str
        :param delete: delete表示请求批量删除对象API。 
        :type delete: str
        :param body: Body of the DeleteObjectsRequest
        :type body: :class:`huaweicloudsdkobs.v1.DeleteObjectsRequestBody`
        """
        
        

        self._content_md5 = None
        self._date = None
        self._bucket_name = None
        self._delete = None
        self._body = None
        self.discriminator = None

        self.content_md5 = content_md5
        if date is not None:
            self.date = date
        self.bucket_name = bucket_name
        self.delete = delete
        if body is not None:
            self.body = body

    @property
    def content_md5(self):
        """Gets the content_md5 of this DeleteObjectsRequest.

        按照RFC 1864标准计算出消息体的MD5摘要字符串，即消息体128-bit MD5值经过base64编码后得到的字符串。 

        :return: The content_md5 of this DeleteObjectsRequest.
        :rtype: str
        """
        return self._content_md5

    @content_md5.setter
    def content_md5(self, content_md5):
        """Sets the content_md5 of this DeleteObjectsRequest.

        按照RFC 1864标准计算出消息体的MD5摘要字符串，即消息体128-bit MD5值经过base64编码后得到的字符串。 

        :param content_md5: The content_md5 of this DeleteObjectsRequest.
        :type content_md5: str
        """
        self._content_md5 = content_md5

    @property
    def date(self):
        """Gets the date of this DeleteObjectsRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :return: The date of this DeleteObjectsRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DeleteObjectsRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :param date: The date of this DeleteObjectsRequest.
        :type date: str
        """
        self._date = date

    @property
    def bucket_name(self):
        """Gets the bucket_name of this DeleteObjectsRequest.

        请求的桶名称。 

        :return: The bucket_name of this DeleteObjectsRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this DeleteObjectsRequest.

        请求的桶名称。 

        :param bucket_name: The bucket_name of this DeleteObjectsRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def delete(self):
        """Gets the delete of this DeleteObjectsRequest.

        delete表示请求批量删除对象API。 

        :return: The delete of this DeleteObjectsRequest.
        :rtype: str
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this DeleteObjectsRequest.

        delete表示请求批量删除对象API。 

        :param delete: The delete of this DeleteObjectsRequest.
        :type delete: str
        """
        self._delete = delete

    @property
    def body(self):
        """Gets the body of this DeleteObjectsRequest.

        :return: The body of this DeleteObjectsRequest.
        :rtype: :class:`huaweicloudsdkobs.v1.DeleteObjectsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteObjectsRequest.

        :param body: The body of this DeleteObjectsRequest.
        :type body: :class:`huaweicloudsdkobs.v1.DeleteObjectsRequestBody`
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
        if not isinstance(other, DeleteObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
