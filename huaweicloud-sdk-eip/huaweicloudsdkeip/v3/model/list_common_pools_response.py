# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCommonPoolsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'common_pools': 'list[CommonPoolDict]',
        'request_id': 'str'
    }

    attribute_map = {
        'common_pools': 'common_pools',
        'request_id': 'request_id'
    }

    def __init__(self, common_pools=None, request_id=None):
        """ListCommonPoolsResponse

        The model defined in huaweicloud sdk

        :param common_pools: 功能说明：公共池对象
        :type common_pools: list[:class:`huaweicloudsdkeip.v3.CommonPoolDict`]
        :param request_id: 本次请求的编号
        :type request_id: str
        """
        
        super(ListCommonPoolsResponse, self).__init__()

        self._common_pools = None
        self._request_id = None
        self.discriminator = None

        if common_pools is not None:
            self.common_pools = common_pools
        if request_id is not None:
            self.request_id = request_id

    @property
    def common_pools(self):
        """Gets the common_pools of this ListCommonPoolsResponse.

        功能说明：公共池对象

        :return: The common_pools of this ListCommonPoolsResponse.
        :rtype: list[:class:`huaweicloudsdkeip.v3.CommonPoolDict`]
        """
        return self._common_pools

    @common_pools.setter
    def common_pools(self, common_pools):
        """Sets the common_pools of this ListCommonPoolsResponse.

        功能说明：公共池对象

        :param common_pools: The common_pools of this ListCommonPoolsResponse.
        :type common_pools: list[:class:`huaweicloudsdkeip.v3.CommonPoolDict`]
        """
        self._common_pools = common_pools

    @property
    def request_id(self):
        """Gets the request_id of this ListCommonPoolsResponse.

        本次请求的编号

        :return: The request_id of this ListCommonPoolsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListCommonPoolsResponse.

        本次请求的编号

        :param request_id: The request_id of this ListCommonPoolsResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListCommonPoolsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
