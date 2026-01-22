# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddBlackWhiteListBatchVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'duplicated_list': 'list[BlackWhiteInfo]',
        'failed_list': 'list[BlackWhiteInfo]',
        'success_list': 'list[BlackWhiteInfo]'
    }

    attribute_map = {
        'duplicated_list': 'duplicated_list',
        'failed_list': 'failed_list',
        'success_list': 'success_list'
    }

    def __init__(self, duplicated_list=None, failed_list=None, success_list=None):
        r"""AddBlackWhiteListBatchVO

        The model defined in huaweicloud sdk

        :param duplicated_list: **参数解释**： 黑白名单重复添加列表 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type duplicated_list: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteInfo`]
        :param failed_list: **参数解释**： 黑白名单添加失败列表 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type failed_list: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteInfo`]
        :param success_list: **参数解释**： 黑白名单添加成功列表 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及
        :type success_list: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteInfo`]
        """
        
        

        self._duplicated_list = None
        self._failed_list = None
        self._success_list = None
        self.discriminator = None

        if duplicated_list is not None:
            self.duplicated_list = duplicated_list
        if failed_list is not None:
            self.failed_list = failed_list
        if success_list is not None:
            self.success_list = success_list

    @property
    def duplicated_list(self):
        r"""Gets the duplicated_list of this AddBlackWhiteListBatchVO.

        **参数解释**： 黑白名单重复添加列表 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The duplicated_list of this AddBlackWhiteListBatchVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteInfo`]
        """
        return self._duplicated_list

    @duplicated_list.setter
    def duplicated_list(self, duplicated_list):
        r"""Sets the duplicated_list of this AddBlackWhiteListBatchVO.

        **参数解释**： 黑白名单重复添加列表 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param duplicated_list: The duplicated_list of this AddBlackWhiteListBatchVO.
        :type duplicated_list: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteInfo`]
        """
        self._duplicated_list = duplicated_list

    @property
    def failed_list(self):
        r"""Gets the failed_list of this AddBlackWhiteListBatchVO.

        **参数解释**： 黑白名单添加失败列表 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The failed_list of this AddBlackWhiteListBatchVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteInfo`]
        """
        return self._failed_list

    @failed_list.setter
    def failed_list(self, failed_list):
        r"""Sets the failed_list of this AddBlackWhiteListBatchVO.

        **参数解释**： 黑白名单添加失败列表 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param failed_list: The failed_list of this AddBlackWhiteListBatchVO.
        :type failed_list: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteInfo`]
        """
        self._failed_list = failed_list

    @property
    def success_list(self):
        r"""Gets the success_list of this AddBlackWhiteListBatchVO.

        **参数解释**： 黑白名单添加成功列表 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The success_list of this AddBlackWhiteListBatchVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteInfo`]
        """
        return self._success_list

    @success_list.setter
    def success_list(self, success_list):
        r"""Sets the success_list of this AddBlackWhiteListBatchVO.

        **参数解释**： 黑白名单添加成功列表 **约束限制**： 不涉及  **取值范围**： 不涉及 **默认取值**： 不涉及

        :param success_list: The success_list of this AddBlackWhiteListBatchVO.
        :type success_list: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteInfo`]
        """
        self._success_list = success_list

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddBlackWhiteListBatchVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
