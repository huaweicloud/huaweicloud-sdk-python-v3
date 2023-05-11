# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaSimpleInfo:

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
        'quota_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'quota_id': 'quota_id'
    }

    def __init__(self, id=None, quota_id=None):
        """QuotaSimpleInfo

        The model defined in huaweicloud sdk

        :param id: 云经销商ID。
        :type id: str
        :param quota_id: 分配给云经销商的代金券额度ID。
        :type quota_id: str
        """
        
        

        self._id = None
        self._quota_id = None
        self.discriminator = None

        self.id = id
        self.quota_id = quota_id

    @property
    def id(self):
        """Gets the id of this QuotaSimpleInfo.

        云经销商ID。

        :return: The id of this QuotaSimpleInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuotaSimpleInfo.

        云经销商ID。

        :param id: The id of this QuotaSimpleInfo.
        :type id: str
        """
        self._id = id

    @property
    def quota_id(self):
        """Gets the quota_id of this QuotaSimpleInfo.

        分配给云经销商的代金券额度ID。

        :return: The quota_id of this QuotaSimpleInfo.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this QuotaSimpleInfo.

        分配给云经销商的代金券额度ID。

        :param quota_id: The quota_id of this QuotaSimpleInfo.
        :type quota_id: str
        """
        self._quota_id = quota_id

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
        if not isinstance(other, QuotaSimpleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
