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
        'resolution': 'str',
        'image_nums': 'int'
    }

    attribute_map = {
        'seed': 'seed',
        'resolution': 'resolution',
        'image_nums': 'image_nums'
    }

    def __init__(self, seed=None, resolution=None, image_nums=None):
        """ImageVariationInference

        The model defined in huaweicloud sdk

        :param seed: 随机数种子
        :type seed: int
        :param resolution: 生成图片分辨率，限定字符串\&quot;512\\*768\&quot;,\&quot;768\\*512\&quot;,\&quot;512\\*512\&quot;，默认\&quot;512\\*512\&quot;
        :type resolution: str
        :param image_nums: 生成图片数量，支持1-4张，默认为1
        :type image_nums: int
        """
        
        

        self._seed = None
        self._resolution = None
        self._image_nums = None
        self.discriminator = None

        if seed is not None:
            self.seed = seed
        if resolution is not None:
            self.resolution = resolution
        if image_nums is not None:
            self.image_nums = image_nums

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

        生成图片分辨率，限定字符串\"512\\*768\",\"768\\*512\",\"512\\*512\"，默认\"512\\*512\"

        :return: The resolution of this ImageVariationInference.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ImageVariationInference.

        生成图片分辨率，限定字符串\"512\\*768\",\"768\\*512\",\"512\\*512\"，默认\"512\\*512\"

        :param resolution: The resolution of this ImageVariationInference.
        :type resolution: str
        """
        self._resolution = resolution

    @property
    def image_nums(self):
        """Gets the image_nums of this ImageVariationInference.

        生成图片数量，支持1-4张，默认为1

        :return: The image_nums of this ImageVariationInference.
        :rtype: int
        """
        return self._image_nums

    @image_nums.setter
    def image_nums(self, image_nums):
        """Sets the image_nums of this ImageVariationInference.

        生成图片数量，支持1-4张，默认为1

        :param image_nums: The image_nums of this ImageVariationInference.
        :type image_nums: int
        """
        self._image_nums = image_nums

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
