# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReconfigureExtDataSourceAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database': 'bool',
        'agency': 'str'
    }

    attribute_map = {
        'database': 'database',
        'agency': 'agency'
    }

    def __init__(self, database=None, agency=None):
        """ReconfigureExtDataSourceAction

        The model defined in huaweicloud sdk

        :param database: 重启。
        :type database: bool
        :param agency: 委托。
        :type agency: str
        """
        
        

        self._database = None
        self._agency = None
        self.discriminator = None

        if database is not None:
            self.database = database
        if agency is not None:
            self.agency = agency

    @property
    def database(self):
        """Gets the database of this ReconfigureExtDataSourceAction.

        重启。

        :return: The database of this ReconfigureExtDataSourceAction.
        :rtype: bool
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ReconfigureExtDataSourceAction.

        重启。

        :param database: The database of this ReconfigureExtDataSourceAction.
        :type database: bool
        """
        self._database = database

    @property
    def agency(self):
        """Gets the agency of this ReconfigureExtDataSourceAction.

        委托。

        :return: The agency of this ReconfigureExtDataSourceAction.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this ReconfigureExtDataSourceAction.

        委托。

        :param agency: The agency of this ReconfigureExtDataSourceAction.
        :type agency: str
        """
        self._agency = agency

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
        if not isinstance(other, ReconfigureExtDataSourceAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
