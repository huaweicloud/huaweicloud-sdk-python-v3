# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleSiteInfo:

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
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status'
    }

    def __init__(self, id=None, status=None):
        r"""SimpleSiteInfo

        The model defined in huaweicloud sdk

        :param id: 云桌面边缘小站id。
        :type id: str
        :param status: 云办公服务的状态。 - PREPARING：准备开通。 - SUBSCRIBING：开通中。 - SUBSCRIBED：已开通。 - SUBSCRIPTION_FAILED：开通失败。 - DEREGISTERING：销户中。 - DEREGISTRATION_FAILED：销户失败。 - CLOSED：已销户未开通。
        :type status: str
        """
        
        

        self._id = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this SimpleSiteInfo.

        云桌面边缘小站id。

        :return: The id of this SimpleSiteInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SimpleSiteInfo.

        云桌面边缘小站id。

        :param id: The id of this SimpleSiteInfo.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this SimpleSiteInfo.

        云办公服务的状态。 - PREPARING：准备开通。 - SUBSCRIBING：开通中。 - SUBSCRIBED：已开通。 - SUBSCRIPTION_FAILED：开通失败。 - DEREGISTERING：销户中。 - DEREGISTRATION_FAILED：销户失败。 - CLOSED：已销户未开通。

        :return: The status of this SimpleSiteInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SimpleSiteInfo.

        云办公服务的状态。 - PREPARING：准备开通。 - SUBSCRIBING：开通中。 - SUBSCRIBED：已开通。 - SUBSCRIPTION_FAILED：开通失败。 - DEREGISTERING：销户中。 - DEREGISTRATION_FAILED：销户失败。 - CLOSED：已销户未开通。

        :param status: The status of this SimpleSiteInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, SimpleSiteInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
