# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateNotificationMasksRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mask_name': 'str',
        'relation_type': 'RelationType',
        'relation_ids': 'list[str]',
        'resources': 'list[Resource]',
        'mask_type': 'MaskType',
        'start_date': 'date',
        'start_time': 'str',
        'end_date': 'date',
        'end_time': 'str'
    }

    attribute_map = {
        'mask_name': 'mask_name',
        'relation_type': 'relation_type',
        'relation_ids': 'relation_ids',
        'resources': 'resources',
        'mask_type': 'mask_type',
        'start_date': 'start_date',
        'start_time': 'start_time',
        'end_date': 'end_date',
        'end_time': 'end_time'
    }

    def __init__(self, mask_name=None, relation_type=None, relation_ids=None, resources=None, mask_type=None, start_date=None, start_time=None, end_date=None, end_time=None):
        """BatchUpdateNotificationMasksRequestBody

        The model defined in huaweicloud sdk

        :param mask_name: 屏蔽规则名称，只能为字母、数字、汉字、-、_，最大长度为64
        :type mask_name: str
        :param relation_type: 
        :type relation_type: :class:`huaweicloudsdkces.v2.RelationType`
        :param relation_ids: 关联编号，relation_type为ALARM_RULE时填屏蔽的告警规则ID；relation_type为RESOURCE_POLICY_NOTIFICATION、RESOURCE_POLICY_ALARM时填屏蔽的告警策略ID；
        :type relation_ids: list[str]
        :param resources: 关联资源，relation_type为RESOURCE、RESOURCE_POLICY_NOTIFICATION、RESOURCE_POLICY_ALARM时填屏蔽的资源信息；
        :type resources: list[:class:`huaweicloudsdkces.v2.Resource`]
        :param mask_type: 
        :type mask_type: :class:`huaweicloudsdkces.v2.MaskType`
        :param start_date: 屏蔽起始日期，yyyy-MM-dd。
        :type start_date: date
        :param start_time: 屏蔽起始时间，HH:mm:ss。
        :type start_time: str
        :param end_date: 屏蔽截止日期，yyyy-MM-dd。
        :type end_date: date
        :param end_time: 屏蔽截止时间，HH:mm:ss。
        :type end_time: str
        """
        
        

        self._mask_name = None
        self._relation_type = None
        self._relation_ids = None
        self._resources = None
        self._mask_type = None
        self._start_date = None
        self._start_time = None
        self._end_date = None
        self._end_time = None
        self.discriminator = None

        if mask_name is not None:
            self.mask_name = mask_name
        self.relation_type = relation_type
        self.relation_ids = relation_ids
        if resources is not None:
            self.resources = resources
        self.mask_type = mask_type
        if start_date is not None:
            self.start_date = start_date
        if start_time is not None:
            self.start_time = start_time
        if end_date is not None:
            self.end_date = end_date
        if end_time is not None:
            self.end_time = end_time

    @property
    def mask_name(self):
        """Gets the mask_name of this BatchUpdateNotificationMasksRequestBody.

        屏蔽规则名称，只能为字母、数字、汉字、-、_，最大长度为64

        :return: The mask_name of this BatchUpdateNotificationMasksRequestBody.
        :rtype: str
        """
        return self._mask_name

    @mask_name.setter
    def mask_name(self, mask_name):
        """Sets the mask_name of this BatchUpdateNotificationMasksRequestBody.

        屏蔽规则名称，只能为字母、数字、汉字、-、_，最大长度为64

        :param mask_name: The mask_name of this BatchUpdateNotificationMasksRequestBody.
        :type mask_name: str
        """
        self._mask_name = mask_name

    @property
    def relation_type(self):
        """Gets the relation_type of this BatchUpdateNotificationMasksRequestBody.

        :return: The relation_type of this BatchUpdateNotificationMasksRequestBody.
        :rtype: :class:`huaweicloudsdkces.v2.RelationType`
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this BatchUpdateNotificationMasksRequestBody.

        :param relation_type: The relation_type of this BatchUpdateNotificationMasksRequestBody.
        :type relation_type: :class:`huaweicloudsdkces.v2.RelationType`
        """
        self._relation_type = relation_type

    @property
    def relation_ids(self):
        """Gets the relation_ids of this BatchUpdateNotificationMasksRequestBody.

        关联编号，relation_type为ALARM_RULE时填屏蔽的告警规则ID；relation_type为RESOURCE_POLICY_NOTIFICATION、RESOURCE_POLICY_ALARM时填屏蔽的告警策略ID；

        :return: The relation_ids of this BatchUpdateNotificationMasksRequestBody.
        :rtype: list[str]
        """
        return self._relation_ids

    @relation_ids.setter
    def relation_ids(self, relation_ids):
        """Sets the relation_ids of this BatchUpdateNotificationMasksRequestBody.

        关联编号，relation_type为ALARM_RULE时填屏蔽的告警规则ID；relation_type为RESOURCE_POLICY_NOTIFICATION、RESOURCE_POLICY_ALARM时填屏蔽的告警策略ID；

        :param relation_ids: The relation_ids of this BatchUpdateNotificationMasksRequestBody.
        :type relation_ids: list[str]
        """
        self._relation_ids = relation_ids

    @property
    def resources(self):
        """Gets the resources of this BatchUpdateNotificationMasksRequestBody.

        关联资源，relation_type为RESOURCE、RESOURCE_POLICY_NOTIFICATION、RESOURCE_POLICY_ALARM时填屏蔽的资源信息；

        :return: The resources of this BatchUpdateNotificationMasksRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v2.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this BatchUpdateNotificationMasksRequestBody.

        关联资源，relation_type为RESOURCE、RESOURCE_POLICY_NOTIFICATION、RESOURCE_POLICY_ALARM时填屏蔽的资源信息；

        :param resources: The resources of this BatchUpdateNotificationMasksRequestBody.
        :type resources: list[:class:`huaweicloudsdkces.v2.Resource`]
        """
        self._resources = resources

    @property
    def mask_type(self):
        """Gets the mask_type of this BatchUpdateNotificationMasksRequestBody.

        :return: The mask_type of this BatchUpdateNotificationMasksRequestBody.
        :rtype: :class:`huaweicloudsdkces.v2.MaskType`
        """
        return self._mask_type

    @mask_type.setter
    def mask_type(self, mask_type):
        """Sets the mask_type of this BatchUpdateNotificationMasksRequestBody.

        :param mask_type: The mask_type of this BatchUpdateNotificationMasksRequestBody.
        :type mask_type: :class:`huaweicloudsdkces.v2.MaskType`
        """
        self._mask_type = mask_type

    @property
    def start_date(self):
        """Gets the start_date of this BatchUpdateNotificationMasksRequestBody.

        屏蔽起始日期，yyyy-MM-dd。

        :return: The start_date of this BatchUpdateNotificationMasksRequestBody.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this BatchUpdateNotificationMasksRequestBody.

        屏蔽起始日期，yyyy-MM-dd。

        :param start_date: The start_date of this BatchUpdateNotificationMasksRequestBody.
        :type start_date: date
        """
        self._start_date = start_date

    @property
    def start_time(self):
        """Gets the start_time of this BatchUpdateNotificationMasksRequestBody.

        屏蔽起始时间，HH:mm:ss。

        :return: The start_time of this BatchUpdateNotificationMasksRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BatchUpdateNotificationMasksRequestBody.

        屏蔽起始时间，HH:mm:ss。

        :param start_time: The start_time of this BatchUpdateNotificationMasksRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_date(self):
        """Gets the end_date of this BatchUpdateNotificationMasksRequestBody.

        屏蔽截止日期，yyyy-MM-dd。

        :return: The end_date of this BatchUpdateNotificationMasksRequestBody.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this BatchUpdateNotificationMasksRequestBody.

        屏蔽截止日期，yyyy-MM-dd。

        :param end_date: The end_date of this BatchUpdateNotificationMasksRequestBody.
        :type end_date: date
        """
        self._end_date = end_date

    @property
    def end_time(self):
        """Gets the end_time of this BatchUpdateNotificationMasksRequestBody.

        屏蔽截止时间，HH:mm:ss。

        :return: The end_time of this BatchUpdateNotificationMasksRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this BatchUpdateNotificationMasksRequestBody.

        屏蔽截止时间，HH:mm:ss。

        :param end_time: The end_time of this BatchUpdateNotificationMasksRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, BatchUpdateNotificationMasksRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
