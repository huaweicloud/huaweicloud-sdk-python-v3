# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class L1Statistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subject_area_group_name': 'str',
        'subject_area_group_name_en': 'str',
        'subject_area_group_guid': 'str',
        'ordinal': 'int',
        'subject_area_count': 'int',
        'business_object_count': 'int',
        'logic_entity_count': 'int',
        'subject_area_statistics': 'list[L2Statistic]'
    }

    attribute_map = {
        'subject_area_group_name': 'subject_area_group_name',
        'subject_area_group_name_en': 'subject_area_group_name_en',
        'subject_area_group_guid': 'subject_area_group_guid',
        'ordinal': 'ordinal',
        'subject_area_count': 'subject_area_count',
        'business_object_count': 'business_object_count',
        'logic_entity_count': 'logic_entity_count',
        'subject_area_statistics': 'subject_area_statistics'
    }

    def __init__(self, subject_area_group_name=None, subject_area_group_name_en=None, subject_area_group_guid=None, ordinal=None, subject_area_count=None, business_object_count=None, logic_entity_count=None, subject_area_statistics=None):
        """L1Statistic

        The model defined in huaweicloud sdk

        :param subject_area_group_name: 主题域分组名称
        :type subject_area_group_name: str
        :param subject_area_group_name_en: 主题域分组英文名称
        :type subject_area_group_name_en: str
        :param subject_area_group_guid: 主题域分组的guid
        :type subject_area_group_guid: str
        :param ordinal: 主题域分组序号
        :type ordinal: int
        :param subject_area_count: 主题总数
        :type subject_area_count: int
        :param business_object_count: 业务对象总数
        :type business_object_count: int
        :param logic_entity_count: 逻辑实体总数
        :type logic_entity_count: int
        :param subject_area_statistics: 主题统计信息
        :type subject_area_statistics: list[:class:`huaweicloudsdkdataartsstudio.v1.L2Statistic`]
        """
        
        

        self._subject_area_group_name = None
        self._subject_area_group_name_en = None
        self._subject_area_group_guid = None
        self._ordinal = None
        self._subject_area_count = None
        self._business_object_count = None
        self._logic_entity_count = None
        self._subject_area_statistics = None
        self.discriminator = None

        if subject_area_group_name is not None:
            self.subject_area_group_name = subject_area_group_name
        if subject_area_group_name_en is not None:
            self.subject_area_group_name_en = subject_area_group_name_en
        if subject_area_group_guid is not None:
            self.subject_area_group_guid = subject_area_group_guid
        if ordinal is not None:
            self.ordinal = ordinal
        if subject_area_count is not None:
            self.subject_area_count = subject_area_count
        if business_object_count is not None:
            self.business_object_count = business_object_count
        if logic_entity_count is not None:
            self.logic_entity_count = logic_entity_count
        if subject_area_statistics is not None:
            self.subject_area_statistics = subject_area_statistics

    @property
    def subject_area_group_name(self):
        """Gets the subject_area_group_name of this L1Statistic.

        主题域分组名称

        :return: The subject_area_group_name of this L1Statistic.
        :rtype: str
        """
        return self._subject_area_group_name

    @subject_area_group_name.setter
    def subject_area_group_name(self, subject_area_group_name):
        """Sets the subject_area_group_name of this L1Statistic.

        主题域分组名称

        :param subject_area_group_name: The subject_area_group_name of this L1Statistic.
        :type subject_area_group_name: str
        """
        self._subject_area_group_name = subject_area_group_name

    @property
    def subject_area_group_name_en(self):
        """Gets the subject_area_group_name_en of this L1Statistic.

        主题域分组英文名称

        :return: The subject_area_group_name_en of this L1Statistic.
        :rtype: str
        """
        return self._subject_area_group_name_en

    @subject_area_group_name_en.setter
    def subject_area_group_name_en(self, subject_area_group_name_en):
        """Sets the subject_area_group_name_en of this L1Statistic.

        主题域分组英文名称

        :param subject_area_group_name_en: The subject_area_group_name_en of this L1Statistic.
        :type subject_area_group_name_en: str
        """
        self._subject_area_group_name_en = subject_area_group_name_en

    @property
    def subject_area_group_guid(self):
        """Gets the subject_area_group_guid of this L1Statistic.

        主题域分组的guid

        :return: The subject_area_group_guid of this L1Statistic.
        :rtype: str
        """
        return self._subject_area_group_guid

    @subject_area_group_guid.setter
    def subject_area_group_guid(self, subject_area_group_guid):
        """Sets the subject_area_group_guid of this L1Statistic.

        主题域分组的guid

        :param subject_area_group_guid: The subject_area_group_guid of this L1Statistic.
        :type subject_area_group_guid: str
        """
        self._subject_area_group_guid = subject_area_group_guid

    @property
    def ordinal(self):
        """Gets the ordinal of this L1Statistic.

        主题域分组序号

        :return: The ordinal of this L1Statistic.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this L1Statistic.

        主题域分组序号

        :param ordinal: The ordinal of this L1Statistic.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def subject_area_count(self):
        """Gets the subject_area_count of this L1Statistic.

        主题总数

        :return: The subject_area_count of this L1Statistic.
        :rtype: int
        """
        return self._subject_area_count

    @subject_area_count.setter
    def subject_area_count(self, subject_area_count):
        """Sets the subject_area_count of this L1Statistic.

        主题总数

        :param subject_area_count: The subject_area_count of this L1Statistic.
        :type subject_area_count: int
        """
        self._subject_area_count = subject_area_count

    @property
    def business_object_count(self):
        """Gets the business_object_count of this L1Statistic.

        业务对象总数

        :return: The business_object_count of this L1Statistic.
        :rtype: int
        """
        return self._business_object_count

    @business_object_count.setter
    def business_object_count(self, business_object_count):
        """Sets the business_object_count of this L1Statistic.

        业务对象总数

        :param business_object_count: The business_object_count of this L1Statistic.
        :type business_object_count: int
        """
        self._business_object_count = business_object_count

    @property
    def logic_entity_count(self):
        """Gets the logic_entity_count of this L1Statistic.

        逻辑实体总数

        :return: The logic_entity_count of this L1Statistic.
        :rtype: int
        """
        return self._logic_entity_count

    @logic_entity_count.setter
    def logic_entity_count(self, logic_entity_count):
        """Sets the logic_entity_count of this L1Statistic.

        逻辑实体总数

        :param logic_entity_count: The logic_entity_count of this L1Statistic.
        :type logic_entity_count: int
        """
        self._logic_entity_count = logic_entity_count

    @property
    def subject_area_statistics(self):
        """Gets the subject_area_statistics of this L1Statistic.

        主题统计信息

        :return: The subject_area_statistics of this L1Statistic.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.L2Statistic`]
        """
        return self._subject_area_statistics

    @subject_area_statistics.setter
    def subject_area_statistics(self, subject_area_statistics):
        """Sets the subject_area_statistics of this L1Statistic.

        主题统计信息

        :param subject_area_statistics: The subject_area_statistics of this L1Statistic.
        :type subject_area_statistics: list[:class:`huaweicloudsdkdataartsstudio.v1.L2Statistic`]
        """
        self._subject_area_statistics = subject_area_statistics

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
        if not isinstance(other, L1Statistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
