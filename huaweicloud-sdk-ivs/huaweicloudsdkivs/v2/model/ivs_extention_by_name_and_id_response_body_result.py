# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IvsExtentionByNameAndIdResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'count': 'int',
        'resp_data': 'list[ExtentionRespDataByNameAndId]'
    }

    attribute_map = {
        'service_name': 'service_name',
        'count': 'count',
        'resp_data': 'resp_data'
    }

    def __init__(self, service_name=None, count=None, resp_data=None):
        """IvsExtentionByNameAndIdResponseBodyResult

        The model defined in huaweicloud sdk

        :param service_name: 子服务名称。
        :type service_name: str
        :param count: 成功的结果数量，与resp_data字段对应。
        :type count: int
        :param resp_data: 请求列表，用于支持批量调用。目前暂时只支持单个数据查询。
        :type resp_data: list[:class:`huaweicloudsdkivs.v2.ExtentionRespDataByNameAndId`]
        """
        
        

        self._service_name = None
        self._count = None
        self._resp_data = None
        self.discriminator = None

        if service_name is not None:
            self.service_name = service_name
        if count is not None:
            self.count = count
        if resp_data is not None:
            self.resp_data = resp_data

    @property
    def service_name(self):
        """Gets the service_name of this IvsExtentionByNameAndIdResponseBodyResult.

        子服务名称。

        :return: The service_name of this IvsExtentionByNameAndIdResponseBodyResult.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this IvsExtentionByNameAndIdResponseBodyResult.

        子服务名称。

        :param service_name: The service_name of this IvsExtentionByNameAndIdResponseBodyResult.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def count(self):
        """Gets the count of this IvsExtentionByNameAndIdResponseBodyResult.

        成功的结果数量，与resp_data字段对应。

        :return: The count of this IvsExtentionByNameAndIdResponseBodyResult.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this IvsExtentionByNameAndIdResponseBodyResult.

        成功的结果数量，与resp_data字段对应。

        :param count: The count of this IvsExtentionByNameAndIdResponseBodyResult.
        :type count: int
        """
        self._count = count

    @property
    def resp_data(self):
        """Gets the resp_data of this IvsExtentionByNameAndIdResponseBodyResult.

        请求列表，用于支持批量调用。目前暂时只支持单个数据查询。

        :return: The resp_data of this IvsExtentionByNameAndIdResponseBodyResult.
        :rtype: list[:class:`huaweicloudsdkivs.v2.ExtentionRespDataByNameAndId`]
        """
        return self._resp_data

    @resp_data.setter
    def resp_data(self, resp_data):
        """Sets the resp_data of this IvsExtentionByNameAndIdResponseBodyResult.

        请求列表，用于支持批量调用。目前暂时只支持单个数据查询。

        :param resp_data: The resp_data of this IvsExtentionByNameAndIdResponseBodyResult.
        :type resp_data: list[:class:`huaweicloudsdkivs.v2.ExtentionRespDataByNameAndId`]
        """
        self._resp_data = resp_data

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
        if not isinstance(other, IvsExtentionByNameAndIdResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
