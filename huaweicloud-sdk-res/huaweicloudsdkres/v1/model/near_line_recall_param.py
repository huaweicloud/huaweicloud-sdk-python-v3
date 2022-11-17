# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NearLineRecallParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_limit': 'bool',
        'time_feature': 'str',
        'retain_days': 'int',
        'recall_fileds': 'list[RecallFiled]',
        'item_cf_job_name': 'str'
    }

    attribute_map = {
        'time_limit': 'time_limit',
        'time_feature': 'timeFeature',
        'retain_days': 'retainDays',
        'recall_fileds': 'recall_fileds',
        'item_cf_job_name': 'itemCF_job_name'
    }

    def __init__(self, time_limit=None, time_feature=None, retain_days=None, recall_fileds=None, item_cf_job_name=None):
        """NearLineRecallParam

        The model defined in huaweicloud sdk

        :param time_limit: 时间过滤。
        :type time_limit: bool
        :param time_feature: 时间特征。
        :type time_feature: str
        :param retain_days: 保留期(天)。
        :type retain_days: int
        :param recall_fileds: 召回字段。
        :type recall_fileds: list[:class:`huaweicloudsdkres.v1.RecallFiled`]
        :param item_cf_job_name: 物品协同过滤作业名称。
        :type item_cf_job_name: str
        """
        
        

        self._time_limit = None
        self._time_feature = None
        self._retain_days = None
        self._recall_fileds = None
        self._item_cf_job_name = None
        self.discriminator = None

        if time_limit is not None:
            self.time_limit = time_limit
        if time_feature is not None:
            self.time_feature = time_feature
        if retain_days is not None:
            self.retain_days = retain_days
        if recall_fileds is not None:
            self.recall_fileds = recall_fileds
        if item_cf_job_name is not None:
            self.item_cf_job_name = item_cf_job_name

    @property
    def time_limit(self):
        """Gets the time_limit of this NearLineRecallParam.

        时间过滤。

        :return: The time_limit of this NearLineRecallParam.
        :rtype: bool
        """
        return self._time_limit

    @time_limit.setter
    def time_limit(self, time_limit):
        """Sets the time_limit of this NearLineRecallParam.

        时间过滤。

        :param time_limit: The time_limit of this NearLineRecallParam.
        :type time_limit: bool
        """
        self._time_limit = time_limit

    @property
    def time_feature(self):
        """Gets the time_feature of this NearLineRecallParam.

        时间特征。

        :return: The time_feature of this NearLineRecallParam.
        :rtype: str
        """
        return self._time_feature

    @time_feature.setter
    def time_feature(self, time_feature):
        """Sets the time_feature of this NearLineRecallParam.

        时间特征。

        :param time_feature: The time_feature of this NearLineRecallParam.
        :type time_feature: str
        """
        self._time_feature = time_feature

    @property
    def retain_days(self):
        """Gets the retain_days of this NearLineRecallParam.

        保留期(天)。

        :return: The retain_days of this NearLineRecallParam.
        :rtype: int
        """
        return self._retain_days

    @retain_days.setter
    def retain_days(self, retain_days):
        """Sets the retain_days of this NearLineRecallParam.

        保留期(天)。

        :param retain_days: The retain_days of this NearLineRecallParam.
        :type retain_days: int
        """
        self._retain_days = retain_days

    @property
    def recall_fileds(self):
        """Gets the recall_fileds of this NearLineRecallParam.

        召回字段。

        :return: The recall_fileds of this NearLineRecallParam.
        :rtype: list[:class:`huaweicloudsdkres.v1.RecallFiled`]
        """
        return self._recall_fileds

    @recall_fileds.setter
    def recall_fileds(self, recall_fileds):
        """Sets the recall_fileds of this NearLineRecallParam.

        召回字段。

        :param recall_fileds: The recall_fileds of this NearLineRecallParam.
        :type recall_fileds: list[:class:`huaweicloudsdkres.v1.RecallFiled`]
        """
        self._recall_fileds = recall_fileds

    @property
    def item_cf_job_name(self):
        """Gets the item_cf_job_name of this NearLineRecallParam.

        物品协同过滤作业名称。

        :return: The item_cf_job_name of this NearLineRecallParam.
        :rtype: str
        """
        return self._item_cf_job_name

    @item_cf_job_name.setter
    def item_cf_job_name(self, item_cf_job_name):
        """Sets the item_cf_job_name of this NearLineRecallParam.

        物品协同过滤作业名称。

        :param item_cf_job_name: The item_cf_job_name of this NearLineRecallParam.
        :type item_cf_job_name: str
        """
        self._item_cf_job_name = item_cf_job_name

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
        if not isinstance(other, NearLineRecallParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
