# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectTypeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_select_all_objects_type': 'bool',
        'objects_type_list': 'list[str]'
    }

    attribute_map = {
        'is_select_all_objects_type': 'is_select_all_objects_type',
        'objects_type_list': 'objects_type_list'
    }

    def __init__(self, is_select_all_objects_type=None, objects_type_list=None):
        """ObjectTypeInfo

        The model defined in huaweicloud sdk

        :param is_select_all_objects_type: 是否选择全部object类型。取值为true时，不包含USER。
        :type is_select_all_objects_type: bool
        :param objects_type_list: 需要评估的object类型列表。is_select_all_objects_type为false时必填。
        :type objects_type_list: list[str]
        """
        
        

        self._is_select_all_objects_type = None
        self._objects_type_list = None
        self.discriminator = None

        self.is_select_all_objects_type = is_select_all_objects_type
        if objects_type_list is not None:
            self.objects_type_list = objects_type_list

    @property
    def is_select_all_objects_type(self):
        """Gets the is_select_all_objects_type of this ObjectTypeInfo.

        是否选择全部object类型。取值为true时，不包含USER。

        :return: The is_select_all_objects_type of this ObjectTypeInfo.
        :rtype: bool
        """
        return self._is_select_all_objects_type

    @is_select_all_objects_type.setter
    def is_select_all_objects_type(self, is_select_all_objects_type):
        """Sets the is_select_all_objects_type of this ObjectTypeInfo.

        是否选择全部object类型。取值为true时，不包含USER。

        :param is_select_all_objects_type: The is_select_all_objects_type of this ObjectTypeInfo.
        :type is_select_all_objects_type: bool
        """
        self._is_select_all_objects_type = is_select_all_objects_type

    @property
    def objects_type_list(self):
        """Gets the objects_type_list of this ObjectTypeInfo.

        需要评估的object类型列表。is_select_all_objects_type为false时必填。

        :return: The objects_type_list of this ObjectTypeInfo.
        :rtype: list[str]
        """
        return self._objects_type_list

    @objects_type_list.setter
    def objects_type_list(self, objects_type_list):
        """Sets the objects_type_list of this ObjectTypeInfo.

        需要评估的object类型列表。is_select_all_objects_type为false时必填。

        :param objects_type_list: The objects_type_list of this ObjectTypeInfo.
        :type objects_type_list: list[str]
        """
        self._objects_type_list = objects_type_list

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
        if not isinstance(other, ObjectTypeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
