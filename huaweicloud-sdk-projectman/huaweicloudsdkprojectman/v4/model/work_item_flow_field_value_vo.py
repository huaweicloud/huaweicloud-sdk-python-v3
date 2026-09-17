# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemFlowFieldValueVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ref_prop': 'str',
        'setting_val_object': 'list[dict(str, object)]'
    }

    attribute_map = {
        'ref_prop': 'ref_prop',
        'setting_val_object': 'setting_val_object'
    }

    def __init__(self, ref_prop=None, setting_val_object=None):
        r"""WorkItemFlowFieldValueVO

        The model defined in huaweicloud sdk

        :param ref_prop: 引用属性名
        :type ref_prop: str
        :param setting_val_object: 配置值对象列表
        :type setting_val_object: list[dict(str, object)]
        """
        
        

        self._ref_prop = None
        self._setting_val_object = None
        self.discriminator = None

        if ref_prop is not None:
            self.ref_prop = ref_prop
        if setting_val_object is not None:
            self.setting_val_object = setting_val_object

    @property
    def ref_prop(self):
        r"""Gets the ref_prop of this WorkItemFlowFieldValueVO.

        引用属性名

        :return: The ref_prop of this WorkItemFlowFieldValueVO.
        :rtype: str
        """
        return self._ref_prop

    @ref_prop.setter
    def ref_prop(self, ref_prop):
        r"""Sets the ref_prop of this WorkItemFlowFieldValueVO.

        引用属性名

        :param ref_prop: The ref_prop of this WorkItemFlowFieldValueVO.
        :type ref_prop: str
        """
        self._ref_prop = ref_prop

    @property
    def setting_val_object(self):
        r"""Gets the setting_val_object of this WorkItemFlowFieldValueVO.

        配置值对象列表

        :return: The setting_val_object of this WorkItemFlowFieldValueVO.
        :rtype: list[dict(str, object)]
        """
        return self._setting_val_object

    @setting_val_object.setter
    def setting_val_object(self, setting_val_object):
        r"""Sets the setting_val_object of this WorkItemFlowFieldValueVO.

        配置值对象列表

        :param setting_val_object: The setting_val_object of this WorkItemFlowFieldValueVO.
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
        if not isinstance(other, WorkItemFlowFieldValueVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
