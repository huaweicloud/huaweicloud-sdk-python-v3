# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidationResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'link_config': 'list[ValidationLinkConfig]'
    }

    attribute_map = {
        'link_config': 'linkConfig'
    }

    def __init__(self, link_config=None):
        r"""ValidationResult

        The model defined in huaweicloud sdk

        :param link_config: 创建或更新连接校验结果，请参见linkConfig参数说明
        :type link_config: list[:class:`huaweicloudsdkcdm.v1.ValidationLinkConfig`]
        """
        
        

        self._link_config = None
        self.discriminator = None

        if link_config is not None:
            self.link_config = link_config

    @property
    def link_config(self):
        r"""Gets the link_config of this ValidationResult.

        创建或更新连接校验结果，请参见linkConfig参数说明

        :return: The link_config of this ValidationResult.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.ValidationLinkConfig`]
        """
        return self._link_config

    @link_config.setter
    def link_config(self, link_config):
        r"""Sets the link_config of this ValidationResult.

        创建或更新连接校验结果，请参见linkConfig参数说明

        :param link_config: The link_config of this ValidationResult.
        :type link_config: list[:class:`huaweicloudsdkcdm.v1.ValidationLinkConfig`]
        """
        self._link_config = link_config

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
        if not isinstance(other, ValidationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
