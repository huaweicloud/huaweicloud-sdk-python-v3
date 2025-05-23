# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePoolResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool': 'PoolResp'
    }

    attribute_map = {
        'pool': 'pool'
    }

    def __init__(self, pool=None):
        r"""UpdatePoolResponse

        The model defined in huaweicloud sdk

        :param pool: 
        :type pool: :class:`huaweicloudsdkelb.v2.PoolResp`
        """
        
        super(UpdatePoolResponse, self).__init__()

        self._pool = None
        self.discriminator = None

        if pool is not None:
            self.pool = pool

    @property
    def pool(self):
        r"""Gets the pool of this UpdatePoolResponse.

        :return: The pool of this UpdatePoolResponse.
        :rtype: :class:`huaweicloudsdkelb.v2.PoolResp`
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        r"""Sets the pool of this UpdatePoolResponse.

        :param pool: The pool of this UpdatePoolResponse.
        :type pool: :class:`huaweicloudsdkelb.v2.PoolResp`
        """
        self._pool = pool

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
        if not isinstance(other, UpdatePoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
