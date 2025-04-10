# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class L2Statistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subject_area_name': 'str',
        'subject_area_guid': 'str',
        'ordinal': 'int',
        'business_object_count': 'int',
        'logic_entity_count': 'int'
    }

    attribute_map = {
        'subject_area_name': 'subject_area_name',
        'subject_area_guid': 'subject_area_guid',
        'ordinal': 'ordinal',
        'business_object_count': 'business_object_count',
        'logic_entity_count': 'logic_entity_count'
    }

    def __init__(self, subject_area_name=None, subject_area_guid=None, ordinal=None, business_object_count=None, logic_entity_count=None):
        r"""L2Statistic

        The model defined in huaweicloud sdk

        :param subject_area_name: 主题名称
        :type subject_area_name: str
        :param subject_area_guid: 主题的guid
        :type subject_area_guid: str
        :param ordinal: 主题序号
        :type ordinal: int
        :param business_object_count: 业务对象总数
        :type business_object_count: int
        :param logic_entity_count: 逻辑实体总数
        :type logic_entity_count: int
        """
        
        

        self._subject_area_name = None
        self._subject_area_guid = None
        self._ordinal = None
        self._business_object_count = None
        self._logic_entity_count = None
        self.discriminator = None

        if subject_area_name is not None:
            self.subject_area_name = subject_area_name
        if subject_area_guid is not None:
            self.subject_area_guid = subject_area_guid
        if ordinal is not None:
            self.ordinal = ordinal
        if business_object_count is not None:
            self.business_object_count = business_object_count
        if logic_entity_count is not None:
            self.logic_entity_count = logic_entity_count

    @property
    def subject_area_name(self):
        r"""Gets the subject_area_name of this L2Statistic.

        主题名称

        :return: The subject_area_name of this L2Statistic.
        :rtype: str
        """
        return self._subject_area_name

    @subject_area_name.setter
    def subject_area_name(self, subject_area_name):
        r"""Sets the subject_area_name of this L2Statistic.

        主题名称

        :param subject_area_name: The subject_area_name of this L2Statistic.
        :type subject_area_name: str
        """
        self._subject_area_name = subject_area_name

    @property
    def subject_area_guid(self):
        r"""Gets the subject_area_guid of this L2Statistic.

        主题的guid

        :return: The subject_area_guid of this L2Statistic.
        :rtype: str
        """
        return self._subject_area_guid

    @subject_area_guid.setter
    def subject_area_guid(self, subject_area_guid):
        r"""Sets the subject_area_guid of this L2Statistic.

        主题的guid

        :param subject_area_guid: The subject_area_guid of this L2Statistic.
        :type subject_area_guid: str
        """
        self._subject_area_guid = subject_area_guid

    @property
    def ordinal(self):
        r"""Gets the ordinal of this L2Statistic.

        主题序号

        :return: The ordinal of this L2Statistic.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        r"""Sets the ordinal of this L2Statistic.

        主题序号

        :param ordinal: The ordinal of this L2Statistic.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def business_object_count(self):
        r"""Gets the business_object_count of this L2Statistic.

        业务对象总数

        :return: The business_object_count of this L2Statistic.
        :rtype: int
        """
        return self._business_object_count

    @business_object_count.setter
    def business_object_count(self, business_object_count):
        r"""Sets the business_object_count of this L2Statistic.

        业务对象总数

        :param business_object_count: The business_object_count of this L2Statistic.
        :type business_object_count: int
        """
        self._business_object_count = business_object_count

    @property
    def logic_entity_count(self):
        r"""Gets the logic_entity_count of this L2Statistic.

        逻辑实体总数

        :return: The logic_entity_count of this L2Statistic.
        :rtype: int
        """
        return self._logic_entity_count

    @logic_entity_count.setter
    def logic_entity_count(self, logic_entity_count):
        r"""Sets the logic_entity_count of this L2Statistic.

        逻辑实体总数

        :param logic_entity_count: The logic_entity_count of this L2Statistic.
        :type logic_entity_count: int
        """
        self._logic_entity_count = logic_entity_count

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
        if not isinstance(other, L2Statistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
