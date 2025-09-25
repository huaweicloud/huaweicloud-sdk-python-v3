# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyHbaConfRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'before_conf': 'object',
        'after_conf': 'object'
    }

    attribute_map = {
        'before_conf': 'before_conf',
        'after_conf': 'after_conf'
    }

    def __init__(self, before_conf=None, after_conf=None):
        r"""ModifyHbaConfRequestBody

        The model defined in huaweicloud sdk

        :param before_conf: **参数解释**: 需要修改的hba配置信息。 **约束限制**: 不涉及。
        :type before_conf: object
        :param after_conf: **参数解释**: 修改后的hba配置信息。 **约束限制**: 不涉及。
        :type after_conf: object
        """
        
        

        self._before_conf = None
        self._after_conf = None
        self.discriminator = None

        self.before_conf = before_conf
        self.after_conf = after_conf

    @property
    def before_conf(self):
        r"""Gets the before_conf of this ModifyHbaConfRequestBody.

        **参数解释**: 需要修改的hba配置信息。 **约束限制**: 不涉及。

        :return: The before_conf of this ModifyHbaConfRequestBody.
        :rtype: object
        """
        return self._before_conf

    @before_conf.setter
    def before_conf(self, before_conf):
        r"""Sets the before_conf of this ModifyHbaConfRequestBody.

        **参数解释**: 需要修改的hba配置信息。 **约束限制**: 不涉及。

        :param before_conf: The before_conf of this ModifyHbaConfRequestBody.
        :type before_conf: object
        """
        self._before_conf = before_conf

    @property
    def after_conf(self):
        r"""Gets the after_conf of this ModifyHbaConfRequestBody.

        **参数解释**: 修改后的hba配置信息。 **约束限制**: 不涉及。

        :return: The after_conf of this ModifyHbaConfRequestBody.
        :rtype: object
        """
        return self._after_conf

    @after_conf.setter
    def after_conf(self, after_conf):
        r"""Sets the after_conf of this ModifyHbaConfRequestBody.

        **参数解释**: 修改后的hba配置信息。 **约束限制**: 不涉及。

        :param after_conf: The after_conf of this ModifyHbaConfRequestBody.
        :type after_conf: object
        """
        self._after_conf = after_conf

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
        if not isinstance(other, ModifyHbaConfRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
