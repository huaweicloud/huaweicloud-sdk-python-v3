# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SQLStatisticsBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_num': 'int',
        'insert_num': 'int',
        'other_num': 'int',
        'period': 'str',
        'select_num': 'int',
        'update_num': 'int'
    }

    attribute_map = {
        'delete_num': 'delete_num',
        'insert_num': 'insert_num',
        'other_num': 'other_num',
        'period': 'period',
        'select_num': 'select_num',
        'update_num': 'update_num'
    }

    def __init__(self, delete_num=None, insert_num=None, other_num=None, period=None, select_num=None, update_num=None):
        r"""SQLStatisticsBean

        The model defined in huaweicloud sdk

        :param delete_num: 删除数量
        :type delete_num: int
        :param insert_num: 插入数量
        :type insert_num: int
        :param other_num: 其他数量
        :type other_num: int
        :param period: 周期
        :type period: str
        :param select_num: 查询数量
        :type select_num: int
        :param update_num: 更新数量
        :type update_num: int
        """
        
        

        self._delete_num = None
        self._insert_num = None
        self._other_num = None
        self._period = None
        self._select_num = None
        self._update_num = None
        self.discriminator = None

        if delete_num is not None:
            self.delete_num = delete_num
        if insert_num is not None:
            self.insert_num = insert_num
        if other_num is not None:
            self.other_num = other_num
        if period is not None:
            self.period = period
        if select_num is not None:
            self.select_num = select_num
        if update_num is not None:
            self.update_num = update_num

    @property
    def delete_num(self):
        r"""Gets the delete_num of this SQLStatisticsBean.

        删除数量

        :return: The delete_num of this SQLStatisticsBean.
        :rtype: int
        """
        return self._delete_num

    @delete_num.setter
    def delete_num(self, delete_num):
        r"""Sets the delete_num of this SQLStatisticsBean.

        删除数量

        :param delete_num: The delete_num of this SQLStatisticsBean.
        :type delete_num: int
        """
        self._delete_num = delete_num

    @property
    def insert_num(self):
        r"""Gets the insert_num of this SQLStatisticsBean.

        插入数量

        :return: The insert_num of this SQLStatisticsBean.
        :rtype: int
        """
        return self._insert_num

    @insert_num.setter
    def insert_num(self, insert_num):
        r"""Sets the insert_num of this SQLStatisticsBean.

        插入数量

        :param insert_num: The insert_num of this SQLStatisticsBean.
        :type insert_num: int
        """
        self._insert_num = insert_num

    @property
    def other_num(self):
        r"""Gets the other_num of this SQLStatisticsBean.

        其他数量

        :return: The other_num of this SQLStatisticsBean.
        :rtype: int
        """
        return self._other_num

    @other_num.setter
    def other_num(self, other_num):
        r"""Sets the other_num of this SQLStatisticsBean.

        其他数量

        :param other_num: The other_num of this SQLStatisticsBean.
        :type other_num: int
        """
        self._other_num = other_num

    @property
    def period(self):
        r"""Gets the period of this SQLStatisticsBean.

        周期

        :return: The period of this SQLStatisticsBean.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this SQLStatisticsBean.

        周期

        :param period: The period of this SQLStatisticsBean.
        :type period: str
        """
        self._period = period

    @property
    def select_num(self):
        r"""Gets the select_num of this SQLStatisticsBean.

        查询数量

        :return: The select_num of this SQLStatisticsBean.
        :rtype: int
        """
        return self._select_num

    @select_num.setter
    def select_num(self, select_num):
        r"""Sets the select_num of this SQLStatisticsBean.

        查询数量

        :param select_num: The select_num of this SQLStatisticsBean.
        :type select_num: int
        """
        self._select_num = select_num

    @property
    def update_num(self):
        r"""Gets the update_num of this SQLStatisticsBean.

        更新数量

        :return: The update_num of this SQLStatisticsBean.
        :rtype: int
        """
        return self._update_num

    @update_num.setter
    def update_num(self, update_num):
        r"""Sets the update_num of this SQLStatisticsBean.

        更新数量

        :param update_num: The update_num of this SQLStatisticsBean.
        :type update_num: int
        """
        self._update_num = update_num

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
        if not isinstance(other, SQLStatisticsBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
