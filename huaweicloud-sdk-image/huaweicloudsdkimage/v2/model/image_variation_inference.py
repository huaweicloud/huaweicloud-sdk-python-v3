# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageVariationInference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'seed': 'int',
        'resolution': 'str'
    }

    attribute_map = {
        'seed': 'seed',
        'resolution': 'resolution'
    }

    def __init__(self, seed=None, resolution=None):
        """ImageVariationInference

        The model defined in huaweicloud sdk

        :param seed: 随机数种子
        :type seed: int
        :param resolution: 生成图片分辨率，限定字符串\&quot;512*768\&quot;,\&quot;768*512\&quot;,\&quot;512*512\&quot;,\&quot;1024*768\&quot;,\&quot;768*1024\&quot;，默认\&quot;512*512\&quot;
        :type resolution: str
        """
        
        

        self._seed = None
        self._resolution = None
        self.discriminator = None

        if seed is not None:
            self.seed = seed
        if resolution is not None:
            self.resolution = resolution

    @property
    def seed(self):
        """Gets the seed of this ImageVariationInference.

        随机数种子

        :return: The seed of this ImageVariationInference.
        :rtype: int
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """Sets the seed of this ImageVariationInference.

        随机数种子

        :param seed: The seed of this ImageVariationInference.
        :type seed: int
        """
        self._seed = seed

    @property
    def resolution(self):
        """Gets the resolution of this ImageVariationInference.

        生成图片分辨率，限定字符串\"512*768\",\"768*512\",\"512*512\",\"1024*768\",\"768*1024\"，默认\"512*512\"

        :return: The resolution of this ImageVariationInference.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ImageVariationInference.

        生成图片分辨率，限定字符串\"512*768\",\"768*512\",\"512*512\",\"1024*768\",\"768*1024\"，默认\"512*512\"

        :param resolution: The resolution of this ImageVariationInference.
        :type resolution: str
        """
        self._resolution = resolution

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
        if not isinstance(other, ImageVariationInference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
