# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowObjectMetaDataResponse(SdkResponse):

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
        'next_marker': 'str',
        'object_list': 'list[ObjectList]'
    }

    attribute_map = {
        'bucket': 'bucket',
        'next_marker': 'next_marker',
        'object_list': 'object_list'
    }

    def __init__(self, bucket=None, next_marker=None, object_list=None):
        r"""ShowObjectMetaDataResponse

        The model defined in huaweicloud sdk

        :param bucket: 桶名 
        :type bucket: str
        :param next_marker: 下次列举对象请求的起始位置。 
        :type next_marker: str
        :param object_list: 媒体元数据列表 
        :type object_list: list[:class:`huaweicloudsdkvod.v1.ObjectList`]
        """
        
        super(ShowObjectMetaDataResponse, self).__init__()

        self._bucket = None
        self._next_marker = None
        self._object_list = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if next_marker is not None:
            self.next_marker = next_marker
        if object_list is not None:
            self.object_list = object_list

    @property
    def bucket(self):
        r"""Gets the bucket of this ShowObjectMetaDataResponse.

        桶名 

        :return: The bucket of this ShowObjectMetaDataResponse.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this ShowObjectMetaDataResponse.

        桶名 

        :param bucket: The bucket of this ShowObjectMetaDataResponse.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ShowObjectMetaDataResponse.

        下次列举对象请求的起始位置。 

        :return: The next_marker of this ShowObjectMetaDataResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ShowObjectMetaDataResponse.

        下次列举对象请求的起始位置。 

        :param next_marker: The next_marker of this ShowObjectMetaDataResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def object_list(self):
        r"""Gets the object_list of this ShowObjectMetaDataResponse.

        媒体元数据列表 

        :return: The object_list of this ShowObjectMetaDataResponse.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ObjectList`]
        """
        return self._object_list

    @object_list.setter
    def object_list(self, object_list):
        r"""Sets the object_list of this ShowObjectMetaDataResponse.

        媒体元数据列表 

        :param object_list: The object_list of this ShowObjectMetaDataResponse.
        :type object_list: list[:class:`huaweicloudsdkvod.v1.ObjectList`]
        """
        self._object_list = object_list

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
        if not isinstance(other, ShowObjectMetaDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
