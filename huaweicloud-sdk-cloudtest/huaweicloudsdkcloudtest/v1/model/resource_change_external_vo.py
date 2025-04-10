# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceChangeExternalVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_name': 'str',
        'custom_field_type': 'str',
        'old_change_info': 'ElementResourceChangeExternalVo',
        'new_change_info': 'ElementResourceChangeExternalVo'
    }

    attribute_map = {
        'field_name': 'field_name',
        'custom_field_type': 'custom_field_type',
        'old_change_info': 'old_change_info',
        'new_change_info': 'new_change_info'
    }

    def __init__(self, field_name=None, custom_field_type=None, old_change_info=None, new_change_info=None):
        r"""ResourceChangeExternalVo

        The model defined in huaweicloud sdk

        :param field_name: 变更字段
        :type field_name: str
        :param custom_field_type: 测试用例自定义字段类型
        :type custom_field_type: str
        :param old_change_info: 
        :type old_change_info: :class:`huaweicloudsdkcloudtest.v1.ElementResourceChangeExternalVo`
        :param new_change_info: 
        :type new_change_info: :class:`huaweicloudsdkcloudtest.v1.ElementResourceChangeExternalVo`
        """
        
        

        self._field_name = None
        self._custom_field_type = None
        self._old_change_info = None
        self._new_change_info = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if custom_field_type is not None:
            self.custom_field_type = custom_field_type
        if old_change_info is not None:
            self.old_change_info = old_change_info
        if new_change_info is not None:
            self.new_change_info = new_change_info

    @property
    def field_name(self):
        r"""Gets the field_name of this ResourceChangeExternalVo.

        变更字段

        :return: The field_name of this ResourceChangeExternalVo.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this ResourceChangeExternalVo.

        变更字段

        :param field_name: The field_name of this ResourceChangeExternalVo.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def custom_field_type(self):
        r"""Gets the custom_field_type of this ResourceChangeExternalVo.

        测试用例自定义字段类型

        :return: The custom_field_type of this ResourceChangeExternalVo.
        :rtype: str
        """
        return self._custom_field_type

    @custom_field_type.setter
    def custom_field_type(self, custom_field_type):
        r"""Sets the custom_field_type of this ResourceChangeExternalVo.

        测试用例自定义字段类型

        :param custom_field_type: The custom_field_type of this ResourceChangeExternalVo.
        :type custom_field_type: str
        """
        self._custom_field_type = custom_field_type

    @property
    def old_change_info(self):
        r"""Gets the old_change_info of this ResourceChangeExternalVo.

        :return: The old_change_info of this ResourceChangeExternalVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ElementResourceChangeExternalVo`
        """
        return self._old_change_info

    @old_change_info.setter
    def old_change_info(self, old_change_info):
        r"""Sets the old_change_info of this ResourceChangeExternalVo.

        :param old_change_info: The old_change_info of this ResourceChangeExternalVo.
        :type old_change_info: :class:`huaweicloudsdkcloudtest.v1.ElementResourceChangeExternalVo`
        """
        self._old_change_info = old_change_info

    @property
    def new_change_info(self):
        r"""Gets the new_change_info of this ResourceChangeExternalVo.

        :return: The new_change_info of this ResourceChangeExternalVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ElementResourceChangeExternalVo`
        """
        return self._new_change_info

    @new_change_info.setter
    def new_change_info(self, new_change_info):
        r"""Sets the new_change_info of this ResourceChangeExternalVo.

        :param new_change_info: The new_change_info of this ResourceChangeExternalVo.
        :type new_change_info: :class:`huaweicloudsdkcloudtest.v1.ElementResourceChangeExternalVo`
        """
        self._new_change_info = new_change_info

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
        if not isinstance(other, ResourceChangeExternalVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
