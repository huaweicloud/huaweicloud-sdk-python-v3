# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DstNodeReq:

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
        'security_token': 'str',
        'bucket': 'str',
        'save_prefix': 'str',
        'region': 'str'
    }

    attribute_map = {
        'ak': 'ak',
        'sk': 'sk',
        'security_token': 'security_token',
        'bucket': 'bucket',
        'save_prefix': 'save_prefix',
        'region': 'region'
    }

    def __init__(self, ak=None, sk=None, security_token=None, bucket=None, save_prefix=None, region=None):
        """DstNodeReq

        The model defined in huaweicloud sdk

        :param ak: 目的端桶的AK（最大长度100个字符）。
        :type ak: str
        :param sk: 目的端桶的SK（最大长度100个字符）。
        :type sk: str
        :param security_token: 目的端的临时Token（最大长度16384个字符）。
        :type security_token: str
        :param bucket: 目的端桶的名称。
        :type bucket: str
        :param save_prefix: 目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。
        :type save_prefix: str
        :param region: 目的端桶所处的区域。  请与Endpoint对应的区域保持一致。
        :type region: str
        """
        
        

        self._ak = None
        self._sk = None
        self._security_token = None
        self._bucket = None
        self._save_prefix = None
        self._region = None
        self.discriminator = None

        self.ak = ak
        self.sk = sk
        if security_token is not None:
            self.security_token = security_token
        self.bucket = bucket
        if save_prefix is not None:
            self.save_prefix = save_prefix
        self.region = region

    @property
    def ak(self):
        """Gets the ak of this DstNodeReq.

        目的端桶的AK（最大长度100个字符）。

        :return: The ak of this DstNodeReq.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this DstNodeReq.

        目的端桶的AK（最大长度100个字符）。

        :param ak: The ak of this DstNodeReq.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this DstNodeReq.

        目的端桶的SK（最大长度100个字符）。

        :return: The sk of this DstNodeReq.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this DstNodeReq.

        目的端桶的SK（最大长度100个字符）。

        :param sk: The sk of this DstNodeReq.
        :type sk: str
        """
        self._sk = sk

    @property
    def security_token(self):
        """Gets the security_token of this DstNodeReq.

        目的端的临时Token（最大长度16384个字符）。

        :return: The security_token of this DstNodeReq.
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        """Sets the security_token of this DstNodeReq.

        目的端的临时Token（最大长度16384个字符）。

        :param security_token: The security_token of this DstNodeReq.
        :type security_token: str
        """
        self._security_token = security_token

    @property
    def bucket(self):
        """Gets the bucket of this DstNodeReq.

        目的端桶的名称。

        :return: The bucket of this DstNodeReq.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this DstNodeReq.

        目的端桶的名称。

        :param bucket: The bucket of this DstNodeReq.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def save_prefix(self):
        """Gets the save_prefix of this DstNodeReq.

        目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。

        :return: The save_prefix of this DstNodeReq.
        :rtype: str
        """
        return self._save_prefix

    @save_prefix.setter
    def save_prefix(self, save_prefix):
        """Sets the save_prefix of this DstNodeReq.

        目的端桶内路径前缀（拼接在对象key前面,组成新的key,拼接后不能超过1024个字符）。

        :param save_prefix: The save_prefix of this DstNodeReq.
        :type save_prefix: str
        """
        self._save_prefix = save_prefix

    @property
    def region(self):
        """Gets the region of this DstNodeReq.

        目的端桶所处的区域。  请与Endpoint对应的区域保持一致。

        :return: The region of this DstNodeReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DstNodeReq.

        目的端桶所处的区域。  请与Endpoint对应的区域保持一致。

        :param region: The region of this DstNodeReq.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, DstNodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
