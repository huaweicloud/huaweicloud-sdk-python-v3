# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StepImageVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'img_id': 'str',
        'img_url': 'str'
    }

    attribute_map = {
        'img_id': 'img_id',
        'img_url': 'img_url'
    }

    def __init__(self, img_id=None, img_url=None):
        r"""StepImageVo

        The model defined in huaweicloud sdk

        :param img_id: 测试步骤图片id
        :type img_id: str
        :param img_url: 测试步骤图片路径
        :type img_url: str
        """
        
        

        self._img_id = None
        self._img_url = None
        self.discriminator = None

        if img_id is not None:
            self.img_id = img_id
        if img_url is not None:
            self.img_url = img_url

    @property
    def img_id(self):
        r"""Gets the img_id of this StepImageVo.

        测试步骤图片id

        :return: The img_id of this StepImageVo.
        :rtype: str
        """
        return self._img_id

    @img_id.setter
    def img_id(self, img_id):
        r"""Sets the img_id of this StepImageVo.

        测试步骤图片id

        :param img_id: The img_id of this StepImageVo.
        :type img_id: str
        """
        self._img_id = img_id

    @property
    def img_url(self):
        r"""Gets the img_url of this StepImageVo.

        测试步骤图片路径

        :return: The img_url of this StepImageVo.
        :rtype: str
        """
        return self._img_url

    @img_url.setter
    def img_url(self, img_url):
        r"""Sets the img_url of this StepImageVo.

        测试步骤图片路径

        :param img_url: The img_url of this StepImageVo.
        :type img_url: str
        """
        self._img_url = img_url

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
        if not isinstance(other, StepImageVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
