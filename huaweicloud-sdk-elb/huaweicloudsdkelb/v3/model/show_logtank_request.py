# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLogtankRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logtank_id': 'str'
    }

    attribute_map = {
        'logtank_id': 'logtank_id'
    }

    def __init__(self, logtank_id=None):
        r"""ShowLogtankRequest

        The model defined in huaweicloud sdk

        :param logtank_id: 云日志ID。
        :type logtank_id: str
        """
        
        

        self._logtank_id = None
        self.discriminator = None

        self.logtank_id = logtank_id

    @property
    def logtank_id(self):
        r"""Gets the logtank_id of this ShowLogtankRequest.

        云日志ID。

        :return: The logtank_id of this ShowLogtankRequest.
        :rtype: str
        """
        return self._logtank_id

    @logtank_id.setter
    def logtank_id(self, logtank_id):
        r"""Sets the logtank_id of this ShowLogtankRequest.

        云日志ID。

        :param logtank_id: The logtank_id of this ShowLogtankRequest.
        :type logtank_id: str
        """
        self._logtank_id = logtank_id

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
        if not isinstance(other, ShowLogtankRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
