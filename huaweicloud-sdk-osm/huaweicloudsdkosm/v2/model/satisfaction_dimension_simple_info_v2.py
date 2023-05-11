# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SatisfactionDimensionSimpleInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'int',
        'satisfaction_id': 'int',
        'satisfaction_name': 'str',
        'satisfaction_desc': 'str',
        'per_value': 'int',
        'sat_category_id': 'str'
    }

    attribute_map = {
        'value': 'value',
        'satisfaction_id': 'satisfaction_id',
        'satisfaction_name': 'satisfaction_name',
        'satisfaction_desc': 'satisfaction_desc',
        'per_value': 'per_value',
        'sat_category_id': 'sat_category_id'
    }

    def __init__(self, value=None, satisfaction_id=None, satisfaction_name=None, satisfaction_desc=None, per_value=None, sat_category_id=None):
        """SatisfactionDimensionSimpleInfoV2

        The model defined in huaweicloud sdk

        :param value: 总的分数
        :type value: int
        :param satisfaction_id: 满意度id
        :type satisfaction_id: int
        :param satisfaction_name: 满意度名称
        :type satisfaction_name: str
        :param satisfaction_desc: 满意度描述
        :type satisfaction_desc: str
        :param per_value: 每格的分数
        :type per_value: int
        :param sat_category_id: 满意度分类id
        :type sat_category_id: str
        """
        
        

        self._value = None
        self._satisfaction_id = None
        self._satisfaction_name = None
        self._satisfaction_desc = None
        self._per_value = None
        self._sat_category_id = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if satisfaction_id is not None:
            self.satisfaction_id = satisfaction_id
        if satisfaction_name is not None:
            self.satisfaction_name = satisfaction_name
        if satisfaction_desc is not None:
            self.satisfaction_desc = satisfaction_desc
        if per_value is not None:
            self.per_value = per_value
        if sat_category_id is not None:
            self.sat_category_id = sat_category_id

    @property
    def value(self):
        """Gets the value of this SatisfactionDimensionSimpleInfoV2.

        总的分数

        :return: The value of this SatisfactionDimensionSimpleInfoV2.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SatisfactionDimensionSimpleInfoV2.

        总的分数

        :param value: The value of this SatisfactionDimensionSimpleInfoV2.
        :type value: int
        """
        self._value = value

    @property
    def satisfaction_id(self):
        """Gets the satisfaction_id of this SatisfactionDimensionSimpleInfoV2.

        满意度id

        :return: The satisfaction_id of this SatisfactionDimensionSimpleInfoV2.
        :rtype: int
        """
        return self._satisfaction_id

    @satisfaction_id.setter
    def satisfaction_id(self, satisfaction_id):
        """Sets the satisfaction_id of this SatisfactionDimensionSimpleInfoV2.

        满意度id

        :param satisfaction_id: The satisfaction_id of this SatisfactionDimensionSimpleInfoV2.
        :type satisfaction_id: int
        """
        self._satisfaction_id = satisfaction_id

    @property
    def satisfaction_name(self):
        """Gets the satisfaction_name of this SatisfactionDimensionSimpleInfoV2.

        满意度名称

        :return: The satisfaction_name of this SatisfactionDimensionSimpleInfoV2.
        :rtype: str
        """
        return self._satisfaction_name

    @satisfaction_name.setter
    def satisfaction_name(self, satisfaction_name):
        """Sets the satisfaction_name of this SatisfactionDimensionSimpleInfoV2.

        满意度名称

        :param satisfaction_name: The satisfaction_name of this SatisfactionDimensionSimpleInfoV2.
        :type satisfaction_name: str
        """
        self._satisfaction_name = satisfaction_name

    @property
    def satisfaction_desc(self):
        """Gets the satisfaction_desc of this SatisfactionDimensionSimpleInfoV2.

        满意度描述

        :return: The satisfaction_desc of this SatisfactionDimensionSimpleInfoV2.
        :rtype: str
        """
        return self._satisfaction_desc

    @satisfaction_desc.setter
    def satisfaction_desc(self, satisfaction_desc):
        """Sets the satisfaction_desc of this SatisfactionDimensionSimpleInfoV2.

        满意度描述

        :param satisfaction_desc: The satisfaction_desc of this SatisfactionDimensionSimpleInfoV2.
        :type satisfaction_desc: str
        """
        self._satisfaction_desc = satisfaction_desc

    @property
    def per_value(self):
        """Gets the per_value of this SatisfactionDimensionSimpleInfoV2.

        每格的分数

        :return: The per_value of this SatisfactionDimensionSimpleInfoV2.
        :rtype: int
        """
        return self._per_value

    @per_value.setter
    def per_value(self, per_value):
        """Sets the per_value of this SatisfactionDimensionSimpleInfoV2.

        每格的分数

        :param per_value: The per_value of this SatisfactionDimensionSimpleInfoV2.
        :type per_value: int
        """
        self._per_value = per_value

    @property
    def sat_category_id(self):
        """Gets the sat_category_id of this SatisfactionDimensionSimpleInfoV2.

        满意度分类id

        :return: The sat_category_id of this SatisfactionDimensionSimpleInfoV2.
        :rtype: str
        """
        return self._sat_category_id

    @sat_category_id.setter
    def sat_category_id(self, sat_category_id):
        """Sets the sat_category_id of this SatisfactionDimensionSimpleInfoV2.

        满意度分类id

        :param sat_category_id: The sat_category_id of this SatisfactionDimensionSimpleInfoV2.
        :type sat_category_id: str
        """
        self._sat_category_id = sat_category_id

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
        if not isinstance(other, SatisfactionDimensionSimpleInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
