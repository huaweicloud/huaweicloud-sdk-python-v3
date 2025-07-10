# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchConfigEvaluationInfoSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image': 'BatchConfigImageInfoSrlz',
        'config': 'BatchConfigABCInfoSrlz'
    }

    attribute_map = {
        'image': 'image',
        'config': 'config'
    }

    def __init__(self, image=None, config=None):
        r"""BatchConfigEvaluationInfoSrlz

        The model defined in huaweicloud sdk

        :param image: 镜像信息
        :type image: :class:`huaweicloudsdkoctopus.v2.BatchConfigImageInfoSrlz`
        :param config: 内置评测配置信息
        :type config: :class:`huaweicloudsdkoctopus.v2.BatchConfigABCInfoSrlz`
        """
        
        

        self._image = None
        self._config = None
        self.discriminator = None

        self.image = image
        self.config = config

    @property
    def image(self):
        r"""Gets the image of this BatchConfigEvaluationInfoSrlz.

        镜像信息

        :return: The image of this BatchConfigEvaluationInfoSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.BatchConfigImageInfoSrlz`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this BatchConfigEvaluationInfoSrlz.

        镜像信息

        :param image: The image of this BatchConfigEvaluationInfoSrlz.
        :type image: :class:`huaweicloudsdkoctopus.v2.BatchConfigImageInfoSrlz`
        """
        self._image = image

    @property
    def config(self):
        r"""Gets the config of this BatchConfigEvaluationInfoSrlz.

        内置评测配置信息

        :return: The config of this BatchConfigEvaluationInfoSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.BatchConfigABCInfoSrlz`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this BatchConfigEvaluationInfoSrlz.

        内置评测配置信息

        :param config: The config of this BatchConfigEvaluationInfoSrlz.
        :type config: :class:`huaweicloudsdkoctopus.v2.BatchConfigABCInfoSrlz`
        """
        self._config = config

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
        if not isinstance(other, BatchConfigEvaluationInfoSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
