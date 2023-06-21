# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAimTemplateMaterialResponseMode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'material_id': 'str',
        'aim_resource_id': 'str'
    }

    attribute_map = {
        'material_id': 'material_id',
        'aim_resource_id': 'aim_resource_id'
    }

    def __init__(self, material_id=None, aim_resource_id=None):
        """UploadAimTemplateMaterialResponseMode

        The model defined in huaweicloud sdk

        :param material_id: 模板素材ID。
        :type material_id: str
        :param aim_resource_id: 资源ID。
        :type aim_resource_id: str
        """
        
        

        self._material_id = None
        self._aim_resource_id = None
        self.discriminator = None

        if material_id is not None:
            self.material_id = material_id
        if aim_resource_id is not None:
            self.aim_resource_id = aim_resource_id

    @property
    def material_id(self):
        """Gets the material_id of this UploadAimTemplateMaterialResponseMode.

        模板素材ID。

        :return: The material_id of this UploadAimTemplateMaterialResponseMode.
        :rtype: str
        """
        return self._material_id

    @material_id.setter
    def material_id(self, material_id):
        """Sets the material_id of this UploadAimTemplateMaterialResponseMode.

        模板素材ID。

        :param material_id: The material_id of this UploadAimTemplateMaterialResponseMode.
        :type material_id: str
        """
        self._material_id = material_id

    @property
    def aim_resource_id(self):
        """Gets the aim_resource_id of this UploadAimTemplateMaterialResponseMode.

        资源ID。

        :return: The aim_resource_id of this UploadAimTemplateMaterialResponseMode.
        :rtype: str
        """
        return self._aim_resource_id

    @aim_resource_id.setter
    def aim_resource_id(self, aim_resource_id):
        """Sets the aim_resource_id of this UploadAimTemplateMaterialResponseMode.

        资源ID。

        :param aim_resource_id: The aim_resource_id of this UploadAimTemplateMaterialResponseMode.
        :type aim_resource_id: str
        """
        self._aim_resource_id = aim_resource_id

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
        if not isinstance(other, UploadAimTemplateMaterialResponseMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
