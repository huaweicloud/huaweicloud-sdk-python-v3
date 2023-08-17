# coding: utf-8

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
        'model_id': 'str'
    }

    attribute_map = {
        'picture_modeling_enable': 'picture_modeling_enable',
        'edit_enable': 'edit_enable',
        'edit_engine': 'edit_engine',
        'model_id': 'model_id'
    }

    def __init__(self, picture_modeling_enable=None, edit_enable=None, edit_engine=None, model_id=None):
        """StyleExtraMeta

        The model defined in huaweicloud sdk

        :param picture_modeling_enable: 是否支持照片建模
        :type picture_modeling_enable: bool
        :param edit_enable: 是否支持模型编辑
        :type edit_enable: bool
        :param edit_engine: 编辑使用引擎
        :type edit_engine: str
        :param model_id: 照片建模算法调用的模型类型
        :type model_id: str
        """
        
        

        self._picture_modeling_enable = None
        self._edit_enable = None
        self._edit_engine = None
        self._model_id = None
        self.discriminator = None

        if picture_modeling_enable is not None:
            self.picture_modeling_enable = picture_modeling_enable
        if edit_enable is not None:
            self.edit_enable = edit_enable
        if edit_engine is not None:
            self.edit_engine = edit_engine
        if model_id is not None:
            self.model_id = model_id

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
    def model_id(self):
        """Gets the model_id of this StyleExtraMeta.

        照片建模算法调用的模型类型

        :return: The model_id of this StyleExtraMeta.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this StyleExtraMeta.

        照片建模算法调用的模型类型

        :param model_id: The model_id of this StyleExtraMeta.
        :type model_id: str
        """
        self._model_id = model_id

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
