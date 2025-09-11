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
        'before_confs': 'object',
        'after_confs': 'object'
    }

    attribute_map = {
        'before_confs': 'before_confs',
        'after_confs': 'after_confs'
    }

    def __init__(self, before_confs=None, after_confs=None):
        r"""ModifyHbaConfRequestBody

        The model defined in huaweicloud sdk

        :param before_confs: **参数解释**: 需要修改的hba配置信息。 **约束限制**: 不涉及。
        :type before_confs: object
        :param after_confs: **参数解释**: 修改后的hba配置信息。 **约束限制**: 不涉及。
        :type after_confs: object
        """
        
        

        self._before_confs = None
        self._after_confs = None
        self.discriminator = None

        self.before_confs = before_confs
        self.after_confs = after_confs

    @property
    def before_confs(self):
        r"""Gets the before_confs of this ModifyHbaConfRequestBody.

        **参数解释**: 需要修改的hba配置信息。 **约束限制**: 不涉及。

        :return: The before_confs of this ModifyHbaConfRequestBody.
        :rtype: object
        """
        return self._before_confs

    @before_confs.setter
    def before_confs(self, before_confs):
        r"""Sets the before_confs of this ModifyHbaConfRequestBody.

        **参数解释**: 需要修改的hba配置信息。 **约束限制**: 不涉及。

        :param before_confs: The before_confs of this ModifyHbaConfRequestBody.
        :type before_confs: object
        """
        self._before_confs = before_confs

    @property
    def after_confs(self):
        r"""Gets the after_confs of this ModifyHbaConfRequestBody.

        **参数解释**: 修改后的hba配置信息。 **约束限制**: 不涉及。

        :return: The after_confs of this ModifyHbaConfRequestBody.
        :rtype: object
        """
        return self._after_confs

    @after_confs.setter
    def after_confs(self, after_confs):
        r"""Sets the after_confs of this ModifyHbaConfRequestBody.

        **参数解释**: 修改后的hba配置信息。 **约束限制**: 不涉及。

        :param after_confs: The after_confs of this ModifyHbaConfRequestBody.
        :type after_confs: object
        """
        self._after_confs = after_confs

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
