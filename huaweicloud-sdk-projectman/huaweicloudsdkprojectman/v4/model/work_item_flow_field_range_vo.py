# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemFlowFieldRangeVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'setting_val_object': 'list[dict(str, object)]'
    }

    attribute_map = {
        'setting_val_object': 'setting_val_object'
    }

    def __init__(self, setting_val_object=None):
        r"""WorkItemFlowFieldRangeVO

        The model defined in huaweicloud sdk

        :param setting_val_object: 可选值对象列表
        :type setting_val_object: list[dict(str, object)]
        """
        
        

        self._setting_val_object = None
        self.discriminator = None

        if setting_val_object is not None:
            self.setting_val_object = setting_val_object

    @property
    def setting_val_object(self):
        r"""Gets the setting_val_object of this WorkItemFlowFieldRangeVO.

        可选值对象列表

        :return: The setting_val_object of this WorkItemFlowFieldRangeVO.
        :rtype: list[dict(str, object)]
        """
        return self._setting_val_object

    @setting_val_object.setter
    def setting_val_object(self, setting_val_object):
        r"""Sets the setting_val_object of this WorkItemFlowFieldRangeVO.

        可选值对象列表

        :param setting_val_object: The setting_val_object of this WorkItemFlowFieldRangeVO.
        :type setting_val_object: list[dict(str, object)]
        """
        self._setting_val_object = setting_val_object

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
        if not isinstance(other, WorkItemFlowFieldRangeVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
