# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTestCasesChangeStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add_testcases_number': 'int',
        'reuse_testcases_number': 'int',
        'modifying_testcases_number': 'int',
        'update_date_timestamp': 'int',
        'update_date': 'datetime'
    }

    attribute_map = {
        'add_testcases_number': 'add_testcases_number',
        'reuse_testcases_number': 'reuse_testcases_number',
        'modifying_testcases_number': 'modifying_testcases_number',
        'update_date_timestamp': 'update_date_timestamp',
        'update_date': 'update_date'
    }

    def __init__(self, add_testcases_number=None, reuse_testcases_number=None, modifying_testcases_number=None, update_date_timestamp=None, update_date=None):
        """ShowTestCasesChangeStatisticsResponse

        The model defined in huaweicloud sdk

        :param add_testcases_number: 新增用例数
        :type add_testcases_number: int
        :param reuse_testcases_number: 复用用例数
        :type reuse_testcases_number: int
        :param modifying_testcases_number: 修改用例数
        :type modifying_testcases_number: int
        :param update_date_timestamp: 修改时间时间戳
        :type update_date_timestamp: int
        :param update_date: 修改时间
        :type update_date: datetime
        """
        
        super(ShowTestCasesChangeStatisticsResponse, self).__init__()

        self._add_testcases_number = None
        self._reuse_testcases_number = None
        self._modifying_testcases_number = None
        self._update_date_timestamp = None
        self._update_date = None
        self.discriminator = None

        if add_testcases_number is not None:
            self.add_testcases_number = add_testcases_number
        if reuse_testcases_number is not None:
            self.reuse_testcases_number = reuse_testcases_number
        if modifying_testcases_number is not None:
            self.modifying_testcases_number = modifying_testcases_number
        if update_date_timestamp is not None:
            self.update_date_timestamp = update_date_timestamp
        if update_date is not None:
            self.update_date = update_date

    @property
    def add_testcases_number(self):
        """Gets the add_testcases_number of this ShowTestCasesChangeStatisticsResponse.

        新增用例数

        :return: The add_testcases_number of this ShowTestCasesChangeStatisticsResponse.
        :rtype: int
        """
        return self._add_testcases_number

    @add_testcases_number.setter
    def add_testcases_number(self, add_testcases_number):
        """Sets the add_testcases_number of this ShowTestCasesChangeStatisticsResponse.

        新增用例数

        :param add_testcases_number: The add_testcases_number of this ShowTestCasesChangeStatisticsResponse.
        :type add_testcases_number: int
        """
        self._add_testcases_number = add_testcases_number

    @property
    def reuse_testcases_number(self):
        """Gets the reuse_testcases_number of this ShowTestCasesChangeStatisticsResponse.

        复用用例数

        :return: The reuse_testcases_number of this ShowTestCasesChangeStatisticsResponse.
        :rtype: int
        """
        return self._reuse_testcases_number

    @reuse_testcases_number.setter
    def reuse_testcases_number(self, reuse_testcases_number):
        """Sets the reuse_testcases_number of this ShowTestCasesChangeStatisticsResponse.

        复用用例数

        :param reuse_testcases_number: The reuse_testcases_number of this ShowTestCasesChangeStatisticsResponse.
        :type reuse_testcases_number: int
        """
        self._reuse_testcases_number = reuse_testcases_number

    @property
    def modifying_testcases_number(self):
        """Gets the modifying_testcases_number of this ShowTestCasesChangeStatisticsResponse.

        修改用例数

        :return: The modifying_testcases_number of this ShowTestCasesChangeStatisticsResponse.
        :rtype: int
        """
        return self._modifying_testcases_number

    @modifying_testcases_number.setter
    def modifying_testcases_number(self, modifying_testcases_number):
        """Sets the modifying_testcases_number of this ShowTestCasesChangeStatisticsResponse.

        修改用例数

        :param modifying_testcases_number: The modifying_testcases_number of this ShowTestCasesChangeStatisticsResponse.
        :type modifying_testcases_number: int
        """
        self._modifying_testcases_number = modifying_testcases_number

    @property
    def update_date_timestamp(self):
        """Gets the update_date_timestamp of this ShowTestCasesChangeStatisticsResponse.

        修改时间时间戳

        :return: The update_date_timestamp of this ShowTestCasesChangeStatisticsResponse.
        :rtype: int
        """
        return self._update_date_timestamp

    @update_date_timestamp.setter
    def update_date_timestamp(self, update_date_timestamp):
        """Sets the update_date_timestamp of this ShowTestCasesChangeStatisticsResponse.

        修改时间时间戳

        :param update_date_timestamp: The update_date_timestamp of this ShowTestCasesChangeStatisticsResponse.
        :type update_date_timestamp: int
        """
        self._update_date_timestamp = update_date_timestamp

    @property
    def update_date(self):
        """Gets the update_date of this ShowTestCasesChangeStatisticsResponse.

        修改时间

        :return: The update_date of this ShowTestCasesChangeStatisticsResponse.
        :rtype: datetime
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this ShowTestCasesChangeStatisticsResponse.

        修改时间

        :param update_date: The update_date of this ShowTestCasesChangeStatisticsResponse.
        :type update_date: datetime
        """
        self._update_date = update_date

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
        if not isinstance(other, ShowTestCasesChangeStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
