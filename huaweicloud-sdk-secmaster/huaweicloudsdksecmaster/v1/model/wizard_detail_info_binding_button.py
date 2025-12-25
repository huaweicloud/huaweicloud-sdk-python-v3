# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WizardDetailInfoBindingButton:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'button_id': 'str',
        'button_name': 'str'
    }

    attribute_map = {
        'button_id': 'button_id',
        'button_name': 'button_name'
    }

    def __init__(self, button_id=None, button_name=None):
        r"""WizardDetailInfoBindingButton

        The model defined in huaweicloud sdk

        :param button_id: 按钮id
        :type button_id: str
        :param button_name: 按钮名称
        :type button_name: str
        """
        
        

        self._button_id = None
        self._button_name = None
        self.discriminator = None

        self.button_id = button_id
        if button_name is not None:
            self.button_name = button_name

    @property
    def button_id(self):
        r"""Gets the button_id of this WizardDetailInfoBindingButton.

        按钮id

        :return: The button_id of this WizardDetailInfoBindingButton.
        :rtype: str
        """
        return self._button_id

    @button_id.setter
    def button_id(self, button_id):
        r"""Sets the button_id of this WizardDetailInfoBindingButton.

        按钮id

        :param button_id: The button_id of this WizardDetailInfoBindingButton.
        :type button_id: str
        """
        self._button_id = button_id

    @property
    def button_name(self):
        r"""Gets the button_name of this WizardDetailInfoBindingButton.

        按钮名称

        :return: The button_name of this WizardDetailInfoBindingButton.
        :rtype: str
        """
        return self._button_name

    @button_name.setter
    def button_name(self, button_name):
        r"""Sets the button_name of this WizardDetailInfoBindingButton.

        按钮名称

        :param button_name: The button_name of this WizardDetailInfoBindingButton.
        :type button_name: str
        """
        self._button_name = button_name

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
        if not isinstance(other, WizardDetailInfoBindingButton):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
