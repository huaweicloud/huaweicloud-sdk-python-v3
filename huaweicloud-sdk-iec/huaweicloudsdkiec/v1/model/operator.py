# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Operator:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'i18n_name': 'str',
        'sa': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'i18n_name': 'i18n_name',
        'sa': 'sa'
    }

    def __init__(self, id=None, name=None, i18n_name=None, sa=None):
        """Operator

        The model defined in huaweicloud sdk

        :param id: 运营商ID。
        :type id: str
        :param name: 运营商名称。  取值范围： - chinamobile：中国移动； - chinaunicom：中国联通； - chinatelecom：中国电信。
        :type name: str
        :param i18n_name: 运营商国际化名称。
        :type i18n_name: str
        :param sa: 运营商的简写。
        :type sa: str
        """
        
        

        self._id = None
        self._name = None
        self._i18n_name = None
        self._sa = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if i18n_name is not None:
            self.i18n_name = i18n_name
        if sa is not None:
            self.sa = sa

    @property
    def id(self):
        """Gets the id of this Operator.

        运营商ID。

        :return: The id of this Operator.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Operator.

        运营商ID。

        :param id: The id of this Operator.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Operator.

        运营商名称。  取值范围： - chinamobile：中国移动； - chinaunicom：中国联通； - chinatelecom：中国电信。

        :return: The name of this Operator.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Operator.

        运营商名称。  取值范围： - chinamobile：中国移动； - chinaunicom：中国联通； - chinatelecom：中国电信。

        :param name: The name of this Operator.
        :type name: str
        """
        self._name = name

    @property
    def i18n_name(self):
        """Gets the i18n_name of this Operator.

        运营商国际化名称。

        :return: The i18n_name of this Operator.
        :rtype: str
        """
        return self._i18n_name

    @i18n_name.setter
    def i18n_name(self, i18n_name):
        """Sets the i18n_name of this Operator.

        运营商国际化名称。

        :param i18n_name: The i18n_name of this Operator.
        :type i18n_name: str
        """
        self._i18n_name = i18n_name

    @property
    def sa(self):
        """Gets the sa of this Operator.

        运营商的简写。

        :return: The sa of this Operator.
        :rtype: str
        """
        return self._sa

    @sa.setter
    def sa(self, sa):
        """Sets the sa of this Operator.

        运营商的简写。

        :param sa: The sa of this Operator.
        :type sa: str
        """
        self._sa = sa

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
        if not isinstance(other, Operator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
