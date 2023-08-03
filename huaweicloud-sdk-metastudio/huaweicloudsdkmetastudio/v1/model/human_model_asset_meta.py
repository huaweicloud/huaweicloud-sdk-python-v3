# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HumanModelAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'style_id': 'str',
        'modeling_type': 'str',
        'modeling_job_id': 'str',
        'model_properties': 'HumanModelMetaProperties',
        'components': 'list[ComponentInfo]'
    }

    attribute_map = {
        'style_id': 'style_id',
        'modeling_type': 'modeling_type',
        'modeling_job_id': 'modeling_job_id',
        'model_properties': 'model_properties',
        'components': 'components'
    }

    def __init__(self, style_id=None, modeling_type=None, modeling_job_id=None, model_properties=None, components=None):
        """HumanModelAssetMeta

        The model defined in huaweicloud sdk

        :param style_id: 数字人模型风格ID。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02  * system_female_002：女性风格02
        :type style_id: str
        :param modeling_type: 数字人模型建模类型。 * UPLOADED：租户上传的模型 * PICTURE_MODELING：照片建模生成的模型 * CHARACTER_CUSTOMIZATION_MODELING：捏脸生成的模型
        :type modeling_type: str
        :param modeling_job_id: 建模任务ID。
        :type modeling_job_id: str
        :param model_properties: 
        :type model_properties: :class:`huaweicloudsdkmetastudio.v1.HumanModelMetaProperties`
        :param components: 可替换组件列表。
        :type components: list[:class:`huaweicloudsdkmetastudio.v1.ComponentInfo`]
        """
        
        

        self._style_id = None
        self._modeling_type = None
        self._modeling_job_id = None
        self._model_properties = None
        self._components = None
        self.discriminator = None

        if style_id is not None:
            self.style_id = style_id
        if modeling_type is not None:
            self.modeling_type = modeling_type
        if modeling_job_id is not None:
            self.modeling_job_id = modeling_job_id
        if model_properties is not None:
            self.model_properties = model_properties
        if components is not None:
            self.components = components

    @property
    def style_id(self):
        """Gets the style_id of this HumanModelAssetMeta.

        数字人模型风格ID。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02  * system_female_002：女性风格02

        :return: The style_id of this HumanModelAssetMeta.
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        """Sets the style_id of this HumanModelAssetMeta.

        数字人模型风格ID。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02  * system_female_002：女性风格02

        :param style_id: The style_id of this HumanModelAssetMeta.
        :type style_id: str
        """
        self._style_id = style_id

    @property
    def modeling_type(self):
        """Gets the modeling_type of this HumanModelAssetMeta.

        数字人模型建模类型。 * UPLOADED：租户上传的模型 * PICTURE_MODELING：照片建模生成的模型 * CHARACTER_CUSTOMIZATION_MODELING：捏脸生成的模型

        :return: The modeling_type of this HumanModelAssetMeta.
        :rtype: str
        """
        return self._modeling_type

    @modeling_type.setter
    def modeling_type(self, modeling_type):
        """Sets the modeling_type of this HumanModelAssetMeta.

        数字人模型建模类型。 * UPLOADED：租户上传的模型 * PICTURE_MODELING：照片建模生成的模型 * CHARACTER_CUSTOMIZATION_MODELING：捏脸生成的模型

        :param modeling_type: The modeling_type of this HumanModelAssetMeta.
        :type modeling_type: str
        """
        self._modeling_type = modeling_type

    @property
    def modeling_job_id(self):
        """Gets the modeling_job_id of this HumanModelAssetMeta.

        建模任务ID。

        :return: The modeling_job_id of this HumanModelAssetMeta.
        :rtype: str
        """
        return self._modeling_job_id

    @modeling_job_id.setter
    def modeling_job_id(self, modeling_job_id):
        """Sets the modeling_job_id of this HumanModelAssetMeta.

        建模任务ID。

        :param modeling_job_id: The modeling_job_id of this HumanModelAssetMeta.
        :type modeling_job_id: str
        """
        self._modeling_job_id = modeling_job_id

    @property
    def model_properties(self):
        """Gets the model_properties of this HumanModelAssetMeta.

        :return: The model_properties of this HumanModelAssetMeta.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.HumanModelMetaProperties`
        """
        return self._model_properties

    @model_properties.setter
    def model_properties(self, model_properties):
        """Sets the model_properties of this HumanModelAssetMeta.

        :param model_properties: The model_properties of this HumanModelAssetMeta.
        :type model_properties: :class:`huaweicloudsdkmetastudio.v1.HumanModelMetaProperties`
        """
        self._model_properties = model_properties

    @property
    def components(self):
        """Gets the components of this HumanModelAssetMeta.

        可替换组件列表。

        :return: The components of this HumanModelAssetMeta.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ComponentInfo`]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this HumanModelAssetMeta.

        可替换组件列表。

        :param components: The components of this HumanModelAssetMeta.
        :type components: list[:class:`huaweicloudsdkmetastudio.v1.ComponentInfo`]
        """
        self._components = components

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
        if not isinstance(other, HumanModelAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
