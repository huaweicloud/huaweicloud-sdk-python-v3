# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileStoreLink:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'store_type': 'FileStoreTypeEnum',
        'bucket_store': 'BucketStore',
        'file_link': 'str'
    }

    attribute_map = {
        'store_type': 'store_type',
        'bucket_store': 'bucket_store',
        'file_link': 'file_link'
    }

    def __init__(self, store_type=None, bucket_store=None, file_link=None):
        r"""FileStoreLink

        The model defined in huaweicloud sdk

        :param store_type: 
        :type store_type: :class:`huaweicloudsdkworkspace.v2.FileStoreTypeEnum`
        :param bucket_store: 
        :type bucket_store: :class:`huaweicloudsdkworkspace.v2.BucketStore`
        :param file_link: 文件下载完整路径。
        :type file_link: str
        """
        
        

        self._store_type = None
        self._bucket_store = None
        self._file_link = None
        self.discriminator = None

        self.store_type = store_type
        if bucket_store is not None:
            self.bucket_store = bucket_store
        if file_link is not None:
            self.file_link = file_link

    @property
    def store_type(self):
        r"""Gets the store_type of this FileStoreLink.

        :return: The store_type of this FileStoreLink.
        :rtype: :class:`huaweicloudsdkworkspace.v2.FileStoreTypeEnum`
        """
        return self._store_type

    @store_type.setter
    def store_type(self, store_type):
        r"""Sets the store_type of this FileStoreLink.

        :param store_type: The store_type of this FileStoreLink.
        :type store_type: :class:`huaweicloudsdkworkspace.v2.FileStoreTypeEnum`
        """
        self._store_type = store_type

    @property
    def bucket_store(self):
        r"""Gets the bucket_store of this FileStoreLink.

        :return: The bucket_store of this FileStoreLink.
        :rtype: :class:`huaweicloudsdkworkspace.v2.BucketStore`
        """
        return self._bucket_store

    @bucket_store.setter
    def bucket_store(self, bucket_store):
        r"""Sets the bucket_store of this FileStoreLink.

        :param bucket_store: The bucket_store of this FileStoreLink.
        :type bucket_store: :class:`huaweicloudsdkworkspace.v2.BucketStore`
        """
        self._bucket_store = bucket_store

    @property
    def file_link(self):
        r"""Gets the file_link of this FileStoreLink.

        文件下载完整路径。

        :return: The file_link of this FileStoreLink.
        :rtype: str
        """
        return self._file_link

    @file_link.setter
    def file_link(self, file_link):
        r"""Sets the file_link of this FileStoreLink.

        文件下载完整路径。

        :param file_link: The file_link of this FileStoreLink.
        :type file_link: str
        """
        self._file_link = file_link

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
        if not isinstance(other, FileStoreLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
