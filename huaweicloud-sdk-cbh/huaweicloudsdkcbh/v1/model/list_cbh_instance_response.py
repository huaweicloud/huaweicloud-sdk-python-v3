# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCbhInstanceResponse(SdkResponse):

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
        'quota_detail': 'QuotaDetail',
        'instance': 'list[InstanceDetail]'
    }

    attribute_map = {
        'total': 'total',
        'quota_detail': 'quota_detail',
        'instance': 'instance'
    }

    def __init__(self, total=None, quota_detail=None, instance=None):
        """ListCbhInstanceResponse

        The model defined in huaweicloud sdk

        :param total: 实例总数
        :type total: int
        :param quota_detail: 
        :type quota_detail: :class:`huaweicloudsdkcbh.v1.QuotaDetail`
        :param instance: 实例列表
        :type instance: list[:class:`huaweicloudsdkcbh.v1.InstanceDetail`]
        """
        
        super(ListCbhInstanceResponse, self).__init__()

        self._total = None
        self._quota_detail = None
        self._instance = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if quota_detail is not None:
            self.quota_detail = quota_detail
        if instance is not None:
            self.instance = instance

    @property
    def total(self):
        """Gets the total of this ListCbhInstanceResponse.

        实例总数

        :return: The total of this ListCbhInstanceResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListCbhInstanceResponse.

        实例总数

        :param total: The total of this ListCbhInstanceResponse.
        :type total: int
        """
        self._total = total

    @property
    def quota_detail(self):
        """Gets the quota_detail of this ListCbhInstanceResponse.

        :return: The quota_detail of this ListCbhInstanceResponse.
        :rtype: :class:`huaweicloudsdkcbh.v1.QuotaDetail`
        """
        return self._quota_detail

    @quota_detail.setter
    def quota_detail(self, quota_detail):
        """Sets the quota_detail of this ListCbhInstanceResponse.

        :param quota_detail: The quota_detail of this ListCbhInstanceResponse.
        :type quota_detail: :class:`huaweicloudsdkcbh.v1.QuotaDetail`
        """
        self._quota_detail = quota_detail

    @property
    def instance(self):
        """Gets the instance of this ListCbhInstanceResponse.

        实例列表

        :return: The instance of this ListCbhInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkcbh.v1.InstanceDetail`]
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ListCbhInstanceResponse.

        实例列表

        :param instance: The instance of this ListCbhInstanceResponse.
        :type instance: list[:class:`huaweicloudsdkcbh.v1.InstanceDetail`]
        """
        self._instance = instance

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
        if not isinstance(other, ListCbhInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
