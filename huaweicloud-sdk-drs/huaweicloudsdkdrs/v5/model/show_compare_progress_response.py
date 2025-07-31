# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCompareProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'full_info': 'QueryCompareJobProgressRespFullInfo',
        'incre_info': 'QueryCompareJobProgressRespIncreInfo',
        'global_info': 'QueryCompareJobProgressRespGlobalInfo'
    }

    attribute_map = {
        'full_info': 'full_info',
        'incre_info': 'incre_info',
        'global_info': 'global_info'
    }

    def __init__(self, full_info=None, incre_info=None, global_info=None):
        r"""ShowCompareProgressResponse

        The model defined in huaweicloud sdk

        :param full_info: 
        :type full_info: :class:`huaweicloudsdkdrs.v5.QueryCompareJobProgressRespFullInfo`
        :param incre_info: 
        :type incre_info: :class:`huaweicloudsdkdrs.v5.QueryCompareJobProgressRespIncreInfo`
        :param global_info: 
        :type global_info: :class:`huaweicloudsdkdrs.v5.QueryCompareJobProgressRespGlobalInfo`
        """
        
        super(ShowCompareProgressResponse, self).__init__()

        self._full_info = None
        self._incre_info = None
        self._global_info = None
        self.discriminator = None

        if full_info is not None:
            self.full_info = full_info
        if incre_info is not None:
            self.incre_info = incre_info
        if global_info is not None:
            self.global_info = global_info

    @property
    def full_info(self):
        r"""Gets the full_info of this ShowCompareProgressResponse.

        :return: The full_info of this ShowCompareProgressResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.QueryCompareJobProgressRespFullInfo`
        """
        return self._full_info

    @full_info.setter
    def full_info(self, full_info):
        r"""Sets the full_info of this ShowCompareProgressResponse.

        :param full_info: The full_info of this ShowCompareProgressResponse.
        :type full_info: :class:`huaweicloudsdkdrs.v5.QueryCompareJobProgressRespFullInfo`
        """
        self._full_info = full_info

    @property
    def incre_info(self):
        r"""Gets the incre_info of this ShowCompareProgressResponse.

        :return: The incre_info of this ShowCompareProgressResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.QueryCompareJobProgressRespIncreInfo`
        """
        return self._incre_info

    @incre_info.setter
    def incre_info(self, incre_info):
        r"""Sets the incre_info of this ShowCompareProgressResponse.

        :param incre_info: The incre_info of this ShowCompareProgressResponse.
        :type incre_info: :class:`huaweicloudsdkdrs.v5.QueryCompareJobProgressRespIncreInfo`
        """
        self._incre_info = incre_info

    @property
    def global_info(self):
        r"""Gets the global_info of this ShowCompareProgressResponse.

        :return: The global_info of this ShowCompareProgressResponse.
        :rtype: :class:`huaweicloudsdkdrs.v5.QueryCompareJobProgressRespGlobalInfo`
        """
        return self._global_info

    @global_info.setter
    def global_info(self, global_info):
        r"""Sets the global_info of this ShowCompareProgressResponse.

        :param global_info: The global_info of this ShowCompareProgressResponse.
        :type global_info: :class:`huaweicloudsdkdrs.v5.QueryCompareJobProgressRespGlobalInfo`
        """
        self._global_info = global_info

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
        if not isinstance(other, ShowCompareProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
