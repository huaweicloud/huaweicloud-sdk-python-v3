# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StyleExtraMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'picture_modeling_enable': 'bool',
        'edit_enable': 'bool',
        'edit_engine': 'str',
        'edit_value_items': 'dict(str, StyleExtraMetaEditValueItems)',
        'edit_color_items': 'dict(str, StyleExtraMetaEditColorItems)',
        'edit_components': 'dict(str, StyleExtraMetaEditComponents)',
        'modelling_algorithm': 'dict(str, StyleExtraMetaModellingAlgorithm)'
    }

    attribute_map = {
        'picture_modeling_enable': 'picture_modeling_enable',
        'edit_enable': 'edit_enable',
        'edit_engine': 'edit_engine',
        'edit_value_items': 'edit_value_items',
        'edit_color_items': 'edit_color_items',
        'edit_components': 'edit_components',
        'modelling_algorithm': 'modelling_algorithm'
    }

    def __init__(self, picture_modeling_enable=None, edit_enable=None, edit_engine=None, edit_value_items=None, edit_color_items=None, edit_components=None, modelling_algorithm=None):
        """StyleExtraMeta

        The model defined in huaweicloud sdk

        :param picture_modeling_enable: 是否支持照片建模
        :type picture_modeling_enable: bool
        :param edit_enable: 是否支持模型编辑
        :type edit_enable: bool
        :param edit_engine: 编辑使用引擎
        :type edit_engine: str
        :param edit_value_items: 值可设置条目列表
        :type edit_value_items: dict(str, StyleExtraMetaEditValueItems)
        :param edit_color_items: 颜色可设置条目列表
        :type edit_color_items: dict(str, StyleExtraMetaEditColorItems)
        :param edit_components: 可替换组件列表
        :type edit_components: dict(str, StyleExtraMetaEditComponents)
        :param modelling_algorithm: 
        :type modelling_algorithm: dict(str, StyleExtraMetaModellingAlgorithm)
        """
        
        

        self._picture_modeling_enable = None
        self._edit_enable = None
        self._edit_engine = None
        self._edit_value_items = None
        self._edit_color_items = None
        self._edit_components = None
        self._modelling_algorithm = None
        self.discriminator = None

        if picture_modeling_enable is not None:
            self.picture_modeling_enable = picture_modeling_enable
        if edit_enable is not None:
            self.edit_enable = edit_enable
        if edit_engine is not None:
            self.edit_engine = edit_engine
        if edit_value_items is not None:
            self.edit_value_items = edit_value_items
        if edit_color_items is not None:
            self.edit_color_items = edit_color_items
        if edit_components is not None:
            self.edit_components = edit_components
        if modelling_algorithm is not None:
            self.modelling_algorithm = modelling_algorithm

    @property
    def picture_modeling_enable(self):
        """Gets the picture_modeling_enable of this StyleExtraMeta.

        是否支持照片建模

        :return: The picture_modeling_enable of this StyleExtraMeta.
        :rtype: bool
        """
        return self._picture_modeling_enable

    @picture_modeling_enable.setter
    def picture_modeling_enable(self, picture_modeling_enable):
        """Sets the picture_modeling_enable of this StyleExtraMeta.

        是否支持照片建模

        :param picture_modeling_enable: The picture_modeling_enable of this StyleExtraMeta.
        :type picture_modeling_enable: bool
        """
        self._picture_modeling_enable = picture_modeling_enable

    @property
    def edit_enable(self):
        """Gets the edit_enable of this StyleExtraMeta.

        是否支持模型编辑

        :return: The edit_enable of this StyleExtraMeta.
        :rtype: bool
        """
        return self._edit_enable

    @edit_enable.setter
    def edit_enable(self, edit_enable):
        """Sets the edit_enable of this StyleExtraMeta.

        是否支持模型编辑

        :param edit_enable: The edit_enable of this StyleExtraMeta.
        :type edit_enable: bool
        """
        self._edit_enable = edit_enable

    @property
    def edit_engine(self):
        """Gets the edit_engine of this StyleExtraMeta.

        编辑使用引擎

        :return: The edit_engine of this StyleExtraMeta.
        :rtype: str
        """
        return self._edit_engine

    @edit_engine.setter
    def edit_engine(self, edit_engine):
        """Sets the edit_engine of this StyleExtraMeta.

        编辑使用引擎

        :param edit_engine: The edit_engine of this StyleExtraMeta.
        :type edit_engine: str
        """
        self._edit_engine = edit_engine

    @property
    def edit_value_items(self):
        """Gets the edit_value_items of this StyleExtraMeta.

        值可设置条目列表

        :return: The edit_value_items of this StyleExtraMeta.
        :rtype: dict(str, StyleExtraMetaEditValueItems)
        """
        return self._edit_value_items

    @edit_value_items.setter
    def edit_value_items(self, edit_value_items):
        """Sets the edit_value_items of this StyleExtraMeta.

        值可设置条目列表

        :param edit_value_items: The edit_value_items of this StyleExtraMeta.
        :type edit_value_items: dict(str, StyleExtraMetaEditValueItems)
        """
        self._edit_value_items = edit_value_items

    @property
    def edit_color_items(self):
        """Gets the edit_color_items of this StyleExtraMeta.

        颜色可设置条目列表

        :return: The edit_color_items of this StyleExtraMeta.
        :rtype: dict(str, StyleExtraMetaEditColorItems)
        """
        return self._edit_color_items

    @edit_color_items.setter
    def edit_color_items(self, edit_color_items):
        """Sets the edit_color_items of this StyleExtraMeta.

        颜色可设置条目列表

        :param edit_color_items: The edit_color_items of this StyleExtraMeta.
        :type edit_color_items: dict(str, StyleExtraMetaEditColorItems)
        """
        self._edit_color_items = edit_color_items

    @property
    def edit_components(self):
        """Gets the edit_components of this StyleExtraMeta.

        可替换组件列表

        :return: The edit_components of this StyleExtraMeta.
        :rtype: dict(str, StyleExtraMetaEditComponents)
        """
        return self._edit_components

    @edit_components.setter
    def edit_components(self, edit_components):
        """Sets the edit_components of this StyleExtraMeta.

        可替换组件列表

        :param edit_components: The edit_components of this StyleExtraMeta.
        :type edit_components: dict(str, StyleExtraMetaEditComponents)
        """
        self._edit_components = edit_components

    @property
    def modelling_algorithm(self):
        """Gets the modelling_algorithm of this StyleExtraMeta.

        :return: The modelling_algorithm of this StyleExtraMeta.
        :rtype: dict(str, StyleExtraMetaModellingAlgorithm)
        """
        return self._modelling_algorithm

    @modelling_algorithm.setter
    def modelling_algorithm(self, modelling_algorithm):
        """Sets the modelling_algorithm of this StyleExtraMeta.

        :param modelling_algorithm: The modelling_algorithm of this StyleExtraMeta.
        :type modelling_algorithm: dict(str, StyleExtraMetaModellingAlgorithm)
        """
        self._modelling_algorithm = modelling_algorithm

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
        if not isinstance(other, StyleExtraMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
