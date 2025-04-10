# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentSatisfactionV2Do:

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
        'satisfaction_value': 'int',
        'satisfaction_name': 'str',
        'per_value': 'int',
        'sat_category_id': 'str',
        'sat_category_name': 'str'
    }

    attribute_map = {
        'value': 'value',
        'satisfaction_id': 'satisfaction_id',
        'satisfaction_value': 'satisfaction_value',
        'satisfaction_name': 'satisfaction_name',
        'per_value': 'per_value',
        'sat_category_id': 'sat_category_id',
        'sat_category_name': 'sat_category_name'
    }

    def __init__(self, value=None, satisfaction_id=None, satisfaction_value=None, satisfaction_name=None, per_value=None, sat_category_id=None, sat_category_name=None):
        r"""IncidentSatisfactionV2Do

        The model defined in huaweicloud sdk

        :param value: 满意度总分数
        :type value: int
        :param satisfaction_id: 满意度分类id
        :type satisfaction_id: int
        :param satisfaction_value: 满意度的值
        :type satisfaction_value: int
        :param satisfaction_name: 满意度分类名称
        :type satisfaction_name: str
        :param per_value: 每格的分数
        :type per_value: int
        :param sat_category_id: 满意度维度id
        :type sat_category_id: str
        :param sat_category_name: 满意度维度名称
        :type sat_category_name: str
        """
        
        

        self._value = None
        self._satisfaction_id = None
        self._satisfaction_value = None
        self._satisfaction_name = None
        self._per_value = None
        self._sat_category_id = None
        self._sat_category_name = None
        self.discriminator = None

        if value is not None:
            self.value = value
        self.satisfaction_id = satisfaction_id
        self.satisfaction_value = satisfaction_value
        if satisfaction_name is not None:
            self.satisfaction_name = satisfaction_name
        if per_value is not None:
            self.per_value = per_value
        if sat_category_id is not None:
            self.sat_category_id = sat_category_id
        if sat_category_name is not None:
            self.sat_category_name = sat_category_name

    @property
    def value(self):
        r"""Gets the value of this IncidentSatisfactionV2Do.

        满意度总分数

        :return: The value of this IncidentSatisfactionV2Do.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this IncidentSatisfactionV2Do.

        满意度总分数

        :param value: The value of this IncidentSatisfactionV2Do.
        :type value: int
        """
        self._value = value

    @property
    def satisfaction_id(self):
        r"""Gets the satisfaction_id of this IncidentSatisfactionV2Do.

        满意度分类id

        :return: The satisfaction_id of this IncidentSatisfactionV2Do.
        :rtype: int
        """
        return self._satisfaction_id

    @satisfaction_id.setter
    def satisfaction_id(self, satisfaction_id):
        r"""Sets the satisfaction_id of this IncidentSatisfactionV2Do.

        满意度分类id

        :param satisfaction_id: The satisfaction_id of this IncidentSatisfactionV2Do.
        :type satisfaction_id: int
        """
        self._satisfaction_id = satisfaction_id

    @property
    def satisfaction_value(self):
        r"""Gets the satisfaction_value of this IncidentSatisfactionV2Do.

        满意度的值

        :return: The satisfaction_value of this IncidentSatisfactionV2Do.
        :rtype: int
        """
        return self._satisfaction_value

    @satisfaction_value.setter
    def satisfaction_value(self, satisfaction_value):
        r"""Sets the satisfaction_value of this IncidentSatisfactionV2Do.

        满意度的值

        :param satisfaction_value: The satisfaction_value of this IncidentSatisfactionV2Do.
        :type satisfaction_value: int
        """
        self._satisfaction_value = satisfaction_value

    @property
    def satisfaction_name(self):
        r"""Gets the satisfaction_name of this IncidentSatisfactionV2Do.

        满意度分类名称

        :return: The satisfaction_name of this IncidentSatisfactionV2Do.
        :rtype: str
        """
        return self._satisfaction_name

    @satisfaction_name.setter
    def satisfaction_name(self, satisfaction_name):
        r"""Sets the satisfaction_name of this IncidentSatisfactionV2Do.

        满意度分类名称

        :param satisfaction_name: The satisfaction_name of this IncidentSatisfactionV2Do.
        :type satisfaction_name: str
        """
        self._satisfaction_name = satisfaction_name

    @property
    def per_value(self):
        r"""Gets the per_value of this IncidentSatisfactionV2Do.

        每格的分数

        :return: The per_value of this IncidentSatisfactionV2Do.
        :rtype: int
        """
        return self._per_value

    @per_value.setter
    def per_value(self, per_value):
        r"""Sets the per_value of this IncidentSatisfactionV2Do.

        每格的分数

        :param per_value: The per_value of this IncidentSatisfactionV2Do.
        :type per_value: int
        """
        self._per_value = per_value

    @property
    def sat_category_id(self):
        r"""Gets the sat_category_id of this IncidentSatisfactionV2Do.

        满意度维度id

        :return: The sat_category_id of this IncidentSatisfactionV2Do.
        :rtype: str
        """
        return self._sat_category_id

    @sat_category_id.setter
    def sat_category_id(self, sat_category_id):
        r"""Sets the sat_category_id of this IncidentSatisfactionV2Do.

        满意度维度id

        :param sat_category_id: The sat_category_id of this IncidentSatisfactionV2Do.
        :type sat_category_id: str
        """
        self._sat_category_id = sat_category_id

    @property
    def sat_category_name(self):
        r"""Gets the sat_category_name of this IncidentSatisfactionV2Do.

        满意度维度名称

        :return: The sat_category_name of this IncidentSatisfactionV2Do.
        :rtype: str
        """
        return self._sat_category_name

    @sat_category_name.setter
    def sat_category_name(self, sat_category_name):
        r"""Sets the sat_category_name of this IncidentSatisfactionV2Do.

        满意度维度名称

        :param sat_category_name: The sat_category_name of this IncidentSatisfactionV2Do.
        :type sat_category_name: str
        """
        self._sat_category_name = sat_category_name

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
        if not isinstance(other, IncidentSatisfactionV2Do):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
