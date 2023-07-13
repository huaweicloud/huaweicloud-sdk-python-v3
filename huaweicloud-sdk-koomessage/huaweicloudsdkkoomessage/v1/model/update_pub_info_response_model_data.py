# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePubInfoResponseModelData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pub_update_log_id': 'str'
    }

    attribute_map = {
        'pub_update_log_id': 'pub_update_log_id'
    }

    def __init__(self, pub_update_log_id=None):
        """UpdatePubInfoResponseModelData

        The model defined in huaweicloud sdk

        :param pub_update_log_id: 服务号更新记录ID。
        :type pub_update_log_id: str
        """
        
        

        self._pub_update_log_id = None
        self.discriminator = None

        if pub_update_log_id is not None:
            self.pub_update_log_id = pub_update_log_id

    @property
    def pub_update_log_id(self):
        """Gets the pub_update_log_id of this UpdatePubInfoResponseModelData.

        服务号更新记录ID。

        :return: The pub_update_log_id of this UpdatePubInfoResponseModelData.
        :rtype: str
        """
        return self._pub_update_log_id

    @pub_update_log_id.setter
    def pub_update_log_id(self, pub_update_log_id):
        """Sets the pub_update_log_id of this UpdatePubInfoResponseModelData.

        服务号更新记录ID。

        :param pub_update_log_id: The pub_update_log_id of this UpdatePubInfoResponseModelData.
        :type pub_update_log_id: str
        """
        self._pub_update_log_id = pub_update_log_id

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
        if not isinstance(other, UpdatePubInfoResponseModelData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
