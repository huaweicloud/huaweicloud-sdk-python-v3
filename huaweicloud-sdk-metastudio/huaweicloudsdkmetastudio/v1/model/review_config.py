# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReviewConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'no_need_review': 'bool'
    }

    attribute_map = {
        'no_need_review': 'no_need_review'
    }

    def __init__(self, no_need_review=None):
        r"""ReviewConfig

        The model defined in huaweicloud sdk

        :param no_need_review: 免审核。 目前仅白名单用户可使用此参数，非白名单用户跟随系统策略审核。
        :type no_need_review: bool
        """
        
        

        self._no_need_review = None
        self.discriminator = None

        if no_need_review is not None:
            self.no_need_review = no_need_review

    @property
    def no_need_review(self):
        r"""Gets the no_need_review of this ReviewConfig.

        免审核。 目前仅白名单用户可使用此参数，非白名单用户跟随系统策略审核。

        :return: The no_need_review of this ReviewConfig.
        :rtype: bool
        """
        return self._no_need_review

    @no_need_review.setter
    def no_need_review(self, no_need_review):
        r"""Sets the no_need_review of this ReviewConfig.

        免审核。 目前仅白名单用户可使用此参数，非白名单用户跟随系统策略审核。

        :param no_need_review: The no_need_review of this ReviewConfig.
        :type no_need_review: bool
        """
        self._no_need_review = no_need_review

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
        if not isinstance(other, ReviewConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
