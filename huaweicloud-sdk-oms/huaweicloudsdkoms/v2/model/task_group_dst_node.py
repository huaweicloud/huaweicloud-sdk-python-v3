# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskGroupDstNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ak': 'str',
        'sk': 'str',
        'region': 'str',
        'bucket': 'str',
        'cloud_type': 'str',
        'save_prefix': 'str'
    }

    attribute_map = {
        'ak': 'ak',
        'sk': 'sk',
        'region': 'region',
        'bucket': 'bucket',
        'cloud_type': 'cloud_type',
        'save_prefix': 'save_prefix'
    }

    def __init__(self, ak=None, sk=None, region=None, bucket=None, cloud_type=None, save_prefix=None):
        """TaskGroupDstNode

        The model defined in huaweicloud sdk

        :param ak: 目的端桶的AK（最大长度100个字符）。
        :type ak: str
        :param sk: 目的端桶的SK（最大长度100个字符）。
        :type sk: str
        :param region: 目的端桶所处的区域。  请与Endpoint对应的区域保持一致。
        :type region: str
        :param bucket: 目的端的桶名称
        :type bucket: str
        :param cloud_type: 华为云目的端信息，默认为HEC
        :type cloud_type: str
        :param save_prefix: 目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。
        :type save_prefix: str
        """
        
        

        self._ak = None
        self._sk = None
        self._region = None
        self._bucket = None
        self._cloud_type = None
        self._save_prefix = None
        self.discriminator = None

        self.ak = ak
        self.sk = sk
        self.region = region
        self.bucket = bucket
        if cloud_type is not None:
            self.cloud_type = cloud_type
        if save_prefix is not None:
            self.save_prefix = save_prefix

    @property
    def ak(self):
        """Gets the ak of this TaskGroupDstNode.

        目的端桶的AK（最大长度100个字符）。

        :return: The ak of this TaskGroupDstNode.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this TaskGroupDstNode.

        目的端桶的AK（最大长度100个字符）。

        :param ak: The ak of this TaskGroupDstNode.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this TaskGroupDstNode.

        目的端桶的SK（最大长度100个字符）。

        :return: The sk of this TaskGroupDstNode.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this TaskGroupDstNode.

        目的端桶的SK（最大长度100个字符）。

        :param sk: The sk of this TaskGroupDstNode.
        :type sk: str
        """
        self._sk = sk

    @property
    def region(self):
        """Gets the region of this TaskGroupDstNode.

        目的端桶所处的区域。  请与Endpoint对应的区域保持一致。

        :return: The region of this TaskGroupDstNode.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TaskGroupDstNode.

        目的端桶所处的区域。  请与Endpoint对应的区域保持一致。

        :param region: The region of this TaskGroupDstNode.
        :type region: str
        """
        self._region = region

    @property
    def bucket(self):
        """Gets the bucket of this TaskGroupDstNode.

        目的端的桶名称

        :return: The bucket of this TaskGroupDstNode.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this TaskGroupDstNode.

        目的端的桶名称

        :param bucket: The bucket of this TaskGroupDstNode.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def cloud_type(self):
        """Gets the cloud_type of this TaskGroupDstNode.

        华为云目的端信息，默认为HEC

        :return: The cloud_type of this TaskGroupDstNode.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this TaskGroupDstNode.

        华为云目的端信息，默认为HEC

        :param cloud_type: The cloud_type of this TaskGroupDstNode.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def save_prefix(self):
        """Gets the save_prefix of this TaskGroupDstNode.

        目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。

        :return: The save_prefix of this TaskGroupDstNode.
        :rtype: str
        """
        return self._save_prefix

    @save_prefix.setter
    def save_prefix(self, save_prefix):
        """Sets the save_prefix of this TaskGroupDstNode.

        目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。

        :param save_prefix: The save_prefix of this TaskGroupDstNode.
        :type save_prefix: str
        """
        self._save_prefix = save_prefix

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
        if not isinstance(other, TaskGroupDstNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
