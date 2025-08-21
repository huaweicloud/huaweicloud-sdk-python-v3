# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostNoteRequiredAttributeDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_assignee_id_required': 'bool',
        'is_review_categories_required': 'bool',
        'is_review_modules_required': 'bool'
    }

    attribute_map = {
        'is_assignee_id_required': 'is_assignee_id_required',
        'is_review_categories_required': 'is_review_categories_required',
        'is_review_modules_required': 'is_review_modules_required'
    }

    def __init__(self, is_assignee_id_required=None, is_review_categories_required=None, is_review_modules_required=None):
        r"""PostNoteRequiredAttributeDto

        The model defined in huaweicloud sdk

        :param is_assignee_id_required: **参数解释：** 是否勾选指派给。
        :type is_assignee_id_required: bool
        :param is_review_categories_required: **参数解释：** 是否勾选意见分类。
        :type is_review_categories_required: bool
        :param is_review_modules_required: **参数解释：** 是否勾选意见模块。
        :type is_review_modules_required: bool
        """
        
        

        self._is_assignee_id_required = None
        self._is_review_categories_required = None
        self._is_review_modules_required = None
        self.discriminator = None

        if is_assignee_id_required is not None:
            self.is_assignee_id_required = is_assignee_id_required
        if is_review_categories_required is not None:
            self.is_review_categories_required = is_review_categories_required
        if is_review_modules_required is not None:
            self.is_review_modules_required = is_review_modules_required

    @property
    def is_assignee_id_required(self):
        r"""Gets the is_assignee_id_required of this PostNoteRequiredAttributeDto.

        **参数解释：** 是否勾选指派给。

        :return: The is_assignee_id_required of this PostNoteRequiredAttributeDto.
        :rtype: bool
        """
        return self._is_assignee_id_required

    @is_assignee_id_required.setter
    def is_assignee_id_required(self, is_assignee_id_required):
        r"""Sets the is_assignee_id_required of this PostNoteRequiredAttributeDto.

        **参数解释：** 是否勾选指派给。

        :param is_assignee_id_required: The is_assignee_id_required of this PostNoteRequiredAttributeDto.
        :type is_assignee_id_required: bool
        """
        self._is_assignee_id_required = is_assignee_id_required

    @property
    def is_review_categories_required(self):
        r"""Gets the is_review_categories_required of this PostNoteRequiredAttributeDto.

        **参数解释：** 是否勾选意见分类。

        :return: The is_review_categories_required of this PostNoteRequiredAttributeDto.
        :rtype: bool
        """
        return self._is_review_categories_required

    @is_review_categories_required.setter
    def is_review_categories_required(self, is_review_categories_required):
        r"""Sets the is_review_categories_required of this PostNoteRequiredAttributeDto.

        **参数解释：** 是否勾选意见分类。

        :param is_review_categories_required: The is_review_categories_required of this PostNoteRequiredAttributeDto.
        :type is_review_categories_required: bool
        """
        self._is_review_categories_required = is_review_categories_required

    @property
    def is_review_modules_required(self):
        r"""Gets the is_review_modules_required of this PostNoteRequiredAttributeDto.

        **参数解释：** 是否勾选意见模块。

        :return: The is_review_modules_required of this PostNoteRequiredAttributeDto.
        :rtype: bool
        """
        return self._is_review_modules_required

    @is_review_modules_required.setter
    def is_review_modules_required(self, is_review_modules_required):
        r"""Sets the is_review_modules_required of this PostNoteRequiredAttributeDto.

        **参数解释：** 是否勾选意见模块。

        :param is_review_modules_required: The is_review_modules_required of this PostNoteRequiredAttributeDto.
        :type is_review_modules_required: bool
        """
        self._is_review_modules_required = is_review_modules_required

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
        if not isinstance(other, PostNoteRequiredAttributeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
