# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_id': 'str',
        'new_view_attrs': 'MultiViewModelViewUpdateAttrDTO',
        'need_set_null': 'list[str]'
    }

    attribute_map = {
        'version_id': 'versionId',
        'new_view_attrs': 'newViewAttrs',
        'need_set_null': 'needSetNull'
    }

    def __init__(self, version_id=None, new_view_attrs=None, need_set_null=None):
        r"""VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO

        The model defined in huaweicloud sdk

        :param version_id: **参数解释：**  版本对象ID。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type version_id: str
        :param new_view_attrs: 
        :type new_view_attrs: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewModelViewUpdateAttrDTO`
        :param need_set_null: **参数解释：**  指定不复制的视图属性，其值将被设置为null。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type need_set_null: list[str]
        """
        
        

        self._version_id = None
        self._new_view_attrs = None
        self._need_set_null = None
        self.discriminator = None

        self.version_id = version_id
        self.new_view_attrs = new_view_attrs
        if need_set_null is not None:
            self.need_set_null = need_set_null

    @property
    def version_id(self):
        r"""Gets the version_id of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.

        **参数解释：**  版本对象ID。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The version_id of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.

        **参数解释：**  版本对象ID。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param version_id: The version_id of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def new_view_attrs(self):
        r"""Gets the new_view_attrs of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.

        :return: The new_view_attrs of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewModelViewUpdateAttrDTO`
        """
        return self._new_view_attrs

    @new_view_attrs.setter
    def new_view_attrs(self, new_view_attrs):
        r"""Sets the new_view_attrs of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.

        :param new_view_attrs: The new_view_attrs of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.
        :type new_view_attrs: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewModelViewUpdateAttrDTO`
        """
        self._new_view_attrs = new_view_attrs

    @property
    def need_set_null(self):
        r"""Gets the need_set_null of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.

        **参数解释：**  指定不复制的视图属性，其值将被设置为null。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The need_set_null of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.
        :rtype: list[str]
        """
        return self._need_set_null

    @need_set_null.setter
    def need_set_null(self, need_set_null):
        r"""Sets the need_set_null of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.

        **参数解释：**  指定不复制的视图属性，其值将被设置为null。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param need_set_null: The need_set_null of this VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.
        :type need_set_null: list[str]
        """
        self._need_set_null = need_set_null

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
        if not isinstance(other, VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
