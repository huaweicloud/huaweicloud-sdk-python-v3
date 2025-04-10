# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNetworkQualityResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'return_code': 'int',
        'return_desc': 'str',
        'qos_list': 'list[UserQos]'
    }

    attribute_map = {
        'return_code': 'returnCode',
        'return_desc': 'returnDesc',
        'qos_list': 'qosList'
    }

    def __init__(self, return_code=None, return_desc=None, qos_list=None):
        r"""ListNetworkQualityResponse

        The model defined in huaweicloud sdk

        :param return_code: 结果码
        :type return_code: int
        :param return_desc: 结果描述
        :type return_desc: str
        :param qos_list: 会场Qos列表
        :type qos_list: list[:class:`huaweicloudsdkmeeting.v1.UserQos`]
        """
        
        super(ListNetworkQualityResponse, self).__init__()

        self._return_code = None
        self._return_desc = None
        self._qos_list = None
        self.discriminator = None

        if return_code is not None:
            self.return_code = return_code
        if return_desc is not None:
            self.return_desc = return_desc
        if qos_list is not None:
            self.qos_list = qos_list

    @property
    def return_code(self):
        r"""Gets the return_code of this ListNetworkQualityResponse.

        结果码

        :return: The return_code of this ListNetworkQualityResponse.
        :rtype: int
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        r"""Sets the return_code of this ListNetworkQualityResponse.

        结果码

        :param return_code: The return_code of this ListNetworkQualityResponse.
        :type return_code: int
        """
        self._return_code = return_code

    @property
    def return_desc(self):
        r"""Gets the return_desc of this ListNetworkQualityResponse.

        结果描述

        :return: The return_desc of this ListNetworkQualityResponse.
        :rtype: str
        """
        return self._return_desc

    @return_desc.setter
    def return_desc(self, return_desc):
        r"""Sets the return_desc of this ListNetworkQualityResponse.

        结果描述

        :param return_desc: The return_desc of this ListNetworkQualityResponse.
        :type return_desc: str
        """
        self._return_desc = return_desc

    @property
    def qos_list(self):
        r"""Gets the qos_list of this ListNetworkQualityResponse.

        会场Qos列表

        :return: The qos_list of this ListNetworkQualityResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.UserQos`]
        """
        return self._qos_list

    @qos_list.setter
    def qos_list(self, qos_list):
        r"""Sets the qos_list of this ListNetworkQualityResponse.

        会场Qos列表

        :param qos_list: The qos_list of this ListNetworkQualityResponse.
        :type qos_list: list[:class:`huaweicloudsdkmeeting.v1.UserQos`]
        """
        self._qos_list = qos_list

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
        if not isinstance(other, ListNetworkQualityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
