# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WizardUpdateRequestPojos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'layout_wizard_update_pojo_list': 'list[WizardUpdateRequestPojo]'
    }

    attribute_map = {
        'layout_wizard_update_pojo_list': 'layout_wizard_update_pojo_list'
    }

    def __init__(self, layout_wizard_update_pojo_list=None):
        r"""WizardUpdateRequestPojos

        The model defined in huaweicloud sdk

        :param layout_wizard_update_pojo_list: 更新页面请求体列表
        :type layout_wizard_update_pojo_list: list[:class:`huaweicloudsdksecmaster.v1.WizardUpdateRequestPojo`]
        """
        
        

        self._layout_wizard_update_pojo_list = None
        self.discriminator = None

        if layout_wizard_update_pojo_list is not None:
            self.layout_wizard_update_pojo_list = layout_wizard_update_pojo_list

    @property
    def layout_wizard_update_pojo_list(self):
        r"""Gets the layout_wizard_update_pojo_list of this WizardUpdateRequestPojos.

        更新页面请求体列表

        :return: The layout_wizard_update_pojo_list of this WizardUpdateRequestPojos.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.WizardUpdateRequestPojo`]
        """
        return self._layout_wizard_update_pojo_list

    @layout_wizard_update_pojo_list.setter
    def layout_wizard_update_pojo_list(self, layout_wizard_update_pojo_list):
        r"""Sets the layout_wizard_update_pojo_list of this WizardUpdateRequestPojos.

        更新页面请求体列表

        :param layout_wizard_update_pojo_list: The layout_wizard_update_pojo_list of this WizardUpdateRequestPojos.
        :type layout_wizard_update_pojo_list: list[:class:`huaweicloudsdksecmaster.v1.WizardUpdateRequestPojo`]
        """
        self._layout_wizard_update_pojo_list = layout_wizard_update_pojo_list

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
        if not isinstance(other, WizardUpdateRequestPojos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
