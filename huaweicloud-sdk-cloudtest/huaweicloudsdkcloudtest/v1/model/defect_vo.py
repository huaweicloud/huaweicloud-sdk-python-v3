# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DefectVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'not_solved': 'int',
        'severity_number_list': 'list[NameAndValueVo]'
    }

    attribute_map = {
        'total': 'total',
        'not_solved': 'not_solved',
        'severity_number_list': 'severity_number_list'
    }

    def __init__(self, total=None, not_solved=None, severity_number_list=None):
        """DefectVo

        The model defined in huaweicloud sdk

        :param total: 缺陷数
        :type total: int
        :param not_solved: 未关闭缺陷数
        :type not_solved: int
        :param severity_number_list: 组装缺陷每种重要程度的名称和对应的数目
        :type severity_number_list: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        
        

        self._total = None
        self._not_solved = None
        self._severity_number_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if not_solved is not None:
            self.not_solved = not_solved
        if severity_number_list is not None:
            self.severity_number_list = severity_number_list

    @property
    def total(self):
        """Gets the total of this DefectVo.

        缺陷数

        :return: The total of this DefectVo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DefectVo.

        缺陷数

        :param total: The total of this DefectVo.
        :type total: int
        """
        self._total = total

    @property
    def not_solved(self):
        """Gets the not_solved of this DefectVo.

        未关闭缺陷数

        :return: The not_solved of this DefectVo.
        :rtype: int
        """
        return self._not_solved

    @not_solved.setter
    def not_solved(self, not_solved):
        """Sets the not_solved of this DefectVo.

        未关闭缺陷数

        :param not_solved: The not_solved of this DefectVo.
        :type not_solved: int
        """
        self._not_solved = not_solved

    @property
    def severity_number_list(self):
        """Gets the severity_number_list of this DefectVo.

        组装缺陷每种重要程度的名称和对应的数目

        :return: The severity_number_list of this DefectVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        return self._severity_number_list

    @severity_number_list.setter
    def severity_number_list(self, severity_number_list):
        """Sets the severity_number_list of this DefectVo.

        组装缺陷每种重要程度的名称和对应的数目

        :param severity_number_list: The severity_number_list of this DefectVo.
        :type severity_number_list: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        self._severity_number_list = severity_number_list

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
        if not isinstance(other, DefectVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
