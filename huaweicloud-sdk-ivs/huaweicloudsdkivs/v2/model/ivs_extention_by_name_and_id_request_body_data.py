# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IvsExtentionByNameAndIdRequestBodyData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'req_data': 'list[ExtentionReqDataByNameAndId]'
    }

    attribute_map = {
        'req_data': 'req_data'
    }

    def __init__(self, req_data=None):
        r"""IvsExtentionByNameAndIdRequestBodyData

        The model defined in huaweicloud sdk

        :param req_data: 请求列表，用于支持批量调用。目前暂时只支持单个数据查询。
        :type req_data: list[:class:`huaweicloudsdkivs.v2.ExtentionReqDataByNameAndId`]
        """
        
        

        self._req_data = None
        self.discriminator = None

        if req_data is not None:
            self.req_data = req_data

    @property
    def req_data(self):
        r"""Gets the req_data of this IvsExtentionByNameAndIdRequestBodyData.

        请求列表，用于支持批量调用。目前暂时只支持单个数据查询。

        :return: The req_data of this IvsExtentionByNameAndIdRequestBodyData.
        :rtype: list[:class:`huaweicloudsdkivs.v2.ExtentionReqDataByNameAndId`]
        """
        return self._req_data

    @req_data.setter
    def req_data(self, req_data):
        r"""Sets the req_data of this IvsExtentionByNameAndIdRequestBodyData.

        请求列表，用于支持批量调用。目前暂时只支持单个数据查询。

        :param req_data: The req_data of this IvsExtentionByNameAndIdRequestBodyData.
        :type req_data: list[:class:`huaweicloudsdkivs.v2.ExtentionReqDataByNameAndId`]
        """
        self._req_data = req_data

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
        if not isinstance(other, IvsExtentionByNameAndIdRequestBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
