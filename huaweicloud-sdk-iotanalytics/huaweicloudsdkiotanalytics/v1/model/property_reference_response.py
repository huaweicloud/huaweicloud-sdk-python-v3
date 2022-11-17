# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PropertyReferenceResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'asset_model_id': 'str',
        'asset_model_name': 'str',
        'property_name': 'str',
        'asset_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'asset_model_id': 'asset_model_id',
        'asset_model_name': 'asset_model_name',
        'property_name': 'property_name',
        'asset_id': 'asset_id'
    }

    def __init__(self, type=None, asset_model_id=None, asset_model_name=None, property_name=None, asset_id=None):
        """PropertyReferenceResponse

        The model defined in huaweicloud sdk

        :param type: 属性引用类型，引用本资产属性（this）、引用其他资产属性（single）、引用子资产属性（children）
        :type type: str
        :param asset_model_id: 引用属性所属的资产模型ID，该字段仅当type为“引用其他资产属性”或“引用子资产属性”时有效；使用导入模型和导出模型接口时，该字段无效
        :type asset_model_id: str
        :param asset_model_name: 引用属性所属的资产模型名称，请求中携带该字段时可以不携带asset_model_id字段
        :type asset_model_name: str
        :param property_name: 引用属性的名称
        :type property_name: str
        :param asset_id: 引用的资产ID，修改资产时携带null表示置空
        :type asset_id: str
        """
        
        

        self._type = None
        self._asset_model_id = None
        self._asset_model_name = None
        self._property_name = None
        self._asset_id = None
        self.discriminator = None

        self.type = type
        if asset_model_id is not None:
            self.asset_model_id = asset_model_id
        if asset_model_name is not None:
            self.asset_model_name = asset_model_name
        self.property_name = property_name
        if asset_id is not None:
            self.asset_id = asset_id

    @property
    def type(self):
        """Gets the type of this PropertyReferenceResponse.

        属性引用类型，引用本资产属性（this）、引用其他资产属性（single）、引用子资产属性（children）

        :return: The type of this PropertyReferenceResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PropertyReferenceResponse.

        属性引用类型，引用本资产属性（this）、引用其他资产属性（single）、引用子资产属性（children）

        :param type: The type of this PropertyReferenceResponse.
        :type type: str
        """
        self._type = type

    @property
    def asset_model_id(self):
        """Gets the asset_model_id of this PropertyReferenceResponse.

        引用属性所属的资产模型ID，该字段仅当type为“引用其他资产属性”或“引用子资产属性”时有效；使用导入模型和导出模型接口时，该字段无效

        :return: The asset_model_id of this PropertyReferenceResponse.
        :rtype: str
        """
        return self._asset_model_id

    @asset_model_id.setter
    def asset_model_id(self, asset_model_id):
        """Sets the asset_model_id of this PropertyReferenceResponse.

        引用属性所属的资产模型ID，该字段仅当type为“引用其他资产属性”或“引用子资产属性”时有效；使用导入模型和导出模型接口时，该字段无效

        :param asset_model_id: The asset_model_id of this PropertyReferenceResponse.
        :type asset_model_id: str
        """
        self._asset_model_id = asset_model_id

    @property
    def asset_model_name(self):
        """Gets the asset_model_name of this PropertyReferenceResponse.

        引用属性所属的资产模型名称，请求中携带该字段时可以不携带asset_model_id字段

        :return: The asset_model_name of this PropertyReferenceResponse.
        :rtype: str
        """
        return self._asset_model_name

    @asset_model_name.setter
    def asset_model_name(self, asset_model_name):
        """Sets the asset_model_name of this PropertyReferenceResponse.

        引用属性所属的资产模型名称，请求中携带该字段时可以不携带asset_model_id字段

        :param asset_model_name: The asset_model_name of this PropertyReferenceResponse.
        :type asset_model_name: str
        """
        self._asset_model_name = asset_model_name

    @property
    def property_name(self):
        """Gets the property_name of this PropertyReferenceResponse.

        引用属性的名称

        :return: The property_name of this PropertyReferenceResponse.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this PropertyReferenceResponse.

        引用属性的名称

        :param property_name: The property_name of this PropertyReferenceResponse.
        :type property_name: str
        """
        self._property_name = property_name

    @property
    def asset_id(self):
        """Gets the asset_id of this PropertyReferenceResponse.

        引用的资产ID，修改资产时携带null表示置空

        :return: The asset_id of this PropertyReferenceResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this PropertyReferenceResponse.

        引用的资产ID，修改资产时携带null表示置空

        :param asset_id: The asset_id of this PropertyReferenceResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

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
        if not isinstance(other, PropertyReferenceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
