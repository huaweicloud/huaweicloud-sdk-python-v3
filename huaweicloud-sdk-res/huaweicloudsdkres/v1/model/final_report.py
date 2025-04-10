# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FinalReport:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'generated_time': 'str',
        'wide_table_num': 'int',
        'user_complete_degree': 'float',
        'item_complete_degree': 'float',
        'bhv_count': 'dict(str, int)',
        'user_long_feature_report': 'list[NumFeatureReport]',
        'user_float_feature_report': 'list[NumFeatureReport]',
        'user_str_feature_report': 'list[StrFeatureReport]',
        'user_str_array_feature_report': 'list[StrFeatureReport]',
        'item_long_feature_report': 'list[NumFeatureReport]',
        'item_float_feature_report': 'list[NumFeatureReport]',
        'item_str_feature_report': 'list[StrFeatureReport]',
        'item_str_array_feature_report': 'list[StrFeatureReport]'
    }

    attribute_map = {
        'generated_time': 'generated_time',
        'wide_table_num': 'wide_table_num',
        'user_complete_degree': 'user_complete_degree',
        'item_complete_degree': 'item_complete_degree',
        'bhv_count': 'bhv_count',
        'user_long_feature_report': 'user_long_feature_report',
        'user_float_feature_report': 'user_float_feature_report',
        'user_str_feature_report': 'user_str_feature_report',
        'user_str_array_feature_report': 'user_strArray_feature_report',
        'item_long_feature_report': 'item_long_feature_report',
        'item_float_feature_report': 'item_float_feature_report',
        'item_str_feature_report': 'item_str_feature_report',
        'item_str_array_feature_report': 'item_strArray_feature_report'
    }

    def __init__(self, generated_time=None, wide_table_num=None, user_complete_degree=None, item_complete_degree=None, bhv_count=None, user_long_feature_report=None, user_float_feature_report=None, user_str_feature_report=None, user_str_array_feature_report=None, item_long_feature_report=None, item_float_feature_report=None, item_str_feature_report=None, item_str_array_feature_report=None):
        r"""FinalReport

        The model defined in huaweicloud sdk

        :param generated_time: 报告生成时间。
        :type generated_time: str
        :param wide_table_num: 宽表条目数，行为数据去重以后的数目。
        :type wide_table_num: int
        :param user_complete_degree: 用户齐全度，一条行为中的用户是否在产生这条行为的时候拥有画像。
        :type user_complete_degree: float
        :param item_complete_degree: 物品齐全度，一条行为中的物品是否在这条行为产生的时候拥有画像。
        :type item_complete_degree: float
        :param bhv_count: 行为次数统计。
        :type bhv_count: dict(str, int)
        :param user_long_feature_report: 用户数字类型特征统计。
        :type user_long_feature_report: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        :param user_float_feature_report: 用户连续类型特征统计。
        :type user_float_feature_report: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        :param user_str_feature_report: 用户单值离散值类型特征统计。
        :type user_str_feature_report: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        :param user_str_array_feature_report: 用户多值离散值类型特征统计。
        :type user_str_array_feature_report: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        :param item_long_feature_report: 物品数字类型特征统计。
        :type item_long_feature_report: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        :param item_float_feature_report: 物品连续类型特征统计。
        :type item_float_feature_report: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        :param item_str_feature_report: 物品单值离散值类型特征统计。
        :type item_str_feature_report: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        :param item_str_array_feature_report: 物品多值离散值类型特征统计。
        :type item_str_array_feature_report: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        """
        
        

        self._generated_time = None
        self._wide_table_num = None
        self._user_complete_degree = None
        self._item_complete_degree = None
        self._bhv_count = None
        self._user_long_feature_report = None
        self._user_float_feature_report = None
        self._user_str_feature_report = None
        self._user_str_array_feature_report = None
        self._item_long_feature_report = None
        self._item_float_feature_report = None
        self._item_str_feature_report = None
        self._item_str_array_feature_report = None
        self.discriminator = None

        if generated_time is not None:
            self.generated_time = generated_time
        if wide_table_num is not None:
            self.wide_table_num = wide_table_num
        if user_complete_degree is not None:
            self.user_complete_degree = user_complete_degree
        if item_complete_degree is not None:
            self.item_complete_degree = item_complete_degree
        if bhv_count is not None:
            self.bhv_count = bhv_count
        if user_long_feature_report is not None:
            self.user_long_feature_report = user_long_feature_report
        if user_float_feature_report is not None:
            self.user_float_feature_report = user_float_feature_report
        if user_str_feature_report is not None:
            self.user_str_feature_report = user_str_feature_report
        if user_str_array_feature_report is not None:
            self.user_str_array_feature_report = user_str_array_feature_report
        if item_long_feature_report is not None:
            self.item_long_feature_report = item_long_feature_report
        if item_float_feature_report is not None:
            self.item_float_feature_report = item_float_feature_report
        if item_str_feature_report is not None:
            self.item_str_feature_report = item_str_feature_report
        if item_str_array_feature_report is not None:
            self.item_str_array_feature_report = item_str_array_feature_report

    @property
    def generated_time(self):
        r"""Gets the generated_time of this FinalReport.

        报告生成时间。

        :return: The generated_time of this FinalReport.
        :rtype: str
        """
        return self._generated_time

    @generated_time.setter
    def generated_time(self, generated_time):
        r"""Sets the generated_time of this FinalReport.

        报告生成时间。

        :param generated_time: The generated_time of this FinalReport.
        :type generated_time: str
        """
        self._generated_time = generated_time

    @property
    def wide_table_num(self):
        r"""Gets the wide_table_num of this FinalReport.

        宽表条目数，行为数据去重以后的数目。

        :return: The wide_table_num of this FinalReport.
        :rtype: int
        """
        return self._wide_table_num

    @wide_table_num.setter
    def wide_table_num(self, wide_table_num):
        r"""Sets the wide_table_num of this FinalReport.

        宽表条目数，行为数据去重以后的数目。

        :param wide_table_num: The wide_table_num of this FinalReport.
        :type wide_table_num: int
        """
        self._wide_table_num = wide_table_num

    @property
    def user_complete_degree(self):
        r"""Gets the user_complete_degree of this FinalReport.

        用户齐全度，一条行为中的用户是否在产生这条行为的时候拥有画像。

        :return: The user_complete_degree of this FinalReport.
        :rtype: float
        """
        return self._user_complete_degree

    @user_complete_degree.setter
    def user_complete_degree(self, user_complete_degree):
        r"""Sets the user_complete_degree of this FinalReport.

        用户齐全度，一条行为中的用户是否在产生这条行为的时候拥有画像。

        :param user_complete_degree: The user_complete_degree of this FinalReport.
        :type user_complete_degree: float
        """
        self._user_complete_degree = user_complete_degree

    @property
    def item_complete_degree(self):
        r"""Gets the item_complete_degree of this FinalReport.

        物品齐全度，一条行为中的物品是否在这条行为产生的时候拥有画像。

        :return: The item_complete_degree of this FinalReport.
        :rtype: float
        """
        return self._item_complete_degree

    @item_complete_degree.setter
    def item_complete_degree(self, item_complete_degree):
        r"""Sets the item_complete_degree of this FinalReport.

        物品齐全度，一条行为中的物品是否在这条行为产生的时候拥有画像。

        :param item_complete_degree: The item_complete_degree of this FinalReport.
        :type item_complete_degree: float
        """
        self._item_complete_degree = item_complete_degree

    @property
    def bhv_count(self):
        r"""Gets the bhv_count of this FinalReport.

        行为次数统计。

        :return: The bhv_count of this FinalReport.
        :rtype: dict(str, int)
        """
        return self._bhv_count

    @bhv_count.setter
    def bhv_count(self, bhv_count):
        r"""Sets the bhv_count of this FinalReport.

        行为次数统计。

        :param bhv_count: The bhv_count of this FinalReport.
        :type bhv_count: dict(str, int)
        """
        self._bhv_count = bhv_count

    @property
    def user_long_feature_report(self):
        r"""Gets the user_long_feature_report of this FinalReport.

        用户数字类型特征统计。

        :return: The user_long_feature_report of this FinalReport.
        :rtype: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        """
        return self._user_long_feature_report

    @user_long_feature_report.setter
    def user_long_feature_report(self, user_long_feature_report):
        r"""Sets the user_long_feature_report of this FinalReport.

        用户数字类型特征统计。

        :param user_long_feature_report: The user_long_feature_report of this FinalReport.
        :type user_long_feature_report: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        """
        self._user_long_feature_report = user_long_feature_report

    @property
    def user_float_feature_report(self):
        r"""Gets the user_float_feature_report of this FinalReport.

        用户连续类型特征统计。

        :return: The user_float_feature_report of this FinalReport.
        :rtype: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        """
        return self._user_float_feature_report

    @user_float_feature_report.setter
    def user_float_feature_report(self, user_float_feature_report):
        r"""Sets the user_float_feature_report of this FinalReport.

        用户连续类型特征统计。

        :param user_float_feature_report: The user_float_feature_report of this FinalReport.
        :type user_float_feature_report: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        """
        self._user_float_feature_report = user_float_feature_report

    @property
    def user_str_feature_report(self):
        r"""Gets the user_str_feature_report of this FinalReport.

        用户单值离散值类型特征统计。

        :return: The user_str_feature_report of this FinalReport.
        :rtype: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        """
        return self._user_str_feature_report

    @user_str_feature_report.setter
    def user_str_feature_report(self, user_str_feature_report):
        r"""Sets the user_str_feature_report of this FinalReport.

        用户单值离散值类型特征统计。

        :param user_str_feature_report: The user_str_feature_report of this FinalReport.
        :type user_str_feature_report: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        """
        self._user_str_feature_report = user_str_feature_report

    @property
    def user_str_array_feature_report(self):
        r"""Gets the user_str_array_feature_report of this FinalReport.

        用户多值离散值类型特征统计。

        :return: The user_str_array_feature_report of this FinalReport.
        :rtype: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        """
        return self._user_str_array_feature_report

    @user_str_array_feature_report.setter
    def user_str_array_feature_report(self, user_str_array_feature_report):
        r"""Sets the user_str_array_feature_report of this FinalReport.

        用户多值离散值类型特征统计。

        :param user_str_array_feature_report: The user_str_array_feature_report of this FinalReport.
        :type user_str_array_feature_report: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        """
        self._user_str_array_feature_report = user_str_array_feature_report

    @property
    def item_long_feature_report(self):
        r"""Gets the item_long_feature_report of this FinalReport.

        物品数字类型特征统计。

        :return: The item_long_feature_report of this FinalReport.
        :rtype: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        """
        return self._item_long_feature_report

    @item_long_feature_report.setter
    def item_long_feature_report(self, item_long_feature_report):
        r"""Sets the item_long_feature_report of this FinalReport.

        物品数字类型特征统计。

        :param item_long_feature_report: The item_long_feature_report of this FinalReport.
        :type item_long_feature_report: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        """
        self._item_long_feature_report = item_long_feature_report

    @property
    def item_float_feature_report(self):
        r"""Gets the item_float_feature_report of this FinalReport.

        物品连续类型特征统计。

        :return: The item_float_feature_report of this FinalReport.
        :rtype: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        """
        return self._item_float_feature_report

    @item_float_feature_report.setter
    def item_float_feature_report(self, item_float_feature_report):
        r"""Sets the item_float_feature_report of this FinalReport.

        物品连续类型特征统计。

        :param item_float_feature_report: The item_float_feature_report of this FinalReport.
        :type item_float_feature_report: list[:class:`huaweicloudsdkres.v1.NumFeatureReport`]
        """
        self._item_float_feature_report = item_float_feature_report

    @property
    def item_str_feature_report(self):
        r"""Gets the item_str_feature_report of this FinalReport.

        物品单值离散值类型特征统计。

        :return: The item_str_feature_report of this FinalReport.
        :rtype: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        """
        return self._item_str_feature_report

    @item_str_feature_report.setter
    def item_str_feature_report(self, item_str_feature_report):
        r"""Sets the item_str_feature_report of this FinalReport.

        物品单值离散值类型特征统计。

        :param item_str_feature_report: The item_str_feature_report of this FinalReport.
        :type item_str_feature_report: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        """
        self._item_str_feature_report = item_str_feature_report

    @property
    def item_str_array_feature_report(self):
        r"""Gets the item_str_array_feature_report of this FinalReport.

        物品多值离散值类型特征统计。

        :return: The item_str_array_feature_report of this FinalReport.
        :rtype: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        """
        return self._item_str_array_feature_report

    @item_str_array_feature_report.setter
    def item_str_array_feature_report(self, item_str_array_feature_report):
        r"""Sets the item_str_array_feature_report of this FinalReport.

        物品多值离散值类型特征统计。

        :param item_str_array_feature_report: The item_str_array_feature_report of this FinalReport.
        :type item_str_array_feature_report: list[:class:`huaweicloudsdkres.v1.StrFeatureReport`]
        """
        self._item_str_array_feature_report = item_str_array_feature_report

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
        if not isinstance(other, FinalReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
