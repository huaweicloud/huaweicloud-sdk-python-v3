# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWarmPoolResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'warm_pool': 'WarmPoolInfo'
    }

    attribute_map = {
        'warm_pool': 'warm_pool'
    }

    def __init__(self, warm_pool=None):
        r"""ShowWarmPoolResponse

        The model defined in huaweicloud sdk

        :param warm_pool: 
        :type warm_pool: :class:`huaweicloudsdkas.v1.WarmPoolInfo`
        """
        
        super(ShowWarmPoolResponse, self).__init__()

        self._warm_pool = None
        self.discriminator = None

        if warm_pool is not None:
            self.warm_pool = warm_pool

    @property
    def warm_pool(self):
        r"""Gets the warm_pool of this ShowWarmPoolResponse.

        :return: The warm_pool of this ShowWarmPoolResponse.
        :rtype: :class:`huaweicloudsdkas.v1.WarmPoolInfo`
        """
        return self._warm_pool

    @warm_pool.setter
    def warm_pool(self, warm_pool):
        r"""Sets the warm_pool of this ShowWarmPoolResponse.

        :param warm_pool: The warm_pool of this ShowWarmPoolResponse.
        :type warm_pool: :class:`huaweicloudsdkas.v1.WarmPoolInfo`
        """
        self._warm_pool = warm_pool

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
        if not isinstance(other, ShowWarmPoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
