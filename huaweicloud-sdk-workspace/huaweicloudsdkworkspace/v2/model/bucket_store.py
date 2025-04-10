# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BucketStore:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'bucket_file_path': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'bucket_file_path': 'bucket_file_path'
    }

    def __init__(self, bucket_name=None, bucket_file_path=None):
        r"""BucketStore

        The model defined in huaweicloud sdk

        :param bucket_name: 桶名称固定格式:wks-appcenter-{project_id}; 需先调用桶授权接口进行授权。
        :type bucket_name: str
        :param bucket_file_path: OBS对象路径。 注: bucket_file_path是对象在obs中的完整路径,不能以/开头。 例如桶存在如下目录结构的数据。   Bucket:     ├─dir1     | ├─object1.txt     | └─object2.txt     └─object3.txt Object1的路径: dir1/object1.txt Object2的路径: dir1/object2.txt Object3的路径: object3.txt
        :type bucket_file_path: str
        """
        
        

        self._bucket_name = None
        self._bucket_file_path = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if bucket_file_path is not None:
            self.bucket_file_path = bucket_file_path

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this BucketStore.

        桶名称固定格式:wks-appcenter-{project_id}; 需先调用桶授权接口进行授权。

        :return: The bucket_name of this BucketStore.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this BucketStore.

        桶名称固定格式:wks-appcenter-{project_id}; 需先调用桶授权接口进行授权。

        :param bucket_name: The bucket_name of this BucketStore.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def bucket_file_path(self):
        r"""Gets the bucket_file_path of this BucketStore.

        OBS对象路径。 注: bucket_file_path是对象在obs中的完整路径,不能以/开头。 例如桶存在如下目录结构的数据。   Bucket:     ├─dir1     | ├─object1.txt     | └─object2.txt     └─object3.txt Object1的路径: dir1/object1.txt Object2的路径: dir1/object2.txt Object3的路径: object3.txt

        :return: The bucket_file_path of this BucketStore.
        :rtype: str
        """
        return self._bucket_file_path

    @bucket_file_path.setter
    def bucket_file_path(self, bucket_file_path):
        r"""Sets the bucket_file_path of this BucketStore.

        OBS对象路径。 注: bucket_file_path是对象在obs中的完整路径,不能以/开头。 例如桶存在如下目录结构的数据。   Bucket:     ├─dir1     | ├─object1.txt     | └─object2.txt     └─object3.txt Object1的路径: dir1/object1.txt Object2的路径: dir1/object2.txt Object3的路径: object3.txt

        :param bucket_file_path: The bucket_file_path of this BucketStore.
        :type bucket_file_path: str
        """
        self._bucket_file_path = bucket_file_path

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
        if not isinstance(other, BucketStore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
